from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QDateEdit, QGridLayout, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSignal ,QDate

class AgregarPasajero(QMainWindow):
    mi_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Agregar pasajero")
        self.setFixedSize(300,150) 
        self.nombre = ''

        widget = QWidget()
        layout = QGridLayout()
        grid_logo = QGridLayout()

        layout.addLayout(grid_logo,0,0)

        # Agregar la imagen en la esquina superior izquierda
        imagen_label = QLabel(self)
        pixmap = QPixmap("logo.png")  
        pixmap = pixmap.scaled(30, 30)  
        imagen_label.setPixmap(pixmap)
        
        grid_logo.addWidget(imagen_label, 0,0)

        # Agregar el QLabel para el nombre del hotel
        hotel_label = QLabel("Hotel CTCh", self)
        grid_logo.addWidget(hotel_label, 0, 1, 1, 3)

        # Agregar el QLabel y QLineEdit para el nombre
        nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        layout.addWidget(nombre_label, 1, 0)  
        layout.addWidget(self.nombre_input, 1, 1)  

        # Agregar el QLabel y QDateEdit para la fecha de nacimiento
        fecha_label = QLabel("Fecha de nacimiento:")
        fecha_input = QDateEdit()
        fecha_input.setMaximumDate(QDate.currentDate())
        layout.addWidget(fecha_label, 2, 0)  
        layout.addWidget(fecha_input, 2, 1) 

        # Agregar botones de volver y aceptar
        self.volver_button = QPushButton("Volver")
        self.agregar_button = QPushButton("Agregar")

        self.agregar_button.clicked.connect(self.emitir_signal)
        self.volver_button.clicked.connect(self.close)
        
        layout.addWidget(self.volver_button, 3, 0, 2, 1)
        layout.addWidget(self.agregar_button, 3, 1, 2, 1) 

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def emitir_signal(self):
        if self.nombre_input.text() != "":
            self.nombre = self.nombre_input.text()
            self.mi_signal.emit()
            self.close()
        else:
            QMessageBox.warning(self,"Error", "El nombre no puede quedar vacio", QMessageBox.StandardButton.Close)