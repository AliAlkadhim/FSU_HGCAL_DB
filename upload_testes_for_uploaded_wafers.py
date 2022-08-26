import pandas as pd
import os
import subprocess as sb
# sb.call('source ')
# 100113 was the first one that was uploaded and checked
## PRiority is the list of sensors in the preseries spreadsheets (FSU preseries)
# then in priority is preseries CERN
# then then prototype multigeometry (start)
#the ones that start with N are proto A

## very few preseries have multiple ones - choose the most recent one if it has multiple
# otherwise choose the one that has the analysis running
wafers_file='CMS_HGCAL_DB/wafers_parts/HGCal Pre-series sensors - 120um HD_AUG26.csv'
unzipped_parts_list_dir = 'CMS_HGCAL_DB/wafers_parts/wafers_parts_1'
# preseries_tested = pd.read_csv('CMS_HGCAL_DB/wafers_parts/HGCal Pre-series sensors - 120um HD_AUG26.csv')
# preseries_tested_scratchpad_id=preseries_tested['Scratch pad ID']
# for ind, row in preseries_tested.iterrows():
#     print(row['Scratch pad ID'])

def return_uploaded_wafers_list_from_spreadsheet(file):
    with open(wafers_file, 'r') as f:
        sensor_id_l=[]; Scratchpad_id_l=[]
        f_readlines = f.readlines()
        for line_ind, line in enumerate(f_readlines):
            if 'Delivery' in line:
                begin_data_ind = line_ind + 1
                for i in range(24):
                    sensor_id = f_readlines[begin_data_ind].split(',')[1]
                    sensor_id_l.append(sensor_id)
                    Scratchpad_id = f_readlines[begin_data_ind].split(',')[2]
                    Scratchpad_id_l.append(Scratchpad_id)
                    # print(Scratchpad_id)
                    begin_data_ind +=1
    return sensor_id_l, Scratchpad_id_l

def return_uploaded_wafers_list_from_zip_file(directory):
    Scratchpad_id_l=[]
    for item in os.listdir(directory):
        Scratchpad_id_l.append(item.split('.')[0])
    return sorted(Scratchpad_id_l)


Scratchpad_id_l=return_uploaded_wafers_list_from_zip_file(unzipped_parts_list_dir)
def get_tested_file_names:
    directories_starting_with_scratchpad_id = 

if __name__=='__main__':
    
    print(tested_sensor_dir_list)
