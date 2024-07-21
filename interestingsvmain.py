import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui.okno import Ui_MainWindow
from ui.okno2 import Ui_secondwindow


class InterestingFacts(QMainWindow):
    def __init__(self):
        super(InterestingFacts, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.second)
        self.second_window = sw()
        self.second_window.ui.pushButton.clicked.connect(self.return_to_first)
    def second(self):
        self.destroy()
        self.second_window.show()

    def return_to_first(self):
        self.second_window.close()
        self.show()


class sw(QMainWindow):
    def __init__(self):
        super(sw, self).__init__()
        self.ui = Ui_secondwindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.destroy)