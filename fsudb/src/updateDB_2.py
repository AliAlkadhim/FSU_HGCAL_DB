import sys
import os
import subprocess as sb
import pandas as pd
#import fsudb
# if args.tablename == "HGC_HPK_Sensor_IV_Summary_LD_and_HD.csv":
#     #the long Ncell_with_1800_greaterthan_2_point_5_times_1600_and_1600_greaterthan_10nA_OR_1800_greaterthan_25nA_and_1600_lessthan_10nA


HGC_HPK_Sensor_IV_Summary_LD_and_HD_fields = ['Sensor_ID', 'Scratch_pad_ID', 
'Thick_ness', 'P_Stop', 
'Oxide_type', 'Flat_band_volt_V', 'P_stop_conc', 
'Proc', 'HD_Or_LD', 
'I_tot_600V_lessthan_100mA', 
'I_tot_800V_lessthan_2_point_5_times_I_tot_600V', 
'Ncell_with_1800_greaterthan_2_point_5_times_1600', 
'More_than_8_bad_cells_require_1_and_2', 
'More_than_two_neighbor_cells_bad_require_1_and_2']

def updateDB():
    """automatically updates the FSUDB, given either IV or CV.
    Big picture: running 'updateDB IV' should:
    1. make a csv file for each table, fill it with all the necessary data from the test results (in TMP or SUMMARY directories
    ,store it in 'new_results' directory
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
        TMPFILES_DIR_IV = os.environ['TMPFILES_DIR_IV']

        grading_dir = TMPFILES_DIR_IV +'/-/grading/'
        cmd = 'ls -t $TMPFILES_DIR_IV/-/grading | head -n 1'
        latest_sensor = sb.Popen(cmd, shell=True,stdin=sb.PIPE, stdout=sb.PIPE, stderr=sb.STDOUT)
        latest_sensor = latest_sensor.stdout.read()
        latest_sensor=latest_sensor[:-1]

        grading_results_for_latest_sensor_file = grading_dir + latest_sensor + '/grading_results.tex'
        

        #scratchpad_ID has to be obtained from the database like HGC_HPK..., I think it has to be imput manually by the user!
        ###########READ INFO FROM DUT
        DUT = pd.read_csv(os.environ['WORKFLOW_DIR']+'/database/csv/DUTs.csv')
        for row_name in DUT['Name']:
            if row_name.endswith(latest_sensor):

                long_name == DUT['Name'][DUT['Name'] == row_name]
                Size = DUT['Size'][DUT['Name'] == row_name]
                NChannels= DUT['NChannels'][DUT['Name'] == row_name]
                Doping = DUT['Doping'][DUT['Name'] == row_name]
                Thickness = DUT['Thickness'][DUT['Name'] == row_name]
                Pstop = DUT['Pstop'][DUT['Name'] == row_name]
                
        ######READ INFO FROM IVMeasurements        
        IVMeasurements = pd.read_csv(os.environ['WORKFLOW_DIR']+'/database/csv/IVMeasurements.csv')
        for row_name in IVMeasurements['ID']:
            if row_name.startswith(latest_sensor):
                #CURRENTLY TAKING THE BARE NAME, without _test01, _testN
                Date = IVMeasurements['Date'][IVMeasurements['ID']==row_name]
                Station = IVMeasurements['Station'][IVMeasurements['ID']==row_name]
                HVResistance = IVMeasurements['HVResistance'][IVMeasurements['ID']==row_name]
                Temperature = IVMeasurements['Temperature'][IVMeasurements['ID']==row_name]

        long_df = pd.DataFrame({
        'Sensor_ID': [latest_sensor],
        'long_name':[long_name],
        'Size':[Size],
        'NChannels':[NChannels],
        'Doping' :[Doping],
        'Thickness' : [Thickness],
        'P_Stop' : [Pstop],

        'Date': [Date],
        'Station':[Station],
        'HVResistance':[HVResistance],
        'Temperature':[Temperature],

        'Scratch_pad_ID':[None],
  
 
        'Oxide_type' : [None],
        #'Flat_band_volt_V' : Not Sure YEt yet
        #'P_stop_conc' : NSY,
        #'Proc' :NSY,
        #'HD_Or_LD' : 

        
                                    })
        with open(grading_results_for_latest_sensor_file, 'r') as f:
            for line_ind, line in enumerate(f.readlines()):
                pass
                # pd_dict = {'Sensor_ID': , 'Scratch_pad_ID':, 
                #     'Thick_ness' : , 'P_Stop' : , 
                #     'Oxide_type' : , 'Flat_band_volt_V' : , 'P_stop_conc' : , 
                #     'Proc' : , 'HD_Or_LD' :, 
                #     'I_tot_600V_lessthan_100mA' : , 
                #     'I_tot_800V_lessthan_2_point_5_times_I_tot_600V' , 
                #     'Ncell_with_1800_greaterthan_2_point_5_times_1600', 
                #     'More_than_8_bad_cells_require_1_and_2', 
                #     'More_than_two_neighbor_cells_bad_require_1_and_2'}
                # df = pd.DataFrame.from_dict(pd_dict)
    print(long_df.head())






if __name__ == '__main__':

    updateDB()

