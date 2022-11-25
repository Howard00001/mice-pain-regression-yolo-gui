import os

p = "G:/code/mice/dataset/video/2018-Aug-CCI/B/0_health_base.MP4"
w = './weights/mix.pt'
n = 'test'

os.system('C:/Users/x/.conda/envs/exp-yolo/python.exe detect.py --source {:} --weights {:}'.format(p,w))

# C:/Users/x/.conda/envs/exp-yolo/python.exe G:/code/mice/old_version/yolo_detect/yolov5/detect.py --source "G:/code/mice/dataset/video/2018-Aug-CCI/B/0_health_base.MP4" --weights "G:/code/mice/old_version/yolo_detect/yolov5/weights/mix.pt"