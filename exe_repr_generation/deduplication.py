from datasketch import MinHash, MinHashLSH
import json
import os
import re

def get_minhash_signature(string):
    m = MinHash()
    for word in string.split():
        m.update(word.encode('utf8'))
    return m

def filter_code(strings, threshold):
    lsh = MinHashLSH(threshold=threshold, num_perm=128)

    minhashes = {}
    for string in strings:
        minhash = get_minhash_signature(string)
        lsh.insert(string, minhash)
        minhashes[string] = minhash

    similar_strings = set()
    for string in strings:
        minhash = minhashes[string]
        result = lsh.query(minhash)

        result_set = set(result)  
        result_set.discard(string)  
        
        similar_strings.update(result_set)  

    filtered_strings = strings - similar_strings
    return filtered_strings

def intersection_list(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    intersection = set1 & set2

    return list(intersection)    


def deduplication_filter_ids_list(fp, threshold):
    with open(fp, 'r') as f: data = json.load(f)
    print(len(data))

    str_set = set()
    for item in data: str_set.add(item["Code"])
    new_set = filter_code(str_set, threshold)


    res = []
    for item in data:
        if item["Code"] in new_set: res.append(item["ID"])
    print(len(res))
    return res
  

def rule_filter_ids_list(code_path):
    py_ids_list = []
    file = code_path + "python.json"
    with open(file, 'r') as f: data = json.load(f)
    py_dict = {}
    for item in data: 
        py_dict[item["ID"]] = item["Code"]
        py_ids_list.append(item["ID"])

    cpp_ids_list = []
    file = code_path + "cpp.json"
    with open(file, 'r') as f: data = json.load(f)
    cpp_dict = {}
    for item in data: 
        cpp_dict[item["ID"]] = item["Code"]
        cpp_ids_list.append(item["ID"])

    java_ids_list = []
    file = code_path + "java.json"
    with open(file, 'r') as f: data = json.load(f)
    java_dict = {}
    for item in data: 
        java_dict[item["ID"]] = item["Code"]
        java_ids_list.append(item["ID"])

    ids_list = intersection_list(py_ids_list, cpp_ids_list)
    ids_list = intersection_list(ids_list, java_ids_list)

    pattern_java = "boolean\s+\w+\s*\(.*?\)"
    pattern_cpp = "bool\s+\w+\s*\(.*?\)"

    for ids in ids_list:
        # py rules:

        # cpp rules:
        if ' or ' in py_dict[ids] and ' || ' not in cpp_dict[ids]: ids_list.remove(ids)
        elif 'vector < int > &' in cpp_dict[ids]: ids_list.remove(ids)    

        # java rules
        elif re.match(pattern_java, java_dict[ids]) and not re.match(pattern_cpp, cpp_dict[ids]): ids_list.remove(ids) 
        # elif 'boolean' in java_dict[ids] and 'bool' not in cpp_dict[ids]: ids_list.remove(ids) 
        elif ' or ' in py_dict[ids] and ' || ' not in java_dict[ids]: ids_list.remove(ids)        
        elif 'Integer' in java_dict[ids]: ids_list.remove(ids) 
        
    
    return ids_list

def filter_ids(fp, ids_list):
    with open(fp, 'r') as f: data = json.load(f)
    print(len(data))

    res = []
    for item in data:
        if item["ID"] in ids_list: res.append(item)
    print(len(res))

    train_json = json.dumps(res, ensure_ascii=False, indent=4)
    with open (fp, 'w+', encoding='utf-8') as file:
        file.write(train_json) 

def filter_dataset(root_save_path):
    ids_list = rule_filter_ids_list(root_save_path + 'NL/')

    path_list = [root_save_path + 'NL/']
    for path in path_list: 
        file_list = os.listdir(path)
        for file in file_list:
            filename = path + file
            ids_list = intersection_list(ids_list, deduplication_filter_ids_list(filename, threshold=0.85))
            print()

    path_list = [root_save_path + 'NL/', root_save_path + 'AST/', root_save_path + 'DFG/']
    for path in path_list: 
        file_list = os.listdir(path)
        for file in file_list:
            filename = path + file
            filter_ids(filename, ids_list)
            print() 

