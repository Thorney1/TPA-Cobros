from PyQt6.QtWidgets import QLabel , QLineEdit , QPushButton , QHBoxLayout , QVBoxLayout , QDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class Transferencia(QDialog):

    def __init__(self):

        super().__init__()
        self.setModal(True)
        self.inicializarui()

    def inicializarui(self):

        self.setGeometry(100, 100, 350, 200)
        self.setWindowTitle("Transferencia")
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

        monto_label = QLabel("Monto")
        monto_input =QLineEdit()

        cuenta_label = QLabel("Numero de cuenta:")
        numcuenta_label = QLabel("76483933-4")

        tipo_label = QLabel("Tipo de cuenta:")
        tcuenta_label = QLabel("Vista")

        volver_button = QPushButton("Volver")
        volver_button.clicked.connect(self.cerrarventana)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(logo_label)
        Hlayout.addWidget(nombreHotel_label)
        Hlayout.addStretch()

        Hlayout1 = QHBoxLayout()
        Hlayout1.addWidget(monto_label)
        Hlayout1.addWidget(monto_input)

        Hlayout2 = QHBoxLayout()
        Hlayout2.addWidget(cuenta_label)
        Hlayout2.addWidget(numcuenta_label)

        Hlayout3 = QHBoxLayout()
        Hlayout3.addWidget(tipo_label)
        Hlayout3.addWidget(tcuenta_label)

        Hlayout4 = QHBoxLayout()
        Hlayout4.addWidget(volver_button)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addLayout(Hlayout3)
        Vlayout.addLayout(Hlayout4)

        self.setLayout(Vlayout)

    def cerrarventana(self):
        self.close()




