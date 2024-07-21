import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from t_okno_1 import Ui_MainWindow
from t_okno_2 import Ui_MainWindow_2
from t_okno_3 import Ui_MainWindow_3
from t_okno_4 import Ui_MainWindow_4
from t_okno_5 import Ui_MainWindow_5
from t_okno_6 import Ui_MainWindow_6
from t_okno_7 import Ui_MainWindow_7
from t_okno_8 import Ui_MainWindow_8
from t_okno_9 import Ui_MainWindow_9
from t_okno_10 import Ui_MainWindow_10
from t_okno_11 import Ui_MainWindow_11
from t_okno_12 import Ui_MainWindow_12
from t_okno_13 import Ui_MainWindow_13
from t_okno_14 import Ui_MainWindow_14
from t_okno_15 import Ui_MainWindow_15
from t_okno_16 import Ui_MainWindow_16

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.second)
        self.ui.pushButton_2.clicked.connect(self.recycle)
    def second(self):
        reimu.show()
        window.close()
    def recycle(self):
        window.close()
        sx.show()
class SecondWindow(QMainWindow):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.ui = Ui_MainWindow_2()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.first)
        self.ui.pushButton.clicked.connect(self.third)
    def first(self):
        window.show()
        reimu.close()
    def third(self):
        reimu.close()
        marisa.show()

class ThirdWindow(QMainWindow):
    def __init__(self):
        super(ThirdWindow, self).__init__()
        self.ui = Ui_MainWindow_3()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.second_back)
        self.ui.pushButton.clicked.connect(self.four)
    def second_back(self):
        reimu.show()
        marisa.close()
    def four(self):
        marisa.close()
        cirno.show()


class FourthWindow(QMainWindow):
    def __init__(self):
        super(FourthWindow, self).__init__()
        self.ui = Ui_MainWindow_4()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.third_back)
        self.ui.pushButton.clicked.connect(self.five)

    def third_back(self):
        cirno.close()
        marisa.show()

    def five(self):
        cirno.close()
        fi.show()

class FiveWindow(QMainWindow):
    def __init__(self):
        super(FiveWindow,self).__init__()
        self.ui = Ui_MainWindow_5()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.four_back)
        self.ui.pushButton.clicked.connect(self.six)

    def four_back(self):
        cirno.show()
        fi.close()
    def six(self):
        fi.close()
        si.show()



class SixWindow(QMainWindow):
    def __init__(self):
        super(SixWindow,self).__init__()
        self.ui = Ui_MainWindow_6()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.five_back)
        self.ui.pushButton.clicked.connect(self.seven)

    def five_back(self):
        si.close()
        fi.show()
    def seven(self):
        si.close()
        se.show()

class SevenWindow(QMainWindow):
    def __init__(self):
        super(SevenWindow,self).__init__()
        self.ui = Ui_MainWindow_7()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.six_back)
        self.ui.pushButton.clicked.connect(self.eight)

    def six_back(self):
        se.close()
        si.show()
    def eight(self):
        se.close()
        ei.show()


class EightWindow(QMainWindow):
    def __init__(self):
        super(EightWindow, self).__init__()
        self.ui = Ui_MainWindow_8()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.seven_back)
        self.ui.pushButton.clicked.connect(self.nine)

    def seven_back(self):
        ei.close()
        se.show()
    def nine(self):
        ni.show()
        ei.close()


class NineWindow(QMainWindow):
    def __init__(self):
        super(NineWindow, self).__init__()
        self.ui = Ui_MainWindow_9()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.eight_back)
        self.ui.pushButton.clicked.connect(self.ten)

    def eight_back(self):
        ni.close()
        ei.show()
    def ten(self):
        ni.close()
        te.show()

class TenWindow(QMainWindow):
    def __init__(self):
        super(TenWindow, self).__init__()
        self.ui = Ui_MainWindow_10()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.nine_back)
        self.ui.pushButton.clicked.connect(self.eleven)

    def nine_back(self):
        te.close()
        ni.show()
    def eleven(self):
        el.show()
        te.close()

class ElevenWindow(QMainWindow):
    def __init__(self):
        super(ElevenWindow, self).__init__()
        self.ui = Ui_MainWindow_11()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.ten_back)
        self.ui.pushButton.clicked.connect(self.twelve)

    def ten_back(self):
        el.close()
        te.show()
    def twelve(self):
        el.close()
        tw.show()

class TwelveWindow(QMainWindow):
    def __init__(self):
        super(TwelveWindow, self).__init__()
        self.ui = Ui_MainWindow_12()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.eleven_back)
        self.ui.pushButton.clicked.connect(self.thirteen)

    def eleven_back(self):
        tw.close()
        el.show()
    def thirteen(self):
        th.show()
        tw.close()

class ThirteendWindow(QMainWindow):
    def __init__(self):
        super(ThirteendWindow, self).__init__()
        self.ui = Ui_MainWindow_13()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.twelve_back)
        self.ui.pushButton.clicked.connect(self.fourteen)

    def twelve_back(self):
        th.close()
        tw.show()
    def fourteen(self):
        th.close()
        ft.show()
class FourteenWindow(QMainWindow):
    def __init__(self):
        super(FourteenWindow, self).__init__()
        self.ui = Ui_MainWindow_14()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.thirteen_back)
        self.ui.pushButton.clicked.connect(self.fiveteen)

    def thirteen_back(self):
        ft.close()
        th.show()
    def fiveteen(self):
        ft.close()
        fit.show()

class FiveteenWindow(QMainWindow):
    def __init__(self):
        super(FiveteenWindow, self).__init__()
        self.ui = Ui_MainWindow_15()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.fourteen_back)
        self.ui.pushButton.clicked.connect(self.sixteen)

    def fourteen_back(self):
        fit.close()
        ft.show()
    def sixteen(self):
        fit.close()
        sx.show()

class SixteenWindow(QMainWindow):
    def __init__(self):
        super(SixteenWindow, self).__init__()
        self.ui = Ui_MainWindow_16()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.fiveteen_back)
        self.ui.pushButton.clicked.connect(self.first_back)

    def fiveteen_back(self):
        fit.show()
        sx.close()
    def first_back(self):
        sx.close()
        window.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    marisa = ThirdWindow()
    reimu = SecondWindow()
    window = MainWindow()
    cirno = FourthWindow()

    fi = FiveWindow()
    si = SixWindow()
    se = SevenWindow()
    ei = EightWindow()
    ni = NineWindow()
    te = TenWindow()
    el = ElevenWindow()
    tw = TwelveWindow()
    th = ThirteendWindow()
    ft = FourteenWindow()
    fit = FiveteenWindow()
    sx = SixteenWindow()

    window.show()



    sys.exit(app.exec())