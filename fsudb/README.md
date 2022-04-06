# Current Functionality: ALL CURRENT USE OF THIS PACKAGE SHOULD BE DONE IN THE `/tests/` DIRECTORY.
----------

# Reconstruct Existing Data Into Database (do this first)- Workflow: 
* Go to /tests/

* First define and store your old tables (these are from the spreadsheets), such that each table is its own csv file, in `FSU_HGCAL_DB/fsudb/tests/old_tables_csv`. The Table names will be the names prior to the ".csv" extension, so make sure you're satisfied with the names! We have added our tables in there, but some attributes of the tables might be changed soon...

* You can go to `FSU_HGCAL_DB/fsudb/tests` and do `python Reconstruct_DB.py --DB <your choice of a database name>`, e.g. `python Reconstruct_DB.py --DB FSUDB` . This generates an sql table syntax for each of your tables in `FSU_HGCAL_DB/fsudb/tests/old_tables_sql` into a complete dataframe in `/complete_DB/<your choice of a database name>.sql`. 

* From there, you can interact with the complete DB. I like to use mysql, where you can do queries such as 

`select Current_location from Full_Sensor;`
 
 or

`select Sensor_ID, Current_location from Full_Sensor;`

or

`select Current_location from Full_Sensor where Sensor_ID='N4791_1';`


------------
## Update DB to Include Latest Analysis Results (do this second) - Workflow:
* Go to /tests/
