import sys
from PySide6.QtGui import QMouseEvent
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QFile
from ui.TasksWindowUI import Ui_MainWindow
from json import *
from sympy import *

class TasksWindow(QMainWindow):
    def __init__(self):
        super(TasksWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        with open("./zxc.json", encoding='utf-8') as f:
            self.config = load(f)

        kkk = [self.config[i]['name'] for i in range(len(self.config))]
        self.ui.listWidget.addItems(kkk)
        self.ui.listWidget.itemClicked.connect(self.update_parts)
        self.ui.pushButton_2.clicked.connect(self.ans_check)
        self.ui.pushButton_3.clicked.connect(self.show_ans)
        self.ui.pushButton_4.clicked.connect(self.show_solution)

    def update_parts(self):
        self.ui.label_5.setPixmap(QPixmap("./pictures/emptyback.png"))
        self.ui.label_9.setText('')
        self.ui.label_10.setPixmap(QPixmap("./pictures/empty.png"))
        self.ui.lineEdit.setText('')

        name = self.ui.listWidget.selectedItems()[0].text()
        task = None
        for i in self.config:
            if i['name'] == name:
                task = i
                break
        self.ui.label_2.setScaledContents(True)
        self.ui.label_3.setText(task["description"])
        self.ui.label_2.setPixmap(QPixmap(task["picture"]))

    def ans_check(self):
        name = self.ui.listWidget.selectedItems()[0].text()
        task = None
        for i in self.config:
            if i['name'] == name:
                task = i
                break
        answer = task['answer']
        self.ui.label_10.setScaledContents(True)
        if answer == self.ui.lineEdit.text():
            self.ui.label_10.setPixmap(QPixmap("./pictures/correct.png"))
        else:
            self.ui.label_10.setPixmap(QPixmap("./pictures/incorrect.png"))

    def show_ans(self):
        name = self.ui.listWidget.selectedItems()[0].text()
        task = None
        for i in self.config:
            if i['name'] == name:
                task = i
                break
        answer = task['answer']
        self.ui.label_9.setText(answer)

    def show_solution(self):
        name = self.ui.listWidget.selectedItems()[0].text()
        task = None
        for i in self.config:
            if i['name'] == name:
                task = i
                break
        solution = task["solve"]
        self.ui.label_5.setScaledContents(True)
        self.ui.label_5.setPixmap(QPixmap(solution))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TasksWindow()
    window.show()

    sys.exit(app.exec())