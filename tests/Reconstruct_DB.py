import os
import csv
import subprocess as sb
import argparse
import convert_csv_to_sql as convert

parser = argparse.ArgumentParser(description='Generate FSU DB SQL file by doing, e.g. python Reconstruct_DB.py --DB FSU_DB')
parser.add_argument('--DB', type=str, required=False, help = '''name of the complete database (which includes all tables)
                        This will be stored in /complete_DB/<DB.sql>''')
args = parser.parse_args()



def Reconstruct_DB():

    """
    just do python Pipeline_ReconstructDB.py in
    1. starts from tests/old_tables_csv
        for table_File in old_tables_csv:
    2.        python convert_csv_to_sql(file): this stores sql files for each table in old_tables_sql
    3. do a command that does open(complete_DB.sql):
        write(drop database if exists and create new database)
        for file in old_tables_csv:
            open it in and write its contents to complete_DB.sql    
    """
    for file in os.listdir('old_tables_csv'):
        convert.convert_csv_to_sql(file)
        #convert.convert_sql_tables_to_one_DB(database = 'FSU_TEST_DB')
        convert.convert_sql_tables_to_one_DB(database = args.DB)
    
if __name__ == '__main__':
    Reconstruct_DB()


'''Now you can do the following in mysql

show tables;
to see that we actually have this table inside the FSU_HGCAL database. And we can run 
select * from Full_Sensor; to see the columns in this table

and we can do any query we want really efficiently, for example

select Current_location from Full_Sensor;

select Sensor_ID, Current_location from Full_Sensor;

select Current_location from Full_Sensor where Sensor_ID='N4791_1';'''
