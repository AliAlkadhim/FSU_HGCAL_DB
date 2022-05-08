try:
    import sqlite3 as sql
    have_sqlite3 = True
except ImportError:
    sqlite3=None
    print("you don't have sqlite3, do 'sudo apt-get install sqlite3'")



