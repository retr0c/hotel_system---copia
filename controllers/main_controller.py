# -*- coding: utf-8 -*-

import customtkinter as ctk
from views.login_view import LoginView
from views.register_view import RegisterView
from views.dashboard_view import DashboardView
from views.reservation_view import ReservationView
from models.hotel import Hotel
from views.history_view import HistoryView

class MainController:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Luxury Hotel Management System")
        self.root.geometry("800x600")
        
        self.hotel = Hotel()
        self.current_user = None
        
        # Configurar el contenedor principal
        self.container = ctk.CTkFrame(self.root)
        self.container.pack(side="top", fill="both", expand=True)
        
        # Configurar el grid del contenedor
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (LoginView, RegisterView, DashboardView, ReservationView, HistoryView):  # Añade HistoryView aquí
            frame = F(self.container, self)
            self.frames[F.__name__.lower().replace("view", "")] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.setup_views()
        
        self.show_login()

    def setup_views(self):
        # Crear y configurar el frame de login
        login_frame = LoginView(self.container, self)
        login_frame.grid(row=0, column=0, sticky="nsew")
        self.frames["login"] = login_frame

        # Crear y configurar el frame de registro
        register_frame = RegisterView(self.container, self)
        register_frame.grid(row=0, column=0, sticky="nsew")
        self.frames["register"] = register_frame

        # Crear y configurar el frame de dashboard
        dashboard_frame = DashboardView(self.container, self)
        dashboard_frame.grid(row=0, column=0, sticky="nsew")
        self.frames["dashboard"] = dashboard_frame

        # Crear y configurar el frame de reservas
        reservation_frame = ReservationView(self.container, self)
        reservation_frame.grid(row=0, column=0, sticky="nsew")
        self.frames["reservation"] = reservation_frame
        
        history_frame = HistoryView(self.container, self)
        history_frame.grid(row=0, column=0, sticky="nsew")
        self.frames["history"] = history_frame

    def show_frame(self, page_name):
       """Muestra el frame especificado"""
       frame = self.frames[page_name]
       frame.tkraise()  # Trae el frame al frente
        
       if hasattr(frame, 'clear'):
            frame.clear()  # Limpia los campos si el método existe
            
       if page_name == "history":
            if hasattr(frame, 'update_reservations'):
                    frame.update_reservations()

    def show_login(self):
        """Muestra la vista de login"""
        self.show_frame("login")

    def show_register(self):
        """Muestra la vista de registro"""
        self.show_frame("register")

    def show_reservation(self):
        """Muestra la vista de reservas"""
        self.show_frame("reservation")

    def login(self, email, password):
        user = self.hotel.iniciar_sesion(email, password)
        if user:
            self.current_user = user
            self.frames["dashboard"].actualizar_usuario(user)
            self.show_frame("dashboard")
        else:
            # Mostrar mensaje de error
            print("Error en login")

    def register(self, name, email, password):
        if self.hotel.registrar_usuario(name, email, password):
            self.show_login()
            print("Registro exitoso")
        else:
            # Mostrar mensaje de error
            print("Error en registro")

    def logout(self):
        self.current_user = None
        self.show_login()

    def make_reservation(self, room_id, check_in_date, check_out_date):
        """Realiza una reserva de habitación"""
        if self.current_user:
            reservation = self.hotel.realizar_reserva(
                room_id,
                self.current_user,
                check_in_date,
                check_out_date
            )
            if reservation:
                return True, "Reserva realizada con éxito"
            return False, "No se pudo realizar la reserva"
        return False, "Debe iniciar sesión para realizar una reserva"

    def get_available_rooms(self):
        """Obtiene la lista de habitaciones disponibles"""
        return [room for room in self.hotel.habitaciones if room.consultar_disponibilidad()]

    def run(self):
        """Inicia la aplicación"""
        self.root.mainloop()
        
    def get_user_reservations(self):
         if self.current_user:
            return [reserva for reserva in self.hotel.reservas.values() if reserva.usuario.correo_electronico == self.current_user.correo_electronico]
         return []

    def modify_reservation(self, reservation_id, new_check_in, new_check_out):
        if self.current_user:
            return self.hotel.modificar_reserva(reservation_id, new_check_in, new_check_out)
        return False

    def cancel_reservation(self, reservation_id):
        if self.current_user:
            return self.hotel.cancelar_reserva(reservation_id)
        return False 
    
    def show_history(self):
        self.frames["history"].update_reservations()
        self.show_frame("history")

    def get_user_reservations(self):
        if self.current_user:
            return self.hotel.obtener_reservas_usuario(self.current_user)
        return []   