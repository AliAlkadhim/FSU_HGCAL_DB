import sys
import os
def updateDB():
    """automatically updates the FSUDB, given either IV or CV"""
    if sys.argv[1]:
        measure = sys.argv[1]#this is either IV or CV
    else:
        print('You must do python updateDB.py IV\n (or CV)')
        return
    if sys.argv[1]== 'IV':
        TMPFILES_DIR_IV = os.environ('TMPFILES_DIR_IV')
        grading_file = TMPFILES_DIR_IV +'/-/grading/'


if __name__ == '__main__':
    
    updateDB()


