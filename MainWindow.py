import sys

from PySide6 import QtCore, QtUiTools
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLayout, QMainWindow

from ConstructWindow import ConstructWindow
from TasksWindow import TasksWindow
from TheoryWindow import TheoryWindow
from ui.MainUI import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabConstruct.setLayout(QHBoxLayout())
        self.ui.tabTheory.setLayout(QHBoxLayout())
        self.ui.tabTasks.setLayout(QHBoxLayout())
        self.construct_tab = ConstructWindow(self.ui.tabConstruct)
        self.tasks_tab = TasksWindow(self.ui.tabTasks)
        self.theory_tab = TheoryWindow(self.ui.tabTheory)
        self.theory_tab.open(QUrl.fromLocalFile('data/Star_Polygons.pdf'))
        self.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
