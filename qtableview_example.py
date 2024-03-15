'''Example application showing how to use the object QTableWidget for 
displaying data in a GUI.

The application uses the contacts.sqlite database.'''

import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)


class Contacts(QMainWindow):
    '''Setting up the view and loading the data.'''

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle('QTableView Example')
        self.resize(450, 250)
        self.view = QTableWidget()
        self.view.setColumnCount(4)
        self.view.setHorizontalHeaderLabels(['ID', 'Name', 'Job', 'Email'])
        query = QSqlQuery('SELECT id, name, job, email FROM contacts')
        while query.next():
            rows = self.view.rowCount()
            self.view.setRowCount(rows + 1)
            self.view.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
            self.view.setItem(rows, 1, QTableWidgetItem(str(query.value(1))))
            self.view.setItem(rows, 2, QTableWidgetItem(str(query.value(2))))
            self.view.setItem(rows, 3, QTableWidgetItem(str(query.value(3))))
        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)


def createConnection():
    '''Create connection with the database and return True in case of 
    success.

    Return False and shows the appropriate message box in case of 
    errors.'''

    con = QSqlDatabase.addDatabase('QSQLITE')
    con.setDatabaseName('contacts.sqlite')
    if not con.open():
        QMessageBox.critical(
            None,
            'QTableView Example - Error!',
            f'Databade Error: {con.lastError().databaseText()}',
        )
        return False
    return True


def main():
    '''Displaying data in a GUI. from the contacts.sqlite database.'''

    app = QApplication(sys.argv)

    if not createConnection():
        sys.exit(1)

    win = Contacts()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
