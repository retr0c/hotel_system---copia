# En rooms_view.py, actualizar la clase RoomView
import customtkinter as ctk


class RoomView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Título
        self.title_label = ctk.CTkLabel(
            self,
            text="Habitaciones Disponibles",
            font=("Helvetica", 24, "bold"),
            text_color="#FFD700"
        )
        self.title_label.pack(pady=20)
        
        # Contenedor para las habitaciones
        self.rooms_frame = ctk.CTkFrame(self)
        self.rooms_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Mostrar habitaciones
        self.show_rooms()
        
        # Frame para botones
        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.pack(pady=10)
        
        # Botón de volver
        self.back_button = ctk.CTkButton(
            self.buttons_frame,
            text="Volver al Dashboard",
            command=self.back_to_dashboard,
            width=200,
            height=40,
            fg_color="#FFD700",
            text_color="black",
            hover_color="#CFB53B"
        )
        self.back_button.pack(side="left", padx=5)

        # Botón de Telegram
        self.telegram_button = ctk.CTkButton(
            self.buttons_frame,
            text="Chatear con nuestro Bot",
            command=self.open_telegram,
            width=200,
            height=40,
            fg_color="#0088cc",  # Color de Telegram
            text_color="white",
            hover_color="#006699"
        )
        self.telegram_button.pack(side="left", padx=5)

    def show_rooms(self):
        for widget in self.rooms_frame.winfo_children():
            widget.destroy()
            
        habitaciones = self.controller.hotel.habitaciones
        tipos = {}
        for hab in habitaciones:
            if hab.tipo not in tipos:
                tipos[hab.tipo] = []
            tipos[hab.tipo].append(hab)
            
        for tipo, habs in tipos.items():
            tipo_frame = ctk.CTkFrame(self.rooms_frame)
            tipo_frame.pack(fill="x", padx=10, pady=5)
            
            # Frame para título y botón de edición
            header_frame = ctk.CTkFrame(tipo_frame, fg_color="transparent")
            header_frame.pack(fill="x", padx=10, pady=5)
            
            # Título del tipo
            ctk.CTkLabel(
                header_frame,
                text=f"Habitación {tipo}",
                font=("Helvetica", 18, "bold"),
                text_color="#FFD700"
            ).pack(side="left", pady=10)
            
            # Botón de editar precio solo para admin
            if self.controller.current_user and self.controller.current_user.es_admin:
                edit_button = ctk.CTkButton(
                    header_frame,
                    text="Editar Precio",
                    command=lambda t=tipo, p=habs[0].precio: self.show_price_dialog(t, p),
                    width=100,
                    height=30,
                    fg_color="#4CAF50",
                    text_color="white",
                    hover_color="#45a049"
                )
                edit_button.pack(side="right", padx=5)
            
            hab = habs[0]
            detalles = f"Precio por noche: ${hab.precio}\n"
            detalles += f"Características:\n{hab.caracteristicas}\n"
            detalles += f"Habitaciones disponibles: {sum(1 for h in habs if h.consultar_disponibilidad())}/{len(habs)}"
            
            ctk.CTkLabel(
                tipo_frame,
                text=detalles,
                font=("Helvetica", 14),
                text_color="#FFD700",
                justify="left"
            ).pack(padx=10, pady=10)

    def show_price_dialog(self, tipo_habitacion, precio_actual):
        dialog = ctk.CTkToplevel(self)
        dialog.title(f"Editar Precio - {tipo_habitacion}")
        dialog.geometry("300x200")
        dialog.transient(self)
        dialog.grab_set()

        ctk.CTkLabel(
            dialog,
            text=f"Precio actual: ${precio_actual}",
            font=("Helvetica", 14)
        ).pack(pady=10)

        precio_var = ctk.StringVar(value=str(precio_actual))
        precio_entry = ctk.CTkEntry(
            dialog,
            textvariable=precio_var,
            width=200
        )
        precio_entry.pack(pady=10)

        def confirmar_cambio():
            try:
                nuevo_precio = float(precio_var.get())
                if nuevo_precio <= 0:
                    self.show_error_message("El precio debe ser mayor que 0")
                    return
                
                if self.controller.hotel.cambiar_precio_habitacion(tipo_habitacion, nuevo_precio):
                    dialog.destroy()
                    self.show_rooms()
                    self.show_success_message("Precio actualizado correctamente")
                else:
                    self.show_error_message("No se pudo actualizar el precio")
            except ValueError:
                self.show_error_message("Por favor ingrese un precio válido")

        ctk.CTkButton(
            dialog,
            text="Confirmar",
            command=confirmar_cambio,
            fg_color="#4CAF50",
            text_color="white",
            hover_color="#45a049"
        ).pack(pady=10)

    def show_success_message(self, message):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Éxito")
        dialog.geometry("300x150")
        dialog.transient(self)
        dialog.grab_set()

        ctk.CTkLabel(
            dialog,
            text=message,
            font=("Helvetica", 14)
        ).pack(pady=20)

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
        dialog.title("Error")
        dialog.geometry("300x150")
        dialog.transient(self)
        dialog.grab_set()

        ctk.CTkLabel(
            dialog,
            text=message,
            font=("Helvetica", 14)
        ).pack(pady=20)

        ctk.CTkButton(
            dialog,
            text="Aceptar",
            command=dialog.destroy,
            fg_color="#f44336",
            text_color="white",
            hover_color="#da190b"
        ).pack(pady=10)

    def open_telegram(self):
        # Aquí puedes poner el link de tu bot de Telegram
        import webbrowser
        webbrowser.open("https://t.me/tu_bot_de_telegram")  # Reemplaza con tu link

    def back_to_dashboard(self):
        self.controller.show_frame("dashboard")