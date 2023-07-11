from PyQt6.QtWidgets import QLabel , QLineEdit , QSpinBox , QDateEdit , QPushButton , QDialog , QHBoxLayout , QVBoxLayout , QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt,QDate

class gerente(QDialog):

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.inicializarui()

    def inicializarui(self):

        self.setGeometry(100, 100, 350, 200)
        self.setWindowTitle("Confirmacion gerente")

        logo_label = QLabel()
        logo_pixmap = QPixmap("logo.png")
        logo_pixmap = logo_pixmap.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        nombre_label = QLabel("Hotel CTCh")
        nombre_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        nombre_label.setFixedHeight(30)

        rut_label = QLabel("RUT")
        rut_label.setFixedWidth(120)
        self.rut_input = QLineEdit()
        self.rut_input.setInputMask("99999999-N")

        contrasena_label = QLabel("Contraseña")
        contrasena_label.setFixedWidth(120)
        self.contrasena_input = QLineEdit()
        self.contrasena_input.setEchoMode(QLineEdit.EchoMode.Password)

        descuento_label = QLabel("Descuento")
        descuento_label.setFixedWidth(120)
        self.descuento_input = QSpinBox()
        self.descuento_input.setRange(0,100)

        fecha_label = QLabel("Fecha")
        fecha_label.setFixedWidth(120)
        self.fecha_input = QDateEdit()
        self.fecha_input.setMinimumDate(QDate.currentDate())

        cancelar_button = QPushButton("Cancelar")
        cancelar_button.clicked.connect(self.cerrarventana)

        confirmar_button = QPushButton("Confirmar descuento")
        confirmar_button.clicked.connect(self.registro_gerente)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(logo_label)
        Hlayout.addWidget(nombre_label)
        Hlayout.addStretch()

        Hlayout1 = QHBoxLayout()
        Hlayout1.addWidget(rut_label)
        Hlayout1.addWidget(self.rut_input)

        Hlayout2 = QHBoxLayout()
        Hlayout2.addWidget(contrasena_label)
        Hlayout2.addWidget(self.contrasena_input)

        Hlayout3 = QHBoxLayout()
        Hlayout3.addWidget(descuento_label)
        Hlayout3.addWidget(self.descuento_input)

        Hlayout4 = QHBoxLayout()
        Hlayout4.addWidget(fecha_label)
        Hlayout4.addWidget(self.fecha_input)

        Hlayout5 = QHBoxLayout()
        Hlayout5.addWidget(cancelar_button)
        Hlayout5.addWidget(confirmar_button)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addLayout(Hlayout3)
        Vlayout.addLayout(Hlayout4)
        Vlayout.addLayout(Hlayout5)

        self.setLayout(Vlayout)

    def registro_gerente(self):
        #Comprobar la existencia de los gerentes capaces de aplicar descuentos
        try:
            archivo_gerentes = open("data/usuarios_gerentes.csv", "r")

            rut_comprobar = self.rut_input.text()
            contrasena_comprobar = self.contrasena_input.text()

            autorizado = False

            for linea in archivo_gerentes:
                if f"{rut_comprobar},{contrasena_comprobar}" == linea:
                    autorizado = True
            archivo_gerentes.close()

            if autorizado == True: #Si esta autorizado
                #Guardar datos y todo lo demas
                try:
                    archivo_descuentos = open("data/descuentos_gerenciales.csv", "a")
                    archivo_descuentos.write(f"\n{self.rut_input.text()},{self.descuento_input.text()},{self.fecha_input.text()}\n")
                    QMessageBox.information(self, "Datos guardados", "El descuento ha sido autorizado y registrado", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
                    self.close()

                except FileNotFoundError:
                    QMessageBox.information(self, "Error", "El archivo descuentos_gerenciales.csv no existe", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            else:
                QMessageBox.information(self, "Informacion", "El gerente ingresado no existe.", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
        except FileNotFoundError:
            QMessageBox.warning(self,"Error", "El archivo usuarios_gerentes.csv no ha sido encontrado.", QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

    def cerrarventana(self):
        self.close()



