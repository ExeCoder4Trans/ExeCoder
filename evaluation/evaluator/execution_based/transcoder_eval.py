import subprocess
import typing
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd
from pathlib import Path
from subprocess import Popen, PIPE
import argparse
import shutil
import json
import re

COMPILED = "#Compiled"
COMPILATION = "#Compilation"
ROOT_PATH = "ExeCoder/"
JAVA_HOME = ROOT_PATH + "tools/jdk-10.0.2/bin/"



def eval_state(proc: typing.Any, proc_name: str) -> typing.Tuple[str, typing.Optional[str]]:
    results = ""
    stderr = b""
    try:
        try:
            result, stderr = proc.communicate(timeout=120)
        except subprocess.TimeoutExpired:
            c = (
                    "kill `ps aux | grep '"
                    + proc_name
                    + "' | grep -v jupyter | grep -v grep | awk '{print($2)}'`"
            )
            subprocess.run(
                c, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            return "timeout", None, proc_name
        results = result.decode("utf8", errors="replace")
        success, n_test = results.split("#Results:")[-1].split(",")
        if int(success) == int(n_test):
            return "success" + ':' + str(success) + ',' + str(n_test), None, proc_name
            # return "success", None, proc_name
        else:
            return "failure" + ':' + str(success) + ',' + str(n_test), result.decode("utf-8",
                                                                                     errors="replace"), proc_name
            # return "failure", result.decode("utf-8", errors="replace"), proc_name
    except KeyboardInterrupt:
        raise
    except:
        if COMPILATION not in results or COMPILED in results:
            return "error", stderr.decode("utf-8", errors="replace"), proc_name
        else:
            return "compilation", stderr.decode("utf-8", errors="replace"), proc_name


MAX_VIRTUAL_MEMORY = 2 * 1024 * 1024 * 1024  # 2 GB


def limit_virtual_memory(max_virtual_memory):
    # We do a soft limit in order to be able to change the limit later if needed
    return f"ulimit -S -v {max_virtual_memory}"


def run_python_program(script_path, i, tmp_dir):
    name = os.path.basename(script_path).split(".")[0]
    proc = subprocess.Popen(
        # f"{limit_virtual_memory(MAX_VIRTUAL_MEMORY)}; python {script_path}",
        f"{limit_virtual_memory(MAX_VIRTUAL_MEMORY)}; python {script_path}",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        # executable="/bin/bash",
    )
    res = eval_state(proc, f"python {script_path}")
    # res = eval_state(proc, f"python {script_path}")
    return res, i


def run_java_program(script_path, i, tmp_dir):
    name = os.path.basename(script_path).split(".")[0]
    classname = name.split('/')[-1]
    filepath = script_path[: len(script_path) - len(name) - 6]
    cmd = f"{os.path.join(JAVA_HOME, 'java')} -cp {filepath} {classname}"
    # print(cmd)
    proc = subprocess.Popen(
        f"{limit_virtual_memory(MAX_VIRTUAL_MEMORY)}; echo '{COMPILATION}'; {os.path.join(JAVA_HOME, 'javac')} {script_path} && echo '{COMPILED}' && {os.path.join(JAVA_HOME, 'java')} -cp {filepath} {classname}",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        # executable="/bin/bash",
    )
    res = eval_state(proc, classname + '.java')
    return res, i


def run_cpp_program(script_path, i, tmp_dir):
    name = os.path.basename(script_path).split(".")[0]
    proc = subprocess.Popen(
        f"{limit_virtual_memory(MAX_VIRTUAL_MEMORY)}; echo '{COMPILATION}'; g++ {script_path} -o {tmp_dir}/{name}_cpp && echo '{COMPILED}' && {tmp_dir}/{name}_cpp",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        # executable="/bin/bash",
    )
    res = eval_state(proc, f"{tmp_dir}/{name}_cpp")
    return res, i


def run_c_program(script_path, i):
    folder = os.path.dirname(script_path)
    name = os.path.basename(script_path).split(".")[0]
    proc = subprocess.Popen(
        f"{limit_virtual_memory(MAX_VIRTUAL_MEMORY)}; cd {folder} && echo '{COMPILATION}'; gcc {name}.c -o {name}_c && echo '{COMPILED}' && ./{name}_c",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        executable="/bin/bash",
    )
    res = eval_state(proc, f"{name}_c")
    return res, i


def load_json(fp):
    if not os.path.exists(fp):
        return dict()

    with open(fp, 'r', encoding='utf8') as f:
        return json.load(f)


# def remove_main_function(cpp_code):
#     # return cpp_code
#     code = cpp_code.split('\n')
#     res = ""
#     for line in code:
#         if "int main" in line: break
#         res += line + '\n'
#     return res

# def wash(code):
#     codes = code.split('```')
#     codes = codes[1]
#     codes = codes.split('\n')[1: ]
#     res = ""
#     for line in codes: res += line + '\n'
#     return res


def remove_main_function(cpp_code):
    # return cpp_code
    code = cpp_code.split('\n')
    res = ""
    for line in code:
        if "int main" in line: break
        res += line + '\n'
    return res


def remove_text(code):
    codes = code.split('\n')
    l = len(codes) - 1
    end = -1
    for i in range(len(codes)):
        if len(codes[l - i]) == 0: continue
        if codes[l - i][0] == ' ' or codes[l - i][0] == '}':
            end = l - i
            break

    res = ""
    for i in range(end + 1): res += codes[i] + '\n'
    return res


def wash_1(code):
    codes = code.split('```')
    if len(codes[0]) > len(codes[1]):
        codes = codes[0]
    else:
        codes = codes[1]
    codes = codes.split('\n')
    res = ""
    for line in codes: res += line + '\n'
    return res


def wash_2(code):
    codes = code.split('```')
    codes = codes[1]
    codes = codes.split('\n')[1:]
    res = ""
    for line in codes: res += line + '\n'
    return res


def extract_java_functions(org_code):
    pattern = r'^\s*static\s+\w+\s+\w+\s*\(.*?\)'
    code = org_code.replace('public static', 'static')
    code = code.replace('public', 'static')
    code = code.split('\n')
    res = ""
    flag = 0
    left = 0
    for code_line in code:
        if 'static' in code_line and ' main ' not in code_line and 'main(' not in code_line and ' Main ' not in code_line and 'Main(' not in code_line and re.match(
            pattern, code_line): flag = 1
        if flag == 1:
            res += code_line + '\n'
            left += code_line.count('{')
            left -= code_line.count('}')
            if left == 0: return res
    if res == "":
        pattern = r'^\s*\w+\s+\w+\s*\(.*?\)'
        code = org_code.replace('public static', 'static')
        code = code.replace('public', 'static')
        code = code.split('\n')
        res = ""
        flag = 0
        left = 0
        for code_line in code:
            if flag == 0 and ' main ' not in code_line and ' Main ' not in code_line and re.match(pattern, code_line):
                if 'static' not in code_line: code_line = 'static ' + code_line
                flag = 1
            if flag == 1:
                res += code_line + '\n'
                left += code_line.count('{')
                left -= code_line.count('}')
                if left == 0: return res
    return res


def out2file(fp, translation_dir, target_lang):
    template_dir = ROOT_PATH + "evaluation/evaluator/execution_based/transcoder_template/" + target_lang
    lang_dict = {"c#": "cs", "python": "py", "cpp": "cpp", "c": "c", "java": "java", "php": "php", "go": "go"}

    file_list = os.listdir(template_dir)
    ids_set = set()
    for file in file_list: ids_set.add(file.split('.')[0])

    data = load_json(fp)
    for item in data:
        code = item["generated_output"]

        # if len(code.split('```')) >= 2: code = wash(code)
        # code = remove_main_function(code)

        if len(code.split('```')) > 2:
            code = wash_2(code)
        elif len(code.split('```')) == 2:
            code = wash_1(code)
        code = remove_text(remove_main_function(code))
        if target_lang == 'java': code = extract_java_functions(code)

        ids = item["id"].split('-')[-1]
        lang = item["pair"].split('-')[1]
        if ids not in ids_set: continue

        test_file_name = template_dir + '/' + ids + '.' + lang_dict[lang]

        with open(test_file_name, 'r') as f:
            test_file = f.read()

        gen_file = test_file.replace("//TOFILL", code).replace("#TOFILL", code)
        filename = translation_dir + '/' + ids + '.' + lang_dict[lang]
        # print(filename)
        with open(filename, 'w') as f:
            f.writelines(gen_file)


def main(args):
    print('testing translations')
    translation_dir = ROOT_PATH + "evaluation/evaluator/execution_based/transcoder_evaluation_code/" + args.model + '/' + args.source_lang + '_to_' + args.target_lang
    if os.path.exists(translation_dir):
        shutil.rmtree(translation_dir)
    os.makedirs(translation_dir)

    tmp_dir = ROOT_PATH + "evaluation/evaluator/execution_based/transcoder_evaluation_generation"
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.makedirs(tmp_dir)

    repo = ROOT_PATH + "evaluation/evaluator/execution_based/transcoder_evaluation_reports/" + args.model
    os.makedirs(repo, exist_ok=True)

    out2file(args.eval_file, translation_dir, args.target_lang)

    compile_failed = []
    test_passed = []
    test_failed = []
    test_failed_details = []
    runtime_failed = []
    runtime_failed_details = []
    infinite_loop = []
    success_case = 0
    all_case = 0
    compiled_case = 0

    main_results = []
    script_paths = os.listdir(translation_dir)
    for i in range(len(script_paths)): script_paths[i] = translation_dir + '/' + script_paths[i]
    max_workers = 8

    if args.target_lang == "cpp":
        evluator = run_cpp_program
    elif args.target_lang == "python":
        evluator = run_python_program
    elif args.target_lang == "java":
        evluator = run_java_program

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_script = {executor.submit(evluator, script_path, i, tmp_dir): script_path for i, script_path in
                            enumerate(script_paths)}

        for future in as_completed(future_to_script):
            script_path = future_to_script[future]
            try:
                res, i = future.result()
                main_results.append((res, i))
            except Exception as exc:
                print(f'{script_path} generated an exception: {exc}')

    # for pair in main_results:
    #     out, idx = pair
    #     res, details, file = out
    #     if res == "success": test_passed.append(file.split('/')[-1])
    #     elif res == "error": runtime_failed.append(file.split('/')[-1])
    #     elif res == "failure": test_failed.append(file.split('/')[-1])
    #     elif res == "compilation": compile_failed.append(file.split('/')[-1])
    #     elif res == "timeout": infinite_loop.append(file.split('/')[-1])

    for pair in main_results:
        out, idx = pair
        res, details, file = out
        if "success" in res:
            test_passed.append(file.split('/')[-1])
            success, n_test = res.split(':')[-1].split(',')
            success_case += int(success)
            compiled_case += int(n_test)
            all_case += int(n_test)
        elif res == "error":
            runtime_failed.append(file.split('/')[-1])
            all_case += int(10)
        elif "failure" in res:
            test_failed.append(file.split('/')[-1])
            success, n_test = res.split(':')[-1].split(',')
            success_case += int(success)
            compiled_case += int(n_test)
            all_case += int(n_test)
        elif res == "compilation":
            compile_failed.append(file.split('/')[-1])
            all_case += int(10)
        elif res == "timeout":
            infinite_loop.append(file.split('/')[-1])
            all_case += int(10)

    test_failed = list(set(test_failed))
    runtime_failed = list(set(runtime_failed))
    compile_failed = list(set(compile_failed))
    infinite_loop = list(set(infinite_loop))
    test_passed = list(set(test_passed))

    # To avoid the total sum is higher than 100%, if an instance is in infinite_loop and test_failed at the same time, then it will be counted as test_failed
    for instance in infinite_loop[:]:
        if instance in test_failed:
            infinite_loop.remove(instance)

    txt_fp = Path(repo).joinpath(str(args.source_lang) + "_to_" + str(args.target_lang) + ".txt")
    with open(txt_fp, "w", encoding="utf-8") as report:
        report.writelines("Total Instances: {}\n\n".format(
            len(test_passed) + len(compile_failed) + len(runtime_failed) + len(test_failed) + len(infinite_loop)))
        report.writelines("Total Correct: {}\n".format(len(test_passed)))
        report.writelines("Total Runtime Failed: {}\n".format(len(runtime_failed)))
        report.writelines("Total Compilation Failed: {}\n".format(len(compile_failed)))
        report.writelines("Total Test Failed: {}\n".format(len(test_failed)))
        report.writelines("Total Infinite Loop: {}\n\n".format(len(infinite_loop)))

        report.writelines("Accuracy: {}\n".format((len(test_passed) / (
                    len(test_passed) + len(compile_failed) + len(runtime_failed) + len(test_failed) + len(
                infinite_loop))) * 100))
        report.writelines("Success Case Rate: {}\n".format((success_case / all_case) * 100))
        report.writelines("Pass Case Rate: {}\n".format((success_case / compiled_case) * 100))
        report.writelines("Successful Compilation: {}\n".format(((len(test_passed) + len(test_failed)) / (
                    len(test_passed) + len(compile_failed) + len(runtime_failed) + len(test_failed) + len(
                infinite_loop))) * 100))
        report.writelines("Runtime Rate: {}\n".format((len(runtime_failed) / (
                    len(test_passed) + len(compile_failed) + len(runtime_failed) + len(test_failed) + len(
                infinite_loop))) * 100))
        report.writelines("Compilation Rate: {}\n".format((len(compile_failed) / (
                    len(test_passed) + len(compile_failed) + len(runtime_failed) + len(test_failed) + len(
                infinite_loop))) * 100))
        report.writelines("Test Failed Rate: {}\n".format((len(test_failed) / (
                    len(test_passed) + len(compile_failed) + len(runtime_failed) + len(test_failed) + len(
                infinite_loop))) * 100))
        report.writelines("Infinite Loop Rate: {}\n\n".format((len(infinite_loop) / (
                    len(test_passed) + len(compile_failed) + len(runtime_failed) + len(test_failed) + len(
                infinite_loop))) * 100))

        report.writelines(
            "=================================================================================================\n")
        report.writelines("Failed Test Files: {} \n".format(test_failed))
        report.writelines("Failed Test Details: {} \n".format(test_failed_details))
        report.writelines(
            "=================================================================================================\n")
        report.writelines("Runtime Error Files: {} \n".format(runtime_failed))
        report.writelines("Runtime Error Details: {} \n".format(runtime_failed_details))
        report.writelines(
            "=================================================================================================\n")
        report.writelines("Compilation Error Files: {} \n".format(compile_failed))
        report.writelines(
            "=================================================================================================\n")
        report.writelines("Infinite Loop Files: {} \n".format(infinite_loop))
        report.writelines(
            "=================================================================================================\n")

    ordered_unsuccessful_fp = Path(repo).joinpath(
        str(args.source_lang) + "_to_" + str(args.target_lang) + "_ordered_unsuccessful.txt")
    with open(ordered_unsuccessful_fp, 'w') as f:
        for unsuccessful_instance in compile_failed + runtime_failed + test_failed + infinite_loop:
            f.write(f"{unsuccessful_instance}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='execute avatar tests')
    parser.add_argument('--source_lang',
                        help='source language to use for code translation. should be one of [Python,Java,C,C++,Go]',
                        required=True, type=str)
    parser.add_argument('--target_lang',
                        help='target language to use for code translation. should be one of [Python,Java,C,C++,Go]',
                        required=True, type=str)
    parser.add_argument('--eval_file', help='file for evaluation', required=True, type=str)
    parser.add_argument('--model', help='model for evaluation', required=True, type=str)
    args = parser.parse_args()

    main(args)

