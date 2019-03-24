import sys
import sqlite3
import time
import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtGui

conn = sqlite3.connect('gm.db')
c = conn.cursor()

class window(QMainWindow):

    # Defines Initial Window Settings
    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(650, 300, 500, 400) # window geometry
        self.home()

    def home(self):
        self.edit = QLineEdit(self)
        self.edit.move(250, 250)
        self.completer = QCompleter()
        self.edit.setCompleter(self.completer)
        self.model = QStringListModel()
        self.completer.setModel(self.model)
        self.get_data()
        self.show()

    def get_data(self):
        c.execute(" SELECT name FROM gtab ")
        results = c.fetchall()
        new_list = [i[0] for i in results]
        print(new_list) # Test print
        self.model.setStringList(new_list) #From here up I was able to get the
        conn.close()
        # code to work but there's no auto completion in the QLineEdit.

def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()