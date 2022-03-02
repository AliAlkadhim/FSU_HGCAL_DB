from fsudb import generate_sqlite3_schema

# def test_create_db(database)
def test_create_db():
    #the parameter database must match the function database (the fixture) in conftest.py
    #db = fsudb.generate_sql_code()
    # sql_schema is the text from that file
    generate_sqlite3_schema(database)#here the database is the temporary connection that is used as an argument conn in the generate_sqliste3 functino
    cur = database.cursor()
    cur.execute('''USE FSU_HGCAL; \
        SELECT * FROM Full_Sensor;''')
    generate_sqlite3_schema(database)
#now in the fsudb directory, you can run
#python -m pytest -v tests