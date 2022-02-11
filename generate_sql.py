import csv
import subprocess as sb
import re

filename = "FSU_tables/Full_Sensor.csv"

fields = []
rows=[]

with open(filename, 'r') as csvfile:
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
    new_field = re.sub('\(', '_', new_field)
    new_field = re.sub('\)', '', new_field)
    new_fields.append(new_field)

fields = new_fields

def generate_sql_code(fields, rows, Tablename, DB_sql_file):
    with open(DB_sql_file,'w') as sql_file:
        database = DB_sql_file[:-4] #name of the database without .sql
        
        sql_file.write('use %s' % database +';\n')
        sql_file.write('drop table '+ Tablename + ';\n') #we drop it before creating it, otherwise it throws an error that table already exists

        sql_file.write('create table ' + Tablename + ' ( ')
        
        for field in fields[:-1]:

            sql_file.write(' ' + field + ' varchar(32),')
        sql_file.write(' ' + fields[-1] + ' varchar(32)')
        sql_file.write(' );\n')




print('field names are: ', fields)
print('\n')
print('rows are:', rows[:5])
generate_sql_code(fields, rows, 'Full_Sensor', 'FSU_HGCAL.sql')