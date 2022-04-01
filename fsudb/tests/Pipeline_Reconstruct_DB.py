import os
import csv
import subprocess as sb
import convert_csv_to_sql as convert
def Pipeline_Reconstruct_DB():

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
    
    if __name__ == '__main__':
        Pipeline_Reconstruct_DB()