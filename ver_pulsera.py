from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QGridLayout, QTableWidget, QHeaderView
from PyQt6.QtGui import QPixmap

class VentanaPulsera(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ver pulsera")
        self.setFixedSize(350,200)  # Establece la posición y el tamaño de la ventana

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
        hotel_label = QLabel("Hotel CTh", self)
        grid_logo.addWidget(hotel_label, 0, 1, 1, 7)

        codigo_label = QLabel("Codigo", self)
        layout.addWidget(codigo_label, 1, 0, 1, 2)

        self.tabla_gastos = QTableWidget(1, 1)  

        self.tabla_gastos.setHorizontalHeaderLabels(["Gastos"])
        self.tabla_gastos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_gastos.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        aceptar_button = QPushButton("Aceptar")
        aceptar_button.clicked.connect(self.close)
        layout.addWidget(aceptar_button,4,1 )


        layout.addWidget(self.tabla_gastos, 2, 0, 2, 2)
        widget.setLayout(layout)
        self.setCentralWidget(widget)