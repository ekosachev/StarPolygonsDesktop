import sys

from PySide6.QtGui import QMouseEvent
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QFile
from penis import Ui_MainWindow
from json import *
from sympy import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        with open("../../Desktop/project/zxc.json") as f:   #open json config with questons
            self.config = load(f)

        kkk = [self.config[i]['name'] for i in range(len(self.config))]    #read json file
        self.ui.listWidget.addItems(kkk)                             #fill listWidget
        self.ui.listWidget.itemClicked.connect(self.update_parts)        #operation when part of listWidget clicked
        self.ui.pushButton_2.clicked.connect(self.ans_check)
        self.ui.pushButton_3.clicked.connect(self.show_ans)


    def update_parts(self):          #update all information on the page after click on part of listWidget
        self.ui.label_9.setText('')
        self.ui.label_10.setPixmap(QPixmap("../../Desktop/project/pictures/empty.png"))
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

    def ans_check(self):        #compare answers
        name = self.ui.listWidget.selectedItems()[0].text()
        task = None
        for i in self.config:
            if i['name'] == name:
                task = i
                break
        answer = task['answer']
        self.ui.label_10.setScaledContents(True)
        if answer == self.ui.lineEdit.text():
            self.ui.label_10.setPixmap(QPixmap("../../Desktop/project/pictures/correct.png"))
        else:
            self.ui.label_10.setPixmap(QPixmap("../../Desktop/project/pictures/incorrect.png"))

    def show_ans(self):    #show answer to task
        name = self.ui.listWidget.selectedItems()[0].text()
        task = None
        for i in self.config:
            if i['name'] == name:
                task = i
                break
        answer = task['answer']
        self.ui.label_9.setText(answer)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())