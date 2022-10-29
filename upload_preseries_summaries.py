import os
FSUDB_OUTPUT_DIR=os.environ['FSUDB_OUTPUT_DIR']

summary_files_paths_file = 'CMS_HGCAL_DB/IV_CV_preseries_tested_at_FSU/preseries_fullpaths_no_duplicates.txt'


def upload_summary_files(IV_or_CV):
    if IV_or_CV=='IV':
        try:
            os.system('mkdir -p %sSUMMARIES_IV/' % FSUDB_OUTPUT_DIR)
        except Exception:
            pass
        summary_output = FSUDB_OUTPUT_DIR+'SUMMARIES_IV/'
        f = open(summary_files_paths_file)
        for line in f.readlines():
            if IV_or_CV=='IV':
                if 'IV' in line:
                    fullpath=str(line)
                    os.sytem('python TXT_TO_XML.py --f %s --t HGC_CERN_SENSOR_IV_SUMRY' % fullpath)
            elif IV_or_CV=='CV':
                if 'CV' in line:
                    fullpath=str(line)
                    os.sytem('python TXT_TO_XML.py --f %s --t HGC_CERN_SENSOR_CV_SUMRY' % fullpath)
        f.close()
                
        


if __name__ == '__main__':
    upload_file('IV')
    
