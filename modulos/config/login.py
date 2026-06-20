import streamlit as st
from modulos.config.conexion import get_connection

def login():
    st.title("🔐 Iniciar sesión")
    usuario = st.text_input("Usuario")
    contrasena = st.text_input("Contraseña", type="password")

    if st.button("Entrar"):
        conn = get_connection()
        if conn is None:
            st.error("No se pudo conectar a la base de datos.")
            return
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM USUARIO WHERE usuario=%s AND contrasena=%s",
            (usuario, contrasena)
        )
        user = cursor.fetchone()
        conn.close()
        if user:
            st.session_state["autenticado"] = True
            st.session_state["usuario"] = usuario
            st.rerun()
        else:
            st.error("Usuario o contraseña incorrectos.")
