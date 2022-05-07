import csv
import re
import os

def preprocess(file):
    rows=[]
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            for element in row:
                # if element.startswith('"'):
                if ',' in element:
                    element = re.sub(',', '-', element)
            rows.append(row)
            print(row)

if __name__ == '__main__':
    preprocess('old_tables_csv/FULL_SENSOR_PLANNING.csv')