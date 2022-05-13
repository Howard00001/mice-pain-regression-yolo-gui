# Mice-pain-regression-steps
 Easy step by step for mice pain regression base structure

## Structure

![structure](.\data\structure.png)

* Based on the paper https://hdl.handle.net/11296/a55786
  - Replaced the Mask-RCNN part with YOLOv5 to detect landmarks

## Features

* Break each step into different jupyter notebooks for more detail operations
* More efficient to generate batch of models and results

## Installation

```Shell
pip install -r requirements.txt
```

* Install pytorch (torch==1.6.0+cu101, torchvision==0.7.0+cu101) manually from the official website

## Step

* 1_detect_all : Detect and output the xml of landmarks
* 2_generateFromXml : convert xml to csv (easier to process).
* 3_traintest : train SVR model and test (plot)
