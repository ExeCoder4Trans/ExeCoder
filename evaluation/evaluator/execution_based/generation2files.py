import json
import os


def load_json(fp):
    if not os.path.exists(fp):
        return dict()

    with open(fp, 'r', encoding='utf8') as f:
        return json.load(f)

def wash(code):
    codes = code.split('```')
    codes = codes[1]
    codes = codes.split('\n')[1: ]
    res = ""
    for line in codes: res += line + '\n'    
    return res

def out2file(fp):
    translation_dir = "evaluation/evaluator/execution_based/evaluation_code"
    lang_dict = {"c#": "cs", "python": "py", "cpp": "cpp", "c": "c", "java": "java", "php": "php", "go": "go"}

    data = load_json(fp)

    for item in data:
        code = item["generated_output"]
        if len(code.split('```')) >= 2: code = wash(code)        
        name = item["id"]
        lang = item["pair"].split('-')[1]
        filename = translation_dir + '/' + name + '.' + lang_dict[lang]
        with open(filename, 'w') as f: f.writelines(code)


def new_out2file(fp, translation_dir):
    lang_dict = {"c#": "cs", "python": "py", "cpp": "cpp", "c": "c", "java": "java", "php": "php", "go": "go"}

    data = load_json(fp)

    for item in data:
        code = item["generated_output"]
        if len(code.split('```')) >= 2: code = wash(code)        
        name = item["id"]
        lang = item["pair"].split('-')[1]
        filename = translation_dir + '/' + name + '.' + lang_dict[lang]
        with open(filename, 'w') as f: f.writelines(code)


# out2file("deepseek-coder-6.7b-instruct_codenet_cpp-python.json")
