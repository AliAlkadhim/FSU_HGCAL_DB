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

FSUDB_OUTPUT_DIR=os.environ['FSUDB_OUTPUT_DIR']

def register_wafer_xml(Wafers_to_register_DF, Sensor_ID):
    KIND_OF_PART='300um LD Si Sensor Wafer'
    ID = str(int(Sensor_ID))
    xml_filename = f'{ID}.xml'
    
    xml_wafer_file = os.path.join(FSUDB_OUTPUT_DIR,xml_filename) 
    sensor_row = Wafers_to_register_DF[Wafers_to_register_DF['Sensor ID'] == Sensor_ID]
    OBA_NUMBER = sensor_row['OBA Number'].item()
    Current_location_sensor = str(sensor_row['Current location sensor'].item())
    Current_location_halfmoons = str(sensor_row['Current location half moons'].item())
    
    with open(xml_wafer_file, 'w+') as xmlf:
        xmlf.write('<ROOT>\n')
        xmlf.write('<PARTS>\n')
        # Sensor Wafer
        xmlf.write('<PART mode="auto">\n')
        xmlf.write(f'\t<KIND_OF_PART>{KIND_OF_PART}</KIND_OF_PART>\n')
        xmlf.write(f'\t<SERIAL_NUMBER>{ID}</SERIAL_NUMBER>\n')
        #NAME LABEL IS NOW OBA NUMBER. e.g. N8738_2 is being replaced with OBA_NUMBER
        xmlf.write(f'\t<NAME_LABEL>{OBA_NUMBER}</NAME_LABEL>\n')
        xmlf.write('\t<COMMENT_DESCRIPTION>preproduction sensor Delivery #1</COMMENT_DESCRIPTION>\n')
        xmlf.write(f'\t<LOCATION>{Current_location_sensor}</LOCATION>\n')
        xmlf.write('\t<MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>\n')
        
        xmlf.write('\t<CHILDREN>\n')
        ############################################################
        # Sensor Wafer Full
        xmlf.write('\t\t<PART mode="auto">\n')
        xmlf.write(f'\t\t<KIND_OF_PART>{KIND_OF_PART} Full</KIND_OF_PART>\n')
        xmlf.write(f'\t\t<SERIAL_NUMBER>{ID}_0</SERIAL_NUMBER>\n')
        xmlf.write(f'\t\t<NAME_LABEL>{OBA_NUMBER}_0</NAME_LABEL>\n')
        xmlf.write(f'\t\t<LOCATION>{Current_location_sensor}</LOCATION>\n')
        xmlf.write(f'\t\t<MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>\n')
        xmlf.write(f'\t\t</PART>\n')
        ############################################################
        # Sensor Wafer Halfmoon_Top
        xmlf.write(f'\t\t<PART mode="auto">\n')
        xmlf.write(f'\t\t<KIND_OF_PART>{KIND_OF_PART} Halfmoon_Top</KIND_OF_PART>\n')
        xmlf.write(f'\t\t<SERIAL_NUMBER>{ID}_TOP</SERIAL_NUMBER>\n')
        xmlf.write(f'\t\t<NAME_LABEL>{OBA_NUMBER}_TOP</NAME_LABEL>\n')
        xmlf.write(f'\t\t<LOCATION>{Current_location_halfmoons}</LOCATION>\n')
        xmlf.write(f'\t\t<MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>\n')
        xmlf.write(f'\t\t</PART>\n')
        ############################################################
        # Sensor Wafer Halfmoon_Bottom

        xmlf.write(f'\t\t <PART mode="auto">\n')
        xmlf.write(f'\t\t <KIND_OF_PART>{KIND_OF_PART} Halfmoon_Bottom</KIND_OF_PART>\n')
        xmlf.write(f'\t\t <SERIAL_NUMBER>{ID}_BOT</SERIAL_NUMBER>\n')
        xmlf.write(f'\t\t <NAME_LABEL>{OBA_NUMBER}_BOT</NAME_LABEL>\n')
        xmlf.write(f'\t\t <LOCATION>{Current_location_halfmoons}</LOCATION>\n')
        xmlf.write(f'\t\t <MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>\n')
        xmlf.write(f'\t\t </PART>\n')
        ############################################################
        # Sensor Wafer Halfmoon_UpperLeft

        xmlf.write(f'\t\t<PART mode="auto">\n')
        xmlf.write(f'\t\t<KIND_OF_PART>{KIND_OF_PART} Halfmoon_UpperLeft</KIND_OF_PART>\n')
        xmlf.write(f'\t\t<SERIAL_NUMBER>{ID}_UL</SERIAL_NUMBER>\n')
        xmlf.write(f'\t\t<NAME_LABEL>{OBA_NUMBER}_UL</NAME_LABEL>\n')
        xmlf.write(f'\t\t<LOCATION>{Current_location_halfmoons}</LOCATION>\n')
        xmlf.write(f'\t\t<MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>\n')
        xmlf.write(f'\t\t</PART>\n')
        ############################################################
        # Sensor Wafer Halfmoon_LowerLeft

        xmlf.write(f'\t\t<PART mode="auto">\n')
        xmlf.write(f'\t\t<KIND_OF_PART>{KIND_OF_PART} Halfmoon_LowerLeft</KIND_OF_PART>\n')
        xmlf.write(f'\t\t<SERIAL_NUMBER>{ID}_LL</SERIAL_NUMBER>\n')
        xmlf.write(f'\t\t<NAME_LABEL>{OBA_NUMBER}_LL</NAME_LABEL>\n')
        xmlf.write(f'\t\t<LOCATION>{Current_location_halfmoons}</LOCATION>\n')
        xmlf.write(f'\t\t<MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>\n')
        xmlf.write(f'\t\t</PART>\n')
        ############################################################
        # Sensor Wafer Halfmoon_LowerRight

        xmlf.write(f'\t\t<PART mode="auto">\n')
        xmlf.write(f'\t\t<KIND_OF_PART>{KIND_OF_PART} Halfmoon_LowerRight</KIND_OF_PART>\n')
        xmlf.write(f'\t\t<SERIAL_NUMBER>{ID}_LR</SERIAL_NUMBER>\n')
        xmlf.write(f'\t\t<NAME_LABEL>{OBA_NUMBER}_LR</NAME_LABEL>\n')
        xmlf.write(f'\t\t<LOCATION>{Current_location_halfmoons}</LOCATION>\n')
        xmlf.write(f'\t\t<MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>\n')
        xmlf.write(f'\t\t</PART>\n')
        ############################################################
        # Sensor Wafer Halfmoon_UpperRight

        xmlf.write(f'\t\t<PART mode="auto">\n')
        xmlf.write(f'\t\t<KIND_OF_PART>{KIND_OF_PART} Halfmoon_UpperRight</KIND_OF_PART>\n')
        xmlf.write(f'\t\t<SERIAL_NUMBER>{ID}_UR</SERIAL_NUMBER>\n')
        xmlf.write(f'\t\t<NAME_LABEL>{OBA_NUMBER}_UR</NAME_LABEL>\n')
        xmlf.write(f'\t\t<LOCATION>{Current_location_halfmoons}</LOCATION>\n')
        xmlf.write(f'\t\t<MANUFACTURER>Hamamatsu-HPK</MANUFACTURER>\n')
        xmlf.write(f'\t\t</PART>\n')
        ############################################################
        xmlf.write('</CHILDREN>\n')
        xmlf.write('</PART>\n')

        xmlf.write('</PARTS>\n')
        xmlf.write('</ROOT>\n')