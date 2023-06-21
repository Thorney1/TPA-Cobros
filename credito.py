from PyQt6.QtWidgets import QLabel , QLineEdit , QPushButton , QHBoxLayout , QVBoxLayout , QDialog , QMessageBox ,QDateEdit, QSpinBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from datetime import date

class credito(QDialog):

    def __init__(self):

        super().__init__()
        self.setModal(True)
        self.inicializarui()

    def inicializarui(self):

        self.setGeometry(100, 100, 350, 200)
        self.setWindowTitle("Tarjeta de credito")
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
        self.monto_input = QSpinBox()
        self.monto_input.setMaximum(2147483647)

        titular_label = QLabel("Titular de la tarjeta")
        self.nombretarjeta_input = QLineEdit()

        numeros_label = QLabel("Numero de tarjeta")
        self.numtarjeta_input = QLineEdit()
        self.numtarjeta_input.setInputMask("9999 9999 9999 9999")

        expiracion_label = QLabel("Fecha de expiracion")
        self.expiracion_input = QDateEdit()

        cvc_label = QLabel("CVC")
        self.cvc_input = QLineEdit()
        self.cvc_input.setInputMask("999")

        volver_button = QPushButton("Volver")
        volver_button.clicked.connect(self.cerrarventana)

        pagar_button = QPushButton("Realizar Pago")
        pagar_button.clicked.connect(self.pago)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(logo_label)
        Hlayout.addWidget(nombreHotel_label)
        Hlayout.addStretch()

        Hlayout1 = QHBoxLayout()
        Hlayout1.addWidget(monto_label)
        Hlayout1.addWidget(self.monto_input)

        Hlayout2 = QHBoxLayout()
        Hlayout2.addWidget(expiracion_label)
        Hlayout2.addWidget(cvc_label)

        Hlayout3 = QHBoxLayout()
        Hlayout3.addWidget(self.expiracion_input)
        Hlayout3.addWidget(self.cvc_input)

        Hlayout4 = QHBoxLayout()
        Hlayout4.addWidget(volver_button)
        Hlayout4.addWidget(pagar_button)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addWidget(titular_label)
        Vlayout.addWidget(self.nombretarjeta_input)
        Vlayout.addWidget(numeros_label)
        Vlayout.addWidget(self.numtarjeta_input)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addLayout(Hlayout3)
        Vlayout.addLayout(Hlayout4)

        self.setLayout(Vlayout)

    def cerrarventana(self):
        self.close()

    def pago(self):
        if self.monto_input.value() != 0:
            if self.nombretarjeta_input.isModified() == True and self.numtarjeta_input.isModified() == True and self.cvc_input.isModified() == True:
                if len(self.numtarjeta_input.text()) == 19 and len(self.cvc_input.text()) == 3:
                    archivo = open("data/pagos_credito.csv", "a")
                    archivo.write(f"{self.monto_input.value()},{self.nombretarjeta_input.text()},{self.numtarjeta_input.text()},{date.today()}\n")
                    archivo.close()
                    QMessageBox.information(self, "Pago exitoso", "El pago se realizo correctamente", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
                    self.close()
                else:
                    QMessageBox.warning(self, "Error", "Ingrese los datos de la tarjeta correctamente", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            else:
                QMessageBox.warning(self, "Error", "No pueden quedar campos vacios", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        else:
            QMessageBox.warning(self, "Error", "Ingrese un monto valido", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)



