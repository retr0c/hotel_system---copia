import customtkinter as ctk
from datetime import datetime

class HistoryView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Frame principal
        self.main_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#2b2b2b")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Mis Reservas",
            font=("Helvetica", 24, "bold"),
            text_color="#FFD700"
        )
        self.title_label.pack(pady=20)
        
        # Frame para la lista de reservas
        self.reservations_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color="#1f1f1f",
            height=400
        )
        self.reservations_frame.pack(fill="x", padx=20, pady=10)
        
        # Botón de volver
        self.back_button = ctk.CTkButton(
            self.main_frame,
            text="Volver al Dashboard",
            command=self.back_to_dashboard,
            width=200,
            height=40,
            fg_color="transparent",
            border_width=2,
            border_color="#FFD700",
            text_color="#FFD700",
            hover_color="#2B2B2B"
        )
        self.back_button.pack(pady=20)

    def update_reservations(self):
        # Limpiar el frame de reservas
        for widget in self.reservations_frame.winfo_children():
            widget.destroy()
        
        # Obtener las reservas del usuario actual
        reservas = self.controller.get_user_reservations()
        
        if not reservas:
            ctk.CTkLabel(
                self.reservations_frame,
                text="No hay reservas registradas",
                font=("Helvetica", 16),
                text_color="#FFD700"
            ).pack(pady=20)
            return
        
        for reserva in reservas:
            # Frame para cada reserva
            reservation_card = ctk.CTkFrame(
                self.reservations_frame,
                fg_color="#2d2d2d",
                corner_radius=10
            )
            reservation_card.pack(fill="x", padx=10, pady=5)
            
            # Información de la reserva
            info_text = (
                f"Habitación: {reserva.tipo_habitacion}\n"
                f"Fecha entrada: {reserva.fecha_entrada}\n"
                f"Fecha salida: {reserva.fecha_salida}\n"
                f"Estado: {reserva.estado}"
            )
            
            ctk.CTkLabel(
                reservation_card,
                text=info_text,
                font=("Helvetica", 14),
                text_color="#FFD700",
                justify="left"
            ).pack(side="left", padx=10, pady=10)

    def back_to_dashboard(self):
        self.controller.show_frame("dashboard")