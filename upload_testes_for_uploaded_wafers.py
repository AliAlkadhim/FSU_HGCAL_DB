import pandas as pd
import os
import subprocess as sb
import get_iv_cv_dicts as dicts
import TXT_TO_XML as XML

INPUT_DIR=os.environ['INPUT_DIR']#this is just export INPUT_DIR="/home/input/"

# FSUDB_OUTPUT_DIR='CMS_HGCAL_DB/IV_CV_preseries_tested_at_FSU/'#where the head of it is the git repo
FSUDB_OUTPUT_DIR=os.environ['FSUDB_OUTPUT_DIR']


# 100113 was the first one that was uploaded and checked
## PRiority is the list of sensors in the preseries spreadsheets (FSU preseries)
# then in priority is preseries CERN
# then then prototype multigeometry (start)
#the ones that start with N are proto A

## very few preseries have multiple ones - choose the most recent one if it has multiple
# otherwise choose the one that has the analysis running

# preseries_tested = pd.read_csv('CMS_HGCAL_DB/wafers_parts/HGCal Pre-series sensors - 120um HD_AUG26.csv')
# preseries_tested_scratchpad_id=preseries_tested['Scratch pad ID']
# for ind, row in preseries_tested.iterrows():
#     print(row['Scratch pad ID'])

wafers_spreadsheet_preseries_120='CMS_HGCAL_DB/wafers_parts/HGCal Pre-series sensors - 120um HD.csv'
wafers_spreadsheet_preseries_200='CMS_HGCAL_DB/wafers_parts/HGCal Pre-series sensors - 200um LD.csv'
wafers_spreadsheet_preseries_300='CMS_HGCAL_DB/wafers_parts/HGCal Pre-series sensors - 300um LD.csv'

def return_preseries_dict_from_spreadsheet(spreadsheet):
    """ This returns a dataframe of {sensor_ID, scratchpad_ID, current_location} from the preseries spreadsheets, 
    such as the ones defined above 
    Example usage: df_12=return_preseries_dict_from_spreadsheet(wafers_spreadsheet_preseries_120)
    """
    if spreadsheet==wafers_spreadsheet_preseries_120:
        length=23+1
    elif spreadsheet==wafers_spreadsheet_preseries_200:
        length=49+1
    elif spreadsheet==wafers_spreadsheet_preseries_300:
        length=49+1
    with open(spreadsheet, 'r') as f:
        sensor_id_l=[]; Scratchpad_id_l=[]; current_location_l=[]
        
        f_readlines = f.readlines()
        for line_ind, line in enumerate(f_readlines):
            if 'Delivery' in line:
                begin_data_ind = line_ind + 1
                for i in range(length):
                    sensor_id = f_readlines[begin_data_ind].split(',')[1]
                    sensor_id_l.append(sensor_id)
                    Scratchpad_id = f_readlines[begin_data_ind].split(',')[2]
                    Scratchpad_id_l.append(Scratchpad_id)
                    current_location = f_readlines[begin_data_ind].split(',')[4]
                    current_location_l.append(current_location)                    
                    # print(Scratchpad_id)
                    begin_data_ind +=1
    preseries_dict=pd.DataFrame({'sensor_id': sensor_id_l,
                 'scratchpad_id':Scratchpad_id_l,
                 'current_location' : current_location_l
    })
    return preseries_dict

def return_uploaded_wafers_list_from_zip_file(directory):
    """This returns a list of scratchpad_IDs associated with the wafers that have been uploaded to the db
    Directory is the file path of the directory where the zipped file of uploaded wafers is
    """
    Scratchpad_id_l=[]
    for item in os.listdir(directory):
        Scratchpad_id_l.append(item.split('.')[0])
    return sorted(Scratchpad_id_l)



# def get_tested_file_names:
#     directories_starting_with_scratchpad_id = 



# unzipped_parts_list_dir = 'CMS_HGCAL_DB/wafers_parts/wafers_parts_1'
# Scratchpad_id_l=return_uploaded_wafers_list_from_zip_file(unzipped_parts_list_dir)




def Replace(ll, orig, replaced):                                                                                                                                                                                   
    for i, n in enumerate(ll):                                                                                                                                                                                         
        if n==orig:                                                                                                                                                                                                        
            ll[i] = replaced                                                                                                                                                                                       
    return ll 


def main():
    ######## spreadsheet analysis
    preseries_dict_120 = return_preseries_dict_from_spreadsheet(wafers_spreadsheet_preseries_120)
    preseries_dict_200 = return_preseries_dict_from_spreadsheet(wafers_spreadsheet_preseries_200)
    preseries_dict_300 = return_preseries_dict_from_spreadsheet(wafers_spreadsheet_preseries_300)


    all_preseries_df = pd.concat([preseries_dict_120,preseries_dict_200, preseries_dict_300])

    #select only the preseries sensors that were tested at FSU
    scratchpad_id_wafers_FSU = all_preseries_df[all_preseries_df.current_location == 'FSU']

    print('scratchpad ids for uploaded wafers testede at FSU') 
    for scratphad_id in scratchpad_id_wafers_FSU['scratchpad_id']:
        print(scratphad_id)

    FSU_scratchpad_IDs=scratchpad_id_wafers_FSU['scratchpad_id']
    dirs_in_input = os.listdir(INPUT_DIR)
    #Replace the stuff for sensor 200119

    dirs_in_input = Replace(dirs_in_input, 'HPK_8in_198ch_2019_200119_20220713_ivretest','HPK_8in_198ch_2019_200119_20220707_test1')
    #remove duplicates
    dirs_in_input=list(set(dirs_in_input))

    IV_file_l=[]; CV_file_l=[];dirs_l=[]

    for scratchpad_id in FSU_scratchpad_IDs:
        for dir in dirs_in_input:
            if  scratchpad_id in dir:
                #get all the directories for the scratchpad ids that we want
                dirs_l.append(dir)
                files_in_dir=os.listdir(INPUT_DIR+dir)
                for file in files_in_dir:
                    if file.endswith('IV.txt'):
                        IV_file=file
                        IV_file_l.append(IV_file)
                    elif file.endswith('CV.txt'):
                        CV_file=file
                        CV_file_l.append(CV_file)

    #scratchpad_id_wafers_FSU['dirs']=dirs_l

    print('dirs_l with no duplicates', dirs_l)
    print('IV_file_l with no duplicates', IV_file_l)

    # CV_file_l.replace('HPK_8in_198ch_2019_200119_20220707_test1_CV.txt', )
    #for dir in dirs_in_input:
    #	if '300057' in dir:
    #		files_in_dir=os.listdir(INPUT_DIR+dir)
    #		for file in files_in_dir:
    #			if file.endswith('IV.txt'):
    #				IV_file=file
    #			elif file.endswith('CV.txt'):
    #				CV_file=file


    # print(IV_file_l)
    print(CV_file_l)
    #take away 'HPK_8in_198ch_2019_200119_20220707_test1_IV.txt' from IV because it was retested

    print('number of preseries at fsu uploaded = ', len(scratchpad_id_wafers_FSU['scratchpad_id']))
    #IV_file_l.remove('HPK_8in_198ch_2019_200119_20220707_test1_IV.txt')
    print('length of IV file list = ', len(IV_file_l))
    print('length of CV file list = ', len(CV_file_l))

    #iterate over the directory and IV file of each preseries sensor (that was uploaded)
    for dir, preseries_IV_file in zip(dirs_l,IV_file_l):
        command='python TXT_TO_XML.py --f %s --t HGC_CERN_SENSOR_IV --location FSU' % str('$INPUT_DIR'+'/'+dir+'/'+preseries_IV_file)	 
        full_path=str(os.path.abspath(os.path.join(INPUT_DIR, dir, preseries_IV_file)) )
        print(full_path)
        IV_DICT = dicts.get_iv_dict(full_path)
        #print(IV_DICT)
        XML.make_xml_schema_HGC_CERN_SENSOR_IV(full_path)
        #os.system('python TXT_TO_XML.py --f %s --t HGC_CERN_SENSOR_IV' % full_path)
        

    for dir, preseries_CV_file in zip(dirs_l,CV_file_l): 
        command='python TXT_TO_XML.py --f %s --t HGC_CERN_SENSOR_IV --location FSU' % str('$INPUT_DIR'+'/'+dir+'/'+preseries_IV_file) 
        full_path=str(os.path.abspath(os.path.join(INPUT_DIR, dir, preseries_CV_file)) )          
        print(full_path)
        CV_DICT = dicts.get_cv_dict(full_path)
        XML.make_xml_schema_HGC_CERN_SENSOR_CV(full_path)


#with open(os.path.join(INPUT_DIR, 'HPK_8in_198ch_2019_100113_20220701','HPK_8in_198ch_2019_100113_20220701_IV.txt')) as f:
#	print(f.readlines())

if __name__=='__main__':
    main()


#############
#to test upload for test file 100113 do 
#python TXT_TO_XML.py --f $INPUT_DIR/HPK_8in_198ch_2019_100113_20220701/HPK_8in_198ch_2019_100113_20220701_IV.txt --t HGC_CERN_SENSOR
