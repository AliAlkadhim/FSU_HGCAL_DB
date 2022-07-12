# Making IV/CV XML Tables for CMS HGCAL DB

To make tables to upload to the `int2r` CMS HGCAL DB, based on the XML table tempates in `CMS_HGCAL_DB/from_Umesh/CMS_HGCAL_DB/from_Umesh/XML Templates HGCAL Si Sensors.docx`, do

`python TXT_TO_XML.py --f <.TXT DATA FILE NAME> --t <TABLE NAME>`

For example, to produce an xml file for the `HGC_CERN_SENSOR_IV` table associated with the test results in `HPK_8in_198ch_2019_N4792_18_03242022_FullRetest_IV.txt` do

**`python TXT_TO_XML.py --f HPK_8in_198ch_2019_N4792_18_03242022_FullRetest_IV.txt --t HGC_CERN_SENSOR_IV`**

This produces `N4792_18_03242022_FullRetest_HGC_CERN_SENSOR_IV_TEST.xml` which can now be uploaded to the DB. Do `python TXT_TO_XML.py --help` for help.

To use other available optional arguments, do for example

`python TXT_TO_XML.py --f HPK_8in_198ch_2019_N4792_18_03242022_FullRetest_IV.txt --t HGC_CERN_SENSOR_IV --user Ali --location FSU --comment 'no comment'`


To produce an xml file for the `HGC_CERN_SENSOR_CV` table associated with the test results in `HPK_8in_198ch_2019_200118_20220707_test1_CV.txt` do

**`python TXT_TO_XML.py --f HPK_8in_198ch_2019_200118_20220707_test1_CV.txt --t HGC_CERN_SENSOR_CV`**

This produces `200118_20220707_test1_HGC_CERN_SENSOR_CV_TEST.xml` which is ready to be uploaded to the the DB. 
