import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QMessageBox


# Create the connection.
con = QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('contacts.sqlite')


# Try to open the connection and handle possible errors.
if not con.open():
    QMessageBox.critical(
        None,
        'App Name - Error!',
        f'DatabaseError: {con.lastError().databaseText()}',
    )
    sys.exit(1)


# Create a query and execute it right away using .exec().
createTableQuery = QSqlQuery()
createTableQuery.exec(
    '''
        CREATE TABLE contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        );
    '''
)


print(con.tables())


# Creating a query for later execution using .prepare().
insertDataQuery = QSqlQuery()
insertDataQuery.prepare(
    '''
        INSERT INTO contacts (
            name,
            job,
            email
        )
        VALUES (?, ?, ?);
    '''
)


# Sample data.
data = [
    ('Петя', 'Senior Web Developer', 'petya@example.com'),
    ('Лера', 'Project Manager', 'lera@example.com'),
    ('Денис', 'Data Analyst', 'denis@example.com'),
    ('Катя', 'Senior Python Developer', 'ket@example.com'),
]


# Use .addBindValue() to insert data.
for name, job, email in data:
    insertDataQuery.addBindValue(name)
    insertDataQuery.addBindValue(job)
    insertDataQuery.addBindValue(email)
    insertDataQuery.exec()
