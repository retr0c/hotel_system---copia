# views/history_view.py

import customtkinter as ctk
from tkcalendar import DateEntry
from datetime import datetime

class HistoryView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.popup_windows = []  # Para mantener referencia de las ventanas emergentes

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
        # Limpiar ventanas emergentes anteriores
        for window in self.popup_windows:
            if window.winfo_exists():
                window.destroy()
        self.popup_windows.clear()

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
                reserva_label.pack(side="left", padx=10, pady=10)

                # Frame para botones
                buttons_frame = ctk.CTkFrame(reserva_frame, fg_color="transparent")
                buttons_frame.pack(side="right", padx=10)

                # Botón Modificar
                modify_button = ctk.CTkButton(
                    buttons_frame,
                    text="Modificar",
                    command=lambda r=reserva: self.show_modify_dialog(r),
                    width=100,
                    height=30,
                    fg_color="#4CAF50",
                    text_color="white",
                    hover_color="#45a049"
                )
                modify_button.pack(side="left", padx=5)

                # Botón Cancelar
                cancel_button = ctk.CTkButton(
                    buttons_frame,
                    text="Cancelar",
                    command=lambda r=reserva: self.show_cancel_dialog(r),
                    width=100,
                    height=30,
                    fg_color="#f44336",
                    text_color="white",
                    hover_color="#da190b"
                )
                cancel_button.pack(side="left", padx=5)

    def show_modify_dialog(self, reserva):
        dialog = ctk.CTkToplevel(self)
        self.popup_windows.append(dialog)
        dialog.title("Modificar Reserva")
        dialog.geometry("400x300")
        dialog.transient(self)  # Hacer la ventana modal
        dialog.grab_set()  # Prevenir interacción con la ventana principal

        # Labels y entradas para las nuevas fechas
        ctk.CTkLabel(dialog, text="Nuevas fechas de reserva:", font=("Helvetica", 16)).pack(pady=10)
        
        dates_frame = ctk.CTkFrame(dialog)
        dates_frame.pack(pady=10)

        # Fecha de entrada
        ctk.CTkLabel(dates_frame, text="Fecha de llegada:").pack(pady=5)
        check_in_date = DateEntry(dates_frame, width=12, background='darkblue',
                                foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        check_in_date.pack(pady=5)
        check_in_date.set_date(reserva.fecha_entrada)

        # Fecha de salida
        ctk.CTkLabel(dates_frame, text="Fecha de salida:").pack(pady=5)
        check_out_date = DateEntry(dates_frame, width=12, background='darkblue',
                                 foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        check_out_date.pack(pady=5)
        check_out_date.set_date(reserva.fecha_salida)

        def confirm_modification():
            new_check_in = check_in_date.get_date()
            new_check_out = check_out_date.get_date()
            
            if self.controller.modify_reservation(reserva.numero_reserva, new_check_in, new_check_out):
                dialog.destroy()
                self.update_reservations()
                self.show_success_message("Reserva modificada exitosamente")
            else:
                self.show_error_message("No se pudo modificar la reserva")

        # Botones
        buttons_frame = ctk.CTkFrame(dialog)
        buttons_frame.pack(pady=20)

        ctk.CTkButton(
            buttons_frame,
            text="Confirmar",
            command=confirm_modification,
            fg_color="#4CAF50",
            text_color="white",
            hover_color="#45a049"
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            buttons_frame,
            text="Cancelar",
            command=dialog.destroy,
            fg_color="#f44336",
            text_color="white",
            hover_color="#da190b"
        ).pack(side="left", padx=5)

    def show_cancel_dialog(self, reserva):
        dialog = ctk.CTkToplevel(self)
        self.popup_windows.append(dialog)
        dialog.title("Cancelar Reserva")
        dialog.geometry("300x200")
        dialog.transient(self)
        dialog.grab_set()

        ctk.CTkLabel(
            dialog,
            text="¿Estás seguro que deseas\ncancelar esta reserva?",
            font=("Helvetica", 16)
        ).pack(pady=20)

        def confirm_cancellation():
            if self.controller.cancel_reservation(reserva.numero_reserva):
                dialog.destroy()
                self.update_reservations()
                self.show_success_message("Reserva cancelada exitosamente")
            else:
                self.show_error_message("No se pudo cancelar la reserva")

        buttons_frame = ctk.CTkFrame(dialog)
        buttons_frame.pack(pady=20)

        ctk.CTkButton(
            buttons_frame,
            text="Confirmar",
            command=confirm_cancellation,
            fg_color="#4CAF50",
            text_color="white",
            hover_color="#45a049"
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            buttons_frame,
            text="Cancelar",
            command=dialog.destroy,
            fg_color="#f44336",
            text_color="white",
            hover_color="#da190b"
        ).pack(side="left", padx=5)

    def show_success_message(self, message):
        dialog = ctk.CTkToplevel(self)
        self.popup_windows.append(dialog)
        dialog.title("Éxito")
        dialog.geometry("300x150")
        dialog.transient(self)
        dialog.grab_set()

        ctk.CTkLabel(dialog, text=message, font=("Helvetica", 14)).pack(pady=20)
        ctk.CTkButton(
            dialog,
            text="Aceptar",
            command=dialog.destroy,
            fg_color="#4CAF50",
            text_color="white",
            hover_color="#45a049"
        ).pack(pady=10)

    def show_error_message(self, message):
        dialog = ctk.CTkToplevel(self)
        self.popup_windows.append(dialog)
        dialog.title("Error")
        dialog.geometry("300x150")
        dialog.transient(self)
        dialog.grab_set()

        ctk.CTkLabel(dialog, text=message, font=("Helvetica", 14)).pack(pady=20)
        ctk.CTkButton(
            dialog,
            text="Aceptar",
            command=dialog.destroy,
            fg_color="#f44336",
            text_color="white",
            hover_color="#da190b"
        ).pack(pady=10)

    def back_to_dashboard(self):
        self.controller.show_frame("dashboard")

    def clear(self):
        for widget in self.reservations_frame.winfo_children():
            widget.destroy()
        
        # Limpiar ventanas emergentes
        for window in self.popup_windows:
            if window.winfo_exists():
                window.destroy()
        self.popup_windows.clear()