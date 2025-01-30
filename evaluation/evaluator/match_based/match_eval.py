# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors and The HuggingFace Inc. team.
# Copyright (c) 2018, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import argparse
import numpy as np
import json
import re
from collections import defaultdict

from CodeBLEU import calc_code_bleu
from bleu import compute_bleu, _bleu_json_select

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

RE_FORMAT_1 = r"```\S+\n(.*?)```"
RE_FORMAT_2 = r"```\S+\n(.*?)"
code2DFG = {
    'c': 'c_sharp',
    'java': 'java',
    'php': 'php',
    'pytorch': 'python',
    'python': 'python',
    'mxnet': 'python',
    'go': 'go',
    'c#': 'c_sharp',
    'tensorflow': 'python',
    'javascript': 'javascript',
    'cpp': 'c_sharp',
    'paddle': 'python'
}


def group_code_bleu(pre_references, hypothesis, ref_languages):
    grouped_data = defaultdict(list)

    # group by ref_languages
    for pre, hypo, lang in zip(pre_references, hypothesis, ref_languages):
        grouped_data[lang].append((pre, hypo))
    
    code_bleu_score_dict = {}

    for lang in grouped_data.keys():
        grouped_value = grouped_data[lang]
        pre, hypo = [_[0] for _ in grouped_value], [_[1] for _ in grouped_value]
        if lang in 'python, c#, java, c, cpp, go, javascript, php':
            code_bleu_score_dict[lang] = calc_code_bleu.get_codebleu_list([pre], hypo, code2DFG[lang])

    code_bleu_score_dict['mean'] = np.mean(list(code_bleu_score_dict.values()))

    return code_bleu_score_dict


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
    if len(codes[0]) > len(codes[1]): codes = codes[0]
    else: codes = codes[1]
    codes = codes.split('\n')
    res = ""
    for line in codes: res += line + '\n'    
    return res

def wash_2(code):
    codes = code.split('```')
    codes = codes[1]
    codes = codes.split('\n')[1: ]
    res = ""
    for line in codes: res += line + '\n'    
    return res

def wash(code):
    if len(code.split('```')) > 2: code = wash_2(code)
    elif len(code.split('```')) == 2: code = wash_1(code)
    code = remove_text(remove_main_function(code))
    return code


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", default=None, type=str)
    parser.add_argument('--codebleu', action='store_true')
    parser.add_argument('--naive', action='store_true')
    args = parser.parse_args()
    dev_accs = []
    hypothesis = []
    pre_references = []
    ref_languages = []
    data = json.load(open(args.input_file, 'r'))
    for json_data in data:
        reference_code = json_data['Code2']
        prediction_code = re.search(RE_FORMAT_1, json_data['generated_output'], re.DOTALL)
        if prediction_code is None:
            prediction_code = re.search(RE_FORMAT_2, json_data['generated_output'], re.DOTALL)
        
        # prediction_code = remove_main_function(prediction_code.group(1)) if prediction_code else remove_main_function(json_data['generated_output']) # No Code in generated content
        
        prediction_code = wash(prediction_code.group(1)) if prediction_code else wash(json_data['generated_output']) # No Code in generated content

        
        if args.naive:
            dev_accs.append(reference_code.strip() == reference_code.strip())
            hypothesis.append(reference_code.strip())
        else:
            dev_accs.append(reference_code.strip() == prediction_code.strip())
            hypothesis.append(prediction_code.strip())
        pre_references.append(reference_code.strip())
        ref_languages.append(json_data['pair'].split('-')[1])

    bleu, _, _, _, _, _ = compute_bleu(list(map(lambda x: [x.split()], pre_references)), list(map(lambda x: x.split(), hypothesis)), smooth=True)

    if args.codebleu:
        codebleu = group_code_bleu(pre_references, hypothesis, ref_languages)
        result = {'em': round(np.mean(dev_accs) * 100, 2), 'bleu': bleu, 'codebleu': codebleu}
    else:
        result = {'em': round(np.mean(dev_accs) * 100, 2), 'bleu': bleu}
    print(result)

# python evaluation\evaluator\match_based\test_trans.py --input_file mixture_test_instruct_1000.json-deepseek-coder-6.7b-instruct-checkpoint-5000 --codebleu
