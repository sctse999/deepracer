
docker run --rm \
--name dr \
--env-file ./robomaker.env \
--network sagemaker-local \
-p 8080:5900 \
-v $(pwd)/aws-robomaker-sample-application-deepracer/simulation_ws/src:/app/robomaker-deepracer/simulation_ws/src \
-it nabcrr/deepracer_robomaker:console "./run.sh build distributed_training.launch"