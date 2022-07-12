#!/usr/bin/env python3

import os
import numpy as np
import xml.etree.ElementTree as etree
import xml.dom.minidom as minidom

from optparse import OptionParser
from io import StringIO



## Function Definitions
## ------------------------------------

def prettify_xml(tree):
    xml_ugly_string = etree.tostring(tree, 'utf-8')
    xml = minidom.parseString(xml_ugly_string)
    xml_pretty_string = xml.toprettyxml(indent="\t")
    return xml_pretty_string
    
    
def create_data_xml(dat_wafer, attr_run, fn):
    root = etree.Element("ROOT")
    
    ## split input path
    path = '/'.join(fn.split('/')[:-1])
    file_name = fn.split('/')[-1]
    
    ## header xml
    header = etree.Element("HEADER")
    root.append(header)
    
    ## fill type xml
    typ = etree.SubElement(header, "TYPE")
    attr_type = {
        'EXTENSION_TABLE_NAME': 'HGC_CERN_SENSOR_IV_SUMRY',
        'NAME': 'HGC CERN Sensor IV Summary'
    }
    for key in attr_type:
        tmp = etree.SubElement(typ, key)
        tmp.text = attr_type[key]
    
    ## fill run xml
    run = etree.SubElement(header, "RUN")
    for key in attr_run:
        tmp = etree.SubElement(run, key)
        tmp.text = attr_run[key]
    
    ## fill part xml
    data_set = etree.Element("DATA_SET")
    root.append(data_set)
    
    part = etree.SubElement(data_set, "PART")
    
    attr_part = {
        'KIND_OF_PART': 'HGC Sensor',
        'SERIAL_NUMBER': dat_wafer['SERIAL_NUMBER']
    }
    
    for key in attr_part:
        tmp = etree.SubElement(part, key)
        tmp.text = attr_part [key]
    
    ## read file and fill xml
    dat = np.genfromtxt(fn, dtype='S10', comments='#')
    table = [dat]
    for tuple in table:
        data = etree.SubElement(data_set, "DATA")

        dat_cell = {
            'TOT_CURNT_NANOAMP_600V': float(tuple[0]),
            'TOT_CURNT_NANOAMP_800V': float(tuple[1]),
            'NUM_BAD_CELLS': int(tuple[2]),
            'GRADE': tuple[3].decode('UTF-8'),
            'PASS': tuple[4].decode('UTF-8')
        }

        for key in dat_cell:
            tmp = etree.SubElement(data, key)
            tmp.text = str(dat_cell[key])
    
    ## add root to tree and save 
    tree = etree.ElementTree(root)
    
    path = os.getcwd()
    with open(path + '/' + '%s-data-iv-summary.xml' % (dat_wafer['SERIAL_NUMBER']), "w") as f:
        f.write(prettify_xml(root))

    return 0



## Main Executable
## ------------------------------------

def main():
    usage = "usage: ./db_register_data_iv_summary.py -i [path_to_file] -s [serial_number] -l [location] -o [operator] [options]"

    parser = OptionParser(usage=usage, version="prog 0.1")
    parser.add_option("-i", "--input", action="store", dest="input_file", type="string", \
        help="path to inut file")
    parser.add_option("-s", "--serial", action="store", dest="sn", type="string", \
        help="sensor serial number [8-CCC-TTT(E)-MM-BBBBB-SSSSS-SE-X]")
    parser.add_option("-l", "--location", action="store", dest="location", type="string", \
        help="wafer location")
    parser.add_option("-o", "--operator", action="store", dest="operator", type="string", \
        help="operator")
    parser.add_option("--comment", "--comment", action="store", dest="comment", type="string", \
        default="", help="comment")

    parser.add_option("--ex", "--examples", action="store_true", dest="fExamples",  help="print examples") 
    
    (options, args) = parser.parse_args()
    
    if options.fExamples:
        print("\nSome example commands for running this script\n")
        print("-- ./db_register_data_iv_summary.py -i ~/Documents/Works/hgc/hgcDatabase/test_iv_summary.txt -s '8-192-300F-00-Z3415-00004-SE-1' --location 'CERN' --operator 'Florian Pitters' --comment 'first real entry'")

    else:
        dat_wafer = {
            'SERIAL_NUMBER': options.sn,
        }
        
        attr_run = {
            'RUN_NAME': 'IV CERN 01',
            'RUN_BEGIN_TIMESTAMP': '2018-05-14 00:00:00',
        	'RUN_END_TIMESTAMP': '2018-05-14 01:00:00',
        	'INITIATED_BY_USER': options.operator,
        	'LOCATION': options.location,
        	'COMMENT_DESCRIPTION': options.comment
        }
        
        ret = create_data_xml(dat_wafer, attr_run, options.input_file)
        


if __name__ == "__main__":
    main()
