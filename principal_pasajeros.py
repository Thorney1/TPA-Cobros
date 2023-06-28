from PyQt6.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QPushButton, QWidget, QGridLayout, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from agregar_pasajero import*
from ver_pulsera import *


class PrincipalPasajeros(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pasajeros")
        self.setFixedSize(350,200)

        self.lista_pasajeros = []

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
        widget.setLayout(layout)
        self.setCentralWidget(widget)


        self.table = QTableWidget(0, 2)  

        self.table.setHorizontalHeaderLabels(["Pasajero", "Pulsera"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        
        # Agregar botones pasajeros
        agregar_pasajero_button = QPushButton("Agregar pasajero")
        eliminar_pasajero = QPushButton("Eliminar pasajero")
        layout.addWidget(agregar_pasajero_button,1,0)
        layout.addWidget(eliminar_pasajero,2,0)
        agregar_pasajero_button.clicked.connect(self.mostrar_agregar_pasajero)
        eliminar_pasajero.clicked.connect(self.eliminar_pasajero)

        # Agregar botones de cancelar y aceptar
        volver_button = QPushButton("Volver")
        #actualizar_button no hace nada
        actualizar_button = QPushButton("Actualizar")

        volver_button.clicked.connect(self.close)
        
        layout.addWidget(volver_button, 4, 0, 1, 1)
        layout.addWidget(actualizar_button, 4, 1, 1, 1) 

        layout.addWidget(self.table, 1, 1, 3, 2)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def mostrar_ventana_ver_pulsera(self):
        self.ventana_ver_pulsera = VentanaPulsera()
        self.ventana_ver_pulsera.show()

    def mostrar_agregar_pasajero(self):
        self.ventana_agregar_pasajero = AgregarPasajero()
        self.ventana_agregar_pasajero.mi_signal.connect(self.agregar_pasajero)
        self.ventana_agregar_pasajero.show()
    
    def eliminar_pasajero(self):
        if (self.table.item((self.table.currentRow()),0)) is not None:
            selected_row = self.table.currentRow()
            self.lista_pasajeros.remove(self.table.item((self.table.currentRow()),0).text())
            self.table.removeRow(selected_row)
        else:
            QMessageBox.critical(None, "Error", "No hay pasajeros a eliminar")
    
    def agregar_pasajero(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        item = QTableWidgetItem(self.ventana_agregar_pasajero.nombre)
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.table.setItem(row_count, 0, item)
        #Añade el pasajero agregado a la lista temporal de pasajeros
        self.lista_pasajeros.append(self.ventana_agregar_pasajero.nombre)

        button = QPushButton("Ver pulsera")
        button.clicked.connect(self.mostrar_ventana_ver_pulsera)
        button.setProperty("tableRow", row_count)
        button.setProperty("tableColumn", 1)
        layout_widget = QWidget()
        button_layout = QHBoxLayout(layout_widget)
        button_layout.addWidget(button)
        button_layout.setAlignment(button, Qt.AlignmentFlag.AlignCenter)
        button_layout.setContentsMargins(0, 0, 0, 0)
        layout_widget.setLayout(button_layout)
        self.table.setCellWidget(row_count, 1, layout_widget)
    
    #Funcion que envia pasajeros a la ventana principal
    def send_pasajeros(self):
        return self.lista_pasajeros

    def clean_pasajeros(self):
        self.lista_pasajeros = []
        aux = self.table.rowCount()
        print(aux)
        for i in range(aux):
            self.table.removeRow(0)
