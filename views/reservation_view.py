# views/reservation_view.py
import customtkinter as ctk
from tkcalendar import DateEntry
from datetime import datetime

class ReservationView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.main_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#2b2b2b")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Hacer Reserva",
            font=("Helvetica", 24, "bold"),
            text_color="#FFD700"
        )
        self.title_label.pack(pady=20)
        
        # Catálogo de habitaciones
        self.room_frame = ctk.CTkFrame(self.main_frame, fg_color="#1f1f1f")
        self.room_frame.pack(fill="x", padx=20, pady=10)
        
        self.room_label = ctk.CTkLabel(
            self.room_frame,
            text="Seleccione una habitación:",
            font=("Helvetica", 16),
            text_color="#FFD700"
        )
        self.room_label.pack(pady=10)
        
        self.room_var = ctk.StringVar()
        self.room_menu = ctk.CTkOptionMenu(
            self.room_frame,
            variable=self.room_var,
            values=["Individual", "Doble", "Suite"],
            fg_color="#FFD700",
            text_color="black",
            button_color="#CFB53B",
            button_hover_color="#DAA520"
        )
        self.room_menu.pack(pady=10)
        
        # Fechas de llegada y salida
        self.dates_frame = ctk.CTkFrame(self.main_frame, fg_color="#1f1f1f")
        self.dates_frame.pack(fill="x", padx=20, pady=10)
        
        self.check_in_label = ctk.CTkLabel(
            self.dates_frame,
            text="Fecha de llegada:",
            font=("Helvetica", 16),
            text_color="#FFD700"
        )
        self.check_in_label.pack(pady=5)
        
        self.check_in_date = DateEntry(
            self.dates_frame,
            width=12,
            background='darkblue',
            foreground='white',
            borderwidth=2,
            date_pattern='dd/mm/yyyy'
        )
        self.check_in_date.pack(pady=5)
        
        self.check_out_label = ctk.CTkLabel(
            self.dates_frame,
            text="Fecha de salida:",
            font=("Helvetica", 16),
            text_color="#FFD700"
        )
        self.check_out_label.pack(pady=5)
        
        self.check_out_date = DateEntry(
            self.dates_frame,
            width=12,
            background='darkblue',
            foreground='white',
            borderwidth=2,
            date_pattern='dd/mm/yyyy'
        )
        self.check_out_date.pack(pady=5)
        
        # Botón de reserva
        self.reserve_button = ctk.CTkButton(
            self.main_frame,
            text="Reservar",
            command=self.make_reservation,
            width=200,
            height=40,
            fg_color="#FFD700",
            text_color="black",
            hover_color="#CFB53B"
        )
        self.reserve_button.pack(pady=20)
        
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
        self.back_button.pack(pady=10)

    def make_reservation(self):
        room_type = self.room_var.get()
        check_in = self.check_in_date.get_date()
        check_out = self.check_out_date.get_date()
        
        # Calcular el número de días
        days = (check_out - check_in).days
        
        # Obtener el precio de la habitación (esto debería venir del modelo)
        prices = {"Individual": 50, "Doble": 80, "Suite": 150}
        price_per_night = prices.get(room_type, 0)
        
        total_price = days * price_per_night
        
        # Mostrar mensaje de confirmación
        confirmation = ctk.CTkToplevel(self)
        confirmation.title("Confirmación de Reserva")
        confirmation.geometry("400x300")
        
        message = f"Reserva confirmada para {self.controller.current_user.nombre}\n\n"
        message += f"Habitación: {room_type}\n"
        message += f"Fecha de llegada: {check_in.strftime('%d/%m/%Y')}\n"
        message += f"Fecha de salida: {check_out.strftime('%d/%m/%Y')}\n"
        message += f"Número de noches: {days}\n"
        message += f"Precio total: ${total_price}"
        
        ctk.CTkLabel(
            confirmation,
            text=message,
            font=("Helvetica", 16),
            text_color="#FFD700",
            wraplength=350
        ).pack(pady=20, padx=20)
        
        ctk.CTkButton(
            confirmation,
            text="Aceptar",
            command=confirmation.destroy,
            fg_color="#FFD700",
            text_color="black",
            hover_color="#CFB53B"
        ).pack(pady=20)

    def back_to_dashboard(self):
        self.controller.show_frame("dashboard")

    def clear(self):
        self.room_var.set("Individual")
        self.check_in_date.set_date(datetime.now())
        self.check_out_date.set_date(datetime.now())