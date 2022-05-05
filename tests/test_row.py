import sys
import os
import subprocess as sb
import pandas as pd
latest_sensor = 'N4790_19'
DUT = pd.read_csv(os.environ['WORKFLOW_DIR']+'/database/csv/DUTs.csv')
latest_sensor_row = DUT.loc[DUT['Name'].endswith(latest_sensor)]
print(latest_sensor_row)
