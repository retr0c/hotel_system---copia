# -*- coding: utf-8 -*-
import customtkinter as ctk
from views.login_view import LoginView
from views.register_view import RegisterView
from views.dashboard_view import DashboardView
from views.reservation_view import ReservationView
from views.history_view import HistoryView
from models.hotel import Hotel
from models.usuario import Usuario
from models.reserva import Reserva

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
        for F in (LoginView, RegisterView, DashboardView, ReservationView, HistoryView):
            frame = F(self.container, self)
            self.frames[F.__name__.lower().replace("view", "")] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.setup_views()
        
        self.show_login()

    def setup_views(self):
        # Crear y configurar las vistas (frames)
        self.frames["login"] = LoginView(self.container, self)
        self.frames["register"] = RegisterView(self.container, self)
        self.frames["dashboard"] = DashboardView(self.container, self)
        self.frames["reservation"] = ReservationView(self.container, self)
        self.frames["history"] = HistoryView(self.container, self)

        # Posicionar las vistas en el contenedor
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        """Muestra el frame especificado"""
        frame = self.frames[page_name]
        frame.tkraise()
        
        if hasattr(frame, 'clear'):
            frame.clear()  # Limpia los campos si el método existe
            
        if page_name == "history" and hasattr(frame, 'update_reservations'):
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
            print("Error en login")

    def register(self, name, email, password):
        if self.hotel.registrar_usuario(name, email, password):
            self.show_login()
            print("Registro exitoso")
        else:
            print("Error en registro")

    def logout(self):
        self.current_user = None
        self.show_login()

    def make_reservation(self, room_type, check_in, check_out):
        if self.current_user:
            reserva = Reserva(self.current_user, room_type, check_in, check_out)
            self.hotel.hacer_reserva(reserva)
            return True
        return False

    def get_available_rooms(self):
        """Obtiene la lista de habitaciones disponibles"""
        return [room for room in self.hotel.habitaciones if room.consultar_disponibilidad()]

    def run(self):
        """Inicia la aplicación"""
        self.root.mainloop()
        
    def get_user_reservations(self):
        """Obtiene las reservas del usuario actual"""
        if self.current_user:
            return self.hotel.obtener_reservas_usuario(self.current_user)
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
