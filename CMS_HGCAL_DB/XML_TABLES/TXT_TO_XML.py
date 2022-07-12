import csv; import re
import argparse


parser=argparse.ArgumentParser(description='Covert test results to xml schemas')
parser.add_argument('--f', type=str, help='the .txt filname', required=False)
parser.add_argument('--t', type=str, help='the XML: Tablename you wish to priduce', required=False)

args = parser.parse_args()

filename = args.f
XML_tablename=args.t



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


def get_everything(file):
    '''
    store the results of EVERY CELL at EVERY VOLTAGE STEP. Return a dictionary
    <VOLTS>: V_list
     <CURNT_NANOAMP>: Channel_Current_list
     <ERR_CURNT_NANOAMP>:Error_Current_list
     <TOT_CURNT_NANOAMP>:Tot_Current_list
    <ACTUAL_VOLTS>: Act_Volts_list
    <TIME_SECS>: Time_llist
    <TEMP_DEGC>: Temp_list
    <HUMIDITY_PRCNT>: Humidity_list
    <CELL_NR>: Cell_Number_list
    '''
    V_list=[]; Channel_Current_list=[]
    Error_Current_list=[];Tot_Current_list=[];
    Act_Volts_list=[]; Time_list=[]
    Temp_list=[]; Humidity_list=[]
    Cell_Number_list=[]

    everything_dict={}
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
            if 'Comments' in line:
                Comments=line.split('\t')[2:]



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
                    Cell_Number_list.append(channel)
                    channel_current=fields[2]
                    Channel_Current_list.append(channel_current)
                    error=fields[3]
                    Error_Current_list.append(error)
                    total_current=fields[4]
                    Tot_Current_list.append(total_current)
                    Act_volt=fields[5]
                    Act_Volts_list.append(Act_volt)
                    Time=fields[6]
                    Time_list.append(Time)
                    Temp=fields[7]
                    Temp_list.append(Temp)
                    Humidity=fields[8]
                    Humidity_list.append(Humidity_list)


    everything_dict['Sensor_tye'] =Sensor_type
    everything_dict['Timestamp'] =Timestamp
    everything_dict['Identifier'] =Run_name
    everything_dict['Comments'] =Comments

        
    everything_dict['V_list'] =V_list

    everything_dict['Channel_Current_list'] = Channel_Current_list
    everything_dict['Error_Current_list']=Error_Current_list
    everything_dict['Tot_Current_list']=Tot_Current_list

    everything_dict['Act_Volts_list']=Act_Volts_list
    everything_dict['Time_list']=Time_list
    everything_dict['Temp_list']=Temp_list 
    everything_dict['Humidity_list']=Humidity_list
    everything_dict['Cell_Number_list']=Cell_Number_list

    print(everything_dict)
    return everything_dict




def make_xml_schema_HGC__CERN_SENSOR_IV(Sensor_type, Timestamp, Run_name, V_list, Tot_Current_list):
    # XML_tablename = 'HGC_SENSOR_IV'

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
            xmlf.write('\t\t\t\t<CURRENT>'+str(Tot_Current_list[i])+'<CURRENT>\n')
        
        xmlf.write('\t\t<DATA_SET>\n')
        xmlf.write('<ROOT>\n')


def make_xml_schema_HGC_CERN_SENSOR_IV(everything_dict):
    # XML_tablename = 'HGC_SENSOR_IV'

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
            xmlf.write('\t\t\t\t<CURRENT>'+str(Tot_Current_list[i])+'<CURRENT>\n')
        
        xmlf.write('\t\t<DATA_SET>\n')
        xmlf.write('<ROOT>\n')


                    

                
if __name__ == '__main__':
    # if XML_tablename=='HGC_SENSOR_IV':
    #     Sensor_type, Timestamp, Run_name, V_list, Tot_Current_list = get_V_I_lists(filename)
    #     make_xml_schema_HGC_SENSOR_IV(Sensor_type, Timestamp, Run_name, V_list, I_list)
    # elif XML_tablename=='HGC_CERN_SENSOR_IV':         
    filename="HPK_8in_198ch_2019_N4792_18_03242022_FullRetest_IV.txt"
print(get_everything(filename))