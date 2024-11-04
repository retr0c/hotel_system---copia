# views/rooms_view.py
import customtkinter as ctk

class RoomsView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Título
        self.title_label = ctk.CTkLabel(
            self,
            text="Catálogo de Habitaciones",
            font=("Helvetica", 24, "bold"),
            text_color="#FFD700"
        )
        self.title_label.pack(pady=20)

        # Contenedor para las habitaciones
        self.rooms_frame = ctk.CTkFrame(self)
        self.rooms_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Mostrar habitaciones
        self.display_rooms()

        # Botón de volver
        self.back_button = ctk.CTkButton(
            self,
            text="Volver al Dashboard",
            command=self.back_to_dashboard,
            width=200,
            height=40,
            fg_color="#FFD700",
            text_color="black",
            hover_color="#CFB53B"
        )
        self.back_button.pack(pady=20)

    def display_rooms(self):
        room_types = {
            "Individual": {
                "precio": 50,
                "caracteristicas": "Cama individual, Wi-Fi, TV, Baño privado",
                "imagen": "🛏️"  # Emoji como placeholder
            },
            "Doble": {
                "precio": 80,
                "caracteristicas": "Dos camas, TV, Wi-Fi, Baño privado, Mini bar",
                "imagen": "🛏️🛏️"
            },
            "Suite": {
                "precio": 150,
                "caracteristicas": "Cama king, Jacuzzi, Wi-Fi, TV 4K, Sala de estar, Mini bar",
                "imagen": "👑"
            }
        }

        for room_type, details in room_types.items():
            room_frame = ctk.CTkFrame(self.rooms_frame, fg_color="#1f1f1f")
            room_frame.pack(fill="x", padx=10, pady=5)

            # Título de la habitación
            title_frame = ctk.CTkFrame(room_frame, fg_color="transparent")
            title_frame.pack(fill="x", padx=10, pady=5)

            ctk.CTkLabel(
                title_frame,
                text=f"{details['imagen']} {room_type}",
                font=("Helvetica", 18, "bold"),
                text_color="#FFD700"
            ).pack(side="left", padx=5)

            ctk.CTkLabel(
                title_frame,
                text=f"${details['precio']}/noche",
                font=("Helvetica", 16),
                text_color="#FFD700"
            ).pack(side="right", padx=5)

            # Características
            ctk.CTkLabel(
                room_frame,
                text=f"Características: {details['caracteristicas']}",
                font=("Helvetica", 14),
                text_color="white",
                wraplength=600,
                justify="left"
            ).pack(padx=10, pady=5)

            # Estado de disponibilidad
            disponibles = self.get_available_count(room_type)
            ctk.CTkLabel(
                room_frame,
                text=f"Habitaciones disponibles: {disponibles}",
                font=("Helvetica", 14),
                text_color="#32CD32" if disponibles > 0 else "#FF0000"
            ).pack(padx=10, pady=5)

    def get_available_count(self, room_type):
        return sum(1 for room in self.controller.hotel.habitaciones 
                  if room.tipo == room_type and room.consultar_disponibilidad())

    def back_to_dashboard(self):
        self.controller.show_frame("dashboard")

    def clear(self):
        for widget in self.rooms_frame.winfo_children():
            widget.destroy()