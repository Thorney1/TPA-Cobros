from PyQt6.QtWidgets import QDialog , QLabel , QPushButton , QLineEdit , QMessageBox , QHBoxLayout , QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ventanaderegistro(QDialog):
     
    def __init__(self):
        super().__init__()
        self.setModal(True)    
        self.datosusuario()

    def datosusuario(self):

        self.setGeometry(100,100,350,200)
        self.setWindowTitle("Ventana de registro")

        logo_label = QLabel()
        logo_pixmap = QPixmap("logo.png")
        logo_pixmap = logo_pixmap.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        nombre_label = QLabel("Hotel CTCh")
        nombre_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        nombre_label.setFixedHeight(30)

        user_label = QLabel(self)
        user_label.setText("Ingrese su RUT")
        user_label.setFont(QFont("Arial",10))
        user_label.move(20,44)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,40)
        self.user_input.setInputMask("99999999-N")

        password1_label = QLabel(self)
        password1_label.setText("Ingrese una contraseña")
        password1_label.setFont(QFont("Arial",10))
        password1_label.move(20,74)

        self.password1_label_input = QLineEdit(self)
        self.password1_label_input.resize(250,24)
        self.password1_label_input.move(90,70)
        self.password1_label_input.setEchoMode(QLineEdit.EchoMode.Password)

        password2_label = QLabel(self)
        password2_label.setText("Confirme su contraseña")
        password2_label.setFont(QFont("Arial",10))
        password2_label.move(20,104)

        self.password2_label_input = QLineEdit(self)
        self.password2_label_input.resize(250,24)
        self.password2_label_input.move(90,100)
        self.password2_label_input.setEchoMode(QLineEdit.EchoMode.Password)

        aceptar_button = QPushButton(self)
        aceptar_button.setText("Aceptar")
        aceptar_button.resize(150,32)
        aceptar_button.move(20,170)
        aceptar_button.clicked.connect(self.crearusuario)

        cancelar_button = QPushButton(self)
        cancelar_button.setText("Cancelar")
        cancelar_button.resize(150,32)
        cancelar_button.move(170,170)
        cancelar_button.clicked.connect(self.cancelarcreacion)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(logo_label)
        Hlayout.addWidget(nombre_label)
        Hlayout.addStretch()

        Hlayout1 = QHBoxLayout()
        Hlayout1.addWidget(user_label)
        Hlayout1.addWidget(self.user_input)

        Hlayout2 = QHBoxLayout()
        Hlayout2.addWidget(password1_label)
        Hlayout2.addWidget(self.password1_label_input)

        Hlayout3 = QHBoxLayout()
        Hlayout3.addWidget(password2_label)
        Hlayout3.addWidget(self.password2_label_input)

        Hlayout4= QHBoxLayout()
        Hlayout4.addWidget(aceptar_button)
        Hlayout4.addWidget(cancelar_button)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addLayout(Hlayout3)
        Vlayout.addLayout(Hlayout4)

        self.setLayout(Vlayout)

    def crearusuario(self):
        try:
            #Abrir el archivo como append y como lectura
            archivo = open("data/usuarios.csv", "a+")
            existe = False
            for linea in archivo:
                if self.user_input.text() in linea and self.user_input.text() != "-":
                    existe = True
            if existe == True:
                QMessageBox.warning(self, "Error", "El usuario ingresado ya existe", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            else:
                #Registrarlo
                if self.user_input.text() != "-" and self.password1_label_input.isModified() == True and self.password2_label_input.isModified() == True and (len(self.user_input.text())==10 or len(self.user_input.text())==9):
                    if self.password1_label_input.text() == self.password2_label_input.text():
                        archivo.write(f"\n{self.user_input.text()},{self.password1_label_input.text()}")
                        QMessageBox.information(self, "Exito", "El usuario ha sido registrado correctamente", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
                        self.close()
                    else:
                        QMessageBox.warning(self, "Error", "Las contraseñas deben ser idénticas, por favor inténtelo de nuevo", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
                else:
                    QMessageBox.information(self,"Advertencia","Ingrese los datos correctamente",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "El archivo usuarios.csv no ha sido encontrado.", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)

    def cancelarcreacion(self):
        self.close()