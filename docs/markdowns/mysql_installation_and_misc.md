# MYSQL INSTALLATION
## Any OS with Conda
The easiest way to install mysql is using conda

`conda install -c conda-forge mysql` 

or `conda install -c conda-forge/label/cf201901 mysql` or `conda install -c conda-forge/label/cf202003 mysql`

## linux: 
* got to https://dev.mysql.com/downloads/repo/apt/ and click download, cd to the download path in a terminal

* `sudo dpkg -i mysql-apt-config_0.8.22-1_all.deb`

* keep the default options and use down arrow to OK & press enter

* `sudo apt-get update`
* ` sudo apt-get -y install mysql-server` 
* enter root user (remember this password), and enter on OK on everything

* Double check to make sure you have the server installed by doing `ps ax | grep mysql` or by doing `sudo service mysql status` (if it shows active (Running) you're good).
* install mysql-workbench by doing `sudo apt-get install mysql-workbench-community` and launch it. 
# MYSQL CONFIGURATION
* the root user (local instance 3306) is created automatically and it is highly discouraged to use it, so create another user with the appropriate privileges.
* Click on the root user (local instance 3306) to connect to it, then click on "Users and Privileges" on the left under "Management"
* Click on "Add Account" on the lower left corner
* change "Login Name" to "admin"
* Under Authentication Type select "caching_sha2_password" (you can also leave this as "standard") 
* Under Limit to Hosts Matching, type "localhost" (so that you can only login from localhost)
* choose a password, type it and confirm it
* Click on Administrative Roles on the tabs at the top
* We want to give admin ALL privileges (to create databases, etc), so under Role, check "DBA", which should check all the rights.
* Keep the rest of the settings as they are, and press "Apply" on the bottom right corner
* Now Click the Home buttom on the upper left corner (you can close your root user connection)
* Under MySQL Connections, press the plus sign button (we want to add a connection for our admin user)
* Under Connection Name type "admin", keep the hostname as is (which is 127.0.0.1 which is localhost), and keep the port to 3306
* Under Username type "admin"
* Leave everything else as they are, and press OK
* click back on admin, you should see a new admin connection for our admin user
* click it and type its password (you can check "save password in keychain" if you're not concerned about your computer's secturity), and click OK. 
### Optional: Check that you can access a database with Workbench

* go to https://www.mysqltutorial.org/mysql-sample-database.aspx and click "Download MySQL Sample Database" 
* in a terminal, cd to where you downloaded it, and do `unzip mysqlsampledatabase.zip`
* in mysql workbench, connect to admin by clicking "admin"
* Under Management in the left pane, click "Data Import/Restore"
* Under Import Options, select "Import from Self-Contained File"
* Click on the ellipses button on the right to browse, go to where you downloaded the .sql file, select it and press "Open"
* Click on the Import Progress tab and click "Start Import" on the lower right corner. (by the way it shows the command that you can execute independetly of the workbench)
* Click on the "Query 1" tab (you can close the Data Import/Restore tab)
* on the query tab, type `show databases;` and press ctrl+enter, you should see the newly imported database, called "classicmodels" show up on the Database grid at the bottom. 
# Reproducing FSU_HGCAL template DB
* `git clone https://github.com/AliAlkadhim/FSU_HGCAL_DB.git`
* `cd FSU_HGCAL_DB`
* `python generate_sql.py`
* this should generate FSU_HGCAL.sql
* on the workbench, press "Open a SQL script file in a new query tab" at the top left corner
* Select FSU_HGCAL_DB.sql from the FSU_HGCAL_DB repository. Make sure you are logged in as "admin".
* press Ctrl+Shift+Enter
* Depending on what you want in the python file, this should create the database and tables, and show the table in the database grid.

# Running This code as a module 
Currently you can go to fsudb/src and do

`python fsudb.py --tablename "strip_sensors_logistics.csv" `

And this generates your sql file with the desired tables. Do

`python fsudb.py --help`

to see more on usage available parameters.

# Ideas (under construction)

The summary results are uploaded automatically from the hgcalanalysisworkflow code into the database.

The hgcal automatic analysis workflow can be obtained with

`docker run -it -v <data directory on host machine>:/home -v <output directory on host>:/output thorbenquast/lcd_hgc_ana_wf`


Each time an IV or CV automatic analysis is run, this package asks the user "do you want to upload these results into the database?" if the user answers with "yes", the package asks the user to double check that the information that was just added (the last row in the table corresponding to the test that was just run) looks correct (the user should at this point check the pdf results of the automatic analysis to make sure the summary results are correct). If the user answers "yes, it looks correct", the test summary results are uploaded to the DB. If the user answers with "no" then nothing is uploaded.

Also:

`pip install fsudb`

`fsudb createdb --tablenames [select from options: Full_Sensor, HPK_structures, MOS_GCD, PQC, strip_sensors_logistics, HGC_CERN_Sensor_IV_Summary, HGC_HPK_Sensor_IV_Summary]`

This makes an database in the file FSU_HGCAL_DB.sql in your current working directory with all the tables you asked for. Now you can query it with your favorite interface, e.g. mysql.

For added functionality, this could be a python module with query functionality? 
