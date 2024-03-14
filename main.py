import sys
from PyQt5.QtSql import QSqlDatabase


# Create the connection.
con = QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('contacts.sqlite')

# Open the connection and handle errors.
if not con.open():
    print('Unable to connect to the database')
    sys.exit(1)
