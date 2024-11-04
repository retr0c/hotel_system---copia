# views/room_view.py
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

    def show_rooms(self):
        # Limpiar el frame de habitaciones
        for widget in self.rooms_frame.winfo_children():
            widget.destroy()
            
        # Obtener todas las habitaciones
        habitaciones = self.controller.hotel.habitaciones
        
        # Agrupar habitaciones por tipo
        tipos = {}
        for hab in habitaciones:
            if hab.tipo not in tipos:
                tipos[hab.tipo] = []
            tipos[hab.tipo].append(hab)
            
        # Mostrar habitaciones por tipo
        for tipo, habs in tipos.items():
            # Frame para el tipo de habitación
            tipo_frame = ctk.CTkFrame(self.rooms_frame)
            tipo_frame.pack(fill="x", padx=10, pady=5)
            
            # Título del tipo
            ctk.CTkLabel(
                tipo_frame,
                text=f"Habitación {tipo}",
                font=("Helvetica", 18, "bold"),
                text_color="#FFD700"
            ).pack(pady=10)
            
            # Detalles de la habitación
            hab = habs[0]  # Tomamos la primera habitación del tipo como referencia
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

    def back_to_dashboard(self):
        self.controller.show_frame("dashboard")