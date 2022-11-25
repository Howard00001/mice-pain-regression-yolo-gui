# Yolo detection in docker

Mice landmark detection using yolov5. Running in docker to skip gpu configuration.

## Process

* pull docker image

```Shell
docker pull pytorch/pytorch:1.6.0-cuda10.1-cudnn7-devel
```

* start container with name "yolo_container"

```shell
docker run --gpus all --name yolo_container -v {path_to_code}:/home/files -it pytorch/pytorch:1.6.0-cuda10.1-cudnn7-devel
```

* install requirements in docker (inside container)

```shell
cd /home/files
apt-get install ffmpeg libsm6 libxext6  -y
pip install -r requirements.txt
```

* evaluation

put video file into code folder (ex. /home/files/test.mp4)

setting: --source {path_to _video} --facialFeature {path_to _output xml}

```shell
// inside container
python /home/files/yolov5/detect_xml.py --source /home/files/test.mp4 --facialFeature /home/files/out/test.xml --weights /home/files/yolov5/weights/mix.pt --clss pain

// outside container
docker exec -id yolo_container python /home/files/yolov5/detect_xml.py --source /home/files/test.mp4 --facialFeature /home/files/out/test.xml --weights /home/files/yolov5/weights/mix.pt --clss pain
```

output will save to  "path_to_code/out/test.xml"
