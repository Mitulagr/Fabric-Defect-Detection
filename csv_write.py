# Converting Test Image Coordinates and Type from json file to csv file

import json
import csv 
    
# field names 

fields_type = ['images id', 'defect_flag'] 
fields_box = ['  image_id', 'X','Y','W','H'] 
    
# opening json files
   
with open('defect_type.json') as f: defect_type = json.load(f)
with open('img_name_type.json') as f: img_name_type = json.load(f)
with open('defect_box.json') as f: defect_box = json.load(f)
with open('img_name_box.json') as f: img_name_box = json.load(f)

# data rows of csv file 

rows_type = []

for i in range(len(defect_type)) : 
    rows_type.append([img_name_type[i],defect_type[i]])

rows_box = []

for i in range(len(defect_box)) : 
    rows_box.append([img_name_box[i],defect_box[i][0],defect_box[i][1],defect_box[i][2],defect_box[i][3]])    

# name of csv file 
filename_type = "Final_DefectType_Xtreme.csv"
filename_box = "Final_DefectBoxes_Xtreme.csv"
    
# writing to csv file 

with open(filename_type, 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields_type) 
    csvwriter.writerows(rows_type)


with open(filename_box, 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields_box) 
    csvwriter.writerows(rows_box)    