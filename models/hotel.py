# -*- coding: utf-8 -*-

from datetime import datetime
from .habitacion import Habitacion
from .usuario import Usuario
from .reserva import Reserva

class Hotel:
    def __init__(self):
        self.habitaciones = [
            Habitacion(1, 'Individual', 50, 'Cama individual, Wi-Fi'),
            Habitacion(2, 'Individual', 50, 'Cama individual, Wi-Fi'),
            Habitacion(3, 'Doble', 80, 'Dos camas, TV, Wi-Fi'),
            Habitacion(4, 'Doble', 80, 'Dos camas, TV, Wi-Fi'),
            Habitacion(5, 'Suite', 150, 'Cama king, Jacuzzi, Wi-Fi'),
            Habitacion(6, 'Suite', 150, 'Cama king, Jacuzzi, Wi-Fi')
        ]
        self.reservas = {}
        self.contador_reservas = 1
        self.usuarios = [Usuario('admin', 'admin@hotel.com', 'admin123', es_admin=True)]

    def obtener_habitacion_por_id(self, id_habitacion):
        for habitacion in self.habitaciones:
            if habitacion.id_habitacion == id_habitacion:
                return habitacion
        return None

    def realizar_reserva(self, id_habitacion, usuario, fecha_entrada, fecha_salida):
        habitacion = self.obtener_habitacion_por_id(id_habitacion)
        if habitacion and habitacion.consultar_disponibilidad():
            reserva = Reserva(self.contador_reservas, habitacion, usuario, fecha_entrada, fecha_salida)
            self.reservas[self.contador_reservas] = reserva
            self.contador_reservas += 1
            habitacion.actualizar_estado('Reservada')
            return reserva
        return None

    def cancelar_reserva(self, numero_reserva, usuario):
        if numero_reserva in self.reservas:
            reserva = self.reservas[numero_reserva]
            if reserva.usuario.correo_electronico == usuario.correo_electronico or usuario.es_admin:
                reserva.habitacion.actualizar_estado('Disponible')
                del self.reservas[numero_reserva]
                return True
        return False

    def modificar_reserva(self, numero_reserva, usuario, nueva_fecha_entrada, nueva_fecha_salida):
        if numero_reserva in self.reservas:
            reserva = self.reservas[numero_reserva]
            if reserva.usuario.correo_electronico == usuario.correo_electronico or usuario.es_admin:
                reserva.fecha_entrada = nueva_fecha_entrada
                reserva.fecha_salida = nueva_fecha_salida
                return True
        return False

    def registrar_usuario(self, nombre, correo, contraseña):
        if any(u.correo_electronico == correo for u in self.usuarios):
            return False
        self.usuarios.append(Usuario(nombre, correo, contraseña))
        return True

    def iniciar_sesion(self, correo, contraseña):
        for usuario in self.usuarios:
            if usuario.correo_electronico == correo and usuario.contraseña == contraseña:
                return usuario
        return None
    
    def modificar_reserva(self, numero_reserva, nueva_fecha_entrada, nueva_fecha_salida):
        if numero_reserva in self.reservas:
            reserva = self.reservas[numero_reserva]
            if reserva.usuario.correo_electronico == self.usuario_actual.correo_electronico or self.usuario_actual.es_admin:
                reserva.fecha_entrada = nueva_fecha_entrada
                reserva.fecha_salida = nueva_fecha_salida
                return True
        return False

    def cancelar_reserva(self, numero_reserva):
        if numero_reserva in self.reservas:
            reserva = self.reservas[numero_reserva]
            if reserva.usuario.correo_electronico == self.usuario_actual.correo_electronico or self.usuario_actual.es_admin:
                del self.reservas[numero_reserva]
                return True
        return False
    
    def __init__(self):
        self.reservas = []  # Lista para almacenar las reservas

    def obtener_reservas_usuario(self, usuario):
        return [reserva for reserva in self.reservas if reserva.usuario == usuario]