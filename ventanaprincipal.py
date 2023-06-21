from PyQt6.QtWidgets import QWidget , QLabel , QLineEdit , QHBoxLayout ,QVBoxLayout , QPushButton ,QDateEdit , QSpinBox , QMessageBox , QDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt 
from costos import costos
from principal_pasajeros import *
import csv

class ventanaprincipal(QDialog):   

    def __init__(self):
        super().__init__()
        self.inicializarui()

    def inicializarui(self):
        self.setGeometry(100,100,350,250)   
        self.setWindowTitle("Sistema de cobros de estadia")
        self.contenido()
        self.show()     

    def contenido(self):
        self.principal_pasajeros = PrincipalPasajeros()
        #Diccionario que va a contener temporalmente toda la informacion
        self.reserva_temp = {"nombre_reservante": None,
                             "fecha_de_nacimiento": None,
                             "habitaciones": None,
                             "tiempo_estadia": None,
                             "fecha": None,
                             "tarjeta": {"titular": None,
                                         "numero": None,
                                         "fecha": None,
                                         "cvc": None},
                             "pasajeros": None}

        logo_label = QLabel()
        logo_pixmap = QPixmap("logo.png")
        logo_pixmap = logo_pixmap.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        nombreHotel_label = QLabel("Hotel CTCh")
        nombreHotel_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        nombreHotel_label.setFixedHeight(30) 

        texto1_label = QLabel("Validar datos de reserva")

        nombre_label = QLabel("Nombre")
        nombre_label.setFixedWidth(120)
        self.nombre_input = QLineEdit()

        fechaN_label = QLabel("Fecha de nacimiento")
        fechaN_label.setFixedWidth(120)
        self.fechaN_input = QDateEdit()

        habitacion_label = QLabel("Habitaciones")
        habitacion_label.setFixedWidth(120)
        self.habitacion_input = QSpinBox()

        estadia_label = QLabel("Tiempo de estadia")
        estadia_label.setFixedWidth(120)
        self.estadia_input = QLineEdit()

        fecha_label = QLabel("Fecha")
        fecha_label.setFixedWidth(120)
        self.fecha_input = QDateEdit()

        pasajeros_button = QPushButton("Pasajeros")
        pasajeros_button.clicked.connect(self.iniciarVentanaPasajero)

        costo_button = QPushButton("Calcular costo de estadia")
        costo_button.clicked.connect(self.iniciarventanacostos)

        texto2_label = QLabel("Registrar tarjeta de credito")

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

        guardar_button = QPushButton("Guardar datos")
        guardar_button.clicked.connect(self.guardar_datos)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(logo_label)
        Hlayout.addWidget(nombreHotel_label)
        Hlayout.addStretch()

        Hlayout1 = QHBoxLayout()
        Hlayout1.addWidget(nombre_label)
        Hlayout1.addWidget(self.nombre_input)

        Hlayout2 = QHBoxLayout()
        Hlayout2.addWidget(fechaN_label)
        Hlayout2.addWidget(self.fechaN_input)

        Hlayout3 = QHBoxLayout()
        Hlayout3.addWidget(habitacion_label)
        Hlayout3.addWidget(self.habitacion_input)

        Hlayout4 = QHBoxLayout()
        Hlayout4.addWidget(estadia_label)
        Hlayout4.addWidget(self.estadia_input)

        Hlayout5 = QHBoxLayout()
        Hlayout5.addWidget(fecha_label)
        Hlayout5.addWidget(self.fecha_input)

        Hlayout6 = QHBoxLayout()
        Hlayout6.addWidget(pasajeros_button)
        Hlayout6.addWidget(costo_button)

        Hlayout7 = QHBoxLayout()
        Hlayout7.addWidget(expiracion_label)
        Hlayout7.addWidget(cvc_label)

        Hlayout8 = QHBoxLayout()
        Hlayout8.addWidget(self.expiracion_input)
        Hlayout8.addWidget(self.cvc_input)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout)
        Vlayout.addWidget(texto1_label)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addLayout(Hlayout3)
        Vlayout.addLayout(Hlayout4)
        Vlayout.addLayout(Hlayout5)
        Vlayout.addLayout(Hlayout6)
        Vlayout.addWidget(texto2_label)
        Vlayout.addWidget(titular_label)
        Vlayout.addWidget(self.nombretarjeta_input)
        Vlayout.addWidget(numeros_label)
        Vlayout.addWidget(self.numtarjeta_input)
        Vlayout.addLayout(Hlayout7)
        Vlayout.addLayout(Hlayout8)
        Vlayout.addWidget(guardar_button)

        self.setLayout(Vlayout)

    def guardar_datos(self):
        #COMPROBAR SI LOS CAMPOS ESTAN VACIOS O NO
        if self.campos_vacios() == False:
            #Verificar tarjeta
            if len(self.numtarjeta_input.text()) == 19 and len(self.cvc_input.text()) == 3:
                #una vez que se presiona guardar datos se reciben los pasajeros de la ventana agregar_pasajero.py
                self.reserva_temp["pasajeros"]= self.principal_pasajeros.send_pasajeros()
                #limpia la lista de pasajeros de la ventana pasajeros
                self.reserva_temp["nombre_reservante"] = self.nombre_input.text()
                self.reserva_temp["fecha_de_nacimiento"] = self.fechaN_input.text()
                self.reserva_temp["habitaciones"] = self.habitacion_input.text()
                self.reserva_temp["tiempo_estadia"] = self.estadia_input.text()
                self.reserva_temp["fecha"] = self.fecha_input.text()
                self.reserva_temp["tarjeta"]["titular"] = self.nombretarjeta_input.text()
                self.reserva_temp["tarjeta"]["numero"] = self.numtarjeta_input.text()
                self.reserva_temp["tarjeta"]["fecha"] = self.expiracion_input.text()
                self.reserva_temp["tarjeta"]["cvc"] = self.cvc_input.text()
    
                archivo = open("data/reservas.csv", "a+")
                cabeceras = list(self.reserva_temp.keys())
                writer = csv.DictWriter(archivo, fieldnames=cabeceras)
                writer.writerow(self.reserva_temp)
    
                archivo.close()
                #una vez que se guardan los datos, se borra self.pasajeros_reserva + se limpia todos los campos
                self.limpiar_campos()
                QMessageBox.information(self, "Datos guardados", "Los datos se han guardado correctamente", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            else:
                QMessageBox.warning(self,"Error", "Verifique que los datos de la tarjeta sean correctos", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        else:
            QMessageBox.warning(self, "Error", "Verifique que todos los campos han sido rellenados y que los pasajeros han sido añadidos", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
    
    def iniciarventanacostos(self):
        self.ventanacostos = costos()
        self.ventanacostos.show()

    def iniciarVentanaPasajero(self):
        self.principal_pasajeros.show()
    
    def limpiar_campos(self):
        self.nombre_input.clear()
        self.fechaN_input.clear()
        self.habitacion_input.clear()
        self.estadia_input.clear()
        self.fecha_input.clear()
        self.nombretarjeta_input.clear()
        self.numtarjeta_input.clear()
        self.expiracion_input.clear()
        self.cvc_input.clear()
        self.principal_pasajeros.clean_pasajeros()
    
    def campos_vacios(self):
        if len(self.principal_pasajeros.send_pasajeros()) != 0 and self.nombre_input.isModified() == True and self.nombretarjeta_input.isModified() == True and self.numtarjeta_input.isModified() and self.cvc_input.isModified() == True:
            return False
        else:
            return True

