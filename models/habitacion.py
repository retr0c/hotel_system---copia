# -*- coding: utf-8 -*-
# models/habitacion.py
from datetime import datetime

class Habitacion:
    def __init__(self, id_habitacion, tipo, precio, caracteristicas):
        self.id_habitacion = id_habitacion
        self.tipo = tipo
        self.precio = precio
        self.caracteristicas = caracteristicas
        self.reservas = []  # Lista de tuplas (fecha_entrada, fecha_salida)

    def consultar_disponibilidad(self, fecha_entrada=None, fecha_salida=None):
        if fecha_entrada is None or fecha_salida is None:
            return not bool(self.reservas)  # Si no hay fechas, solo verifica si hay reservas
        
        # Convertir fechas a datetime si son strings
        if isinstance(fecha_entrada, str):
            fecha_entrada = datetime.strptime(fecha_entrada, '%Y-%m-%d')
        if isinstance(fecha_salida, str):
            fecha_salida = datetime.strptime(fecha_salida, '%Y-%m-%d')

        # Verificar si hay solapamiento con alguna reserva existente
        for reserva_entrada, reserva_salida in self.reservas:
            if (fecha_entrada < reserva_salida and fecha_salida > reserva_entrada):
                return False
        return True

    def agregar_reserva(self, fecha_entrada, fecha_salida):
        if self.consultar_disponibilidad(fecha_entrada, fecha_salida):
            self.reservas.append((fecha_entrada, fecha_salida))
            return True
        return False

    def cancelar_reserva(self, fecha_entrada, fecha_salida):
        if (fecha_entrada, fecha_salida) in self.reservas:
            self.reservas.remove((fecha_entrada, fecha_salida))
            return True
        return False