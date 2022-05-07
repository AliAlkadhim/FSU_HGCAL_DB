This repo is uses mysql (as well as sqlite3) to build an SQL relational database for the HGCAL data at FSU from existing spreadsheets (converted to csv tables). The power really comes when it is combined with the HGCAL automatic analysis code (at https://gitlab.cern.ch/CLICdp/HGCAL/lcd_hgcal_analysisworkflows). Thus this package, when the analysis code is also installed, allows for completely automatic updating of the database. To interact with the database (queries, etc.), our choice is to use mysql, interfaced with mysql Workbench.

# ALL CURRENT USE OF THIS PACKAGE SHOULD BE DONE IN THE `/tests/` DIRECTORY. WE HAVE FUNCTIONALITY FOR BOTH MYSQL AND SQLITE, WHERE SQLITE IS MUCH FASTER AND MORE LIGHTWEIGHT FOR QUICK AND EASY QUERIES

----------
# Go to `/tests/` and do the following tests:

# TEST 1) 

PLEASE INSPECT OUR SQLITE DATABASE CALLED `TESTME.db` WITH SQLITE BROWSER. THIS CAN BE DONE WITH THE COMMAND

`sqlitebrowser TESTME.db `

This can also be done by anyone at home! Sqlite3 comes preinstalled with most python installations, and if you don't have sqlitebrowser, install it with the command
`sudo apt-get install sqlitebrowser` for Debian or `brew install --cask db-browser-for-sqlite` for MacOS.

After opening `TESTME.db`, there are countless things you can do with sqlitebrowser (including queries and updating). However, for these checks, go to the `Browse Data` tab, and choose which table you want from the `Table` dropdown menu. You'll see that for IV we have
1) FULL_SENSOR_PLANNING <br>
2) MOS_GCD PLANNING <br>
3) STRIP_SENSOR_LOGISTICS <br>
4) DIODES_NP_LOGISTICS <br>
5) PQC_LOGISTICS <br>
6) HPK_STRUCTURES_LOGISTICS
7) IV_GRADING_RESULTS

After choosing a table from the dropdown, type any query you would like under the column(s) that you would like to use (i.e. type under the columns where it says "Filter").

MORE SPECIFICALLY, CHECK THAT IV_GRADING_RESULTS TABLE AGREES WITH THE SPREADSHEETS “LD Sensor IV Grading” and “HD Sensor IV Grading” ON GOOGLE DOCS. 









# Other tests (these use mysql, so slower and not as important for now)

# Reconstruct Existing Data Into Database (do this first)- Workflow: 
* Go to /tests/

* First define and store your old tables (these are from the spreadsheets), such that each table is its own csv file, in `FSU_HGCAL_DB/fsudb/tests/old_tables_csv`. The Table names will be the names prior to the ".csv" extension, so make sure you're satisfied with the names! We have added our tables in there, but some attributes of the tables might be changed soon...

* You can go to `FSU_HGCAL_DB/fsudb/tests` and do `python Reconstruct_DB.py --DB <your choice of a database name>`, e.g. `python Reconstruct_DB.py --DB FSUDB` . This generates an sql table syntax for each of your tables in `FSU_HGCAL_DB/fsudb/tests/old_tables_sql` into a complete dataframe in `/complete_DB/<your choice of a database name>.sql`. Do `python Reconstruct_DB.py --help` for help.

* From there, you can interact with the complete DB. I like to use mysql, if you want a really nice way to use mysql, use mysql Workbench, the instructions to install it is in the README in https://github.com/AliAlkadhim/FSU_HGCAL_DB . Suppose you want to look at the locations of the sensors in the `Full_Sensor` table, you can do the following query: 

`select Current_location from Full_Sensor;`
 
 or, say you want to look at the sensor ID and location, do:

`select Sensor_ID, Current_location from Full_Sensor;`

or, say you want to find the location of the sensor whose sensor ID is 'N4791_1' from the `Full_Sensor` table, do:

`select Current_location from Full_Sensor where Sensor_ID='N4791_1';`


------------
## Update DB to Include Latest Analysis Results (do this second) - Workflow:
The automatic updates are meant to be run after the `AnalyseMeasurement` command (e.g. `AnalyseMeasurement_IV 2 N3308_5` where N3308_5 is the sensor ID) but before deleting the output of the analysis result with the command `DeleteAnalysisFiles` (e.g. `DeleteAnalysisFiles_IV N3308_5`). After you run `AnalyseMeasurement_IV <Sensor ID>` do the following:

* Go to /tests/

* Do `python updateDB.py <IV or CV>` (currently only IV works). This then generates a csv file with all summary results of the latest measurement in `/new_results_csv/`, and an sql database, that is formatted in the same way as you original database (which is in `/complete_DB/`) with the same tables for only the latest measuremtn. It then appends these tables to your databse, and prints a summary results for you to confirm that the results are correct. Do `python updateDB.py --help` for help.


Soon this can be installed with `python setup.py install` (don't try this yet)
