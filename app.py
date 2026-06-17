import streamlit as st

# 1. Configuración inicial de la página
st.set_page_config(page_title="Login App", page_icon="🔐", layout="centered")

# 2. Inicializar el estado de la sesión si no existe
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Base de datos simulada (En producción, usa contraseñas inactivas/hasheadas y bases de datos reales)
USER_CREDENTIALS = {
    "admin": "deepseek2026",
    "gerardo": "python123"
}

# 3. Función para validar las credenciales
def login_user(user, password):
    if user in USER_CREDENTIALS and USER_CREDENTIALS[user] == password:
        st.session_state.authenticated = True
        st.session_state.username = user
        st.rerun()  # Recarga la app para mostrar el contenido privado
    else:
        st.error("Usuario o contraseña incorrectos")

# 4. Función para cerrar sesión
def logout_user():
    st.session_state.authenticated = False
    st.session_state.username = ""
    st.rerun()

# --- VISTAS DE LA APLICACIÓN ---

# Vista de Login (Si el usuario NO está autenticado)
if not st.session_state.authenticated:
    st.title("🔐 Iniciar Sesión")
    st.write("Introduce tus credenciales para acceder al panel de control de Chat-PDF.")
    
    with st.form("login_form"):
        username_input = st.text_input("Usuario", placeholder="Ej: gerardo")
        password_input = st.text_input("Contraseña", type="password", placeholder="••••••••")
        submit_button = st.form_submit_button("Ingresar")
        
        if submit_button:
            if username_input and password_input:
                login_user(username_input, password_input)
            else:
                st.warning("Por favor, rellena todos los campos.")

# Vista Privada (Si el usuario SÍ está autenticado)
else:
    # Barra lateral con información del usuario y botón de salida
    with st.sidebar:
        st.success(f"Conectado como: **{st.session_state.username}**")
        if st.button("Cerrar Sesión", type="primary"):
            logout_user()
            
    # Contenido principal de tu aplicación
    st.title("🚀 Bienvenido al Panel Principal")
    st.write(f"Hola {st.session_state.username.capitalize()}, has ingresado correctamente.")
    
    # Aquí puedes meter la lógica de tu chat-pdf
    st.info("El sistema está listo. Sube tus archivos PDF desde el menú correspondiente.")
