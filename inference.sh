#!/usr/bin/bash


nvidia-smi

ROOT=ExecCoder
MODEL_PATH=$ROOT


BASE_DATA_PATH=$ROOT/data/testset
BASE_MODEL_PATH=$ROOT/checkpoint
BASE_SAVED_PATH=$ROOT/evaluation/eval_results

data_file1=transcoder_cpp-python.json
data_file2=transcoder_python-cpp.json
data_file3=transcoder_cpp-java.json
data_file4=transcoder_java-cpp.json
data_file5=transcoder_java-python.json
data_file6=transcoder_python-java.json

EVAL_PATH=$ROOT/evaluation/eval_results



MODALs=("code")
MODELS=("deepseek-coder-6.7b-instruct")
models=("code")


length=${#MODALs[@]}

for (( i=0; i<$length; i++ ))
do
  MODAL=${MODALs[$i]}
  MODEL=${MODELS[$i]}
  model=${models[$i]}

  # inference
   python $ROOT/evaluation/vllm_inference.py \
       --data_path $BASE_DATA_PATH/$data_file1 \
       --model_name_or_path $BASE_MODEL_PATH/$model \
       --saved_path $BASE_SAVED_PATH/$model-$data_file1
   #    --cot

   python $ROOT/evaluation/vllm_inference.py \
       --data_path $BASE_DATA_PATH/$data_file2 \
       --model_name_or_path $BASE_MODEL_PATH/$model \
       --saved_path $BASE_SAVED_PATH/$model-$data_file2
   #    --cot

  python $ROOT/evaluation/vllm_inference.py \
      --data_path $BASE_DATA_PATH/$data_file3 \
      --model_name_or_path $BASE_MODEL_PATH/$model \
      --saved_path $BASE_SAVED_PATH/$model-$data_file3
  #    --cot

  python $ROOT/evaluation/vllm_inference.py \
     --data_path $BASE_DATA_PATH/$data_file4 \
     --model_name_or_path $BASE_MODEL_PATH/$model \
     --saved_path $BASE_SAVED_PATH/$model-$data_file4
  #    --cot

  python $ROOT/evaluation/vllm_inference.py \
     --data_path $BASE_DATA_PATH/$data_file5 \
     --model_name_or_path $BASE_MODEL_PATH/$model \
     --saved_path $BASE_SAVED_PATH/$model-$data_file5
  #    --cot

  python $ROOT/evaluation/vllm_inference.py \
     --data_path $BASE_DATA_PATH/$data_file6 \
     --model_name_or_path $BASE_MODEL_PATH/$model \
     --saved_path $BASE_SAVED_PATH/$model-$data_file6
  #    --cot

done
