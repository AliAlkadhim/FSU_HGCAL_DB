import csv 
import re
filename="HPK_8in_198ch_2019_N4792_18_03242022_FullRetest_IV.txt"

# with open(filename) as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     for row in f_csv:
#         print(row)
#         break

def get_V_I_lists(file):
    V_list=[]; I_list=[]
    with open(filename, "r") as f:
        fs = f.readlines()#.split('\n')
        for lineind, line in enumerate(fs):
            #get HEADER info
            if 'Sensor type' in line:
                Sensor_type = line.split('\t')[2]
            if 'Timestamp' in line:
                Timestamp=line.split('\t')[2]
            if 'Identifier' in line:
                Run_name = line.split('\t')[2]


            if 'Error' in line:
                headers = line
                headers_ind = lineind
                # print(headers.split('#'))
                rows_ind = headers_ind + 2
                rows = fs[rows_ind:]
                for row in rows:
                    # print(row)
                    fields = row.strip().split('\t')
                    voltage = fields[0]
                    V_list.append(voltage)
                    channel = fields[1]
                    # current=float(fields[2])
                    # error=float(fields[3])
                    total_current=float(fields[4])
                    I_list.append(total_current)
                    
    return Sensor_type, Timestamp, Run_name, V_list, I_list

def make_xml_schema(Sensor_type, Timestamp, Run_name, V_list, I_list):
    XML_tablename = 'HGC_SENSOR_IV'

    Name = 'HGC Sensor Manufacturer IV Test'
    Run_number=Run_name
    location='FSU'
    Kind_of_part = '200um Si Sensor SD Full'
    serial_number ='HPK_8in_198ch_N4792_18'

    xml_table_file = 'N4792_18' + XML_tablename + 'test.xml'

    with open(xml_table_file, 'w') as xmlf:
        xmlf.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
        xmlf.write('<ROOT xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n')
        xmlf.write('<HEADER>\n')
        xmlf.write('\t<TYPE>\n')
        xmlf.write('\t\t<EXTENSION_TABLE_NAME> HGC_SENSOR_IV</EXTENSION_TABLE_NAME>\n')
        xmlf.write('\t\t<NAME> HGC Sensor Manufacturer IV Test</NAME>\n')
        xmlf.write('\t<TYPE>\n')
        xmlf.write('\t\t<RUN>\n')
        xmlf.write('\t\t\t<RUN_TYPE>' + Run_number + '<RUN_TYPE>\n')
        xmlf.write('\t\t\t<RUN_NUMER>' + Run_number + '<RUN_NUMER>\n')
        xmlf.write('\t\t\t<RUN_BEGIN_TIMESTAMP>'+Timestamp+'</RUN_BEGIN_TIMESTAMP>\n')
        xmlf.write('\t\t\t<RUN_END_TIMESTAMP>'+Timestamp+'</RUN_END_TIMESTAMP>\n')
        xmlf.write('\t\t\t<INITIATED_BY_USER>'+'Ali'+'<INITIATED_BY_USER>\n')
        xmlf.write('\t\t\t<LOCATION>'+location+'<LOCATION>\n')
        xmlf.write('\t\t\t<COMMENT_DESCRIPTION>'+'Example table' + '<COMMENT_DESCRIPTION>\n')
        xmlf.write('\t\t</RUN>\n')
        xmlf.write(' </HEADER>\n')

        xmlf.write('\t\t<DATA_SET>\n')
        xmlf.write('\t\t\t<PART>\n')
        xmlf.write('\t\t\t\t<KIND_OF_PART>'+Kind_of_part+'</KIND_OF_PART>\n')
        xmlf.write('\t\t\t\t<SERIAL_NUMBER>'+serial_number+'<SERIAL_NUMBER>\n')
        xmlf.write('\t\t\t<PART>\n')

        for i in range(len(V_list)):
            xmlf.write('\t\t\t<DATA>\n')
            xmlf.write('\t\t\t\t<VOLTS>'+str(V_list[i])+'<VOLTS>\n')
            xmlf.write('\t\t\t\t<CURRENT>'+str(I_list[i])+'<CURRENT>\n')
        
        xmlf.write('\t\t<DATA_SET>\n')
        xmlf.write('<ROOT>\n')




                    

                
if __name__ == '__main__':
    Sensor_type, Timestamp, Run_name, V_list, I_list = get_V_I_lists(filename)
    make_xml_schema(Sensor_type, Timestamp, Run_name, V_list, I_list)