# Fabric-Defect-Detection
Detecting Defects in Fabric using YOLO to minimize wastage in its fabric due to various defects in the fabric. If there is even a single defect in any of the cut pieces, the whole piece  goes to waste.

Training and Testing Data given by PrithviAI

For Model and Yolo Files : https://drive.google.com/drive/folders/17mR3MJN8RAkwODiRGC-0Ro9LUfSxmunx?usp=sharing

Python / Jupyter Files : 

1) bad_seg.py : To segerate the images having defect from all the training images
2) yolo_format.py : To convert coordinates from csv file to txt file to use for training yolo model
3) Training_Model_Defect.ipynb : For training the yolo model using around 600 Images
4) Testing_Images.ipynb : For testing the model on around 1100 Images
5) csv_write.py : Converting Test Image Coordinates and Type from json file to csv file

csv/json Files : 

1) Train_DefectType_PrithviAI.csv
2) Train_DefectBoxes_PrithviAI.csv
3) img_name_type.json
4) img_name_box.json
5) Final_DefectType_Xtreme.csv
6) Final_DefectBoxes_Xtreme.csv
