# -*- coding: utf-8 -*-

class Usuario:
    def __init__(self, nombre, correo_electronico, contraseña, es_admin=False):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.contraseña = contraseña
        self.es_admin = es_admin

    def enviar_notificacion(self, mensaje):
        return mensaje