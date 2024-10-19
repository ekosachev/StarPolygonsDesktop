# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(920, 534)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lstTasks = QListView(self.centralwidget)
        self.lstTasks.setObjectName(u"lstTasks")
        self.lstTasks.setMinimumSize(QSize(200, 0))
        self.lstTasks.setMaximumSize(QSize(300, 16777215))
        self.lstTasks.setAlternatingRowColors(True)
        self.lstTasks.setBatchSize(2)
        self.lstTasks.setWordWrap(False)

        self.horizontalLayout.addWidget(self.lstTasks)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblDrawing = QLabel(self.frame_2)
        self.lblDrawing.setObjectName(u"lblDrawing")
        self.lblDrawing.setMinimumSize(QSize(300, 300))
        self.lblDrawing.setFrameShape(QFrame.Shape.Panel)
        self.lblDrawing.setFrameShadow(QFrame.Shadow.Raised)
        self.lblDrawing.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lblDrawing)

        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(350, 0))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblInfo = QLabel(self.groupBox)
        self.lblInfo.setObjectName(u"lblInfo")
        self.lblInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.lblInfo.setFrameShadow(QFrame.Shadow.Plain)
        self.lblInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.lblInfo)


        self.horizontalLayout_2.addWidget(self.groupBox)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 100))
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame_3)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.btnCheck = QPushButton(self.frame_3)
        self.btnCheck.setObjectName(u"btnCheck")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.btnCheck)

        self.ledAnswer = QLineEdit(self.frame_3)
        self.ledAnswer.setObjectName(u"ledAnswer")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ledAnswer)

        self.lblResult = QLabel(self.frame_3)
        self.lblResult.setObjectName(u"lblResult")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.lblResult)

        self.btnShowAnswer = QPushButton(self.frame_3)
        self.btnShowAnswer.setObjectName(u"btnShowAnswer")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.btnShowAnswer)

        self.lblCorrectAnswer = QLabel(self.frame_3)
        self.lblCorrectAnswer.setObjectName(u"lblCorrectAnswer")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lblCorrectAnswer)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblDrawing.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0440\u0442\u0435\u0436 \u0434\u043b\u044f \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u043e\u0432\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.lblInfo.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u0443\u0441\u043b\u043e\u0432\u0438\u044f \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.btnCheck.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043e\u0442\u0432\u0435\u0442", None))
        self.lblResult.setText("")
        self.btnShowAnswer.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043e\u0442\u0432\u0435\u0442", None))
        self.lblCorrectAnswer.setText("")
    # retranslateUi

