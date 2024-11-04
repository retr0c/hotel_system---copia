# views/admin_view.py
import customtkinter as ctk

class AdminView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Título
        self.title_label = ctk.CTkLabel(
            self,
            text="Panel de Administración",
            font=("Helvetica", 24, "bold"),
            text_color="#FFD700"
        )
        self.title_label.pack(pady=20)
        
        # Frame para cambio de precios
        self.price_frame = ctk.CTkFrame(self)
        self.price_frame.pack(pady=20, padx=20, fill="x")
        
        # Selector de tipo de habitación
        self.room_type_var = ctk.StringVar(value="Individual")
        self.room_type_label = ctk.CTkLabel(
            self.price_frame,
            text="Tipo de Habitación:",
            font=("Helvetica", 14)
        )
        self.room_type_label.pack(pady=5)
        
        self.room_type_menu = ctk.CTkOptionMenu(
            self.price_frame,
            values=["Individual", "Doble", "Suite"],
            variable=self.room_type_var
        )
        self.room_type_menu.pack(pady=5)
        
        # Entry para nuevo precio
        self.price_label = ctk.CTkLabel(
            self.price_frame,
            text="Nuevo Precio ($):",
            font=("Helvetica", 14)
        )
        self.price_label.pack(pady=5)
        
        self.price_entry = ctk.CTkEntry(
            self.price_frame,
            placeholder_text="Ingrese el nuevo precio"
        )
        self.price_entry.pack(pady=5)
        
        # Botón para actualizar precio
        self.update_button = ctk.CTkButton(
            self.price_frame,
            text="Actualizar Precio",
            command=self.update_price,
            fg_color="#FFD700",
            text_color="black",
            hover_color="#CFB53B"
        )
        self.update_button.pack(pady=10)

        # Frame para el enlace de Telegram
        self.telegram_frame = ctk.CTkFrame(self)
        self.telegram_frame.pack(pady=20, padx=20, fill="x")
        
        # Enlace de Telegram
        self.telegram_label = ctk.CTkLabel(
            self.telegram_frame,
            text="Chat con nuestro bot de Telegram",
            font=("Helvetica", 16, "bold"),
            text_color="#FFD700"
        )
        self.telegram_label.pack(pady=5)
        
        self.telegram_link = ctk.CTkLabel(
            self.telegram_frame,
            text="t.me/TuBotDeTelegram",  # Reemplaza con tu link real
            font=("Helvetica", 14, "underline"),
            text_color="#4169E1",
            cursor="hand2"
        )
        self.telegram_link.pack(pady=5)
        
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

    def update_price(self):
        try:
            nuevo_precio = float(self.price_entry.get())
            tipo_habitacion = self.room_type_var.get()
            
            if nuevo_precio <= 0:
                self.show_message("Error", "El precio debe ser mayor que 0")
                return
                
            if self.controller.hotel.cambiar_precio_habitacion(tipo_habitacion, nuevo_precio):
                # Actualizar la vista de habitaciones
                if "room" in self.controller.frames:
                    self.controller.frames["room"].show_rooms()
                self.show_message("Éxito", "Precio actualizado correctamente")
                self.price_entry.delete(0, 'end')
            else:
                self.show_message("Error", "No se pudo actualizar el precio")
        except ValueError:
            self.show_message("Error", "Por favor ingrese un precio válido")

    def show_message(self, title, message):
        dialog = ctk.CTkToplevel(self)
        dialog.title(title)
        dialog.geometry("300x150")
        dialog.transient(self)
        dialog.grab_set()
        
        ctk.CTkLabel(dialog, text=message, font=("Helvetica", 14)).pack(pady=20)
        ctk.CTkButton(
            dialog,
            text="Aceptar",
            command=dialog.destroy,
            fg_color="#FFD700",
            text_color="black",
            hover_color="#CFB53B"
        ).pack(pady=10)

    def back_to_dashboard(self):
        self.controller.show_frame("dashboard")