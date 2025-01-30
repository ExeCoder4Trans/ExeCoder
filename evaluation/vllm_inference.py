from vllm import LLM, SamplingParams
import json
from transformers import AutoTokenizer
from pathlib import Path


def generate_batch(examples, tokenizer, llm, model: str):
    stop = None
    # if 'deepseek-coder' in model:
    #     prompts = [
    #         tokenizer.apply_chat_template([{'role': 'user', 'content': ex['instruction'] + '\n' + ex['input'] }], tokenize=False, add_generation_prompt=True)
    #         for ex in examples
    #     ]
    # else:
    #     raise NotImplementedError()
    prompts = [
        tokenizer.apply_chat_template([{'role': 'user', 'content': ex['instruction'] + '\n' + ex['input'] }], tokenize=False, add_generation_prompt=True)
        for ex in examples
    ]

    # Create a sampling params object.
    sampling_params = SamplingParams(
        temperature=0.0,
        # top_p=0.95,
        # top_p=1e-9,
        max_tokens=2048,
        stop=stop
    )

    print("Sample prompt: {}".format(prompts[0]))
    outputs = llm.generate(prompts, sampling_params)
    for i in range(len(examples)):
        examples[i]['generated_output'] = outputs[i].outputs[0].text

    return examples

def generate_main(data_path: str, model_name_or_path: str, saved_path: str, cot: bool=False):
    examples = json.load(open(data_path, 'r'))
    def _convert_for_sft(ex):
        ex['instruction'] = ex["instruction"] + "\nYou need first write a step-by-step outline and then write the code."
        return ex
    
    if cot:
        examples = [_convert_for_sft(x) for x in examples]
        saved_path = saved_path.replace(".jsonl", ".cot.jsonl")

    print(model_name_or_path)
    print("Model `{}`, COT = {}:{}".format(model_name_or_path, cot, model_name_or_path))
    print("Saved path: {}".format(saved_path))
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=True)
    print("load tokenizer {} from {} over.".format(tokenizer.__class__, model_name_or_path))

    # Create an LLM.
    llm = LLM(
        model=model_name_or_path,
        pipeline_parallel_size=1,
        tensor_parallel_size=8,
        max_num_seqs=512,
        max_num_batched_tokens=8192,
        max_model_len=4096,
        gpu_memory_utilization=0.85,
        trust_remote_code=True,
        dtype="float32"
    )
    
    generated_examples = generate_batch(examples, tokenizer, llm, model_name_or_path)    
    print("Generate all over!!!")
    with open(saved_path, 'w', encoding='utf-8') as fw:
        json.dump(generated_examples, fw, indent=4)
        # for ex in generated_examples:
        #     fw.write(json.dumps(ex) + '\n')
        print("Save {} processed examples into {} over!".format(len(generated_examples), saved_path))

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, default=Path(__file__).parent.joinpath(f"data/intput.json").as_posix())
    parser.add_argument('--model_name_or_path', type=str, default='deepseek-ai/deepseek-coder-7b-instruct')
    parser.add_argument('--saved_path', type=str, default=f'output/output.json')
    parser.add_argument('--cot', action='store_true', default=False)
    args = parser.parse_args()

    generate_main(
        data_path=args.data_path,
        model_name_or_path=args.model_name_or_path,
        saved_path=args.saved_path,
        cot=args.cot,
    )
