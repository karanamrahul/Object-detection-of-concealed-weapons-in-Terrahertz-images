# Object-detection-of-concealed-weapons-in-Terrahertz-images

<div align="center">
  <img src="https://github.com/karanamrahul/Object-detection-of-concealed-weapons-in-Terrahertz-images/blob/main/result/logo.png?sanitize=true" width="110" height="110"/>
  <br/>
  <br/>
  <br/>
  
  <img src="https://github.com/karanamrahul/Object-detection-of-concealed-weapons-in-Terrahertz-images/blob/main/result/example.jpg?sanitize=true" width="400" height="300"/>
  <img src="https://github.com/karanamrahul/Object-detection-of-concealed-weapons-in-Terrahertz-images/blob/main/result/example_2.jpg?sanitize=true" width="400" height="300"/>
    
    
</div>

<br/>
<br/>

## Table of Contents

- [Getting Started](#getting-started)
- [File Directory Structure](#file-directory-structure)
- [Dataset](#input-dataset)
    - [Packages Needed](#packages-needed)
    - [TODO](#todo)
    - [Basic Usage](#Steps-to-Run-the-code-and-visualize-the-bbox)

   

### Getting Started

This project focuses on detecting concealed weapons in terahertz images and compares the performance of different object detection models.
### File Directory Structure
```
├── Code
|  ├── draw.py
|  ├── utils
├── Dataset
|  ├── Annotations
|  ├── JPEGImages
|  ├── labels
├── Results
|  |  ├── .png files
```
### Input Dataset 

```
/Dataset
    /Annotations
        /D_N_F1_CK_F_LA_WB_F_S_back_0907140917.xml
        /D_N_F1_CK_F_LA_WB_F_S_front_0907140917.xml
        /D_N_F1_CL_V_LA_LW_V_RA_back_0907141138.xml
        /...
        /T_P_M6_MD_F_LL_CK_F_C_WB_F_RT_front_0906154134.xml
    /JPEGImages
        /D_N_F1_CK_F_LA_WB_F_S_back_0907140917.jpg
        /D_N_F1_CK_F_LA_WB_F_S_front_0907140917.jpg
        /D_N_F1_CL_V_LA_LW_V_RA_back_0907141138.jpg
        /...
        /T_P_M6_MD_F_LL_CK_F_C_WB_F_RT_front_0906154134.jpg
    /labels
        /D_N_F1_CK_F_LA_WB_F_S_back_0907140917.txt
        /D_N_F1_CK_F_LA_WB_F_S_front_0907140917.txt
        /D_N_F1_CL_V_LA_LW_V_RA_back_0907141138.txt
        /...
        /T_P_M6_MD_F_LL_CK_F_C_WB_F_RT_front_0906154134.txt

```

The filename format is as follows:
Item Quantity_Whether the item exists_Model Number_Item1 Name_Item1 Direction_Item1 Position_(Item2 Name_Item2 Direction_Item2 Position_Item3 Name_Item3 Direction_Item3 Position_) Front and Back ID_Timestamp.jpg

- Number of Items: S (Single Item), D (Double Item), T (Triple Item).
- Whether the item exists: P (item exists), N (item does not exist).
- Model numbers: M1 (male size 1), M2 (male size 2), M3 (male size 3), M4 (male size 4), M5 (male size 5), M6 (male size 6), F1 (female size 1), F2 (Female No. 2), F3 (Female No. 3), F4 (Female No. 4).
- Item name: GA (gun), KK (chopping knife), SS (scissors), MD (dagger), CK (ceramic fruit knife), WB (mineral water bottle), KC (keychain), CP (mobile phone), CL (lighter), LW (wallet).
- Item orientation: F (front), V (back), L (left), R (right).
- Item location: LA (left arm), RA (right arm), S (abdomen), C (chest), B (back), W (waist), N (hip), LT (left thigh), RT (right thigh), LL (left calf), RL (right calf).
- Front and back identification: front (front image), back (reverse image).
- Timestamp: data collection time (month, day, hour, minute, second)


Please downlaod the dataset from this [drive link](https://drive.google.com/drive/folders/1Ncu-uFPR_P3P_GJd9t4KNWN24LCdgkAb?usp=share_link).

### Packages needed 

- OpenCV
- PIL
- Pytorch / Tensorflow

### TODO

- Develop a comprehensive pipeline to facilitate a thorough performance comparison among state-of-the-art models including YOLOv3, YOLOv4, RetinaNet, CenterNet, YOLOX, MobileNet, and EfficientNet. This meticulous evaluation will allow us to discern the nuances in their respective capabilities and efficiency, empowering us to make informed decisions based on quantitative results. *[ In Progress]*

- Engineer an instance segmentation pipeline that leverages the strengths of Mask-RCNN and U-Net, strategically modifying their network architectures to optimize overall accuracy. This intricate process will involve meticulous analysis and careful architectural adjustments, ensuring that we achieve superior segmentation performance and elevate the standards of accuracy in the realm of computer vision.

- Undertake a comprehensive exploration of evaluation metrics specifically tailored to image analysis. In this endeavor, we will delve into precision, recall, F1-score, intersection over union (IoU), mean average precision (mAP), and various other sophisticated metrics. By meticulously studying and implementing these metrics, we will gain a deep understanding of the quantitative assessment of image analysis algorithms and their performance.

- Embark on a research journey to merge spectral analysis with low-level features, augmenting the representation of concealed weapons detection. By integrating these two domains, we aim to extract richer and more comprehensive insights, enabling us to enhance the accuracy and effectiveness of concealed weapons detection systems. This scientific inquiry will unlock new possibilities in detecting and identifying concealed weapons with greater precision.

- Push the boundaries of innovation by combining the powerful techniques of Generative Adversarial Networks (GANs) and Convolutional Neural Networks (CNNs) to tackle the complex task of segmenting concealed weapons. This groundbreaking experiment will explore the synergistic effects of these advanced technologies, paving the way for enhanced detection and segmentation capabilities. Through this fusion of GANs and CNNs, we anticipate breakthroughs in concealed weapon identification and an unparalleled advancement in the field of computer vision.

### Steps to Run the code and visualize the bbox 

## Please change the filename and path according to your directory structure

1. Clone the repository:
```
git clone --recursive https://github.com/karanamrahul/Object-detection-of-concealed-weapons-in-Terrahertz-images.git
cd Object-detection-of-concealed-weapons-in-Terrahertz-images/

```

2. Run the code

```- [Basic Usage](#basic-usage)
python3 draw.py
```


### Credits

- [Active Terahertz Imaging Datasets
for Concealed Object Segmentation and Concealed Object Detection](https://linglix.github.io/THz_Dataset/)
- [Concealed Object Detection for Passive Millimeter-Wave Security Imaging Based on Task-Aligned Detection Transformer](https://arxiv.org/abs/2212.00313)
- [Real-time Concealed Object Detection from Passive Millimeter Wave Images Based on the YOLOv3 Algorithm](https://www.mdpi.com/1424-8220/20/6/1678)



