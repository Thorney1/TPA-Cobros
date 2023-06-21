from PyQt6.QtWidgets import QLabel , QLineEdit , QPushButton , QHBoxLayout , QVBoxLayout , QDialog , QMessageBox, QSpinBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from datetime import date

class debito(QDialog):

    def __init__(self):

        super().__init__()
        self.setModal(True)
        self.inicializarui()

    def inicializarui(self):

        self.setGeometry(100, 100, 350, 200)
        self.setWindowTitle("Tarjeta de debito")
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

        numeros_label = QLabel("Numero de tarjeta")
        self.numtarjeta_input = QLineEdit()
        self.numtarjeta_input.setInputMask("9999 9999 9999 9999")

        rut_label = QLabel("RUT")
        self.rut_input = QLineEdit()
        self.rut_input.setInputMask("99999999-N")

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
        Hlayout2.addWidget(rut_label)
        Hlayout2.addWidget(self.rut_input)

        Hlayout3 = QHBoxLayout()
        Hlayout3.addWidget(volver_button)
        Hlayout3.addWidget(pagar_button)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addWidget(numeros_label)
        Vlayout.addWidget(self.numtarjeta_input)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addLayout(Hlayout3)

        self.setLayout(Vlayout)

    def cerrarventana(self):
        self.close()

    def pago(self):
        if self.monto_input.value() != 0:
            if self.numtarjeta_input.isModified() == True and self.rut_input.isModified() == True:
                if len(self.numtarjeta_input.text()) == 19:
                    if len(self.rut_input.text()) == 10 or len(self.rut_input.text()) == 9:
                        archivo = open("data/pagos_debito.csv", "a")
                        #monto,numero_de_tarjeta,rut,fecha
                        archivo.write(f"{self.monto_input.value()},{self.numtarjeta_input.text()},{self.rut_input.text()},{date.today()}\n")
                        archivo.close()
                        QMessageBox.information(self, "Pago exitoso", "El pago se realizo correctamente", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
                        self.close()
                    else:
                        QMessageBox.warning(self,"Error", "Ingrese el RUT correctamente", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
                else:
                    QMessageBox.warning(self, "Error", "Ingrese el numero de la tarjeta correctamente", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            else:
                QMessageBox.warning(self, "Error", "No pueden quedar campos vacios", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        else:
            QMessageBox.warning(self, "Error", "Ingrese un monto valido", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)



