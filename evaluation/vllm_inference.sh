BASE_DATA_PATH=data/testset
BASE_MODEL_PATH=checkpoint
BASE_SAVED_PATH=evaluation/eval_results
model=deepseek-coder-6.7b-instruct
data_file=codenet_cpp-python.json

python evaluation/vllm_inference.py \
    --data_path $BASE_DATA_PATH/$data_file \
    --model_name_or_path $BASE_MODEL_PATH/$model \
    --saved_path $BASE_SAVED_PATH/$model-$data_file
#    --cot 
