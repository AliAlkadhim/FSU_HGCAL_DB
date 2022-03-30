import sys
import os
import subprocess as sb
import pandas as pd
# if args.tablename == "HGC_HPK_Sensor_IV_Summary_LD_and_HD.csv":
#     #the long Ncell_with_1800_greaterthan_2_point_5_times_1600_and_1600_greaterthan_10nA_OR_1800_greaterthan_25nA_and_1600_lessthan_10nA
#     fields = ['Sensor_ID', 'Scratch_pad_ID', 
#     'Thick_ness', 'P_Stop', 
#     'Oxide_type', 'Flat_band_volt_V', 'P_stop_conc', 
#     'Proc', 'HD_Or_LD', 
#     'I_tot_600V_lessthan_100mA', 
#     'I_tot_800V_lessthan_2_point_5_times_I_tot_600V', 
#     'Ncell_with_1800_greaterthan_2_point_5_times_1600', 
#     'More_than_8_bad_cells_require_1_and_2', 
#     'More_than_two_neighbor_cells_bad_require_1_and_2']

def updateDB():
    """automatically updates the FSUDB, given either IV or CV"""
    if sys.argv[1]:
        measure = sys.argv[1]#this is either IV or CV
    else:
	    print('You must do python updateDB.py IV\n (or CV)')
        #return
    if sys.argv[1]== 'IV':
        TMPFILES_DIR_IV = os.environ['TMPFILES_DIR_IV']

        grading_dir = TMPFILES_DIR_IV +'/-/grading/'
        cmd = 'ls -t $TMPFILES_DIR_IV/-/grading | head -n 1'
        latest_sensor = sb.Popen(cmd, shell=True,stdin=sb.PIPE, stdout=sb.PIPE, stderr=sb.STDOUT)
        latest_sensor = latest_sensor.stdout.read()
        latest_sensor=latest_sensor[:-1]

        grading_results_for_latest_sensor_file = grading_dir + latest_sensor + '/grading_results.tex'
        

        #scratchpad_ID has to be obtained from the database like HGC_HPK..., I think it has to be imput manually by the user!

        DUT = pd.read_csv(os.environ['WORKFLOW_DIR']+'/database/csv/DUTs.csv')
        for row in DUT['Name']:
            if row.endswith(latest_sensor):

                Thickness = DUT['Thickness'][DUT['Name'] == row]
                Pstop = DUT['Pstop'][DUT['Name'] == row]


        df = pd.DataFrame({'Sensor_ID': [latest_sensor],
        'Scratch_pad_ID':[None],
        'Thickness' : Thickness,
        'P_Stop' : Pstop,
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
    print(df)






if __name__ == '__main__':

    updateDB()

