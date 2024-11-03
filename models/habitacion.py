# -*- coding: utf-8 -*-

class Habitacion:
    def __init__(self, id_habitacion, tipo, precio, caracteristicas):
        self.id_habitacion = id_habitacion
        self.tipo = tipo
        self.precio = precio
        self.caracteristicas = caracteristicas
        self.estado = 'Disponible'

    def consultar_disponibilidad(self):
        return self.estado == 'Disponible'

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio