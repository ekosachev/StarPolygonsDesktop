# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TheoryWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)
import ui.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionZoom_In = QAction(MainWindow)
        self.actionZoom_In.setObjectName(u"actionZoom_In")
        icon = QIcon()
        iconThemeName = u"zoom-in"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/icons/images/zoom-in.svgz", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionZoom_In.setIcon(icon)
        self.actionZoom_Out = QAction(MainWindow)
        self.actionZoom_Out.setObjectName(u"actionZoom_Out")
        icon1 = QIcon()
        iconThemeName = u"zoom-out"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u":/icons/images/zoom-out.svgz", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionZoom_Out.setIcon(icon1)
        self.actionPrevious_Page = QAction(MainWindow)
        self.actionPrevious_Page.setObjectName(u"actionPrevious_Page")
        icon2 = QIcon()
        iconThemeName = u"go-previous-view-page"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u":/icons/images/go-previous-view-page.svgz", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionPrevious_Page.setIcon(icon2)
        self.actionNext_Page = QAction(MainWindow)
        self.actionNext_Page.setObjectName(u"actionNext_Page")
        icon3 = QIcon()
        iconThemeName = u"go-next-view-page"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u":/icons/images/go-next-view-page.svgz", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionNext_Page.setIcon(icon3)
        self.actionContinuous = QAction(MainWindow)
        self.actionContinuous.setObjectName(u"actionContinuous")
        self.actionContinuous.setCheckable(True)
        self.actionBack = QAction(MainWindow)
        self.actionBack.setObjectName(u"actionBack")
        self.actionBack.setEnabled(False)
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/go-previous-view.svgz", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionBack.setIcon(icon4)
        self.actionForward = QAction(MainWindow)
        self.actionForward.setObjectName(u"actionForward")
        self.actionForward.setEnabled(False)
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/go-next-view.svgz", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionForward.setIcon(icon5)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pdfView = QPdfView(self.widget)
        self.pdfView.setObjectName(u"pdfView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pdfView.sizePolicy().hasHeightForWidth())
        self.pdfView.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pdfView)


        self.verticalLayout.addWidget(self.widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.centralWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 700, 22))
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        self.mainToolBar.setMovable(False)
        self.mainToolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuView.menuAction())
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuView.addAction(self.actionPrevious_Page)
        self.menuView.addAction(self.actionNext_Page)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionContinuous)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionZoom_Out)
        self.mainToolBar.addAction(self.actionZoom_In)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionBack)
        self.mainToolBar.addAction(self.actionForward)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PDF Viewer", None))
        self.actionZoom_In.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u043b\u0438\u0437\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.actionZoom_In.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl++", None))
#endif // QT_CONFIG(shortcut)
        self.actionZoom_Out.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0430\u043b\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.actionZoom_Out.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+-", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrevious_Page.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
#if QT_CONFIG(shortcut)
        self.actionPrevious_Page.setShortcut(QCoreApplication.translate("MainWindow", u"PgUp", None))
#endif // QT_CONFIG(shortcut)
        self.actionNext_Page.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
#if QT_CONFIG(shortcut)
        self.actionNext_Page.setShortcut(QCoreApplication.translate("MainWindow", u"PgDown", None))
#endif // QT_CONFIG(shortcut)
        self.actionContinuous.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0441\u0442\u0430\u0442\u044c \u0446\u0435\u043b\u0438\u043a\u043e\u043c", None))
        self.actionBack.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
#if QT_CONFIG(tooltip)
        self.actionBack.setToolTip(QCoreApplication.translate("MainWindow", u"back to previous view", None))
#endif // QT_CONFIG(tooltip)
        self.actionForward.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0435\u0440\u0435\u0434", None))
#if QT_CONFIG(tooltip)
        self.actionForward.setToolTip(QCoreApplication.translate("MainWindow", u"forward to next view", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0441\u0442\u0430\u0439\u0442\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0430\u043c\u0438 PgUp \u0438 PgDown", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 \u043c\u0435\u043d\u044e", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434", None))
    # retranslateUi

