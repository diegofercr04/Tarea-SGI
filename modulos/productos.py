import streamlit as st
import pandas as pd
from modulos.config.conexion import get_connection

def mostrar():
    st.title("📦 Productos")
    conn = get_connection()
    if conn is None:
        st.error("Error de conexión.")
        return

    # Mostrar registros existentes
    df = pd.read_sql("SELECT * FROM PRODUCTOS", conn)
    st.dataframe(df, use_container_width=True)

    # Formulario para insertar
    st.subheader("Agregar producto")
    nombre = st.text_input("Nombre del producto")
    precio = st.number_input("Precio", min_value=0.0, format="%.2f")
    stock  = st.number_input("Stock disponible", min_value=0, step=1)

    if st.button("Guardar producto"):
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO PRODUCTOS (nombre, precio, stock) VALUES (%s, %s, %s)",
            (nombre, precio, stock)
        )
        conn.commit()
        conn.close()
        st.success("Producto guardado correctamente.")
        st.rerun()
