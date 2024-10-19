import json
import sys

from PIL.ImageQt import QImage
from PySide6 import QtCore
from PySide6.QtGui import QMouseEvent
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy
from PySide6.QtCore import QFile, Qt
from ui.TaskWindowUI import Ui_MainWindow
from json import *


class TaskModel(QtCore.QAbstractListModel):
    def __init__(self, *args, path_to_file: str, **kwargs):
        super(TaskModel, self).__init__(*args, **kwargs)
        with open(path_to_file, 'r', encoding='utf-8') as f:
            self.tasks = json.load(f)

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            text = self.tasks[index.row()]['name']
            return text

    def rowCount(self, index):
        return len(self.tasks)


class TasksWindow(QMainWindow):
    def __init__(self, parent):
        super(TasksWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.lblDrawing.setScaledContents(True)
        self.ui.lblDrawing.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        self.ui.lblInfo.setWordWrap(True)
        self.model = TaskModel(path_to_file='data/tasks.json')
        self.ui.lstTasks.setModel(self.model)
        # self.ui.lstTasks.clicked.connect(self.on_new_task_selected)
        self.ui.lstTasks.selectionModel().selectionChanged.connect(self.on_new_task_selected)
        self.ui.btnCheck.clicked.connect(self.on_check_answer_clicked)
        self.ui.btnShowAnswer.clicked.connect(self.on_show_answer_clicked)
        parent.layout().addWidget(self.centralWidget())
        self.ui.lblDrawing.resizeEvent = lambda event: self.ui.lblDrawing.setPixmap(QPixmap.fromImage(QImage(self.selected_task['picture']).scaled(self.ui.lblDrawing.size(), aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)))
        self.selected_task = {}

    def on_new_task_selected(self, current, *args, **kwargs):
        self.selected_task = self.model.tasks[current.indexes()[0].row()]
        self.ui.lblInfo.setText(self.selected_task['description'])
        self.ui.lblDrawing.setPixmap(QPixmap.fromImage(QImage(self.selected_task['picture']).scaled(self.ui.lblDrawing.size(), aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)))

    def on_check_answer_clicked(self):
        correct_answers = self.selected_task.get('answer') or []
        if self.ui.ledAnswer.text() in correct_answers:
            self.ui.lblResult.setText('Верно')
        else:
            self.ui.lblResult.setText('Неверно')

    def on_show_answer_clicked(self):
        self.ui.lblCorrectAnswer.setText(self.selected_task['ans_show'])

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TasksWindow()
    window.show()

    sys.exit(app.exec())