import streamlit as st
import pandas as pd
from modulos.config.conexion import get_connection

def mostrar():
    st.title("👥 Clientes")
    conn = get_connection()
    if conn is None:
        st.error("Error de conexión.")
        return

    # Mostrar registros existentes
    df = pd.read_sql("SELECT * FROM CLIENTES", conn)
    st.dataframe(df, use_container_width=True)

    # Formulario para insertar
    st.subheader("Agregar cliente")
    nombre = st.text_input("Nombre")
    email  = st.text_input("Email")
    telefono = st.text_input("Teléfono")

    if st.button("Guardar cliente"):
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO CLIENTES (nombre, email, telefono) VALUES (%s, %s, %s)",
            (nombre, email, telefono)
        )
        conn.commit()
        conn.close()
        st.success("Cliente guardado correctamente.")
        st.rerun()
