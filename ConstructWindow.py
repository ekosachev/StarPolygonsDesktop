import sys
import time
from math import gcd, ceil
from threading import Thread

from PIL import Image
from PIL.ImageQt import ImageQt
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QApplication, QMainWindow, QSizePolicy, QWidget

from sp_math.draw_sp import draw_sp
from sp_math.sp_math import vertex_angle, area, perimeter, central_angle, side_length
from sp_math.exploding_polygon import draw_exploding_polygon
from ui.ConstructWindowUI import Ui_MainWindow


class ConstructWindow(QMainWindow):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setScaledContents(True)
        self.ui.label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        self.ui.btnConstruct.clicked.connect(self.construct)
        self.ui.btnExplode.setDisabled(True)
        self.ui.btnUnexplode.setDisabled(True)
        self.ui.btnExplode.clicked.connect(self.start_exploding_polygon)
        self.ui.btnUnexplode.clicked.connect(self.start_unexploding_polygon)

        self.ui.sbxM.valueChanged.connect(lambda: self.ui.btnExplode.setDisabled(True))
        self.ui.sbxN.valueChanged.connect(lambda: self.ui.btnExplode.setDisabled(True))
        self.lastAction = None
        self.ui.label.resizeEvent = lambda event: self.lastAction() if self.lastAction is not None else None

        self.ui.sbxN.valueChanged.connect(self.update_m_restrictions)

        parent.layout().addWidget(self.centralWidget())

    def update_m_restrictions(self):
        n = self.ui.sbxN.value()
        min_m = 2
        max_m = (ceil(n / 2) - 1)
        self.ui.sbxM.setMinimum(min_m)
        self.ui.sbxM.setMaximum(max_m)

    def construct(self):
        n = self.ui.sbxN.value()
        m = self.ui.sbxM.value()
        r = self.ui.sbxR.value()
        m = min(m, n-m)

        draw_n_gon = self.ui.cbxDisplayNgon.isChecked()
        draw_inner_sp = self.ui.cbxDisplayInnnerSP.isChecked()
        draw_vertex_coords = self.ui.cbxDisplayVertexCoords.isChecked()
        draw_circumcircle = self.ui.btnDisplayCircumcircle.isChecked()

        geometry = self.ui.label.size().toTuple()

        self.ui.label.setPixmap(QPixmap.fromImage(
            QImage(
                ImageQt(
                    draw_sp(
                        n,
                        m,
                        r,
                        draw_n_gon,
                        draw_inner_sp,
                        draw_vertex_coords,
                        draw_circumcircle,
                        geometry
                    )
                )
            ).scaled(geometry[0], geometry[1], Qt.AspectRatioMode.KeepAspectRatio)
        ))

        self.ui.lblVertexAngle.setText(f"{vertex_angle(n, m):.2f}°")
        self.ui.lblArea.setText(f"{area(n, m, r):.2f}")
        self.ui.lblPerimeter.setText(f"{perimeter(n, m, r):.2f}")
        self.ui.lblTheta.setText(f"{central_angle(n):.2f}°")
        self.ui.lblSideLength.setText(f"{side_length(n, m, r):.2f}")
        if gcd(n, m) == 1:
            self.ui.lblConnected.setText("Связный")
            self.ui.btnExplode.setDisabled(True)
        else:
            self.ui.lblConnected.setText("Несвязный")
            self.ui.btnExplode.setDisabled(False)
            self.ui.lblCompN.setText(f"{n // gcd(n, m)}")
            self.ui.lblCompM.setText(f"{m // gcd(n, m)}")
            self.ui.lblCompAmount.setText(f"{gcd(n, m)}")

        self.lastAction = self.construct

    def start_exploding_polygon(self):
        thread = Thread(target=self.explode_polygon)
        thread.start()

    def start_unexploding_polygon(self):
        thread =Thread(target=self.unexplode_polygon)
        thread.start()


    def explode_polygon(self):
        n = self.ui.sbxN.value()
        m = self.ui.sbxM.value()
        m = min(m, n-m)

        t = 0
        while t <= 1:
            self.ui.label.setPixmap(QPixmap.fromImage(
                QImage(
                    ImageQt(
                        draw_exploding_polygon(
                            n,
                            m,
                            self.ui.label.size().toTuple(),
                            t
                        )
                    )
                ).scaled(self.ui.label.size().toTuple()[0], self.ui.label.size().toTuple()[1], Qt.AspectRatioMode.KeepAspectRatio)
            ))
            time.sleep(0.01)
            t += 0.01
        self.ui.btnExplode.setDisabled(True)
        self.ui.btnUnexplode.setEnabled(True)

    def unexplode_polygon(self):
        n = self.ui.sbxN.value()
        m = self.ui.sbxM.value()
        m = min(m, n-m)

        t = 1
        while t >= 0:
            self.ui.label.setPixmap(QPixmap.fromImage(
                QImage(
                    ImageQt(
                        draw_exploding_polygon(
                            n,
                            m,
                            self.ui.label.size().toTuple(),
                            t
                        )
                    )
                ).scaled(self.ui.label.size().toTuple()[0], self.ui.label.size().toTuple()[1], Qt.AspectRatioMode.KeepAspectRatio)
            ))
            time.sleep(0.01)
            t -= 0.01

        self.ui.btnUnexplode.setDisabled(True)
        self.ui.btnExplode.setEnabled(True)
        self.construct()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ConstructWindow()
    window.show()

    sys.exit(app.exec())
