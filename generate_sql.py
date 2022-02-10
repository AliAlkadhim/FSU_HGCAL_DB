import csv
import subprocess as sb
filename = "Full_Sensor.csv"

fields = []
rows=[]

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)





def generate_sql_code(fields, rows, Tablename, DB_sql_file):
    with open(DB_sql_file,'w') as sql_file:
        database = DB_sql_file[:-4] #name of the database without .sql
        
        sql_file.write('use %s' % database +';\n')

        sql_file.write('create table ' + Tablename + ' ( ')
        
        for field in fields:
            field.replace("\s", "_")
            sql_file.write(' ' + field + ' varchar(16),')
        sql_file.write(' );\n')









print('field names are: ', fields)
print('\n')
print('rows are:', rows[:5])
generate_sql_code(fields, rows, 'Full_Sensor', 'FSU_HGCAL.sql')