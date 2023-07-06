import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from ventanaprincipal import ventanaprincipal
from registrarse import ventanaderegistro

class Login(QWidget):
    
    def __init__(self):
        super().__init__()
        self.inicializarui()

    def inicializarui(self):
        self.setGeometry(100, 100, 350, 200)
        self.setWindowTitle("Registro recepcionista")
        self.informacion()
        self.show()

    def informacion(self):
        
        logo_label = QLabel()
        logo_pixmap = QPixmap("logo.png")
        logo_pixmap = logo_pixmap.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        nombreHotel_label = QLabel("Hotel CTCh")
        nombreHotel_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        nombreHotel_label.setFixedHeight(30)

        user_label = QLabel("Ingrese su RUT:")
        user_label.setFixedWidth(120)
        self.user_input = QLineEdit()
        self.user_input.setInputMask("99999999-N")

        password_label = QLabel("Ingrese su contraseña:")
        password_label.setFixedWidth(120)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        check_ver_contraseña = QCheckBox("Ver contraseña")
        check_ver_contraseña.toggled.connect(self.mostrarcontrasena)

        ingresar_button = QPushButton("Ingresar")
        ingresar_button.setDefault(True)
        ingresar_button.clicked.connect(self.iniciarventanaingreso)

        registro_button = QPushButton("Registrarse")
        registro_button.clicked.connect(self.iniciarventanaderegistro)

        layout = QHBoxLayout()
        layout.addWidget(logo_label)
        layout.addWidget(nombreHotel_label)
        layout.addStretch()

        Hlayout1 = QHBoxLayout()
        Hlayout1.addWidget(user_label)
        Hlayout1.addWidget(self.user_input)

        Hlayout2 = QHBoxLayout()
        Hlayout2.addWidget(password_label)
        Hlayout2.addWidget(self.password_input)

        Hlayout3 = QHBoxLayout()
        Hlayout3.addWidget(check_ver_contraseña)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(layout)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addLayout(Hlayout3)
        Vlayout.addWidget(ingresar_button)
        Vlayout.addWidget(registro_button)

        self.setLayout(Vlayout)

    def mostrarcontrasena(self, clicked):
        if clicked:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    def iniciarventanaderegistro(self):
        self.nuevousuario = ventanaderegistro()
        self.nuevousuario.show()

    def iniciarventanaingreso(self):
        try:
            usuarios = open("data/usuarios.csv", "r")
            encontrado = False
            autorizado = False
            if self.user_input.text() != "-" and self.password_input.isModified() == True and (len(self.user_input.text())==10 or len(self.user_input.text())==9):
                for linea in usuarios:
                    if self.user_input.text() in linea:
                        encontrado = True
                if encontrado == True:
                    #Funcion seek permite "rebobinar" un archivo ya recorrido mediante un ciclo for
                    usuarios.seek(0)
                    for usuario in usuarios:
                        if f"{self.user_input.text()},{self.password_input.text()}" in usuario:
                            autorizado = True
                    if autorizado == True:
                        #loguear
                        QMessageBox.information(self,"Inicio de sesion","Se ha iniciado sesion correctamente",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
                        self.abrirventanaprincipal()
                        usuarios.close()
                        self.close()
                    else:
                        QMessageBox.information(self,"Advertencia", "La contraseña ingresada es incorrecta", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.warning(self,"Error", "El usuario ingresado no existe", QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            else:
                QMessageBox.information(self,"Advertencia","Ingrese los datos correctamente",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
        except FileNotFoundError:
            QMessageBox.warning(self,"Error", "El archivo usuarios.csv no ha sido encontrado.", QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
            
    def abrirventanaprincipal(self):
        self.ventanaprincipal = ventanaprincipal()
        self.ventanaprincipal.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Login()
    #Como el modulo "Login_recepcionista.py" es el archivo principal para arrancar el programa,
    #se aprovecha de comprobar de que los archivos principales a usar donde se guardara la informacion
    # de las reservas, usuarios, descuentos y gerentes se encuentren en el directorio raiz del programa.

    try:#Crea el directorio donde se almacenan los datos
        os.mkdir("data")
    except FileExistsError:
        pass

    archivos = ["data/usuarios.csv", "data/usuarios_gerentes.csv", "data/reservas.csv", "data/descuentos_gerenciales.csv", "data/pagos_efectivo.csv", "data/pagos_debito.csv", "data/pagos_credito.csv"]
    for archivo in archivos:
        try:
            temp = open(archivo, "x")
            if archivo == "data/usuarios.csv":
                temp.write("rut,contrasena\n")
            elif archivo == "data/usuarios_gerentes.csv":
                temp.write("rut,contrasena\n")
            elif archivo == "data/reservas.csv":
                temp.write("nombre_reservante,fecha_de_nacimiento,habitaciones,tiempo_estadia,fecha,tarjeta,pasajeros\n")
            elif archivo == "data/descuentos_gerenciales.csv": 
                temp.write("rut_gerente,descuento,fecha\n")
            elif archivo == "data/pagos_efectivo.csv":
                temp.write("monto,fecha\n")
            elif archivo == "data/pagos_debito.csv":
                temp.write("monto,numero_de_tarjeta,rut,fecha\n")
            elif archivo == "data/pagos_credito.csv":
                temp.write("monto,titular,numero_de_tarjeta,fecha\n")
            temp.close()
        except FileExistsError:
            pass

    sys.exit(app.exec())
