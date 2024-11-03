# views/history_view.py

import customtkinter as ctk

class HistoryView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.title_label = ctk.CTkLabel(
            self,
            text="Historial de Reservas",
            font=("Helvetica", 24, "bold"),
            text_color="#FFD700"
        )
        self.title_label.pack(pady=20)

        self.reservations_frame = ctk.CTkFrame(self)
        self.reservations_frame.pack(fill="both", expand=True, padx=20, pady=20)

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

    def update_reservations(self):
        for widget in self.reservations_frame.winfo_children():
            widget.destroy()

        reservas = self.controller.get_user_reservations()

        if not reservas:
            no_reservations_label = ctk.CTkLabel(
                self.reservations_frame,
                text="No tienes reservas aún.",
                font=("Helvetica", 16),
                text_color="#FFD700"
            )
            no_reservations_label.pack(pady=20)
        else:
            for reserva in reservas:
                reserva_frame = ctk.CTkFrame(self.reservations_frame)
                reserva_frame.pack(fill="x", padx=10, pady=5)

                info = f"Habitación: {reserva.habitacion.tipo}\n"
                info += f"Fecha de llegada: {reserva.fecha_entrada.strftime('%d/%m/%Y')}\n"
                info += f"Fecha de salida: {reserva.fecha_salida.strftime('%d/%m/%Y')}"

                reserva_label = ctk.CTkLabel(
                    reserva_frame,
                    text=info,
                    font=("Helvetica", 14),
                    text_color="#FFD700",
                    justify="left"
                )
                reserva_label.pack(padx=10, pady=10)

    def back_to_dashboard(self):
        self.controller.show_frame("dashboard")

    def clear(self):
        for widget in self.reservations_frame.winfo_children():
            widget.destroy()