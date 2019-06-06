export MINIO_ACCESS_KEY=minio
export MINIO_SECRET_KEY=miniokey
export AWS_ACCESS_KEY_ID=minio
export AWS_SECRET_ACCESS_KEY=miniokey
export WORLD_NAME=hard_track
export ROS_AWS_REGION=us-east-1
export AWS_REGION=us-east-1
export AWS_DEFAULT_REGION=us-east-1
export MODEL_S3_PREFIX=rl-deepracer-sagemaker
export MODEL_S3_BUCKET=bucket
export LOCAL=True
# export S3_ENDPOINT_URL=http://$(hostname):9000
export S3_ENDPOINT_URL=http://minio1:9000

export MARKOV_PRESET_FILE=deepracer.py
export LOCAL_ENV_VAR_JSON_PATH=$(readlink -f ./env_vars.json)
# export LOCAL_ENV_VAR_JSON_PATH=/Users/jonathantse/projects/deepracer/rl_coach/env_vars.json

# ipython rl_deepracer_coach_robomaker.py