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

        # Contenedor para las tarjetas de habitaciones
        self.rooms_container = ctk.CTkFrame(self)
        self.rooms_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Crear tarjetas para cada tipo de habitación
        self.create_room_cards()

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

    def create_room_cards(self):
        room_types = [
            {
                "tipo": "Individual",
                "precio": "50",
                "caracteristicas": [
                    "Cama individual",
                    "Wi-Fi gratuito",
                    "Baño privado",
                    "TV LCD",
                    "Aire acondicionado"
                ]
            },
            {
                "tipo": "Doble",
                "precio": "80",
                "caracteristicas": [
                    "Dos camas individuales",
                    "Wi-Fi gratuito",
                    "Baño privado",
                    "TV LCD",
                    "Aire acondicionado",
                    "Mini nevera"
                ]
            },
            {
                "tipo": "Suite",
                "precio": "150",
                "caracteristicas": [
                    "Cama king size",
                    "Wi-Fi gratuito",
                    "Baño de lujo con jacuzzi",
                    "TV LCD 55\"",
                    "Aire acondicionado",
                    "Mini bar",
                    "Sala de estar",
                    "Vista panorámica"
                ]
            }
        ]

        for room in room_types:
            # Crear marco para la tarjeta
            card = ctk.CTkFrame(self.rooms_container, fg_color="#1f1f1f")
            card.pack(fill="x", padx=20, pady=10)

            # Título de la habitación
            ctk.CTkLabel(
                card,
                text=f"Habitación {room['tipo']}",
                font=("Helvetica", 20, "bold"),
                text_color="#FFD700"
            ).pack(pady=10)

            # Precio
            ctk.CTkLabel(
                card,
                text=f"${room['precio']} por noche",
                font=("Helvetica", 16),
                text_color="#FFD700"
            ).pack(pady=5)

            # Características
            for caracteristica in room['caracteristicas']:
                ctk.CTkLabel(
                    card,
                    text=f"• {caracteristica}",
                    font=("Helvetica", 14),
                    text_color="white"
                ).pack(pady=2)

            # Botón de reservar
            ctk.CTkButton(
                card,
                text="Reservar",
                command=lambda t=room['tipo']: self.go_to_reservation(t),
                width=150,
                height=35,
                fg_color="#FFD700",
                text_color="black",
                hover_color="#CFB53B"
            ).pack(pady=15)

    def go_to_reservation(self, room_type):
        self.controller.frames["reservation"].room_var.set(room_type)
        self.controller.show_reservation()

    def back_to_dashboard(self):
        self.controller.show_frame("dashboard")

    def clear(self):
        pass