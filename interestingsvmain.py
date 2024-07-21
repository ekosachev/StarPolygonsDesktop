import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from okno import Ui_MainWindow
from okno2 import Ui_secondwindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.second)
    def second(self):
        seconwindow.show()
        window.close()


class sw(QMainWindow):
    def __init__(self):
        super(sw, self).__init__()
        self.ui = Ui_secondwindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.first)
    def first(self):
        window.show()
        seconwindow.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    seconwindow = sw()
    window = MainWindow()
    window.show()


    sys.exit(app.exec())
