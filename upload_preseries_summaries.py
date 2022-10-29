import os
# import TXT_TO_XML
FSUDB_OUTPUT_DIR=os.environ['FSUDB_OUTPUT_DIR']

summary_files_paths_file = 'CMS_HGCAL_DB/IV_CV_preseries_tested_at_FSU/preseries_fullpaths_no_duplicates.txt'

def save_upload_preseries_commands(file):
    #if local: FSUDB_OUTPUT_DIR= 'CMS_HGCAL_DB/IV_CV_preseries_tested_at_FSU/'
    command_file = open('CMS_HGCAL_DB/IV_CV_preseries_tested_at_FSU/'+'save_summary_commands.txt','w')
    fp = open(summary_files_paths_file,'r')
    for line in fp.readlines():
        if 'IV' in line:
            fullpathIV=str(line)
            command_file.write('python TXT_TO_XML.py --f %s --t HGC_CERN_SENSOR_IV_SUMRY' % fullpathIV)
            command_file.write('\n')
        if 'CV' in line:
            fullpathCV=str(line)
            command_file.write('python TXT_TO_XML.py --f %s --t HGC_CERN_SENSOR_CV_SUMRY' % fullpathCV)
            command_file.write('\n')
    fp.close()
    command_file.close()

# def upload_summary_files(IV_or_CV):
#     if IV_or_CV=='IV':
#         try:
#             os.system('mkdir -p %sSUMMARIES_IV/' % FSUDB_OUTPUT_DIR)
#         except Exception:
#             pass
#         summary_output = FSUDB_OUTPUT_DIR+'SUMMARIES_IV/'
#         f = open(summary_files_paths_file,'r')
#         for line in f.readlines():
#             if IV_or_CV=='IV':
#                 if 'IV' in line:
#                     fullpath=str(line)
#                     # os.system('python TXT_TO_XML.py --f %s --t HGC_CERN_SENSOR_IV_SUMRY' % fullpath)
#                     TXT_TO_XML.make_xml_schema_HGC_CERN_SENSOR_IV_SUMRY(fullpath)
#             elif IV_or_CV=='CV':
#                 if 'CV' in line:
#                     fullpath=str(line)
#                     # os.system('python TXT_TO_XML.py --f %s --t HGC_CERN_SENSOR_CV_SUMRY' % fullpath)
#                     TXT_TO_XML.make_xml_schema_HGC_CERN_SENSOR_CV_SUMRY(fullpath)

#         f.close()
                
        


if __name__ == '__main__':
    # upload_summary_files('IV')
    save_upload_preseries_commands(summary_files_paths_file)
    
