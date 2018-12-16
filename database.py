import pymssql
# from datetime import datetime
import pandas as pd

# Connect to Database
def conn():
    db = pymssql.connect(host='localhost', user='sa', password='<YourStrong!Passw0rd>', database='datashareits')
    return db

# # Get data from table
def readSql(tableName, connection = conn()):
    data = pd.read_sql_query("SELECT * FROM %s;" % tableName, connection)
    return data

# Convert Date
def convertDate(table, column='LastAccess'):
    table[column] = pd.to_datetime(table[column])

# Database tables
dosen = readSql('dbo.dosen')
mahasiswa = readSql('dbo.Mahasiswa')

# Convert LastAccess column to DateTime Type
convertDate(dosen)
convertDate(mahasiswa)

# fakultas = dosen['Fakultas'].unique()