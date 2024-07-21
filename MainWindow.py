import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from ConstructWindow import ConstructWindow
from TasksWindow import TasksWindow
from interestingsvmain import InterestingFacts
from ui.MainWindowUI import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.construct_window = ConstructWindow()
        self.tasks_window = TasksWindow()
        self.interesting_facts_window = InterestingFacts()

        self.construct_window.ui.btnBack.clicked.connect(self.return_to_main)
        self.ui.btnConstruct.clicked.connect(self.open_construct_window)
        self.ui.btnExersises.clicked.connect(self.open_tasks_window)
        self.tasks_window.ui.pushButton.clicked.connect(self.return_to_main)
        self.ui.btnFacts.clicked.connect(self.open_interesting_facts_window)
        self.interesting_facts_window.second_window.ui.pushButton_2.clicked.connect(self.show)

        self.show()

    def open_construct_window(self):
        self.destroy()
        self.construct_window.show()

    def open_tasks_window(self):
        self.destroy()
        self.tasks_window.show()

    def open_interesting_facts_window(self):
        self.destroy()
        self.interesting_facts_window.show()

    def return_to_main(self):
        self.window().destroy()
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
