'''Example application showing how to use the object QSqlTableModel for 
displaying and changing data in a GUI.

The application uses the contacts.sqlite database.'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableView,
)


class Contacts(QMainWindow):
    '''Setting up the model and view.'''

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle('QTableView Example')
        self.resize(415, 200)
        # Set up the model.
        self.model = QSqlTableModel(self)
        self.model.setTable('contacts')
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, Qt.Horizontal, 'Name')
        self.model.setHeaderData(2, Qt.Horizontal, 'Job')
        self.model.setHeaderData(3, Qt.Horizontal, 'Email')
        self.model.select()
        # Set up the view.
        self.view = QTableView()
        self.view.setModel(self.model)
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
