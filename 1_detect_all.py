import os

# path config
code_path = "E:/exp_trial"
video_path = "E:/exp_trial/data/video/test"
save_path = "E:/exp_trial/data/xml/test"
env_pythonexe = 'C:/Users/x/.conda/envs/micelab/python.exe'

model = code_path+"/yolov5/weights/mix.pt"

for root, dirs, files in os.walk(video_path):
    root = root.replace('\\','/')
    newRoot = root.replace(video_path,save_path)
    if not os.path.isdir(newRoot):
        os.makedirs(newRoot)
    for file in files:
        if (file.find('.MP4')==-1 and file.find('.mp4')==-1):
            continue
        file_path = root + '/' + file
        newFile = newRoot + '/' + file
        newXml = newFile.replace(".MP4",".xml")
        newXml = newXml.replace(".mp4",".xml")
        # if not os.path.isfile(newXml):
        open(newXml, "w").close()
        os.system(env_pythonexe+ " " + code_path + "/yolov5/detect_xml.py --source {:} --facialFeature {:} --weights {:}".format(
            file_path, newXml , model))

