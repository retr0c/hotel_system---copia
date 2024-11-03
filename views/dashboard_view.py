# views/dashboard_view.py
import customtkinter as ctk
from datetime import datetime

class DashboardView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Frame principal
        self.main_frame = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color="#2b2b2b"
        )
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header con información del usuario
        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="#1f1f1f")
        self.header_frame.pack(fill="x", padx=20, pady=10)
        
        self.welcome_label = ctk.CTkLabel(
            self.header_frame,
            text="Bienvenido",
            font=("Helvetica", 24, "bold"),
            text_color="#FFD700"
        )
        self.welcome_label.pack(pady=10)
        
        # Contenedor para los botones principales
        self.buttons_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.buttons_frame.pack(pady=20)
        
        # Botones de funcionalidades
        self.ver_habitaciones_btn = ctk.CTkButton(
            self.buttons_frame,
            text="Ver Habitaciones",
            command=self.ver_habitaciones,
            width=200,
            height=40,
            fg_color="#FFD700",
            text_color="black",
            hover_color="#CFB53B"
        )
        self.ver_habitaciones_btn.pack(pady=10)
        
        self.hacer_reserva_btn = ctk.CTkButton(
            self.buttons_frame,
            text="Hacer Reserva",
            command=self.hacer_reserva,
            width=200,
            height=40,
            fg_color="#FFD700",
            text_color="black",
            hover_color="#CFB53B"
        )
        self.hacer_reserva_btn.pack(pady=10)
        
        self.mis_reservas_btn = ctk.CTkButton(
            self.buttons_frame,
            text="Mis Reservas",
            command=self.ver_mis_reservas,
            width=200,
            height=40,
            fg_color="#FFD700",
            text_color="black",
            hover_color="#CFB53B"
        )
        self.mis_reservas_btn.pack(pady=10)
        
        # Botón de cerrar sesión
        self.logout_btn = ctk.CTkButton(
            self.buttons_frame,
            text="Cerrar Sesión",
            command=self.logout,
            width=200,
            height=40,
            fg_color="transparent",
            border_width=2,
            border_color="#FFD700",
            text_color="#FFD700",
            hover_color="#2B2B2B"
        )
        self.logout_btn.pack(pady=20)

    def actualizar_usuario(self, usuario):
        self.welcome_label.configure(text=f"Bienvenido, {usuario.nombre}")

    def ver_habitaciones(self):
        # Por implementar
        print("Ver habitaciones")
        
    def hacer_reserva(self):
         self.controller.show_reservation()
        
    def ver_mis_reservas(self):
        self.controller.show_frame("history")
        
    def logout(self):
        self.controller.logout()

    def clear(self):
        pass