from tree_sitter import Language, Parser
import tree_sitter_python as tspy
import tree_sitter_cpp as tscpp
import tree_sitter_c_sharp as tscsharp
import tree_sitter_java as tsjava
import json
import graphviz
from tqdm import tqdm
from lang_processors import LangProcessor
from collections import deque
import os

PY_LANGUAGE = Language(tspy.language(), "python")
CPP_LANGUAGE = Language(tscpp.language(), "cpp")
CSHARP_LANGUAGE = Language(tscsharp.language(), "cpp")
JAVA_LANGUAGE = Language(tsjava.language(), "java")


def get_lang_processor(lang):
    if lang == 'csharp': lang = 'cpp'
    return LangProcessor.processors[lang]()

def get_code_from_node(node, source):
    start_byte = node.start_byte
    end_byte = node.end_byte
    return source[start_byte:end_byte].decode('utf-8')

def serialize(node, code, depth = 0):
    if node is None:
        return None
    if node.children:
        return {
            "source_text": get_code_from_node(node, code),
            "children": [serialize(child, code, depth + 1) for child in node.children],
            "type": node.type,
            "depth": str(depth)
        }
    else:
        return {
            "source_text": get_code_from_node(node, code),
            "type": node.type,
            "depth": str(depth)
        }

def parse_code(code, language):
    parser_dict = {"cpp": CPP_LANGUAGE, "python": PY_LANGUAGE, "csharp": CSHARP_LANGUAGE, 'java': JAVA_LANGUAGE}
    
    parser = Parser()
    parser.set_language(parser_dict[language])
    
    tree = parser.parse(bytes(code, 'utf8'))

    ast_json = serialize(tree.root_node, bytes(code, 'utf8'))
    return ast_json

def prune_non_leaf_nodes(json_data):
    if "children" in json_data and json_data["children"]:
        # 递归处理子节点
        pruned_children = [prune_non_leaf_nodes(child) for child in json_data["children"]]
        
        # 只保留子节点
        return {
            "source_text": "",
            "children": pruned_children,
            "type": json_data["type"],
            "depth": json_data["depth"]
        }
    else:
        # 叶节点，保留其内容
        return {
            "source_text": json_data["source_text"],
            "type": json_data["type"],
            "depth": json_data["depth"]
        }

def load_json(file):
    with open(file, 'r', encoding='utf8') as f:
        return json.load(f)

def ast2nodelist(json_data):
    if json_data is None:
        return []

    result = []
    queue = deque([(json_data, 0)]) 

    index = 0 

    while queue:
        current_node, depth = queue.popleft()  

        node_info = {
            "source_text": current_node["source_text"],
            "index": index,
            "children_index": [i for i in range(index + 1, index + 1 + (len(current_node.get("children", [])) if "children" in current_node else 0))],
            "depth": str(depth)
        }

        result.append(node_info)  
        index += 1  

        if "children" in current_node and current_node["children"]:
            for child in current_node["children"]:
                queue.append((child, depth + 1))

    return result

def nodelist2graph(dfg):
    nodes = dfg
    edges = []
    for node in dfg: 
        if len(node["children_index"]) != 0:
            for f_idx in node["children_index"]: edges.append((node["index"], f_idx))
    return (nodes, edges)

def create_name_dict(nodes, types):
    name = []
    if types == 'incident':
        for i in range(len(nodes)): 
           name.append(str(i))

    # elif types == 'friendship':
    #     for i in range(len(nodes)): 
    #         node_name = ""
    #         x = i
    #         while x:
    #             node_name += POPULAR_NAMES[x % 20] + " "
    #             x = int(x / 20)
    #         if node_name == '': node_name += POPULAR_NAMES[0] + " "
    #         name.append(node_name[: -1])

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
    if not source_node["source_text"] == "":
        output += "Node %s represents code %s.\n" % (
            source_node["index"],
            source_node["source_text"]
        ) 

  if edges:
    output += "In this graph:\n"

  for source_node in nodes:
    target_nodes = source_node["children_index"]
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

def code2ast_text(code, lang):
    ast_json = parse_code(code, lang)
    ast_json = prune_non_leaf_nodes(ast_json)
    nodelist = ast2nodelist(ast_json)
    graph = nodelist2graph(nodelist)
    graph2text = incident_encoder_with_text(graph)
    return graph2text

def generate_AST(root_save_path):
    # if not os.path.exists(save_path):
    #     os.makedirs(save_path)
    code_path = root_save_path + 'NL/'
    file_list = os.listdir(code_path)
    for file in file_list:
        file_path = code_path + file
        data = load_json(file_path)
        res = []
        lang = file.split('.')[0]
        processer = get_lang_processor(lang)

        for item in tqdm(data):
            item["AST"] = code2ast_text(processer.detokenize_code(item["Code"]), lang)
            res.append(item)


        dev_json = json.dumps(res, ensure_ascii=False, indent=4)
        save_path = root_save_path + 'AST/'
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        with open (save_path + lang + '.json', 'w+', encoding='utf-8') as file:
            file.write(dev_json)  

