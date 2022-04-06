# Current Functionality: ALL CURRENT USE OF THIS PACKAGE SHOULD BE DONE IN THE `/tests/` DIRECTORY.
----------

# Reconstruct Existing Data Into Database (do this first)- Workflow: 
* Go to /tests/

* First define and store your old tables (these are from the spreadsheets), such that each table is its own csv file, in `FSU_HGCAL_DB/fsudb/tests/old_tables_csv`. The Table names will be the names prior to the ".csv" extension, so make sure you're satisfied with the names! We have added our tables in there, but some attributes of the tables might be changed soon...

* You can go to `FSU_HGCAL_DB/fsudb/tests` and do `python Reconstruct_DB.py --DB <your choice of a database name>`, e.g. `python Reconstruct_DB.py --DB FSUDB` . This generates an sql table syntax for each of your tables in `FSU_HGCAL_DB/fsudb/tests/old_tables_sql` into a complete dataframe in `/complete_DB/<your choice of a database name>.sql`. Do `python Reconstruct_DB.py --help` for help.

* From there, you can interact with the complete DB. I like to use mysql, where you can do queries such as 

`select Current_location from Full_Sensor;`
 
 or

`select Sensor_ID, Current_location from Full_Sensor;`

or

`select Current_location from Full_Sensor where Sensor_ID='N4791_1';`


------------
## Update DB to Include Latest Analysis Results (do this second) - Workflow:
The automatic updates are meant to be run after the `AnalyseMeasurement` command (e.g. `AnalyseMeasurement_IV 2 N3308_5` where N3308_5 is the sensor ID) but before deleting the output of the analysis result with the command `DeleteAnalysisFiles` (e.g. `DeleteAnalysisFiles_IV N3308_5`). After you run `AnalyseMeasurement_IV <Sensor ID>` do the following:

* Go to /tests/

* Do `python updateDB.py <IV or CV>` (currently only IV works). This then generates a csv file with all summary results of the latest measurement in `/new_results_csv/`, and an sql database, that is formatted in the same way as you original database (which is in `/complete_DB/`) with the same tables for only the latest measuremtn. It then appends these tables to your databse, and prints a summary results for you to confirm that the results are correct. Do python `updateDB.py --help` for help.
