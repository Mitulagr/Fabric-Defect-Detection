# To convert coordinates from csv file to txt file to use for training yolo model

import os
import cv2
import pandas as pd

data = pd.read_csv('Train_DefectBoxes_PrithviAI.csv')   
id = list(data["  image_id"])
blx = list(data["X"])
bly = list(data["Y"])
w = list(data["W"])
h = list(data["H"])
n = len(id)

for i in range (n) :
    if(os.path.exists(f"Defect\\{id[i]}")):
        blx[i] = float(blx[i])
        bly[i] = float(bly[i])
        w[i] = float(w[i])
        h[i] = float(h[i])
        f= open(f"Defect\\{id[i][:-4]}.txt","w+")
        f.write(f"0 {blx[i]} {bly[i]} {w[i]} {h[i]}")
        f.close()   
