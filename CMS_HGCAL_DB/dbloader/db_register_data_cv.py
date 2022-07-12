#!/usr/bin/env python3

import os
import numpy as np
import xml.etree.ElementTree as etree
import xml.dom.minidom as minidom

from optparse import OptionParser



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
        'EXTENSION_TABLE_NAME': 'HGC_CERN_SENSOR_CV',
        'NAME': 'HGC CERN Sensor CV Test'
    }
    for key in attr_type:
        tmp = etree.SubElement(typ, key)
        tmp.text = attr_type[key]

    ## fill run xml
    run = etree.SubElement(header, "RUN")
    for key in attr_run:
        tmp = etree.SubElement(run, key)
        tmp.text = attr_run[key]
        
    ## load measurement data
    ## columns structure is [v, j, c, dc, cur_tot, vol, t, temp, hum, -, -, imp, dimp, phi, dphi, -, c_unc]
    dat = np.genfromtxt(fn, dtype='float', comments='#')

    ## get volts and channels
    volts = np.array([d for d in dat if d[1] == dat[0, 1]])[:, 0]
    chans = np.array([d for d in dat if d[0] == dat[0, 0]])[:, 1]

    nvolts = len(volts)
    nchans = len(chans)
    
    ## skip last voltage steps if not complete
    if len([d for d in dat if d[1] == dat[-1, 1]]) != nchans:
        volts = np.delete(volts, -1, 0)
        nvolts = len(volts)
    
    ## fill part xml
    data_set = etree.Element("DATA_SET")
    root.append(data_set)
    
    part = etree.SubElement(data_set, "PART")
    
    attr_part = {
        'KIND_OF_PART': 'HGC Sensor',
        'SERIAL_NUMBER': dat_wafer['SERIAL_NUMBER']
    }
    
    for key in attr_part :
        tmp = etree.SubElement(part, key)
        tmp.text = attr_part [key]
    
    ## retrieve data on channel basis and write to xml
    for c in chans:
        table = np.array([d for d in dat if d[1] == c])
                    
        ## fill measurement xml
        for tuple in table:
            data = etree.SubElement(data_set, "DATA")
        
            dat_cell = {
                'VOLTS': tuple[0],
                'CELL_NR': int(tuple[1]),
                'CPCTNCE_PFRD': tuple[2],
                'ERR_CPCTNC_PFRD': tuple[3],
                'TOT_CURNT_NANOAMP': tuple[4],
                'ACTUAL_VOLTS': tuple[5],
                'TIME_SECS': tuple[6],
                'TEMP_DEGC': tuple[7],
                'HUMIDITY_PRCNT': tuple[8],
                'IMP_OHM': tuple[11],
                'PHS_RAD': tuple[13],
                'ORG_CPCTNC_PFRD': tuple[15]
            }
            
            for key in dat_cell:
                tmp = etree.SubElement(data, key)
                tmp.text = str(dat_cell[key])
                
    ## add root to tree and save 
    tree = etree.ElementTree(root)
    
    path = os.getcwd()
    with open(path + '/' + '%s-data-cv.xml' % (dat_wafer['SERIAL_NUMBER']), "w") as f:
        f.write(prettify_xml(root))

    return 0



## Main Executable
## ------------------------------------

def main():
    usage = "usage: ./db_register_data_cv.py -i [path_to_file] -s [serial_number] -l [location] -o [operator] [options]"

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
        print("-- ./db_register_data_cv.py -i /Volumes/Media/Data/hgc/sensor_testing/cern/probecard/HPK_8in_198ch_300um_com_Z3415_4/1stMeasurement/HPK_8in_198ch_300um_com_Z3415_4_CV.txt -s '8-192-300F-00-Z3415-00004-SE-1' --location 'CERN' --operator 'Florian Pitters' --comment 'first real entry'")

    else:
        dat_wafer = {
            'SERIAL_NUMBER': options.sn,
        }
        
        attr_run = {
            'RUN_NAME': 'CV CERN 01',
            'RUN_BEGIN_TIMESTAMP': '2018-05-14 00:00:00',
        	'RUN_END_TIMESTAMP': '2018-05-14 01:00:00',
        	'INITIATED_BY_USER': options.operator,
        	'LOCATION': options.location,
        	'COMMENT_DESCRIPTION': options.comment
        }
        
        ret = create_data_xml(dat_wafer, attr_run, options.input_file)
        


if __name__ == "__main__":
    main()
    
