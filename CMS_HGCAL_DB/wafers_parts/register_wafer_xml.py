import pandas as pd
import os
import subprocess as sb
# import TXT_TO_XML as XML
# import logging


####################### CONFIGURATIONS ####################
# for working locally on my laptop, do
# export INPUT_DIR=/home/ali/Desktop/Pulled_Github_Repositories/FSU_HGCAL_DB/CMS_HGCAL_DB/wafers_parts/Preproduction
# export FSUDB_OUTPUT_DIR=/home/ali/Desktop/Pulled_Github_Repositories/FSU_HGCAL_DB/CMS_HGCAL_DB/wafers_parts/Preproduction/Preproduction_Wafers_Parts

INPUT_DIR=os.environ['INPUT_DIR']

# FSUDB_OUTPUT_DIR='CMS_HGCAL_DB/IV_CV_preseries_tested_at_FSU/'#where the head of it is the git repo
FSUDB_OUTPUT_DIR=os.environ['FSUDB_OUTPUT_DIR']

def register_wafer_xml(Sensor_ID):
    KIND_OF_PART='300um LD Si Sensor Wafer'
    xml_filename = f'{Sensor_ID}.xml'
    xml_wafer_file = os.path.join(FSUDB_OUTPUT_DIR,xml_filename) 
    with open(xml_wafer_file, 'w+') as xmlf:
        xmlf.write('<ROOT>\n')

        <PARTS>


        <PART mode="auto">
            <KIND_OF_PART>300um LD Si Sensor Wafer</KIND_OF_PART>
            <SERIAL_NUMBER>100114</SERIAL_NUMBER>
            <NAME_LABEL>N8738_2</NAME_LABEL>
            <COMMENT_DESCRIPTION>preseries sensor Delivery #1</COMMENT_DESCRIPTION>
            <LOCATION>FSU</LOCATION>
            <MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>


            <CHILDREN>

                <PART mode="auto">
                <KIND_OF_PART>300um LD Si Sensor Wafer Full</KIND_OF_PART>
                <SERIAL_NUMBER>100114_0</SERIAL_NUMBER>
                <NAME_LABEL>N8738_2_0</NAME_LABEL>
                <LOCATION>FSU</LOCATION>
                <MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>
                </PART>


                <PART mode="auto">
                <KIND_OF_PART>300um LD Si Sensor Wafer Halfmoon_Top</KIND_OF_PART>
                <SERIAL_NUMBER>100114_TOP</SERIAL_NUMBER>
                <NAME_LABEL>N8738_2_TOP</NAME_LABEL>
                <LOCATION>CERN</LOCATION>
                <MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>
                </PART>


                <PART mode="auto">
                <KIND_OF_PART>300um LD Si Sensor Wafer Halfmoon_Bottom</KIND_OF_PART>
                <SERIAL_NUMBER>100114_BOT</SERIAL_NUMBER>
                <NAME_LABEL>N8738_2_BOT</NAME_LABEL>
                <LOCATION>CERN</LOCATION>
                <MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>
                </PART>


                <PART mode="auto">
                <KIND_OF_PART>300um LD Si Sensor Wafer Halfmoon_UpperLeft</KIND_OF_PART>
                <SERIAL_NUMBER>100114_UL</SERIAL_NUMBER>
                <NAME_LABEL>N8738_2_UL</NAME_LABEL>
                <LOCATION>CERN</LOCATION>
                <MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>
                </PART>


                <PART mode="auto">
                <KIND_OF_PART>300um LD Si Sensor Wafer Halfmoon_LowerLeft</KIND_OF_PART>
                <SERIAL_NUMBER>100114_LL</SERIAL_NUMBER>
                <NAME_LABEL>N8738_2_LL</NAME_LABEL>
                <LOCATION>CERN</LOCATION>
                <MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>
                </PART>


                <PART mode="auto">
                <KIND_OF_PART>300um LD Si Sensor Wafer Halfmoon_LowerRight</KIND_OF_PART>
                <SERIAL_NUMBER>100114_LR</SERIAL_NUMBER>
                <NAME_LABEL>N8738_2_LR</NAME_LABEL>
                <LOCATION>CERN</LOCATION>
                <MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>
                </PART>


                <PART mode="auto">
                <KIND_OF_PART>300um LD Si Sensor Wafer Halfmoon_UpperRight</KIND_OF_PART>
                <SERIAL_NUMBER>100114_UR</SERIAL_NUMBER>
                <NAME_LABEL>N8738_2_UR</NAME_LABEL>
                <LOCATION>CERN</LOCATION>
                <MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>
                </PART>
            </CHILDREN>
        </PART>


        </PARTS>
        </ROOT>