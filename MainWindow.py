import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from ConstructWindow import ConstructWindow
from ui.MainWindowUI import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.construct_window = ConstructWindow()

        self.construct_window.ui.btnBack.clicked.connect(self.return_to_main)
        self.ui.btnConstruct.clicked.connect(self.open_construct_window)

    def open_construct_window(self):
        self.destroy()
        self.construct_window.show()

    def return_to_main(self):
        self.construct_window.destroy()
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
