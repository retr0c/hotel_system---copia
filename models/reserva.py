# -*- coding: utf-8 -*-

from datetime import datetime

class Reserva:
    def __init__(self, numero_reserva, habitacion, usuario, fecha_entrada, fecha_salida):
        self.numero_reserva = numero_reserva
        self.habitacion = habitacion
        self.usuario = usuario
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

    def calcular_precio_total(self):
        dias_estancia = (self.fecha_salida - self.fecha_entrada).days
        return dias_estancia * self.habitacion.precio