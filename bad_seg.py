# To segerate the images having defect from all the training images

import pandas as pd
import shutil


data = pd.read_csv('Train_DefectType_PrithviAI.csv')   
id = list(data["images id"])
flag = list(data["defect_flag"])
n = len(id)

for i in range (n) :
    if(flag[i]==1) :
        try :
            shutil.copy(f"Images\\{id[i]}","Defect")
        except : pass     
