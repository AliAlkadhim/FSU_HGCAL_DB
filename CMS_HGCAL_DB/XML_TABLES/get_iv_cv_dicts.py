import csv; import re
import argparse


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


def get_iv_dict(file):
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

if __name__ == '__main__':
    filename="HPK_8in_198ch_2019_N4792_18_03242022_FullRetest_IV.txt"
    get_iv_dict(filename)