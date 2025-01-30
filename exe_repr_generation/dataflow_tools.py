# Copyright (c) Microsoft Corporation. 
# Licensed under the MIT license.

from tree_sitter import Language, Parser
import pdb

import tree_sitter_python as tspython
import tree_sitter_go as tsgo
import tree_sitter_javascript as tsjavascript
import tree_sitter_php as tsphp
import tree_sitter_java as tsjava
import tree_sitter_c_sharp as tscsharp
import tree_sitter_cpp as tscpp
import tree_sitter_java as tsjava
from lang_processors import LangProcessor

import json
import re
from io import StringIO
import tokenize
from tqdm import tqdm
import os

PY_LANGUAGE = Language(tspython.language(), "python")
CPP_LANGUAGE = Language(tscpp.language(), "cpp")
CSHARP_LANGUAGE = Language(tscsharp.language(), "cpp")
JAVA_LANGUAGE = Language(tsjava.language(), "java")


def get_lang_processor(lang):
    if lang == 'csharp': lang = 'cpp'
    return LangProcessor.processors[lang]()

def remove_comments_and_docstrings(source, lang):
    if lang in ['python']:
        """
        Returns 'source' minus comments and docstrings.
        """
        io_obj = StringIO(source)
        out = ""
        prev_toktype = tokenize.INDENT
        last_lineno = -1
        last_col = 0
        for tok in tokenize.generate_tokens(io_obj.readline):
            token_type = tok[0]
            token_string = tok[1]
            start_line, start_col = tok[2]
            end_line, end_col = tok[3]
            ltext = tok[4]
            if start_line > last_lineno:
                last_col = 0
            if start_col > last_col:
                out += (" " * (start_col - last_col))
            # Remove comments:
            if token_type == tokenize.COMMENT:
                pass
            # This series of conditionals removes docstrings:
            elif token_type == tokenize.STRING:
                if prev_toktype != tokenize.INDENT:
                    # This is likely a docstring; double-check we're not inside an operator:
                    if prev_toktype != tokenize.NEWLINE:
                        if start_col > 0:
                            out += token_string
            else:
                out += token_string
            prev_toktype = token_type
            last_col = end_col
            last_lineno = end_line
        temp = []
        for x in out.split('\n'):
            if x.strip() != "":
                temp.append(x)
        return '\n'.join(temp)
    elif lang in ['ruby']:
        return source
    else:
        def replacer(match):
            s = match.group(0)
            if s.startswith('/'):
                return " "  # note: a space and not an empty string
            else:
                return s

        pattern = re.compile(
            r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
            re.DOTALL | re.MULTILINE
        )
        temp = []
        for x in re.sub(pattern, replacer, source).split('\n'):
            if x.strip() != "":
                temp.append(x)
        return '\n'.join(temp)


def tree_to_token_index(root_node):
    if (len(root_node.children) == 0 or root_node.type in ['string_literal', 'string',
                                                           'character_literal']) and root_node.type != 'comment':
        return [(root_node.start_point, root_node.end_point)]
    else:
        code_tokens = []
        for child in root_node.children:
            code_tokens += tree_to_token_index(child)
        return code_tokens


def tree_to_variable_index(root_node, index_to_code):
    if (len(root_node.children) == 0 or root_node.type in ['string_literal', 'string',
                                                           'character_literal']) and root_node.type != 'comment':
        index = (root_node.start_point, root_node.end_point)
        _, code = index_to_code[index]
        if root_node.type != code:
            return [(root_node.start_point, root_node.end_point)]
        else:
            return []
    else:
        code_tokens = []
        for child in root_node.children:
            code_tokens += tree_to_variable_index(child, index_to_code)
        return code_tokens


def index_to_code_token(index, code):
    start_point = index[0]
    end_point = index[1]
    if start_point[0] == end_point[0]:
        s = code[start_point[0]][start_point[1]:end_point[1]]
    else:
        s = ""
        s += code[start_point[0]][start_point[1]:]
        for i in range(start_point[0] + 1, end_point[0]):
            s += code[i]
        s += code[end_point[0]][:end_point[1]]
    return s


def DFG_python(root_node,index_to_code,states):
    assignment=['assignment','augmented_assignment','for_in_clause']
    if_statement=['if_statement']
    for_statement=['for_statement']
    while_statement=['while_statement']
    do_first_statement=['for_in_clause'] 
    def_statement=['default_parameter']
    states=states.copy() 
    if (len(root_node.children)==0 or root_node.type in ['string_literal','string','character_literal']) and root_node.type!='comment':        
        idx,code=index_to_code[(root_node.start_point,root_node.end_point)]
        if root_node.type==code:
            return [],states
        elif code in states:
            return [(code,idx,'comesFrom',[code],states[code].copy())],states
        else:
            if root_node.type=='identifier':
                states[code]=[idx]
            return [(code,idx,'comesFrom',[],[])],states
    elif root_node.type in def_statement:
        name=root_node.child_by_field_name('name')
        value=root_node.child_by_field_name('value')
        DFG=[]
        if value is None:
            indexs=tree_to_variable_index(name,index_to_code)
            for index in indexs:
                idx,code=index_to_code[index]
                DFG.append((code,idx,'comesFrom',[],[]))
                states[code]=[idx]
            return sorted(DFG,key=lambda x:x[1]),states
        else:
            name_indexs=tree_to_variable_index(name,index_to_code)
            value_indexs=tree_to_variable_index(value,index_to_code)
            temp,states=DFG_python(value,index_to_code,states)
            DFG+=temp            
            for index1 in name_indexs:
                idx1,code1=index_to_code[index1]
                for index2 in value_indexs:
                    idx2,code2=index_to_code[index2]
                    DFG.append((code1,idx1,'comesFrom',[code2],[idx2]))
                states[code1]=[idx1]   
            return sorted(DFG,key=lambda x:x[1]),states        
    elif root_node.type in assignment:
        if root_node.type=='for_in_clause':
            right_nodes=[root_node.children[-1]]
            left_nodes=[root_node.child_by_field_name('left')]
        else:
            if root_node.child_by_field_name('right') is None:
                return [],states
            left_nodes=[x for x in root_node.child_by_field_name('left').children if x.type!=',']
            right_nodes=[x for x in root_node.child_by_field_name('right').children if x.type!=',']
            if len(right_nodes)!=len(left_nodes):
                left_nodes=[root_node.child_by_field_name('left')]
                right_nodes=[root_node.child_by_field_name('right')]
            if len(left_nodes)==0:
                left_nodes=[root_node.child_by_field_name('left')]
            if len(right_nodes)==0:
                right_nodes=[root_node.child_by_field_name('right')]
        DFG=[]
        for node in right_nodes:
            temp,states=DFG_python(node,index_to_code,states)
            DFG+=temp
            
        for left_node,right_node in zip(left_nodes,right_nodes):
            left_tokens_index=tree_to_variable_index(left_node,index_to_code)
            right_tokens_index=tree_to_variable_index(right_node,index_to_code)
            temp=[]
            for token1_index in left_tokens_index:
                idx1,code1=index_to_code[token1_index]
                temp.append((code1,idx1,'computedFrom',[index_to_code[x][1] for x in right_tokens_index],
                             [index_to_code[x][0] for x in right_tokens_index]))
                states[code1]=[idx1]
            DFG+=temp        
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in if_statement:
        DFG=[]
        current_states=states.copy()
        others_states=[]
        tag=False
        if 'else' in root_node.type:
            tag=True
        for child in root_node.children:
            if 'else' in child.type:
                tag=True
            if child.type not in ['elif_clause','else_clause']:
                temp,current_states=DFG_python(child,index_to_code,current_states)
                DFG+=temp
            else:
                temp,new_states=DFG_python(child,index_to_code,states)
                DFG+=temp
                others_states.append(new_states)
        others_states.append(current_states)
        if tag is False:
            others_states.append(states)
        new_states={}
        for dic in others_states:
            for key in dic:
                if key not in new_states:
                    new_states[key]=dic[key].copy()
                else:
                    new_states[key]+=dic[key]
        for key in new_states:
            new_states[key]=sorted(list(set(new_states[key])))
        return sorted(DFG,key=lambda x:x[1]),new_states
    elif root_node.type in for_statement:
        DFG=[]
        for i in range(2):
            right_nodes=[x for x in root_node.child_by_field_name('right').children if x.type!=',']
            left_nodes=[x for x in root_node.child_by_field_name('left').children if x.type!=',']
            if len(right_nodes)!=len(left_nodes):
                left_nodes=[root_node.child_by_field_name('left')]
                right_nodes=[root_node.child_by_field_name('right')]
            if len(left_nodes)==0:
                left_nodes=[root_node.child_by_field_name('left')]
            if len(right_nodes)==0:
                right_nodes=[root_node.child_by_field_name('right')]
            for node in right_nodes:
                temp,states=DFG_python(node,index_to_code,states)
                DFG+=temp
            for left_node,right_node in zip(left_nodes,right_nodes):
                left_tokens_index=tree_to_variable_index(left_node,index_to_code)
                right_tokens_index=tree_to_variable_index(right_node,index_to_code)
                temp=[]
                for token1_index in left_tokens_index:
                    idx1,code1=index_to_code[token1_index]
                    temp.append((code1,idx1,'computedFrom',[index_to_code[x][1] for x in right_tokens_index],
                                 [index_to_code[x][0] for x in right_tokens_index]))
                    states[code1]=[idx1]
                DFG+=temp   
            if  root_node.children[-1].type=="block":
                temp,states=DFG_python(root_node.children[-1],index_to_code,states)
                DFG+=temp 
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in while_statement:  
        DFG=[]
        for i in range(2):
            for child in root_node.children:
                temp,states=DFG_python(child,index_to_code,states)
                DFG+=temp    
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states        
    else:
        DFG=[]
        for child in root_node.children:
            if child.type in do_first_statement:
                temp,states=DFG_python(child,index_to_code,states)
                DFG+=temp
        for child in root_node.children:
            if child.type not in do_first_statement:
                temp,states=DFG_python(child,index_to_code,states)
                DFG+=temp
        
        return sorted(DFG,key=lambda x:x[1]),states
        

def DFG_java(root_node,index_to_code,states):
    assignment=['assignment_expression']
    def_statement=['variable_declarator']
    increment_statement=['update_expression']
    if_statement=['if_statement','else']
    for_statement=['for_statement']
    enhanced_for_statement=['enhanced_for_statement']
    while_statement=['while_statement']
    do_first_statement=[]    
    states=states.copy()
    if (len(root_node.children)==0 or root_node.type in ['string_literal','string','character_literal']) and root_node.type!='comment':
        idx,code=index_to_code[(root_node.start_point,root_node.end_point)]
        if root_node.type==code:
            return [],states
        elif code in states:
            return [(code,idx,'comesFrom',[code],states[code].copy())],states
        else:
            if root_node.type=='identifier':
                states[code]=[idx]
            return [(code,idx,'comesFrom',[],[])],states
    elif root_node.type in def_statement:
        name=root_node.child_by_field_name('name')
        value=root_node.child_by_field_name('value')
        DFG=[]
        if value is None:
            indexs=tree_to_variable_index(name,index_to_code)
            for index in indexs:
                idx,code=index_to_code[index]
                DFG.append((code,idx,'comesFrom',[],[]))
                states[code]=[idx]
            return sorted(DFG,key=lambda x:x[1]),states
        else:
            name_indexs=tree_to_variable_index(name,index_to_code)
            value_indexs=tree_to_variable_index(value,index_to_code)
            temp,states=DFG_java(value,index_to_code,states)
            DFG+=temp            
            for index1 in name_indexs:
                idx1,code1=index_to_code[index1]
                for index2 in value_indexs:
                    idx2,code2=index_to_code[index2]
                    DFG.append((code1,idx1,'comesFrom',[code2],[idx2]))
                states[code1]=[idx1]   
            return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in assignment:
        left_nodes=root_node.child_by_field_name('left')
        right_nodes=root_node.child_by_field_name('right')
        DFG=[]
        temp,states=DFG_java(right_nodes,index_to_code,states)
        DFG+=temp            
        name_indexs=tree_to_variable_index(left_nodes,index_to_code)
        value_indexs=tree_to_variable_index(right_nodes,index_to_code)        
        for index1 in name_indexs:
            idx1,code1=index_to_code[index1]
            for index2 in value_indexs:
                idx2,code2=index_to_code[index2]
                DFG.append((code1,idx1,'computedFrom',[code2],[idx2]))
            states[code1]=[idx1]   
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in increment_statement:
        DFG=[]
        indexs=tree_to_variable_index(root_node,index_to_code)
        for index1 in indexs:
            idx1,code1=index_to_code[index1]
            for index2 in indexs:
                idx2,code2=index_to_code[index2]
                DFG.append((code1,idx1,'computedFrom',[code2],[idx2]))
            states[code1]=[idx1]
        return sorted(DFG,key=lambda x:x[1]),states   
    elif root_node.type in if_statement:
        DFG=[]
        current_states=states.copy()
        others_states=[]
        flag=False
        tag=False
        if 'else' in root_node.type:
            tag=True
        for child in root_node.children:
            if 'else' in child.type:
                tag=True
            if child.type not in if_statement and flag is False:
                temp,current_states=DFG_java(child,index_to_code,current_states)
                DFG+=temp
            else:
                flag=True
                temp,new_states=DFG_java(child,index_to_code,states)
                DFG+=temp
                others_states.append(new_states)
        others_states.append(current_states)
        if tag is False:
            others_states.append(states)
        new_states={}
        for dic in others_states:
            for key in dic:
                if key not in new_states:
                    new_states[key]=dic[key].copy()
                else:
                    new_states[key]+=dic[key]
        for key in new_states:
            new_states[key]=sorted(list(set(new_states[key])))
        return sorted(DFG,key=lambda x:x[1]),new_states
    elif root_node.type in for_statement:
        DFG=[]
        for child in root_node.children:
            temp,states=DFG_java(child,index_to_code,states)
            DFG+=temp
        flag=False
        for child in root_node.children:
            if flag:
                temp,states=DFG_java(child,index_to_code,states)
                DFG+=temp                
            elif child.type=="local_variable_declaration":
                flag=True
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in enhanced_for_statement:
        name=root_node.child_by_field_name('name')
        value=root_node.child_by_field_name('value')
        body=root_node.child_by_field_name('body')
        DFG=[]
        for i in range(2):
            temp,states=DFG_java(value,index_to_code,states)
            DFG+=temp       
            name_indexs=tree_to_variable_index(name,index_to_code)
            value_indexs=tree_to_variable_index(value,index_to_code)        
            for index1 in name_indexs:
                idx1,code1=index_to_code[index1]
                for index2 in value_indexs:
                    idx2,code2=index_to_code[index2]
                    DFG.append((code1,idx1,'computedFrom',[code2],[idx2]))
                states[code1]=[idx1]   
            temp,states=DFG_java(body,index_to_code,states)
            DFG+=temp                       
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in while_statement:  
        DFG=[]
        for i in range(2):
            for child in root_node.children:
                temp,states=DFG_java(child,index_to_code,states)
                DFG+=temp    
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states        
    else:
        DFG=[]
        for child in root_node.children:
            if child.type in do_first_statement:
                temp,states=DFG_java(child,index_to_code,states)
                DFG+=temp
        for child in root_node.children:
            if child.type not in do_first_statement:
                temp,states=DFG_java(child,index_to_code,states)
                DFG+=temp
        
        return sorted(DFG,key=lambda x:x[1]),states

def DFG_csharp(root_node,index_to_code,states):
    assignment=['assignment_expression']
    def_statement=['variable_declarator']
    increment_statement=['postfix_unary_expression']
    if_statement=['if_statement','else']
    for_statement=['for_statement']
    enhanced_for_statement=['for_each_statement']
    while_statement=['while_statement']
    do_first_statement=[]    
    states=states.copy()
    if (len(root_node.children)==0 or root_node.type in ['string_literal','string','character_literal']) and root_node.type!='comment':
        idx,code=index_to_code[(root_node.start_point,root_node.end_point)]
        if root_node.type==code:
            return [],states
        elif code in states:
            return [(code,idx,'comesFrom',[code],states[code].copy())],states
        else:
            if root_node.type=='identifier':
                states[code]=[idx]
            return [(code,idx,'comesFrom',[],[])],states
    elif root_node.type in def_statement:
        if len(root_node.children)==2:
            name=root_node.children[0]
            value=root_node.children[1]
        else:
            name=root_node.children[0]
            value=None
        DFG=[]
        if value is None:
            indexs=tree_to_variable_index(name,index_to_code)
            for index in indexs:
                idx,code=index_to_code[index]
                DFG.append((code,idx,'comesFrom',[],[]))
                states[code]=[idx]
            return sorted(DFG,key=lambda x:x[1]),states
        else:
            name_indexs=tree_to_variable_index(name,index_to_code)
            value_indexs=tree_to_variable_index(value,index_to_code)
            temp,states=DFG_csharp(value,index_to_code,states)
            DFG+=temp            
            for index1 in name_indexs:
                idx1,code1=index_to_code[index1]
                for index2 in value_indexs:
                    idx2,code2=index_to_code[index2]
                    DFG.append((code1,idx1,'comesFrom',[code2],[idx2]))
                states[code1]=[idx1]   
            return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in assignment:
        left_nodes=root_node.child_by_field_name('left')
        right_nodes=root_node.child_by_field_name('right')
        DFG=[]
        temp,states=DFG_csharp(right_nodes,index_to_code,states)
        DFG+=temp            
        name_indexs=tree_to_variable_index(left_nodes,index_to_code)
        value_indexs=tree_to_variable_index(right_nodes,index_to_code)        
        for index1 in name_indexs:
            idx1,code1=index_to_code[index1]
            for index2 in value_indexs:
                idx2,code2=index_to_code[index2]
                DFG.append((code1,idx1,'computedFrom',[code2],[idx2]))
            states[code1]=[idx1]   
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in increment_statement:
        DFG=[]
        indexs=tree_to_variable_index(root_node,index_to_code)
        for index1 in indexs:
            idx1,code1=index_to_code[index1]
            for index2 in indexs:
                idx2,code2=index_to_code[index2]
                DFG.append((code1,idx1,'computedFrom',[code2],[idx2]))
            states[code1]=[idx1]
        return sorted(DFG,key=lambda x:x[1]),states   
    elif root_node.type in if_statement:
        DFG=[]
        current_states=states.copy()
        others_states=[]
        flag=False
        tag=False
        if 'else' in root_node.type:
            tag=True
        for child in root_node.children:
            if 'else' in child.type:
                tag=True
            if child.type not in if_statement and flag is False:
                temp,current_states=DFG_csharp(child,index_to_code,current_states)
                DFG+=temp
            else:
                flag=True
                temp,new_states=DFG_csharp(child,index_to_code,states)
                DFG+=temp
                others_states.append(new_states)
        others_states.append(current_states)
        if tag is False:
            others_states.append(states)
        new_states={}
        for dic in others_states:
            for key in dic:
                if key not in new_states:
                    new_states[key]=dic[key].copy()
                else:
                    new_states[key]+=dic[key]
        for key in new_states:
            new_states[key]=sorted(list(set(new_states[key])))
        return sorted(DFG,key=lambda x:x[1]),new_states
    elif root_node.type in for_statement:
        DFG=[]
        for child in root_node.children:
            temp,states=DFG_csharp(child,index_to_code,states)
            DFG+=temp
        flag=False
        for child in root_node.children:
            if flag:
                temp,states=DFG_csharp(child,index_to_code,states)
                DFG+=temp                
            elif child.type=="local_variable_declaration":
                flag=True
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in enhanced_for_statement:
        name=root_node.child_by_field_name('left')
        value=root_node.child_by_field_name('right')
        body=root_node.child_by_field_name('body')
        DFG=[]
        for i in range(2):
            temp,states=DFG_csharp(value,index_to_code,states)
            DFG+=temp       
            name_indexs=tree_to_variable_index(name,index_to_code)
            value_indexs=tree_to_variable_index(value,index_to_code)        
            for index1 in name_indexs:
                idx1,code1=index_to_code[index1]
                for index2 in value_indexs:
                    idx2,code2=index_to_code[index2]
                    DFG.append((code1,idx1,'computedFrom',[code2],[idx2]))
                states[code1]=[idx1]   
            temp,states=DFG_csharp(body,index_to_code,states)
            DFG+=temp                       
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in while_statement:  
        DFG=[]
        for i in range(2):
            for child in root_node.children:
                temp,states=DFG_csharp(child,index_to_code,states)
                DFG+=temp    
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states        
    else:
        DFG=[]
        for child in root_node.children:
            if child.type in do_first_statement:
                temp,states=DFG_csharp(child,index_to_code,states)
                DFG+=temp
        for child in root_node.children:
            if child.type not in do_first_statement:
                temp,states=DFG_csharp(child,index_to_code,states)
                DFG+=temp
        
        return sorted(DFG,key=lambda x:x[1]),states


def DFG_ruby(root_node,index_to_code,states):
    assignment=['assignment','operator_assignment']
    if_statement=['if','elsif','else','unless','when']
    for_statement=['for']
    while_statement=['while_modifier','until']
    do_first_statement=[] 
    def_statement=['keyword_parameter']
    if (len(root_node.children)==0 or root_node.type in ['string_literal','string','character_literal']) and root_node.type!='comment':
        states=states.copy()
        idx,code=index_to_code[(root_node.start_point,root_node.end_point)]
        if root_node.type==code:
            return [],states
        elif code in states:
            return [(code,idx,'comesFrom',[code],states[code].copy())],states
        else:
            if root_node.type=='identifier':
                states[code]=[idx]
            return [(code,idx,'comesFrom',[],[])],states
    elif root_node.type in def_statement:
        name=root_node.child_by_field_name('name')
        value=root_node.child_by_field_name('value')
        DFG=[]
        if value is None:
            indexs=tree_to_variable_index(name,index_to_code)
            for index in indexs:
                idx,code=index_to_code[index]
                DFG.append((code,idx,'comesFrom',[],[]))
                states[code]=[idx]
            return sorted(DFG,key=lambda x:x[1]),states
        else:
            name_indexs=tree_to_variable_index(name,index_to_code)
            value_indexs=tree_to_variable_index(value,index_to_code)
            temp,states=DFG_ruby(value,index_to_code,states)
            DFG+=temp            
            for index1 in name_indexs:
                idx1,code1=index_to_code[index1]
                for index2 in value_indexs:
                    idx2,code2=index_to_code[index2]
                    DFG.append((code1,idx1,'comesFrom',[code2],[idx2]))
                states[code1]=[idx1]   
            return sorted(DFG,key=lambda x:x[1]),states        
    elif root_node.type in assignment:
        left_nodes=[x for x in root_node.child_by_field_name('left').children if x.type!=',']
        right_nodes=[x for x in root_node.child_by_field_name('right').children if x.type!=',']
        if len(right_nodes)!=len(left_nodes):
            left_nodes=[root_node.child_by_field_name('left')]
            right_nodes=[root_node.child_by_field_name('right')]
        if len(left_nodes)==0:
            left_nodes=[root_node.child_by_field_name('left')]
        if len(right_nodes)==0:
            right_nodes=[root_node.child_by_field_name('right')]
        if root_node.type=="operator_assignment":
            left_nodes=[root_node.children[0]]
            right_nodes=[root_node.children[-1]]

        DFG=[]
        for node in right_nodes:
            temp,states=DFG_ruby(node,index_to_code,states)
            DFG+=temp
            
        for left_node,right_node in zip(left_nodes,right_nodes):
            left_tokens_index=tree_to_variable_index(left_node,index_to_code)
            right_tokens_index=tree_to_variable_index(right_node,index_to_code)
            temp=[]
            for token1_index in left_tokens_index:
                idx1,code1=index_to_code[token1_index]
                temp.append((code1,idx1,'computedFrom',[index_to_code[x][1] for x in right_tokens_index],
                             [index_to_code[x][0] for x in right_tokens_index]))
                states[code1]=[idx1]
            DFG+=temp        
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in if_statement:
        DFG=[]
        current_states=states.copy()
        others_states=[]
        tag=False
        if 'else' in root_node.type:
            tag=True
        for child in root_node.children:
            if 'else' in child.type:
                tag=True
            if child.type not in if_statement:
                temp,current_states=DFG_ruby(child,index_to_code,current_states)
                DFG+=temp
            else:
                temp,new_states=DFG_ruby(child,index_to_code,states)
                DFG+=temp
                others_states.append(new_states)
        others_states.append(current_states)
        if tag is False:
            others_states.append(states)
        new_states={}
        for dic in others_states:
            for key in dic:
                if key not in new_states:
                    new_states[key]=dic[key].copy()
                else:
                    new_states[key]+=dic[key]
        for key in new_states:
            new_states[key]=sorted(list(set(new_states[key])))
        return sorted(DFG,key=lambda x:x[1]),new_states
    elif root_node.type in for_statement:
        DFG=[]
        for i in range(2):
            left_nodes=[root_node.child_by_field_name('pattern')]
            right_nodes=[root_node.child_by_field_name('value')]
            assert len(right_nodes)==len(left_nodes)
            for node in right_nodes:
                temp,states=DFG_ruby(node,index_to_code,states)
                DFG+=temp
            for left_node,right_node in zip(left_nodes,right_nodes):
                left_tokens_index=tree_to_variable_index(left_node,index_to_code)
                right_tokens_index=tree_to_variable_index(right_node,index_to_code)
                temp=[]
                for token1_index in left_tokens_index:
                    idx1,code1=index_to_code[token1_index]
                    temp.append((code1,idx1,'computedFrom',[index_to_code[x][1] for x in right_tokens_index],
                                 [index_to_code[x][0] for x in right_tokens_index]))
                    states[code1]=[idx1]
                DFG+=temp 
            temp,states=DFG_ruby(root_node.child_by_field_name('body'),index_to_code,states)
            DFG+=temp 
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in while_statement:  
        DFG=[]
        for i in range(2):
            for child in root_node.children:
                temp,states=DFG_ruby(child,index_to_code,states)
                DFG+=temp    
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states        
    else:
        DFG=[]
        for child in root_node.children:
            if child.type in do_first_statement:
                temp,states=DFG_ruby(child,index_to_code,states)
                DFG+=temp
        for child in root_node.children:
            if child.type not in do_first_statement:
                temp,states=DFG_ruby(child,index_to_code,states)
                DFG+=temp
        
        return sorted(DFG,key=lambda x:x[1]),states

def DFG_go(root_node,index_to_code,states):
    assignment=['assignment_statement',]
    def_statement=['var_spec']
    increment_statement=['inc_statement']
    if_statement=['if_statement','else']
    for_statement=['for_statement']
    enhanced_for_statement=[]
    while_statement=[]
    do_first_statement=[]    
    states=states.copy()
    if (len(root_node.children)==0 or root_node.type in ['string_literal','string','character_literal']) and root_node.type!='comment':
        idx,code=index_to_code[(root_node.start_point,root_node.end_point)]
        if root_node.type==code:
            return [],states
        elif code in states:
            return [(code,idx,'comesFrom',[code],states[code].copy())],states
        else:
            if root_node.type=='identifier':
                states[code]=[idx]
            return [(code,idx,'comesFrom',[],[])],states
    elif root_node.type in def_statement:
        name=root_node.child_by_field_name('name')
        value=root_node.child_by_field_name('value')
        DFG=[]
        if value is None:
            indexs=tree_to_variable_index(name,index_to_code)
            for index in indexs:
                idx,code=index_to_code[index]
                DFG.append((code,idx,'comesFrom',[],[]))
                states[code]=[idx]
            return sorted(DFG,key=lambda x:x[1]),states
        else:
            name_indexs=tree_to_variable_index(name,index_to_code)
            value_indexs=tree_to_variable_index(value,index_to_code)
            temp,states=DFG_go(value,index_to_code,states)
            DFG+=temp            
            for index1 in name_indexs:
                idx1,code1=index_to_code[index1]
                for index2 in value_indexs:
                    idx2,code2=index_to_code[index2]
                    DFG.append((code1,idx1,'comesFrom',[code2],[idx2]))
                states[code1]=[idx1]   
            return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in assignment:
        left_nodes=root_node.child_by_field_name('left')
        right_nodes=root_node.child_by_field_name('right')
        DFG=[]
        temp,states=DFG_go(right_nodes,index_to_code,states)
        DFG+=temp            
        name_indexs=tree_to_variable_index(left_nodes,index_to_code)
        value_indexs=tree_to_variable_index(right_nodes,index_to_code)        
        for index1 in name_indexs:
            idx1,code1=index_to_code[index1]
            for index2 in value_indexs:
                idx2,code2=index_to_code[index2]
                DFG.append((code1,idx1,'computedFrom',[code2],[idx2]))
            states[code1]=[idx1]   
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in increment_statement:
        DFG=[]
        indexs=tree_to_variable_index(root_node,index_to_code)
        for index1 in indexs:
            idx1,code1=index_to_code[index1]
            for index2 in indexs:
                idx2,code2=index_to_code[index2]
                DFG.append((code1,idx1,'computedFrom',[code2],[idx2]))
            states[code1]=[idx1]
        return sorted(DFG,key=lambda x:x[1]),states   
    elif root_node.type in if_statement:
        DFG=[]
        current_states=states.copy()
        others_states=[]
        flag=False
        tag=False
        if 'else' in root_node.type:
            tag=True
        for child in root_node.children:
            if 'else' in child.type:
                tag=True
            if child.type not in if_statement and flag is False:
                temp,current_states=DFG_go(child,index_to_code,current_states)
                DFG+=temp
            else:
                flag=True
                temp,new_states=DFG_go(child,index_to_code,states)
                DFG+=temp
                others_states.append(new_states)
        others_states.append(current_states)
        if tag is False:
            others_states.append(states)
        new_states={}
        for dic in others_states:
            for key in dic:
                if key not in new_states:
                    new_states[key]=dic[key].copy()
                else:
                    new_states[key]+=dic[key]
        for key in states:
            if key not in new_states:
                new_states[key]=states[key]
            else:
                new_states[key]+=states[key]
        for key in new_states:
            new_states[key]=sorted(list(set(new_states[key])))
        return sorted(DFG,key=lambda x:x[1]),new_states
    elif root_node.type in for_statement:
        DFG=[]
        for child in root_node.children:
            temp,states=DFG_go(child,index_to_code,states)
            DFG+=temp
        flag=False
        for child in root_node.children:
            if flag:
                temp,states=DFG_go(child,index_to_code,states)
                DFG+=temp                
            elif child.type=="for_clause":
                if child.child_by_field_name('update') is not None:
                    temp,states=DFG_go(child.child_by_field_name('update'),index_to_code,states)
                    DFG+=temp                 
                flag=True
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states
    else:
        DFG=[]
        for child in root_node.children:
            if child.type in do_first_statement:
                temp,states=DFG_go(child,index_to_code,states)
                DFG+=temp
        for child in root_node.children:
            if child.type not in do_first_statement:
                temp,states=DFG_go(child,index_to_code,states)
                DFG+=temp
        
        return sorted(DFG,key=lambda x:x[1]),states

    
    

def DFG_php(root_node,index_to_code,states):
    assignment=['assignment_expression','augmented_assignment_expression']
    def_statement=['simple_parameter']
    increment_statement=['update_expression']
    if_statement=['if_statement','else_clause']
    for_statement=['for_statement']
    enhanced_for_statement=['foreach_statement']
    while_statement=['while_statement']
    do_first_statement=[]    
    states=states.copy()
    if (len(root_node.children)==0 or root_node.type in ['string_literal','string','character_literal']) and root_node.type!='comment':
        idx,code=index_to_code[(root_node.start_point,root_node.end_point)]
        if root_node.type==code:
            return [],states
        elif code in states:
            return [(code,idx,'comesFrom',[code],states[code].copy())],states
        else:
            if root_node.type=='identifier':
                states[code]=[idx]
            return [(code,idx,'comesFrom',[],[])],states
    elif root_node.type in def_statement:
        name=root_node.child_by_field_name('name')
        value=root_node.child_by_field_name('default_value')
        DFG=[]
        if value is None:
            indexs=tree_to_variable_index(name,index_to_code)
            for index in indexs:
                idx,code=index_to_code[index]
                DFG.append((code,idx,'comesFrom',[],[]))
                states[code]=[idx]
            return sorted(DFG,key=lambda x:x[1]),states
        else:
            name_indexs=tree_to_variable_index(name,index_to_code)
            value_indexs=tree_to_variable_index(value,index_to_code)
            temp,states=DFG_php(value,index_to_code,states)
            DFG+=temp            
            for index1 in name_indexs:
                idx1,code1=index_to_code[index1]
                for index2 in value_indexs:
                    idx2,code2=index_to_code[index2]
                    DFG.append((code1,idx1,'comesFrom',[code2],[idx2]))
                states[code1]=[idx1]   
            return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in assignment:
        left_nodes=root_node.child_by_field_name('left')
        right_nodes=root_node.child_by_field_name('right')
        DFG=[]
        temp,states=DFG_php(right_nodes,index_to_code,states)
        DFG+=temp            
        name_indexs=tree_to_variable_index(left_nodes,index_to_code)
        value_indexs=tree_to_variable_index(right_nodes,index_to_code)        
        for index1 in name_indexs:
            idx1,code1=index_to_code[index1]
            for index2 in value_indexs:
                idx2,code2=index_to_code[index2]
                DFG.append((code1,idx1,'computedFrom',[code2],[idx2]))
            states[code1]=[idx1]   
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in increment_statement:
        DFG=[]
        indexs=tree_to_variable_index(root_node,index_to_code)
        for index1 in indexs:
            idx1,code1=index_to_code[index1]
            for index2 in indexs:
                idx2,code2=index_to_code[index2]
                DFG.append((code1,idx1,'computedFrom',[code2],[idx2]))
            states[code1]=[idx1]
        return sorted(DFG,key=lambda x:x[1]),states   
    elif root_node.type in if_statement:
        DFG=[]
        current_states=states.copy()
        others_states=[]
        flag=False
        tag=False
        if 'else' in root_node.type:
            tag=True
        for child in root_node.children:
            if 'else' in child.type:
                tag=True
            if child.type not in if_statement and flag is False:
                temp,current_states=DFG_php(child,index_to_code,current_states)
                DFG+=temp
            else:
                flag=True
                temp,new_states=DFG_php(child,index_to_code,states)
                DFG+=temp
                others_states.append(new_states)
        others_states.append(current_states)
        new_states={}
        for dic in others_states:
            for key in dic:
                if key not in new_states:
                    new_states[key]=dic[key].copy()
                else:
                    new_states[key]+=dic[key]
        for key in states:
            if key not in new_states:
                new_states[key]=states[key]
            else:
                new_states[key]+=states[key]
        for key in new_states:
            new_states[key]=sorted(list(set(new_states[key])))
        return sorted(DFG,key=lambda x:x[1]),new_states
    elif root_node.type in for_statement:
        DFG=[]
        for child in root_node.children:
            temp,states=DFG_php(child,index_to_code,states)
            DFG+=temp
        flag=False
        for child in root_node.children:
            if flag:
                temp,states=DFG_php(child,index_to_code,states)
                DFG+=temp                
            elif child.type=="assignment_expression":               
                flag=True
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in enhanced_for_statement:
        name=None
        value=None
        for child in root_node.children:
            if child.type=='variable_name' and value is None:
                value=child
            elif child.type=='variable_name' and name is None:
                name=child
                break
        body=root_node.child_by_field_name('body')
        DFG=[]
        for i in range(2):
            temp,states=DFG_php(value,index_to_code,states)
            DFG+=temp       
            name_indexs=tree_to_variable_index(name,index_to_code)
            value_indexs=tree_to_variable_index(value,index_to_code)        
            for index1 in name_indexs:
                idx1,code1=index_to_code[index1]
                for index2 in value_indexs:
                    idx2,code2=index_to_code[index2]
                    DFG.append((code1,idx1,'computedFrom',[code2],[idx2]))
                states[code1]=[idx1]   
            temp,states=DFG_php(body,index_to_code,states)
            DFG+=temp                       
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in while_statement:  
        DFG=[]
        for i in range(2):
            for child in root_node.children:
                temp,states=DFG_php(child,index_to_code,states)
                DFG+=temp    
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states        
    else:
        DFG=[]
        for child in root_node.children:
            if child.type in do_first_statement:
                temp,states=DFG_php(child,index_to_code,states)
                DFG+=temp
        for child in root_node.children:
            if child.type not in do_first_statement:
                temp,states=DFG_php(child,index_to_code,states)
                DFG+=temp
        
        return sorted(DFG,key=lambda x:x[1]),states


def DFG_javascript(root_node,index_to_code,states):
    assignment=['assignment_pattern','augmented_assignment_expression']
    def_statement=['variable_declarator']
    increment_statement=['update_expression']
    if_statement=['if_statement','else']
    for_statement=['for_statement']
    enhanced_for_statement=[]
    while_statement=['while_statement']
    do_first_statement=[]    
    states=states.copy()
    if (len(root_node.children)==0 or root_node.type in ['string_literal','string','character_literal']) and root_node.type!='comment':
        idx,code=index_to_code[(root_node.start_point,root_node.end_point)]
        if root_node.type==code:
            return [],states
        elif code in states:
            return [(code,idx,'comesFrom',[code],states[code].copy())],states
        else:
            if root_node.type=='identifier':
                states[code]=[idx]
            return [(code,idx,'comesFrom',[],[])],states
    elif root_node.type in def_statement:
        name=root_node.child_by_field_name('name')
        value=root_node.child_by_field_name('value')
        DFG=[]
        if value is None:
            indexs=tree_to_variable_index(name,index_to_code)
            for index in indexs:
                idx,code=index_to_code[index]
                DFG.append((code,idx,'comesFrom',[],[]))
                states[code]=[idx]
            return sorted(DFG,key=lambda x:x[1]),states
        else:
            name_indexs=tree_to_variable_index(name,index_to_code)
            value_indexs=tree_to_variable_index(value,index_to_code)
            temp,states=DFG_javascript(value,index_to_code,states)
            DFG+=temp            
            for index1 in name_indexs:
                idx1,code1=index_to_code[index1]
                for index2 in value_indexs:
                    idx2,code2=index_to_code[index2]
                    DFG.append((code1,idx1,'comesFrom',[code2],[idx2]))
                states[code1]=[idx1]   
            return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in assignment:
        left_nodes=root_node.child_by_field_name('left')
        right_nodes=root_node.child_by_field_name('right')
        DFG=[]
        temp,states=DFG_javascript(right_nodes,index_to_code,states)
        DFG+=temp            
        name_indexs=tree_to_variable_index(left_nodes,index_to_code)
        value_indexs=tree_to_variable_index(right_nodes,index_to_code)        
        for index1 in name_indexs:
            idx1,code1=index_to_code[index1]
            for index2 in value_indexs:
                idx2,code2=index_to_code[index2]
                DFG.append((code1,idx1,'computedFrom',[code2],[idx2]))
            states[code1]=[idx1]   
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in increment_statement:
        DFG=[]
        indexs=tree_to_variable_index(root_node,index_to_code)
        for index1 in indexs:
            idx1,code1=index_to_code[index1]
            for index2 in indexs:
                idx2,code2=index_to_code[index2]
                DFG.append((code1,idx1,'computedFrom',[code2],[idx2]))
            states[code1]=[idx1]
        return sorted(DFG,key=lambda x:x[1]),states   
    elif root_node.type in if_statement:
        DFG=[]
        current_states=states.copy()
        others_states=[]
        flag=False
        tag=False
        if 'else' in root_node.type:
            tag=True
        for child in root_node.children:
            if 'else' in child.type:
                tag=True
            if child.type not in if_statement and flag is False:
                temp,current_states=DFG_javascript(child,index_to_code,current_states)
                DFG+=temp
            else:
                flag=True
                temp,new_states=DFG_javascript(child,index_to_code,states)
                DFG+=temp
                others_states.append(new_states)
        others_states.append(current_states)
        if tag is False:
            others_states.append(states)        
        new_states={}
        for dic in others_states:
            for key in dic:
                if key not in new_states:
                    new_states[key]=dic[key].copy()
                else:
                    new_states[key]+=dic[key]
        for key in states:
            if key not in new_states:
                new_states[key]=states[key]
            else:
                new_states[key]+=states[key]
        for key in new_states:
            new_states[key]=sorted(list(set(new_states[key])))
        return sorted(DFG,key=lambda x:x[1]),new_states
    elif root_node.type in for_statement:
        DFG=[]
        for child in root_node.children:
            temp,states=DFG_javascript(child,index_to_code,states)
            DFG+=temp
        flag=False
        for child in root_node.children:
            if flag:
                temp,states=DFG_javascript(child,index_to_code,states)
                DFG+=temp                
            elif child.type=="variable_declaration":               
                flag=True
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states
    elif root_node.type in while_statement:  
        DFG=[]
        for i in range(2):
            for child in root_node.children:
                temp,states=DFG_javascript(child,index_to_code,states)
                DFG+=temp    
        dic={}
        for x in DFG:
            if (x[0],x[1],x[2]) not in dic:
                dic[(x[0],x[1],x[2])]=[x[3],x[4]]
            else:
                dic[(x[0],x[1],x[2])][0]=list(set(dic[(x[0],x[1],x[2])][0]+x[3]))
                dic[(x[0],x[1],x[2])][1]=sorted(list(set(dic[(x[0],x[1],x[2])][1]+x[4])))
        DFG=[(x[0],x[1],x[2],y[0],y[1]) for x,y in sorted(dic.items(),key=lambda t:t[0][1])]
        return sorted(DFG,key=lambda x:x[1]),states    
    else:
        DFG=[]
        for child in root_node.children:
            if child.type in do_first_statement:
                temp,states=DFG_javascript(child,index_to_code,states)
                DFG+=temp
        for child in root_node.children:
            if child.type not in do_first_statement:
                temp,states=DFG_javascript(child,index_to_code,states)
                DFG+=temp
        
        return sorted(DFG,key=lambda x:x[1]),states


     




dfg_function={
    'python':DFG_python,
    'java':DFG_java,
    'ruby':DFG_ruby,
    'go':DFG_go,
    'php':DFG_php,
    'javascript':DFG_javascript,
    'c_sharp':DFG_csharp,
}

tsl_function = {
    'python': tspython,
    'java': tsjava,
    'go': tsgo,
    'php': tsphp,
    'javascript': tsjavascript,
    'c_sharp': tscsharp,
}

def calc_dataflow_match(references, candidate, lang):
    return corpus_dataflow_match([references], [candidate], lang)

def corpus_dataflow_match(references, candidates, lang):   
    if lang == 'php':
        LANGUAGE = Language(tsl_function[lang].language_php(), lang)
    else:
        LANGUAGE = Language(tsl_function[lang].language(), lang)
    parser = Parser()
    parser.set_language(LANGUAGE)
    parser = [parser,dfg_function[lang]]
    match_count = 0
    total_count = 0

    for i in range(len(candidates)):
        references_sample = references[i]
        candidate = candidates[i] 
        for reference in references_sample:
            try:
                candidate=remove_comments_and_docstrings(candidate,'java')
            except:
                pass    
            try:
                reference=remove_comments_and_docstrings(reference,'java')
            except:
                pass  

            cand_dfg = get_data_flow(candidate, parser)
            ref_dfg = get_data_flow(reference, parser)
            
            normalized_cand_dfg = normalize_dataflow(cand_dfg)
            normalized_ref_dfg = normalize_dataflow(ref_dfg)

            if len(normalized_ref_dfg) > 0:
                total_count += len(normalized_ref_dfg)
                for dataflow in normalized_ref_dfg:
                    if dataflow in normalized_cand_dfg:
                            match_count += 1
                            normalized_cand_dfg.remove(dataflow)  
    if total_count == 0:
        print("WARNING: There is no reference data-flows extracted from the whole corpus, and the data-flow match score degenerates to 0. Please consider ignoring this score.")
        return 0
    score = match_count / total_count
    return score

def get_data_flow(code, parser):
    try:
        tree = parser[0].parse(bytes(code,'utf8'))    
        root_node = tree.root_node  
        tokens_index=tree_to_token_index(root_node)     
        code=code.split('\n')
        code_tokens=[index_to_code_token(x,code) for x in tokens_index]  
        index_to_code={}
        for idx,(index,code) in enumerate(zip(tokens_index,code_tokens)):
            index_to_code[index]=(idx,code)  
        try:
            DFG,_=parser[1](root_node,index_to_code,{}) 
        except:
            DFG=[]
        DFG=sorted(DFG,key=lambda x:x[1])
        indexs=set()
        for d in DFG:
            if len(d[-1])!=0:
                indexs.add(d[1])
            for x in d[-1]:
                indexs.add(x)
        new_DFG=[]
        for d in DFG:
            if d[1] in indexs:
                new_DFG.append(d)
        codes=code_tokens
        dfg=new_DFG
    except:
        codes=code.split()
        dfg=[]
    #merge nodes
    dic={}
    for d in dfg:
        if d[1] not in dic:
            dic[d[1]]=d
        else:
            dic[d[1]]=(d[0],d[1],d[2],list(set(dic[d[1]][3]+d[3])),list(set(dic[d[1]][4]+d[4])))
    DFG=[]
    for d in dic:
        DFG.append(dic[d])
    dfg=DFG
    return dfg

def normalize_dataflow_item(dataflow_item):
    var_name = dataflow_item[0]
    var_pos = dataflow_item[1]
    relationship = dataflow_item[2]
    par_vars_name_list = dataflow_item[3]
    par_vars_pos_list = dataflow_item[4]

    var_names = list(set(par_vars_name_list+[var_name]))
    norm_names = {}
    for i in range(len(var_names)):
        norm_names[var_names[i]] = 'var_'+str(i)

    norm_var_name = norm_names[var_name]
    relationship = dataflow_item[2]
    norm_par_vars_name_list = [norm_names[x] for x in par_vars_name_list]

    return (norm_var_name, relationship, norm_par_vars_name_list)

def normalize_dataflow(dataflow):
    var_dict = {}
    i = 0
    normalized_dataflow = []
    for item in dataflow:
        var_name = item[0]
        relationship = item[2]
        par_vars_name_list = item[3]
        for name in par_vars_name_list:
            if name not in var_dict:
                var_dict[name] = 'var_'+str(i)
                i += 1
        if var_name not in var_dict:
            var_dict[var_name] = 'var_'+str(i)
            i+= 1
        normalized_dataflow.append((var_dict[var_name], relationship, [var_dict[x] for x in par_vars_name_list]))
    return normalized_dataflow
    
def gen_dataflow(code, lang):   
    if lang == 'php':
        LANGUAGE = Language(tsl_function[lang].language_php(), lang)
    else:
        LANGUAGE = Language(tsl_function[lang].language(), lang)
    parser = Parser()
    parser.set_language(LANGUAGE)
    parser = [parser,dfg_function[lang]]

    dfg = get_data_flow(code, parser)

    # dfg = normalize_dataflow(dfg)
    
    return dfg


def build_graph(data):
    node_map = {}
    result = []

    for text, index, node_type, father_texts, father_indices in data:
        node = {
            "source_text": text,
            "index": index,
            "father_index": father_indices,
            "depth": 0  
        }
        node_map[index] = node

    for index in node_map:
        node = node_map[index]
        father_indices = node["father_index"]
        
        max_depth = -1
        for father_index in father_indices:
            if father_index in node_map: 
                if node_map[father_index]["depth"] > max_depth: max_depth = node_map[father_index]["depth"]
        node["depth"] = max_depth + 1


        # if father_indices:
        #     max_depth = max(node_map[father_index]["depth"] for father_index in father_indices if father_index in node_map)
        #     node["depth"] = max_depth + 1

        result.append(node)
    

    result = rename_id(result)

    return result
    # return json.dumps(result, indent=4)

def rename_id(graph):
    idx = -1
    idx_dict = {}
    for item in graph:
        idx += 1
        idx_dict[str(item["index"])] = idx
    for item in graph:
        item["index"] = idx_dict[str(item["index"])]
        for i in range(len(item["father_index"])):
            if str(item["father_index"][i]) in idx_dict.keys():
                item["father_index"][i] = idx_dict[str(item["father_index"][i])]
            else:
                item["father_index"][i] = 0
    return graph




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


INTEGER_NAMES = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
]

POPULAR_NAMES = [
    "James",
    "Robert",
    "John",
    "Michael",
    "David",
    "Mary",
    "Patricia",
    "Jennifer",
    "Linda",
    "Elizabeth",
    "William",
    "Richard",
    "Joseph",
    "Thomas",
    "Christopher",
    "Barbara",
    "Susan",
    "Jessica",
    "Sarah",
    "Karen",
]

def create_name_dict(nodes, types):
    name = []
    if types == 'incident':
        for i in range(len(nodes)): 
           name.append(str(i))

    elif types == 'friendship':
        for i in range(len(nodes)): 
            node_name = ""
            x = i
            while x:
                node_name += POPULAR_NAMES[x % 20] + " "
                x = int(x / 20)
            if node_name == '': node_name += POPULAR_NAMES[0] + " "
            name.append(node_name[: -1])

    elif types == 'var':
        for i in range(len(nodes)): 
            name.append(nodes[i]["source_text"])

    name_dict = {}
    for ind, value in enumerate(name):
        name_dict[ind] = value
    return name_dict

def create_node_string(name_dict, nnodes):
  node_string = ""
  for i in range(nnodes - 1):
    node_string += name_dict[i] + ", "
  node_string += "and " + name_dict[nnodes - 1]
  return node_string


def incident_encoder_with_text(graph):
  """Encoding a graph with its incident lists."""
  nodes, edges = graph
  name_dict = create_name_dict(nodes, types = "incident")
  nodes_string = create_node_string(name_dict, len(nodes))
  output = "G describes a graph among nodes %s.\n" % nodes_string
  
  output += "In this graph:\n"
  for source_node in nodes:
    output += "Node %s represents variable %s.\n" % (
        source_node["index"],
        source_node["source_text"]
    ) 

  if edges:
    output += "In this graph:\n"

  for source_node in nodes:
    target_nodes = source_node["father_index"]
    target_nodes_str = ""
    nedges = 0
    for target_node in target_nodes:
      target_nodes_str += name_dict[target_node] + ", "
      nedges += 1
    if nedges > 1:
      output += "Node %s is connected to nodes %s.\n" % (
          source_node["index"],
          target_nodes_str[:-2],
      )
    elif nedges == 1:
      output += "Node %d is connected to node %s.\n" % (
          source_node["index"],
          target_nodes_str[:-2],
      )
  return output


def code2dfg_text(code, lang):
    dataflow = gen_dataflow(code, code2DFG[lang])
    dfg = build_graph(dataflow)
    return json.dumps(dfg)

def code2dfg(code, lang):
    dataflow = gen_dataflow(code, code2DFG[lang])
    dfg = build_graph(dataflow)
    return dfg


def dfg2graph(dfg):
    nodes = dfg
    edges = []
    for node in dfg: 
        if len(node["father_index"]) != 0:
            for f_idx in node["father_index"]: edges.append((node["index"], f_idx))
    return (nodes, edges)

def load_json(file):
    with open(file, 'r', encoding='utf8') as f:
        return json.load(f)



def generate_DFG(root_save_path, graph_encoder = incident_encoder_with_text):
    code_path = root_save_path + 'NL/'
    file_list = os.listdir(code_path)
    for file in file_list:
        file_path = code_path + file
        data = load_json(file_path)
        lang = file.split('.')[0]
        processer = get_lang_processor(lang)

        data = load_json(code_path + lang + ".json")
        res = []

        for item in tqdm(data):
            dfg = code2dfg(processer.detokenize_code(item["Code"]), lang)
            if len(dfg) == 0: 
                item["DFG"] = ""
            else:
                graph = dfg2graph(dfg)
                graph2text = graph_encoder(graph)
                item["DFG"] = graph2text
            res.append(item)

        save_path = root_save_path + 'DFG/'
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        dev_json = json.dumps(res, ensure_ascii=False, indent=4)
        with open (save_path + lang + ".json", 'w+', encoding='utf-8') as file:
            file.write(dev_json)  

