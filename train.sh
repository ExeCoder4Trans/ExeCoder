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

  # train

  deepspeed $ROOT/src/train.py \
      --model_name_or_path $MODEL_PATH/checkpoint/$MODEL \
      --data_path $MODEL_PATH/data/XLCoST-Instruct/$MODAL/train.json \
      --dev_data_path $MODEL_PATH/data/XLCoST-Instruct/$MODAL/dev.json \
      --cache_dir $MODEL_PATH/data_cache \
      --output_dir $MODEL_PATH/results \
      --num_train_epochs 1 \
      --model_max_length 3076 \
      --per_device_train_batch_size 16 \
      --per_device_eval_batch_size 8 \
      --gradient_accumulation_steps 2 \
      --evaluation_strategy "steps" \
      --eval_steps 100 \
      --save_strategy "steps" \
      --save_steps 100 \
      --save_total_limit 1 \
      --load_best_model_at_end True \
      --learning_rate 2e-6 \
      --warmup_steps 2 \
      --logging_steps 2 \
      --lr_scheduler_type "cosine" \
      --report_to "tensorboard" \
      --gradient_checkpointing True \
      --deepspeed $ROOT/src/configs/deepspeed_config_zero2.json \
      --fp16 True


done