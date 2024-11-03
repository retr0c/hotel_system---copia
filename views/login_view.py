# -*- coding: utf-8 -*-

import customtkinter as ctk

import customtkinter as ctk

class LoginView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Configuración del tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        # Frame del formulario con fondo dorado
        self.login_frame = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color="#2b2b2b"  # Color de fondo oscuro
        )
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Título
        self.title_label = ctk.CTkLabel(
            self.login_frame,
            text="Luxury Hotel",
            font=("Helvetica", 24, "bold"),
            text_color="#FFD700"  # Color dorado
        )
        self.title_label.pack(pady=20, padx=40)
        
        # Subtítulo
        self.subtitle_label = ctk.CTkLabel(
            self.login_frame,
            text="Bienvenido",
            font=("Helvetica", 16),
            text_color="#FFD700"
        )
        self.subtitle_label.pack(pady=(0, 20))
        
        # Campos de entrada
        self.email_entry = ctk.CTkEntry(
            self.login_frame,
            placeholder_text="Correo electrónico",
            width=300,
            height=40,
            border_color="#FFD700",
            border_width=2
        )
        self.email_entry.pack(pady=10, padx=40)
        
        self.password_entry = ctk.CTkEntry(
            self.login_frame,
            placeholder_text="Contraseña",
            show="•",
            width=300,
            height=40,
            border_color="#FFD700",
            border_width=2
        )
        self.password_entry.pack(pady=10)
        
        # Botones
        self.login_button = ctk.CTkButton(
            self.login_frame,
            text="Iniciar Sesión",
            command=self.login,
            width=200,
            height=40,
            fg_color="#FFD700",
            text_color="black",
            hover_color="#CFB53B"
        )
        self.login_button.pack(pady=20)
        
        self.register_button = ctk.CTkButton(
            self.login_frame,
            text="Registrarse",
            command=self.show_register,
            width=200,
            height=40,
            fg_color="transparent",
            border_width=2,
            border_color="#FFD700",
            text_color="#FFD700",
            hover_color="#2B2B2B"
        )
        self.register_button.pack(pady=(0, 20))

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.controller.login(email, password)

    def show_register(self):
        self.controller.show_register()

    def clear(self):
        self.email_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')