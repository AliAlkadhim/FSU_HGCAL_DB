import csv; import re
import argparse
import get_iv_cv_dicts as dicts


parser=argparse.ArgumentParser(description='Covert test results to xml schemas')
parser.add_argument('--f', type=str, help='the .txt filname', required=True)
parser.add_argument('--t', type=str, help='the XML: Tablename you wish to priduce. Available options are: [HGC_CERN_SENSOR_IV,HGC_CERN_SENSOR_IV_SUMRY]', required=True)
parser.add_argument('--user', type=str, help='The name of the user who did this test. Default is Alex.', required=False, default='Alex')
parser.add_argument('--location', type=str, help='The locatino where this test was carried. Default is "FSU"', required=False, default='FSU')
parser.add_argument('--comment', type=str, help='Any comments on this test. Default is the comment from the .txt file', required=False,)

args = parser.parse_args()

filename = args.f
XML_tablename=args.t







# def make_xml_schema_HGC_SENSOR_IV(Sensor_type, Timestamp, Run_name, V_list, Tot_Current_list):
#     # XML_tablename = 'HGC_SENSOR_IV'

#     Name = 'HGC Sensor Manufacturer IV Test'
#     Run_number=Run_name
#     location='FSU'
#     Kind_of_part = '200um Si Sensor SD Full'
#     serial_number ='HPK_8in_198ch_N4792_18'

#     xml_table_file = 'N4792_18' + XML_tablename + 'TESTxml'

#     with open(xml_table_file, 'w') as xmlf:
#         xmlf.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
#         xmlf.write('<ROOT xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n')
#         xmlf.write('<HEADER>\n')
#         xmlf.write('\t<TYPE>\n')
#         xmlf.write('\t\t<EXTENSION_TABLE_NAME> HGC_SENSOR_IV</EXTENSION_TABLE_NAME>\n')
#         xmlf.write('\t\t<NAME> HGC Sensor Manufacturer IV Test</NAME>\n')
#         xmlf.write('\t<TYPE>\n')
#         xmlf.write('\t\t<RUN>\n')
#         xmlf.write('\t\t\t<RUN_TYPE>' + Run_number + '<RUN_TYPE>\n')
#         xmlf.write('\t\t\t<RUN_NUMER>' + Run_number + '<RUN_NUMER>\n')
#         xmlf.write('\t\t\t<RUN_BEGIN_TIMESTAMP>'+Timestamp+'</RUN_BEGIN_TIMESTAMP>\n')
#         xmlf.write('\t\t\t<RUN_END_TIMESTAMP>'+Timestamp+'</RUN_END_TIMESTAMP>\n')
#         xmlf.write('\t\t\t<INITIATED_BY_USER>'+'Ali'+'<INITIATED_BY_USER>\n')
#         xmlf.write('\t\t\t<LOCATION>'+location+'<LOCATION>\n')
#         xmlf.write('\t\t\t<COMMENT_DESCRIPTION>'+'Example table' + '<COMMENT_DESCRIPTION>\n')
#         xmlf.write('\t\t</RUN>\n')
#         xmlf.write(' </HEADER>\n')

#         xmlf.write('\t\t<DATA_SET>\n')
#         xmlf.write('\t\t\t<PART>\n')
#         xmlf.write('\t\t\t\t<KIND_OF_PART>'+Kind_of_part+'</KIND_OF_PART>\n')
#         xmlf.write('\t\t\t\t<SERIAL_NUMBER>'+serial_number+'<SERIAL_NUMBER>\n')
#         xmlf.write('\t\t\t<PART>\n')

#         for i in range(len(V_list)):
#             xmlf.write('\t\t\t<DATA>\n')
#             xmlf.write('\t\t\t\t<VOLTS>'+str(V_list[i])+'<VOLTS>\n')
#             xmlf.write('\t\t\t\t<CURRENT>'+str(Tot_Current_list[i])+'<CURRENT>\n')
        
#         xmlf.write('\t\t<DATA_SET>\n')
#         xmlf.write('<ROOT>\n')

##################### #####################  IV TABLES #####################  ##################### 

def make_xml_schema_HGC_CERN_SENSOR_IV(filename):
    
    IVDICT = dicts.get_iv_dict(filename)
    XML_tablename = 'HGC_CERN_SENSOR_IV'

    Name = 'HGC Sensor Manufacturer IV Test'
    Sensor_Type = IVDICT['Sensor_type']
    Run_Name = IVDICT['Identifier'].split()[0]
    location=args.location
    Kind_of_part = '200um Si Sensor SD Full'
    serial_number ='HPK_8in_198ch_N4792_18'
    # serial_number = Sensor_Type + Run_Name
    xml_table_file = Run_Name + '_'+ XML_tablename + '_TEST.xml'

    with open(xml_table_file, 'w+') as xmlf:
        xmlf.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
        xmlf.write('<ROOT xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n')
        xmlf.write('<HEADER>\n')
        xmlf.write('\t<TYPE>\n')
        xmlf.write('\t\t<EXTENSION_TABLE_NAME> HGC_SENSOR_IV</EXTENSION_TABLE_NAME>\n')
        xmlf.write('\t\t<NAME> HGC CERN Sensor IV Test</NAME>\n')
        xmlf.write('\t<TYPE>\n')
        xmlf.write('\t\t<RUN>\n')
        xmlf.write('\t\t\t<RUN_NAME>' + Run_Name + '<RUN_NAME>\n')
        xmlf.write('\t\t\t<RUN_BEGIN_TIMESTAMP>'+IVDICT['Timestamp']+'</RUN_BEGIN_TIMESTAMP>\n')
        xmlf.write('\t\t\t<RUN_END_TIMESTAMP>'+IVDICT['Timestamp']+'</RUN_END_TIMESTAMP>\n')
        xmlf.write('\t\t\t<INITIATED_BY_USER>'+args.user+'<INITIATED_BY_USER>\n')
        xmlf.write('\t\t\t<LOCATION>'+location+'<LOCATION>\n')
        if args.comment:
            xmlf.write('\t\t\t<COMMENT_DESCRIPTION>'+args.comment+ '<COMMENT_DESCRIPTION>\n')
        else:
            xmlf.write('\t\t\t<COMMENT_DESCRIPTION>'+str(IVDICT['Comments'])+ '<COMMENT_DESCRIPTION>\n')
        xmlf.write('\t\t</RUN>\n')
        xmlf.write(' </HEADER>\n')

        xmlf.write('\t\t<DATA_SET>\n')
        xmlf.write('\t\t\t<PART>\n')
        xmlf.write('\t\t\t\t<KIND_OF_PART>'+Kind_of_part+'</KIND_OF_PART>\n')
        xmlf.write('\t\t\t\t<SERIAL_NUMBER>'+serial_number+'<SERIAL_NUMBER>\n')
        xmlf.write('\t\t\t<PART>\n')


        for i in range(len(IVDICT['V_list'])):
            xmlf.write('\t\t\t<DATA>\n')
            xmlf.write('\t\t\t\t<VOLTS>'+str(IVDICT['V_list'][i])+'<VOLTS>\n')
            #BELLOW IS CHANNEL CURRENT
            xmlf.write('\t\t\t\t<CURNT_NANOAMP>'+str(IVDICT['Channel_Current_list'][i])+'<CURNT_NANOAMP>\n')
            #BLLOW IS CHANNEL ERROR CURRENT
            xmlf.write('\t\t\t\t<ERR_CURNT_NANOAMP>'+str(IVDICT['Error_Current_list'][i])+'<ERR_CURNT_NANOAMP>\n')
            #BELLOW IS TOT CURRENT 
            xmlf.write('\t\t\t\t<TOT_CURNT_NANOAMP>'+str(IVDICT['Tot_Current_list'][i])+'<TOT_CURNT_NANOAMP>\n')
            xmlf.write('\t\t\t\t<ACTUAL_VOLTS>'+str(IVDICT['Act_Volts_list'][i])+'<ACTUAL_VOLTS>\n')
            xmlf.write('\t\t\t\t<TIME_SECS>'+str(IVDICT['Time_list'][i])+'<TIME_SECS>\n')
            xmlf.write('\t\t\t\t<TEMP_DEGC>'+str(IVDICT['Temp_list'][i])+'<TEMP_DEGC>\n')
            # xmlf.write('\t\t\t\t<HUMIDITY_PRCNT>'+str(IVDICT['Humidity_list'][i])+'<HUMIDITY_PRCNT>\n')
            xmlf.write('\t\t\t\t<HUMIDITY_PRCNT>'+str(0.000000E+0)	+'<HUMIDITY_PRCNT>\n')

            xmlf.write('\t\t\t\t<CELL_NR>'+str(IVDICT['Cell_Number_list'][i])+'<CELL_NR>\n')


        
        xmlf.write('\t\t<DATA_SET>\n')
        xmlf.write('<ROOT>\n')


                    

####################################################CV TABLES######################################################3


def make_xml_schema_HGC_CERN_SENSOR_CV(filename):
    
    CVDICT = dicts.get_cv_dict(filename)
    XML_tablename = 'HGC_CERN_SENSOR_CV'

    Name = 'HGC Sensor Manufacturer IV Test'
    Run_Name = CVDICT['Identifier'].split()[0]
    location=args.location
    Kind_of_part = '200um Si Sensor SD Full'
    serial_number ='HPK_8in_198ch_N4792_18'
    # serial_number = Sensor_Type + Run_Name

    xml_table_file = Run_Name + '_'+ XML_tablename + '_TEST.xml'

    with open(xml_table_file, 'w+') as xmlf:
        xmlf.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
        xmlf.write('<ROOT xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n')
        xmlf.write('<HEADER>\n')
        xmlf.write('\t<TYPE>\n')
        xmlf.write('\t\t<EXTENSION_TABLE_NAME> HGC_SENSOR_CV</EXTENSION_TABLE_NAME>\n')
        xmlf.write('\t\t<NAME> HGC CERN Sensor CV Test</NAME>\n')
        xmlf.write('\t<TYPE>\n')
        xmlf.write('\t\t<RUN>\n')
        xmlf.write('\t\t\t<RUN_NAME>' + Run_Name + '<RUN_NAME>\n')
        xmlf.write('\t\t\t<RUN_BEGIN_TIMESTAMP>'+CVDICT['Timestamp']+'</RUN_BEGIN_TIMESTAMP>\n')
        xmlf.write('\t\t\t<RUN_END_TIMESTAMP>'+CVDICT['Timestamp']+'</RUN_END_TIMESTAMP>\n')
        xmlf.write('\t\t\t<INITIATED_BY_USER>'+args.user+'<INITIATED_BY_USER>\n')
        xmlf.write('\t\t\t<LOCATION>'+location+'<LOCATION>\n')
        if args.comment:
            xmlf.write('\t\t\t<COMMENT_DESCRIPTION>'+args.comment+ '<COMMENT_DESCRIPTION>\n')
        else:
            xmlf.write('\t\t\t<COMMENT_DESCRIPTION>'+str(CVDICT['Comments'])+ '<COMMENT_DESCRIPTION>\n')
        xmlf.write('\t\t</RUN>\n')
        xmlf.write(' </HEADER>\n')

        xmlf.write('\t\t<DATA_SET>\n')
        xmlf.write('\t\t\t<PART>\n')
        xmlf.write('\t\t\t\t<KIND_OF_PART>'+Kind_of_part+'</KIND_OF_PART>\n')
        xmlf.write('\t\t\t\t<SERIAL_NUMBER>'+serial_number+'<SERIAL_NUMBER>\n')
        xmlf.write('\t\t\t<PART>\n')


        for i in range(len(CVDICT['V_list'])):
            xmlf.write('\t\t\t<DATA>\n')
            xmlf.write('\t\t\t\t<VOLTS>'+str(CVDICT['V_list'][i])+'<VOLTS>\n')
            xmlf.write('\t\t\t\t<CPCTNCE_PFRD>'+str(CVDICT['Cs_list'][i])+'<CPCTNCE_PFRD>:\n')
            xmlf.write('\t\t\t\t<ERR_CPCTNC_PFRD>'+str(CVDICT['Error_capacitance_list'][i])+'<ERR_CPCTNC_PFRD>\n')

            xmlf.write('\t\t\t\t<TOT_CURNT_NANOAMP>'+str(CVDICT['Tot_Current_list'][i])+'<TOT_CURNT_NANOAMP>\n')

            xmlf.write('\t\t\t\t<ACTUAL_VOLTS>'+str(CVDICT['Act_Volts_list'][i])+'<ACTUAL_VOLTS>\n')
            xmlf.write('\t\t\t\t<ORG_CPCTNC_PFRD>'+str(CVDICT['Cs_uncorr_list'][i])+'<ORG_CPCTNC_PFRD>\n')
            xmlf.write('\t\t\t\t<TEMP_DEGC>'+str(CVDICT['Temp_list'][i])+'<TEMP_DEGC>\n')
            xmlf.write('\t\t\t\t<HUMIDITY_PRCNT>'+str(CVDICT['Humidity_list'][i])+'<HUMIDITY_PRCNT>\n')
        # xmlf.write('\t\t\t\t<HUMIDITY_PRCNT>'+str(0.000000E+0)	+'<HUMIDITY_PRCNT>\n')
            xmlf.write('\t\t\t\t<IMP_OHM>'+str(CVDICT['Impedence_list'][i])+'<IMP_OHM>n')
            xmlf.write('\t\t\t\t<PHS_RAD>'+str(CVDICT['Phase_list'][i])+'<PHS_RAD>n')
            xmlf.write('\t\t\t\t<TIME_SECS>'+str(CVDICT['Time_list'][i])+'<TIME_SECS>\n')
            xmlf.write('\t\t\t\t<CELL_NR>'+str(CVDICT['Cell_Number_list'][i])+'<CELL_NR>\n')


        
        xmlf.write('\t\t<DATA_SET>\n')
        xmlf.write('<ROOT>\n')




                
if __name__ == '__main__':
    # if XML_tablename=='HGC_SENSOR_IV':
    #     Sensor_type, Timestamp, Run_name, V_list, Tot_Current_list = get_V_I_lists(filename)
    #     make_xml_schema_HGC_SENSOR_IV(Sensor_type, Timestamp, Run_name, V_list, I_list)
    # elif XML_tablename=='HGC_CERN_SENSOR_IV':         
    # filename="HPK_8in_198ch_2019_N4792_18_0324iv_dict2022_FullRetest_IV.txt"
    filename=args.f
    if args.t == 'HGC_CERN_SENSOR_IV':
        make_xml_schema_HGC_CERN_SENSOR_IV(filename)
    elif args.t == 'HGC_CERN_SENSOR_CV':
        make_xml_schema_HGC_CERN_SENSOR_CV(filename)