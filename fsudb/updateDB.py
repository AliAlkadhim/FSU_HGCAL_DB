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
        latest_sensor = sb.Popen(cmd, shell=True)
        print('the latest sensor is ', latest_sensor)
if __name__ == '__main__':
    
    updateDB()


