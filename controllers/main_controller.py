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
from views.rooms_view import RoomView
from views.admin_view import AdminView


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
        for F in (LoginView, RegisterView, DashboardView, ReservationView, HistoryView, RoomView, AdminView):
            frame = F(self.container, self)
            self.frames[F.__name__.lower().replace("view", "")] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
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
        
    def show_rooms(self):
        """Muestra la vista de habitaciones"""
        self.show_frame("room")    

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
            # Buscar habitación disponible del tipo solicitado
            habitacion = None
            for h in self.hotel.habitaciones:
                if h.tipo == room_type and self.hotel.verificar_disponibilidad(h.id_habitacion, check_in, check_out):
                    habitacion = h
                    break

            if habitacion:
                reserva = self.hotel.realizar_reserva(
                    habitacion.id_habitacion,
                    self.current_user,
                    check_in,
                    check_out
                )
                return True if reserva else False
            return False
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
        self.debug_reservations()
        self.frames["history"].update_reservations()
        self.show_frame("history")
        
    def debug_reservations(self):
        """Método de depuración para verificar las reservas"""
        print("\nDebug Reservations:")
        print(f"Usuario actual: {self.current_user.nombre if self.current_user else 'None'}")
        reservas = self.get_user_reservations()
        print(f"Número de reservas: {len(reservas)}")
        for reserva in reservas:
            print(f"Reserva: {reserva.habitacion.tipo} - {reserva.fecha_entrada} a {reserva.fecha_salida}")    

    def modify_reservation(self, reservation_id, new_check_in, new_check_out):
        """Modifica una reserva existente"""
        return self.hotel.modificar_reserva(reservation_id, new_check_in, new_check_out)

    def cancel_reservation(self, reservation_id):
        """Cancela una reserva existente"""
        return self.hotel.cancelar_reserva(reservation_id)
    
    def show_dashboard(self):
        self.show_frame("dashboard")
        
    def update_room_prices(self):
        """Actualiza las vistas después de un cambio en los precios"""
        # Actualizar la vista de habitaciones si está visible
        if "room" in self.frames:
            self.frames["room"].show_rooms()
            
        
        # Actualizar la vista de reservas si existe
        
        if "reservation" in self.frames:
            if hasattr(self.frames["reservation"], "update_prices"):
                self.frames["reservation"].update_prices()

    def show_rooms(self):
        """Muestra la vista de habitaciones"""
        self.show_frame("room")
        # Asegurarse de que los precios estén actualizados
        self.frames["room"].show_rooms()    
