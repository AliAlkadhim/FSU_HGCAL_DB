import pandas as pd
import os
import subprocess as sb
from Register_wafer_xml import register_wafer_xml as wafer_xml
# import TXT_TO_XML as XML
# import logging


####################### CONFIGURATIONS ####################
# for working locally on my laptop, do
# export INPUT_DIR=/home/ali/Desktop/Pulled_Github_Repositories/FSU_HGCAL_DB/CMS_HGCAL_DB/wafers_parts/Preproduction
# export FSUDB_OUTPUT_DIR=/home/ali/Desktop/Pulled_Github_Repositories/FSU_HGCAL_DB/CMS_HGCAL_DB/wafers_parts/Preproduction/Preproduction_Wafers_Parts

INPUT_DIR=os.environ['INPUT_DIR']

FSUDB_OUTPUT_DIR=os.environ['FSUDB_OUTPUT_DIR']

Wafers_Spreadsheet = pd.read_csv(
    os.path.join(INPUT_DIR, 'HGCal Pre-production and production sensors - 300um LD (S15591-01).csv'),
    skiprows=1
)

# Get the list of sensors to upload
sensors_to_register_l=[]
with open(os.path.join(INPUT_DIR,'sensors_to_register.txt'), 'r') as f:
    # content_without_newlines = ''.join(f.readlines()).replace('\n', ',')
    for line in f:
        line_r = line.rstrip('\n')
        sensors_to_register_l.append(line_r)

sensors_to_register_l=pd.Series(filter(None, sensors_to_register_l), dtype='float64')
print(sensors_to_register_l)
        
    


# print(Wafers_Spreadsheet['Sensor ID'])

# Get the DF with 
mask = (Wafers_Spreadsheet['Sensor ID'].isin(sensors_to_register_l))
Wafers_to_register_DF=Wafers_Spreadsheet[mask]
print(Wafers_to_register_DF)
for ID in sensors_to_register_l:
    wafer_xml(Wafers_to_register_DF=Wafers_to_register_DF, Sensor_ID=ID)



# print(Wafers_Spreadsheet['Sensor ID'].dtype)


# if __name__=='__main__':
    #  register_wafer_xml(Sensor_ID=100360)
    # sensor_row=Wafers_to_register_DF[Wafers_to_register_DF['Sensor ID'] == 100360] 
    
    # print(sensor_row['OBA Number'])
    # wafer_xml(Wafers_to_register_DF=Wafers_to_register_DF, Sensor_ID=100360)