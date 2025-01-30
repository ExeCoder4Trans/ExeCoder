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

# evaluation
  python $ROOT/evaluation/evaluator/execution_based/transcoder_eval.py \
      --source_lang "cpp" \
      --target_lang "python" \
      --eval_file $EVAL_PATH/$model-$data_file1 \
      --model $model

  python $ROOT/evaluation/evaluator/execution_based/transcoder_eval.py \
      --source_lang "python" \
      --target_lang "cpp" \
      --eval_file $EVAL_PATH/$model-$data_file2 \
      --model $model

  python $ROOT/evaluation/evaluator/execution_based/transcoder_eval.py \
      --source_lang "cpp" \
      --target_lang "java" \
      --eval_file $EVAL_PATH/$model-$data_file3 \
      --model $model

  python $ROOT/evaluation/evaluator/execution_based/transcoder_eval.py \
      --source_lang "java" \
      --target_lang "cpp" \
      --eval_file $EVAL_PATH/$model-$data_file4 \
      --model $model

  python $ROOT/evaluation/evaluator/execution_based/transcoder_eval.py \
      --source_lang "java" \
      --target_lang "python" \
      --eval_file $EVAL_PATH/$model-$data_file5 \
      --model $model

  python $ROOT/evaluation/evaluator/execution_based/transcoder_eval.py \
      --source_lang "python" \
      --target_lang "java" \
      --eval_file $EVAL_PATH/$model-$data_file6 \
      --model $model

done