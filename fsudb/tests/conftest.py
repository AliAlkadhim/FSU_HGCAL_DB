import pytest
import sqlite3

@pytest.fixture
def database():
	conn = sqlite3.connect(':memory:') #creating a temprary connection in RAM
	yield conn
	conn.close()	
