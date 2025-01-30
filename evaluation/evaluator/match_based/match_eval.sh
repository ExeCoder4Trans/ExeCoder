EVAL_PATH=evaluation/eval_results

python evaluation/evaluator/match_based/match_eval.py \
    --input_file $EVAL_PATH/deepseek-coder-6.7b-instruct-transcoder_cpp-python.json \
    --codebleu
#    --naive 
