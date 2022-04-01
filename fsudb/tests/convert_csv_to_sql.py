import sys
import csv
import re
import os

def convert_csv_to_sql(csv_file):
    """input: csv file for a table
    output: an sql table syntax for that csv file"""
    #tablename = csv_file.split('/')[-1][:-4]
    Tablename= csv_file.split('.')[0]
    #example Tablename: 'HGC_HPK_Sensor_IV_Summary_LD_and_HD_fields'
    fields = []
    rows=[]
    csv_file_path = 'old_tables_csv/'
    with open(csv_file_path + csv_file,'r') as csvfile:
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
    #or with open(new_results_sql/...)
    with open('old_tables_sql/' + Tablename+'.sql','w') as table_sqlfile:
        table_sqlfile.write('CREATE TABLE ' + Tablename + ' ( ')
        
        for field in fields[:-1]:

            table_sqlfile.write(' ' + field + ' VARCHAR(64),')
        table_sqlfile.write(' ' + fields[-1] + ' VARCHAR(64)')
        table_sqlfile.write(' );\n')
        # the syntax for INSERTing rows is: INSERT INTO test VALUES (1, 'here', ' nahmean');
        for row in rows:
            table_sqlfile.write('INSERT INTO ' + Tablename +' VALUES (')
            for element in row[:-1]:
                if (not element) or (element=='-'):#check if the string is empty, if it is, it should be NULL in sql
                    table_sqlfile.write('NULL' +', ')
                else:
                    table_sqlfile.write("'" + element.strip() + "', ")
            if (not row[-1]) or (row[-1]=='-'):
                table_sqlfile.write('NULL' +' ')
            # if row[-1] == '-':
            #     table_sqlfile.write('NULL' +' ')
            else:
                table_sqlfile.write("'" + row[-1].strip() + "' ")
            table_sqlfile.write(');\n')




#csv_file = 'new_results_csv/long_df.csv'
# if __name__ == '__main__':
#     # for file in os.listdir('old_tables_csv'):
#     convert_csv_to_sql(file)