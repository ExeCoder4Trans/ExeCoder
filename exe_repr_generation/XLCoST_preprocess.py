import os
import json
import numpy as np
from lang_processors import LangProcessor
from ast_tools import generate_AST
from dataflow_tools import generate_DFG
from deduplication import filter_dataset


XL_DATA_PATH = 'data/XLCoST/generation/pair_data_tok_full_desc'

CMT_PATH = 'data/XLCoST/generation/pair_data_tok_full_desc_comment'

ROOT_SAVE_PATH = 'data/XLCoST-Instruct/'
CODE_SAVE_PATH = ROOT_SAVE_PATH + 'NL/'


def get_lang_processor(lang):
    if lang == "py":
        return LangProcessor.processors["python"]()
    return LangProcessor.processors[lang]()

def load_json(file):
    with open(file, 'r', encoding='utf8') as f:
        return json.load(f)


def preprocess_XLCoST():
    if not os.path.exists(CODE_SAVE_PATH):
        os.makedirs(CODE_SAVE_PATH)
    cpp = []
    py = []
    java = []
    res_list = [cpp, py, java] 

    cpp_set = set()
    csharp_set = set()
    c_set = set()
    py_set = set()
    java_set = set()
    php_set = set()
    js_set = set()
    set_list = [cpp_set, py_set, java_set]

    language_list = ['cpp','py', 'java']
    mapname_list = ['train-C++-map.jsonl', 'train-Python-map.jsonl', 'train-Java-map.jsonl']

    CMTname_list = ['C++-desc', 'Python-desc', 'Java-desc']


    dir_list = os.listdir(XL_DATA_PATH)
    for j in range(len(language_list)):
        res = res_list[j]
        sets = set_list[j]
        languages = language_list[j]
        mapname = mapname_list[j]

        cmt_res = {}

        cmt_dir = CMT_PATH + '/' + CMTname_list[j]
        for item in os.listdir(cmt_dir):
            if item.split('-')[0] == 'train' and item.split('.')[-1] == 'txt': 
                cmt_file = cmt_dir + '/' + item
                with open(cmt_file, 'r') as f: 
                    cmt = f.readlines()
                id_file = cmt_dir + '/' + mapname_list[j]
                with open(id_file, 'r') as f:
                    for i, line in enumerate(f): 
                        ids = line.strip()   
                        if ids.split('-')[-1] == '1': continue
                        ids = ids.split('-')[0] + '-' + ids.split('-')[-1]
                        cmt_res[ids] = cmt[i].strip()

        for dir_item in dir_list:
            now_path = XL_DATA_PATH + '/' + dir_item
            file_list = os.listdir(now_path)
            for file in file_list:
                if file.split('.')[-1] == languages and file.split('-')[0] == 'train':
                    id_file = now_path + '/' + mapname
                    code_file = now_path + '/' + file
                    with open(code_file, 'r') as f: code_data = f.readlines()
                    with open(id_file, 'r') as f:
                        for i, line in enumerate(f):
                            ids = line.strip()
                            if ids.split('-')[-1] == '1' or ids in sets: continue
                            sets.add(ids)
                            ids = ids.split('-')[0] + '-' + ids.split('-')[-1]
                            if ids not in cmt_res.keys(): continue
                            res.append({"ID": ids, "Code": code_data[i].strip(), "Type": languages, "NL": cmt_res[ids]})

        sorted_data = sorted(res, key=lambda x: x['ID'])
        data_json = json.dumps(sorted_data, ensure_ascii=False, indent=4)
        if languages == 'py': languages = 'python'
        with open (CODE_SAVE_PATH + languages + '.json', 'w+', encoding='utf-8') as file:
            file.write(data_json) 

def clean_cpp_code():
    data = load_json(CODE_SAVE_PATH + "cpp.json")
    for i in range(len(data)):
        data[i]["Code"] = data[i]["Code"].replace("NEW_LINE", 'NNEEWW__LLIINNEE')

    dev_json = json.dumps(data, ensure_ascii=False, indent=4)
    with open (CODE_SAVE_PATH + "cpp.json", 'w+', encoding='utf-8') as file:
        file.write(dev_json)  

def clean_java_code():
    # wash ' a ' to 'a'
    data = load_json(CODE_SAVE_PATH + "java.json")
    for i in range(len(data)):
        data[i]["Code"] = data[i]["Code"].replace(" \' ", '\'')

    dev_json = json.dumps(data, ensure_ascii=False, indent=4)
    with open (CODE_SAVE_PATH + "java.json", 'w+', encoding='utf-8') as file:
        file.write(dev_json) 


def gen_tuning_data():
    language_list = ['python', 'cpp', "java"]
    res = []
    train = []
    dev = []

    typeslist = ["code", "NL", "DFG", "AST"]

    for types in typeslist:

        if types == "code":
            DATA_PATH = ROOT_SAVE_PATH + 'NL/'
            instruction_tmp = "Translate the given code from {} to {}. The input Code is marked with <Code> and </Code>. Please note that the code entered is a complete program with main fuction."
        if types == "NL":
            DATA_PATH = ROOT_SAVE_PATH + 'NL/'
            instruction_tmp = "Translate the given code from {} to {}. The input contains the source code and a description of the code. The input Code is marked with <Code> and </Code>. Please note that the code entered is a complete program with main fuction. The description of the code is marked with <NL> and </NL>."       
        elif types == "DFG": 
            DATA_PATH = ROOT_SAVE_PATH + 'DFG/'   
            instruction_tmp = "Translate the given code from {} to {}. The input contains the source code and a Dataflow Graph of the code. The input Code is marked with <Code> and </Code>. Please note that the code entered is a complete program with main fuction. The Dataflow Graph of the code is marked with <DFG> and </DFG>."
        elif types == "AST": 
            DATA_PATH = ROOT_SAVE_PATH + 'AST/' 
            instruction_tmp = "Translate the given code from {} to {}. The input contains the source code and a Abstract Syntax Tree of the code. The input Code is marked with <Code> and </Code>. Please note that the code entered is a complete program with main fuction. The Abstract Syntax Tree of the code is marked with <AST> and </AST>."


        for i in range(len(language_list)):
            for j in range(len(language_list)):
                if j == i: continue

                source = language_list[i]
                target = language_list[j]

                source_processer = get_lang_processor(source)
                target_processer = get_lang_processor(target)

                instruction = instruction_tmp.format(source, target)

                with open(DATA_PATH + source + '.json', 'r') as f: source_data = json.load(f)

                for k in range(len(source_data)):  source_data[k]["Code"] = source_processer.detokenize_code(source_data[k]["Code"]).replace('NNEEWW__LLIINNEE', '\n')

                source_code_dict = {}
                for item in source_data: source_code_dict[item['ID']] = '<Code>\n' + item["Code"] + '\n</Code>'
                if types == "NL":
                    source_NL_dict = {}
                    for item in source_data: source_NL_dict[item['ID']] = '<NL>\n' + item["NL"] + '\n</NL>'
                if types == "DFG":
                    source_DFG_dict = {}
                    for item in source_data: source_DFG_dict[item['ID']] = '<DFG>\n' + item["DFG"] + '\n</DFG>'
                if types == "AST":
                    source_AST_dict = {}
                    for item in source_data: source_AST_dict[item['ID']] = '<AST>\n' + item["AST"] + '\n</AST>'

                with open(DATA_PATH + target + '.json', 'r') as f: target_data = json.load(f)

                for k in range((len(target_data))):  target_data[k]["Code"] = target_processer.detokenize_code(target_data[k]["Code"]).replace('NNEEWW__LLIINNEE', '\n')

                target_code_dict = {}
                for item in target_data: target_code_dict[item['ID']] = '```' + target + '\n' + item["Code"] + '\n```'
                if types == "NL":
                    target_NL_dict = {}
                    for item in target_data: target_NL_dict[item['ID']] = item["NL"] 
                if types == "DFG":
                    target_DFG_dict = {}
                    for item in target_data: target_DFG_dict[item['ID']] = item["DFG"]
                if types == "AST":
                    target_AST_dict = {}
                    for item in target_data: target_AST_dict[item['ID']] = item["AST"] 

                tmp = []
                for ids in source_code_dict.keys():
                    if ids in target_code_dict.keys():
                        if types == "code":
                            tmp.append({"instruction": instruction, "input": source_code_dict[ids], "output": target_code_dict[ids]})
                        elif types == "NL":
                            tmp.append({"instruction": instruction, "input": source_code_dict[ids] + '\n\n\n' + source_NL_dict[ids], "output": target_code_dict[ids]})
                        elif types == "DFG":
                            tmp.append({"instruction": instruction, "input": source_code_dict[ids] + '\n\n\n' + source_DFG_dict[ids], "output": target_code_dict[ids]})
                        elif types == "AST":
                            tmp.append({"instruction": instruction, "input": source_code_dict[ids] + '\n\n\n' + source_AST_dict[ids], "output": target_code_dict[ids]})
                res += tmp
                
                train += res[: int(0.9 * len(res))]
                dev += res[int(0.9 * len(res)): ]
                res = []

        np.random.shuffle(train)
        np.random.shuffle(dev)

        print(len(train))
        print(len(dev))


        if not os.path.exists(ROOT_SAVE_PATH + 'Tuning/' + types): 
            os.makedirs(ROOT_SAVE_PATH + 'Tuning/' + types)

        train_json = json.dumps(train, ensure_ascii=False, indent=4)
        with open (ROOT_SAVE_PATH + 'Tuning/' + types + '/train.json', 'w+', encoding='utf-8') as file:
            file.write(train_json)    

        dev_json = json.dumps(dev, ensure_ascii=False, indent=4)
        with open (ROOT_SAVE_PATH + 'Tuning/' + types + '/dev.json', 'w+', encoding='utf-8') as file:
            file.write(dev_json)    

        res = []
        train = []
        dev = []


def gen_XLCoST_Instruct():
    preprocess_XLCoST()
    clean_cpp_code()
    clean_java_code()
    generate_AST(ROOT_SAVE_PATH)
    generate_DFG(ROOT_SAVE_PATH)
    filter_dataset(ROOT_SAVE_PATH)
    gen_tuning_data()


gen_XLCoST_Instruct()