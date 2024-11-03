# -*- coding: utf-8 -*-

import customtkinter as ctk

class RegisterView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Frame del formulario con fondo dorado
        self.register_frame = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color="#2b2b2b"
        )
        self.register_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Título
        self.title_label = ctk.CTkLabel(
            self.register_frame,
            text="Luxury Hotel",
            font=("Helvetica", 24, "bold"),
            text_color="#FFD700"
        )
        self.title_label.pack(pady=20, padx=40)
        
        # Subtítulo
        self.subtitle_label = ctk.CTkLabel(
            self.register_frame,
            text="Registro de Usuario",
            font=("Helvetica", 16),
            text_color="#FFD700"
        )
        self.subtitle_label.pack(pady=(0, 20))
        
        # Campos de entrada
        self.name_entry = ctk.CTkEntry(
            self.register_frame,
            placeholder_text="Nombre completo",
            width=300,
            height=40,
            border_color="#FFD700",
            border_width=2
        )
        self.name_entry.pack(pady=10)
        
        self.email_entry = ctk.CTkEntry(
            self.register_frame,
            placeholder_text="Correo electrónico",
            width=300,
            height=40,
            border_color="#FFD700",
            border_width=2
        )
        self.email_entry.pack(pady=10)
        
        self.password_entry = ctk.CTkEntry(
            self.register_frame,
            placeholder_text="Contraseña",
            show="•",
            width=300,
            height=40,
            border_color="#FFD700",
            border_width=2
        )
        self.password_entry.pack(pady=10)
        
        # Botones
        self.register_button = ctk.CTkButton(
            self.register_frame,
            text="Registrarse",
            command=self.register,
            width=200,
            height=40,
            fg_color="#FFD700",
            text_color="black",
            hover_color="#CFB53B"
        )
        self.register_button.pack(pady=20)
        
        self.back_button = ctk.CTkButton(
            self.register_frame,
            text="Volver",
            command=self.back_to_login,
            width=200,
            height=40,
            fg_color="transparent",
            border_width=2,
            border_color="#FFD700",
            text_color="#FFD700",
            hover_color="#2B2B2B"
        )
        self.back_button.pack(pady=(0, 20))

    def register(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.controller.register(name, email, password)

    def back_to_login(self):
        self.controller.show_login()

    def clear(self):
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')