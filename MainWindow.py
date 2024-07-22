import sys

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow

from ConstructWindow import ConstructWindow
from TasksWindow import TasksWindow
from TheoryWindow import TheoryWindow
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
        self.construct_window.ui.btnBack.clicked.connect(self.return_to_main_c)
        self.ui.btnConstruct.clicked.connect(self.open_construct_window)
        self.ui.btnExersises.clicked.connect(self.open_tasks_window)
        self.theory_window = TheoryWindow()
        self.ui.btnTheory.clicked.connect(self.open_theory_window)
        self.tasks_window.ui.pushButton.clicked.connect(self.return_to_main_ta)
        self.ui.btnFacts.clicked.connect(self.open_interesting_facts_window)
        self.interesting_facts_window.second_window.ui.pushButton_2.clicked.connect(self.show)
        self.theory_window.ui.pushButton.clicked.connect(self.return_to_main_t)
        self.interesting_facts_window.ui.pushButton_2.clicked.connect(self.return_to_main_i)
        self.ui.btnExit.clicked.connect(self.close)

        self.showMaximized()

    def open_construct_window(self):
        self.destroy()
        self.construct_window.showMaximized()

    def open_theory_window(self):
        self.destroy()
        self.theory_window.showMaximized()
        self.theory_window.open(QUrl.fromLocalFile("./Star_Polygons.pdf"))


    def open_tasks_window(self):
        self.destroy()
        self.tasks_window.showMaximized()

    def return_to_main_ta(self):
        self.tasks_window.close()
        self.showMaximized()

    def return_to_main_i(self):
        self.interesting_facts_window.close()
        self.showMaximized()

    def open_interesting_facts_window(self):
        self.destroy()
        self.interesting_facts_window.showMaximized()

    def return_to_main_c(self):
        self.construct_window.close()
        self.showMaximized()

    def return_to_main_t(self):
        self.theory_window.close()
        self.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
