def test_imports():
    try:
        from models.usuario import Usuario
        from models.habitacion import Habitacion
        from models.reserva import Reserva
        from models.hotel import Hotel
        from views.login_view import LoginView
        from views.register_view import RegisterView
        from controllers.main_controller import MainController
        print("✅ Todas las importaciones funcionan correctamente")
    except Exception as e:
        print(f"❌ Error en las importaciones: {str(e)}")

if __name__ == "__main__":
    test_imports()