import sys
import os
import subprocess as sb
import csv
import re
import pandas as pd
# from fsudb.utils import convert_to_csv
# if args.tablename == "HGC_HPK_Sensor_IV_Summary_LD_and_HD.csv":
    #the long Ncell_with_1800_greaterthan_2_point_5_times_1600_and_1600_greaterthan_10nA_OR_1800_greaterthan_25nA_and_1600_lessthan_10nA


HGC_HPK_Sensor_IV_Summary_LD_and_HD_fields = [
#identifiers
'Sensor_ID', 'Scratch_pad_ID', 
'Thick_ness', 'P_Stop', 
'Oxide_type', 'Flat_band_volt_V', 'P_stop_conc', 
'Proc', 'HD_Or_LD', 
#results
'I_tot_600V_lessthan_100mA', 
'I_tot_800V_lessthan_2_point_5_times_I_tot_600V', 
'Ncell_with_1800_greaterthan_2_point_5_times_1600', 
'More_than_8_bad_cells_require_1_and_2', 
'More_than_two_neighbor_cells_bad_require_1_and_2']


csv_file = 'new_results_csv/long_df.csv'

def updateDB():
    """automatically updates the FSUDB, given either IV or CV.
    Big picture: running 'updateDB IV' should:
    1. make a csv file for each table, fill it with all the necessary data from the test results, store it in 'new_results' directory
    2. make sql tables from the csv data that we just got.
    3. show pdf of compiled table of latest results.
    4. update the necessary tables from the central fsu database"""

    if sys.argv[1]:
        measure = sys.argv[1]#this is either IV or CV
    else:
	    print('You must do python updateDB.py IV\n (or CV)')
        #return
    if sys.argv[1]== 'IV':
        #HGC_HPK_Sensor_IV_Summary_LD_and_HD.csv is the only table we need to worry about updating for IV
            #     with open(grading_results_for_latest_sensor_file, 'r') as f:
    #         for line_ind, line in enumerate(f.readlines()):
    #             pass
    #             # pd_dict = {'Sensor_ID': , 'Scratch_pad_ID':, 
    #             #     'Thick_ness' : , 'P_Stop' : , 
    #             #     'Oxide_type' : , 'Flat_band_volt_V' : , 'P_stop_conc' : , 
    #             #     'Proc' : , 'HD_Or_LD' :, 
    #             #     'I_tot_600V_lessthan_100mA' : , 
    #             #     'I_tot_800V_lessthan_2_point_5_times_I_tot_600V' , 
    #             #     'Ncell_with_1800_greaterthan_2_point_5_times_1600', 
    #             #     'More_than_8_bad_cells_require_1_and_2', 
    #             #     'More_than_two_neighbor_cells_bad_require_1_and_2'}
    #             # df = pd.DataFrame.from_dict(pd_dict)
    # #print(long_df)

        ########################## READ GRADING RESULTS ################################
        TMPFILES_DIR_IV = os.environ['TMPFILES_DIR_IV']

        grading_dir = TMPFILES_DIR_IV +'/-/grading/'
        cmd = 'ls -t $TMPFILES_DIR_IV/-/grading | head -n 1'
        latest_sensor = sb.Popen(cmd, shell=True,stdin=sb.PIPE, stdout=sb.PIPE, stderr=sb.STDOUT)
        latest_sensor = latest_sensor.stdout.read()
        latest_sensor=latest_sensor[:-1]

        grading_results_for_latest_sensor_file = grading_dir + latest_sensor + '/grading_results.tex'
        with open(grading_results_for_latest_sensor_file,'r') as gr:
            for line in gr.readlines():
                #pass
                if '<= 100 $\mu$A integrated' in line:
                    criteria_I_tot_600V_lessthan_100mA = line.split('textcolor')[1].strip()
                    if "Passed" in criteria_I_tot_600V_lessthan_100mA:
                        criteria_I_tot_600V_lessthan_100mA = "Passed"
                    else:
                        criteria_I_tot_600V_lessthan_100mA = "Failed"
                #I_tot_800V_lessthan_2_point_5_times_I_tot_600V looks like \item I800 < 2.5 x I600: \textcolor{green}{Passed}
                if 'I800 < 2.5 x I600' in line:
                    criteria_I_tot_800V_lessthan_2_point_5_times_I_tot_600V = line.split('textcolor')[1].strip()
                    if "Passed" in criteria_I_tot_800V_lessthan_2_point_5_times_I_tot_600V:
                        criteria_I_tot_800V_lessthan_2_point_5_times_I_tot_600V = "Passed"
                    else:
                        criteria_I_tot_800V_lessthan_2_point_5_times_I_tot_600V = "Failed"
                
                # Ncell_with_1800_greaterthan_2_point_5_times_1600 from the other tex file

                #More_than_8_bad_cells_require_1_and_2 looks like \item Number of bad pads 0 <= 8 for full-sized sensors: \textcolor{green}{Passed}
                if 'Number of bad pads 0 <= 8 for full-sized sensors' in line:
                    criteria_More_than_8_bad_cells_require_1_and_2 = line.split('textcolor')[1].strip()
                    if "Passed" in criteria_More_than_8_bad_cells_require_1_and_2:
                        criteria_More_than_8_bad_cells_require_1_and_2 = "Passed"
                    else:
                        criteria_More_than_8_bad_cells_require_1_and_2 = "Failed"

                # More_than_two_neighbor_cells_bad_require_1_and_2 looks like \item Allowed number of adjacent bad pads <= 2: \textcolor{green}{Passed}
                if 'Allowed number of adjacent bad pads <= 2' in line:
                    criteria_More_than_two_neighbor_cells_bad_require_1_and_2 = line.split('textcolor')[1].strip()
                    if "Passed" in criteria_More_than_two_neighbor_cells_bad_require_1_and_2:
                        criteria_More_than_two_neighbor_cells_bad_require_1_and_2 = "Passed"
                    else:
                        criteria_More_than_two_neighbor_cells_bad_require_1_and_2 = "Failed"

                # print(criteria_I_tot_600V_lessthan_100mA)
        

        #scratchpad_ID has to be obtained from the database like HGC_HPK..., I think it has to be imput manually by the user!
        ###################### READ INFO FROM DUT ######################
        DUT = pd.read_csv(os.environ['WORKFLOW_DIR']+'/database/csv/DUTs.csv')
        for ind, row in DUT.iterrows():
            if row['Name'].endswith(latest_sensor):
                #long_name_ == DUT['Name'][DUT['Name'] == row_name]
                long_name = row['Name']
                Size = row['Size']
                
                NChannels= row['NChannels']
                Doping = row['Doping']
                Thickness = row['Thickness']
                Pstop = row['Pstop']
        # latest_sensor_row = DUT.loc[DUT['Name'].endswith(latest_sensor)]

                
        ################## READ INFO FROM IVMeasurements ########################        
        IVMeasurements = pd.read_csv(os.environ['WORKFLOW_DIR']+'/database/csv/IVMeasurements.csv')
        for ind, row in IVMeasurements.iterrows():
            if row['ID'].startswith(latest_sensor):
                #CURRENTLY TAKING THE BARE NAME, without _test01, _testN
                Date = row['Date']
                Station = row['Station']
                HVResistance = row['HVResistance']
                Temperature = row['Temperature']

        #construct long_df
        long_df = pd.DataFrame({
        #DUT
        'Sensor_ID': [latest_sensor],
        'long_name':[long_name],
        'Size':[Size],
        'NChannels':[NChannels],
        'Doping' :[Doping],
        'Thickness' : [Thickness],
        'P_Stop' : [Pstop],
        #IV_MEASUREMENT
        'Date': [Date],
        'Station':[Station],
        'HVResistance':[HVResistance],
        'Temperature':[Temperature],
        #GRADING_RESULTS
        'I_tot_600V_lessthan_100mA':[criteria_I_tot_600V_lessthan_100mA], 
        'I_tot_800V_lessthan_2_point_5_times_I_tot_600V':[criteria_I_tot_800V_lessthan_2_point_5_times_I_tot_600V], 
        #'Ncell_with_1800_greaterthan_2_point_5_times_1600':[criteria_Ncell_with_1800_greaterthan_2_point_5_times_1600], 
        'More_than_8_bad_cells_require_1_and_2':[criteria_More_than_8_bad_cells_require_1_and_2], 
        'More_than_two_neighbor_cells_bad_require_1_and_2':[criteria_More_than_two_neighbor_cells_bad_require_1_and_2]

        # 'Scratch_pad_ID':[None],
  
 
        # 'Oxide_type' : [None],
        # 'Flat_band_volt_V' : Not Sure YEt yet
        # 'P_stop_conc' : NSY,
        # 'Proc' :NSY,
        # 'HD_Or_LD' : 

        
                                    })
    #save it in /new_results
    pd.set_option('expand_frame_repr', False)

    print(long_df)
    long_df.to_csv(csv_file)


    #print(criteria_More_than_two_neighbor_cells_bad_require_1_and_2)

#Tablename = HGC_HPK_Sensor_IV_Summary_LD_and_HD_fields





if __name__ == '__main__':

    updateDB()
#     #convert_csv_to_sql(csv_file)