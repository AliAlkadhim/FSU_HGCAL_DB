import csv
import subprocess as sb
import re

filename_Full_Sensor = "FSU_tables/strip_sensors.csv"
#"FSU_tables/Full_Sensor.csv"

fields = []
rows=[]

with open(filename_Full_Sensor, 'r') as csvfile:
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
        
        sql_file.write('DROP DATABASE IF EXISTS %s' % database + ';\n')
        sql_file.write('CREATE DATABASE %s' % database +';\n')
        sql_file.write('USE %s' % database +';\n')
        sql_file.write('DROP TABLE IF EXISTS %s' % Tablename + ';\n') #we drop it before creating it, 
        #otherwise it throws an error that table already exists

        sql_file.write('CREATE TABLE ' + Tablename + ' ( ')
        
        for field in fields[:-1]:

            sql_file.write(' ' + field + ' VARCHAR(32),')
        sql_file.write(' ' + fields[-1] + ' VARCHAR(32)')
        sql_file.write(' );\n')
        # the syntax for INSERTing rows is: INSERT INTO test VALUES (1, 'here', ' nahmean');
        for row in rows:
            sql_file.write('INSERT INTO ' + Tablename +' VALUES (')
            for element in row[:-1]:
                if (not element) or (element=='-'):#check if the string is empty, if it is, it should be NULL in sql
                    sql_file.write('NULL' +', ')
                else:
                    sql_file.write("'" + element.strip() + "', ")
            if (not row[-1]) or (row[-1]=='-'):
                sql_file.write('NULL' +' ')
            # if row[-1] == '-':
            #     sql_file.write('NULL' +' ')
            else:
                sql_file.write("'" + row[-1].strip() + "' ")
            sql_file.write(');\n')
        sql_file.write('SELECT * FROM %s' % Tablename + ';\n')


print('field names are: ', fields)
print('\n')
print('last rows are:', rows[- 1])

generate_sql_code(fields, rows, Tablename='Full_Sensor', DB_sql_file='FSU_HGCAL.sql')





##PQC
#next: other tables - list of fields and list of rows for each table, which are each list of lists!

# filename_PQC = "FSU_tables/PQC.csv"

# fields_PQC = []
# rows_PQC=[]

# with open(filename_PQC, 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     fields_PQC = next(csvreader)
#     for row in csvreader:
#         rows_PQC.append(row)

# new_fields = []
# for field in fields_PQC:
#     #we have to replace whitespace with _, field names have to be continuous
#     #we have to remove "-"" from field names and other characters
#     new_field = re.sub('\s+', '_', field)
#     new_field = re.sub('-', '', new_field)
#     new_field = re.sub('\.', '', new_field)
#     new_field = re.sub('\?', '', new_field)
#     new_field = re.sub('\(', '_', new_field)
#     new_field = re.sub('\)', '', new_field)
#     new_fields.append(new_field)

# fields_PQC = new_fields


#generate_sql_code(fields_PQC, rows_PQC, Tablename='PQC', DB_sql_file='FSU_HGCAL.sql')



# show tables;
# to see that we actually have this table inside the FSU_HGCAL database. And we can run 
# select * from Full_Sensor; to see the columns in this table

# and we can do any query we want really efficiently, for example

# select Current_location from Full_Sensor;

# select Sensor_ID, Current_location from Full_Sensor;

# select Current_location from Full_Sensor where Sensor_ID='N4791_1';


#NEXT: do markdown instructions for everything 
# Monday: talk about Unpref business - text Harry about Monday meeting time
# 
