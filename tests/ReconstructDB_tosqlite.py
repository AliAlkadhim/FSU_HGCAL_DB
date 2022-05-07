import sqlite3
import sys
import csv
import re
import os

try:
    import sqlite3 as sql
    have_sqlite3 = True
except ImportError:
    sqlite3=None
    have_sqlite3=False
    print("you don't have sqlite3, do 'sudo apt-get install sqlite3'")

csv_file_dir = 'old_tables_csv/'

def format_field(fields):
    '''CONVERT FIELDS TO SQLITE SYNTAX WHEN CREATING A NEW TABLE
    '''
    ex_statement = ''
    for f in fields[:-1]:
        ex_statement=ex_statement + ' '+ f + ' TEXT '  +','
    ex_statement = ex_statement + fields[-1] + ' TEXT'
    return '  (  '   + ex_statement + ' ) '


def tuple_field_names(fields):
    """Return tuple of field names for sqlite like ( Sensor_ID, Scratch_pad_ID, Thick_ness, P_Stop, ...)"""
    s = ' ( ' + fields[0]
    for f in fields[1:]:
        s = s+ ', ' + f
    s = s + ' )'
    return s

def convert_row_to_tuple(row):
    """Given a list of strings, which constitutes a row, convert it to ('row[0]', 'row[1]', ... """
    row_tuple = '('
    for element in row[:-1]:
        # element = ''.join(element)
        # element = re.sub('\,', '_', element)
        # split_element = element.split(' ')
        # if len(split_element) > 1:
        #     element = split_element[0] + split_element[1]
        row_tuple=row_tuple+ "'" + element + "', "
    row_tuple = row_tuple + "'" + row[-1] + "'"
    row_tuple = row_tuple + ')'
    return row_tuple

# def return_row_data(rows):
#     for element in ro


def convert_csv_to_sqlite_table(csv_file):
    """input: csv file for a table
    output: an sql table syntax for that csv file"""
    #tablename = csv_file.split('/')[-1][:-4]
    # csv_file_path = csv_file_dir
    Tablename= csv_file.split('.')[0]

    #example Tablename: 'HGC_HPK_Sensor_IV_Summary_LD_and_HD_fields'
    fields = []
    rows=[]
    csv_file_dir = 'old_tables_csv/'

    #with open(csv_file_dir + csv_file,'r') as csvfile: #use this if you are running on one file, where the command is something like "convert_csv_to_sqlite_table('Full_Sensor.csv')
    with open(csv_file_dir + csv_file,'r') as csvfile:    #use this when running on multiple files (tables), where the command is for file in os.listdir(csv_file_dir): convert_csv_to_sqlite_table(csv_file)
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)

    new_fields = []
    for field in fields:
        #we have to replace whitespace with _, field names have to be continuous
        #we have to remove "-"" from field names and other characters
        new_field = re.sub('\s+', '_', field)
        new_field = re.sub('-', '', new_field)
        new_field = re.sub('\.', '', new_field)
        new_field = re.sub('\?', '', new_field)
        new_field = re.sub('\<', 'LT', new_field)#LESS THAN
        new_field = re.sub('\>', 'MT', new_field)#MORE THAN
        new_field = re.sub('\*', 'TIMES', new_field)
        new_field = re.sub('1_', 'ONE_', new_field)
        new_field = re.sub('\/', '', new_field)
        new_field = re.sub('\(', '_', new_field)
        new_field = re.sub('\)', '', new_field)
        new_fields.append(new_field)

    fields = new_fields
    print(fields)
    try:
        DB_NAME =   'TEST_2.db'
        connection = sql.connect(DB_NAME)

        cursor = connection.cursor()
    except sqlite3.Error as err:
        print('could not open database %s' % err)
        exit(1)
    # cursor.execute("DROP DATABASE IF EXISTS 'SQLITE_TEST.db'",  DB_NAME)
    # cursor.execute("CREATE DATABASE ?",  DB_NAME)
    # cursor.execute("USE ?",  DB_NAME)

    execute_command0 = 'DROP TABLE IF EXISTS {}'.format(Tablename)
    cursor.execute(execute_command0)

    execute_command1 = 'CREATE TABLE IF NOT EXISTS {} '.format(Tablename)
    # execute_command2 = ''.join(
    # execute_command = '''CREATE TABLE IF NOT EXISTS %s  (
    # Sensor_ID INTEGER PRIMARY KEY, Scratch_pad_ID TEXT, Thick_ness TEXT, 
    # P_Stop TEXT, Oxide_type TEXT, Flat_band_volt__V TEXT, P_Stop_conc TEXT, Proc TEXT, Status_in_view_of_dicing_frame_removal TEXT, 
    # Current_location TEXT, RINSC_plan TEXT, Pre_irrad_test_on_DF TEXT, Pre_irrad_test_off_DF TEXT, 
    # Sent_to_RINSC TEXT, RINSC_irrad_round TEXT, Post_irrad_test TEXT 
    # )
    # ''' % Tablename
    
    execute_command2 = format_field(fields)
 
    execute_command = execute_command1 + execute_command2
    print('\nexecute command=', execute_command)

    cursor.execute(execute_command)
    # print(Tablename)
    ############ADD ROWS TO TABLES
    
    for row in rows:
        row_ex_command1 = 'INSERT INTO ' + Tablename 
        row_ex_command2 = tuple_field_names(fields)
        print('tuple_field_names(fields) = ', tuple_field_names(fields))
        row_ex_command3 = ' VALUES'
        row_ex_command4 = convert_row_to_tuple(row)



        row_ex_command =  row_ex_command1 + row_ex_command2 + row_ex_command3 + row_ex_command4 
        print(row_ex_command)
        cursor.execute(row_ex_command)
        # for element in row[:-1]:
        #     if (not element) or (element=='-'):#check if the string is empty, if it is, it should be NULL in sql
        #         row_ex_command = row_ex_command + 'NONE'
        #     else:
        #         row_ex_command = row_ex_command +

        #  cursor.executemany(row_ex_command)

    connection.commit()
    cursor.close()
    connection.close()







# DB_NAME = 'SQLITE_TEST.db'
# connection = sql.connect(DB_NAME)

# cursor = connection.cursor()


# cursor.execute(SQL_COMMAND)

if __name__ == '__main__':
    for csv_file in os.listdir('old_tables_csv'):
        if csv_file.endswith('.csv'):
            convert_csv_to_sqlite_table(csv_file)