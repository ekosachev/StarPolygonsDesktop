# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConstructWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFormLayout,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(914, 713)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(400, 16777215))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.sbxN = QSpinBox(self.groupBox)
        self.sbxN.setObjectName(u"sbxN")
        self.sbxN.setMinimum(5)
        self.sbxN.setValue(5)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.sbxN)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.sbxM = QSpinBox(self.groupBox)
        self.sbxM.setObjectName(u"sbxM")
        self.sbxM.setMinimum(2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sbxM)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.sbxR = QDoubleSpinBox(self.groupBox)
        self.sbxR.setObjectName(u"sbxR")
        self.sbxR.setMinimum(0.010000000000000)
        self.sbxR.setSingleStep(0.100000000000000)
        self.sbxR.setValue(1.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sbxR)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.formLayout_3 = QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.cbxDisplayNgon = QCheckBox(self.groupBox_3)
        self.cbxDisplayNgon.setObjectName(u"cbxDisplayNgon")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.cbxDisplayNgon)

        self.cbxDisplayInnnerSP = QCheckBox(self.groupBox_3)
        self.cbxDisplayInnnerSP.setObjectName(u"cbxDisplayInnnerSP")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.cbxDisplayInnnerSP)

        self.cbxDisplayVertexCoords = QCheckBox(self.groupBox_3)
        self.cbxDisplayVertexCoords.setObjectName(u"cbxDisplayVertexCoords")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.cbxDisplayVertexCoords)

        self.btnDisplayCircumcircle = QCheckBox(self.groupBox_3)
        self.btnDisplayCircumcircle.setObjectName(u"btnDisplayCircumcircle")

        self.formLayout_3.setWidget(3, QFormLayout.SpanningRole, self.btnDisplayCircumcircle)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.btnConstruct = QPushButton(self.frame)
        self.btnConstruct.setObjectName(u"btnConstruct")

        self.verticalLayout.addWidget(self.btnConstruct)

        self.btnExplode = QPushButton(self.frame)
        self.btnExplode.setObjectName(u"btnExplode")

        self.verticalLayout.addWidget(self.btnExplode)

        self.btnUnexplode = QPushButton(self.frame)
        self.btnUnexplode.setObjectName(u"btnUnexplode")

        self.verticalLayout.addWidget(self.btnUnexplode)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblSideLength = QLabel(self.groupBox_2)
        self.lblSideLength.setObjectName(u"lblSideLength")
        self.lblSideLength.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lblSideLength)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.lblPerimeter = QLabel(self.groupBox_2)
        self.lblPerimeter.setObjectName(u"lblPerimeter")
        self.lblPerimeter.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lblPerimeter)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.lblVertexAngle = QLabel(self.groupBox_2)
        self.lblVertexAngle.setObjectName(u"lblVertexAngle")
        self.lblVertexAngle.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lblVertexAngle)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.lblArea = QLabel(self.groupBox_2)
        self.lblArea.setObjectName(u"lblArea")
        self.lblArea.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lblArea)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_13)

        self.lblTheta = QLabel(self.groupBox_2)
        self.lblTheta.setObjectName(u"lblTheta")
        self.lblTheta.setTextFormat(Qt.TextFormat.RichText)
        self.lblTheta.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lblTheta)

        self.lblConnected = QLabel(self.groupBox_2)
        self.lblConnected.setObjectName(u"lblConnected")
        self.lblConnected.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_2.setWidget(5, QFormLayout.SpanningRole, self.lblConnected)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout_4 = QFormLayout(self.groupBox_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.lblCompAmount = QLabel(self.groupBox_4)
        self.lblCompAmount.setObjectName(u"lblCompAmount")
        self.lblCompAmount.setTextFormat(Qt.TextFormat.AutoText)
        self.lblCompAmount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lblCompAmount)

        self.lblCompN = QLabel(self.groupBox_4)
        self.lblCompN.setObjectName(u"lblCompN")
        self.lblCompN.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lblCompN)

        self.lblCompM = QLabel(self.groupBox_4)
        self.lblCompM.setObjectName(u"lblCompM")
        self.lblCompM.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.lblCompM)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnBack = QPushButton(self.frame)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.btnBack)


        self.horizontalLayout.addWidget(self.frame)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.Shape.Panel)
        self.label.setFrameShadow(QFrame.Shadow.Raised)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"StarPolygons", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0437\u0432\u0435\u0437\u0434\u0447\u0430\u0442\u043e\u0433\u043e \u043c\u043d\u043e\u0433\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u0435\u0440\u0448\u0438\u043d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441 \u043e\u043f\u0438\u0441\u0430\u043d\u043d\u043e\u0439 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.sbxR.setPrefix("")
        self.sbxR.setSuffix("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.cbxDisplayNgon.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 N-\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a", None))
        self.cbxDisplayInnnerSP.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u0432\u043b\u043e\u0436\u0435\u043d\u043d\u044b\u0435 \u0437\u0432\u0435\u0437\u0434\u0447\u0430\u0442\u044b\u0435 \u043c\u043d\u043e\u0433\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0438", None))
        self.cbxDisplayVertexCoords.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043f\u0438\u0441\u044b\u0432\u0430\u0442\u044c \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b \u0432\u0435\u0440\u0448\u0438\u043d", None))
        self.btnDisplayCircumcircle.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u043e\u043f\u0438\u0441\u0430\u043d\u043d\u0443\u044e \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.btnConstruct.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.btnExplode.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0441\u043e\u0441\u0442\u0430\u0432\u043d\u044b\u0435 \u0447\u0430\u0441\u0442\u0438", None))
        self.btnUnexplode.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044a\u0435\u0434\u0438\u043d\u0438\u0442\u044c \u0441\u043e\u0441\u0442\u0430\u0432\u043d\u044b\u0435 \u0447\u0430\u0441\u0442\u0438", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0447\u0438c\u043b\u0435\u043d\u043d\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.lblSideLength.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u043e", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u0441\u0442\u043e\u0440\u043e\u043d\u044b", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043c\u0435\u0442\u0440", None))
        self.lblPerimeter.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u043e", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043e\u043b \u043f\u0440\u0438 \u0432\u0435\u0440\u0448\u0438\u043d\u0435", None))
        self.lblVertexAngle.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u043e", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c", None))
        self.lblArea.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u043e", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u0443\u0433\u043e\u043b \u043c\u0435\u0436\u0434\u0443 \u043b\u0443\u0447\u0430\u043c\u0438", None))
        self.lblTheta.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u043e", None))
        self.lblConnected.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u044f\u0437\u043d\u043e\u0441\u0442\u044c \u043d\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0430", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u044f\u0437\u043d\u044b\u0435 \u043a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442\u044b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u0435\u0440\u0448\u0438\u043d", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433", None))
        self.lblCompAmount.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u043e", None))
        self.lblCompN.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u043e", None))
        self.lblCompM.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u043e", None))
        self.btnBack.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c\" \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0437\u0432\u0435\u0437\u0434\u0447\u0430\u0442\u044b\u0439 \u043c\u043d\u043e\u0433\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a", None))
    # retranslateUi

