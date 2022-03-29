import sys
import os
import subprocess as sb
def updateDB():
    """automatically updates the FSUDB, given either IV or CV"""
    if sys.argv[1]:
        measure = sys.argv[1]#this is either IV or CV
    else:
	print('You must do python updateDB.py IV\n (or CV)')
        return
    if sys.argv[1]== 'IV':
        TMPFILES_DIR_IV = os.environ['TMPFILES_DIR_IV']

        grading_dir = TMPFILES_DIR_IV +'/-/grading/'
        cmd = 'ls -t $TMPFILES_DIR_IV/-/grading | head -n 1'
        latest_sensor = sb.Popen(cmd, shell=True,stdin=sb.PIPE, stdout=sb.PIPE, stderr=sb.STDOUT)
        latest_sensor = latest_sensor.stdout.read()
        latest_sensor=latest_sensor[:-1]

        grading_results_for_latest_sensor_file = grading_dir + latest_sensor + '/grading_results.tex'
        with open(grading_results_for_latest_sensor_file, 'r') as f:
            for line in f.readlines():
                print(line)






if __name__ == '__main__':

    updateDB()

