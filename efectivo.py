from PyQt6.QtWidgets import QLabel , QSpinBox , QPushButton , QHBoxLayout , QVBoxLayout , QDialog , QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from datetime import date

class efectivo(QDialog):

    def __init__(self):

        super().__init__()
        self.setModal(True)
        self.inicializarui()

    def inicializarui(self):

        self.setGeometry(100, 100, 350, 200)
        self.setWindowTitle("Efectivo")
        self.contenido()

    def contenido(self):

        logo_label = QLabel()
        logo_pixmap = QPixmap("logo.png")
        logo_pixmap = logo_pixmap.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        nombreHotel_label = QLabel("Hotel CTCh")
        nombreHotel_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        nombreHotel_label.setFixedHeight(30)

        monto_label = QLabel("Monto $")
        self.monto_input = QSpinBox()
        self.monto_input.setMaximum(2147483647)

        volver_button = QPushButton("Volver")
        volver_button.clicked.connect(self.cerrarventana)

        pagar_button = QPushButton("Realizar pago")
        pagar_button.clicked.connect(self.pago)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(logo_label)
        Hlayout.addWidget(nombreHotel_label)
        Hlayout.addStretch()

        Hlayout1 = QHBoxLayout()
        Hlayout1.addWidget(monto_label)
        Hlayout1.addWidget(self.monto_input)

        Hlayout2 = QHBoxLayout()
        Hlayout2.addWidget(volver_button)
        Hlayout2.addWidget(pagar_button)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addLayout(Hlayout2)

        self.setLayout(Vlayout)

    def cerrarventana(self):
        self.close()

    def pago(self):
        if self.monto_input.value() != 0:
            archivo = open("data/pagos_efectivo.csv", "a")
            archivo.write(f"{self.monto_input.value()},{date.today()}\n")
            archivo.close()
            QMessageBox.information(self, "Pago exitoso", "El pago se realizo correctamente", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Ingrese un monto valido", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)