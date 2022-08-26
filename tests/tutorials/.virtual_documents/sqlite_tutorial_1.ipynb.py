try:
    import sqlite3 as sql
    have_sqlite3 = True
except ImportError:
    sqlite3=None
    print("you don't have sqlite3, do 'sudo apt-get install sqlite3'")


def query(query_string):
    connection=None
    try:
        DB_NAME = '../TESTME.db'
        connection = sql.connect(DB_NAME)
        cursor = connection.cursor()
        
    except sqlite3.Error as err:
        print('could not open database get_ipython().run_line_magic("s'", " % err)")
        if connection:
            connection.rollback()
        exit(1)
        
    cur = cursor.execute(query_string)
    col_names = [cn[0] for cn in cur.description]
    print(col_names,'\n')
    rows = cur.fetchall()
    print(rows)
    

    if connection:
        connection.close()


query_string ="""SELECT * FROM IV_GRADING_RESULTS WHERE Sensor_ID='N4788_5'"""
query(query_string)



