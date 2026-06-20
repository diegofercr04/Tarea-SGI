import streamlit as st
import pandas as pd
from modulos.config.conexion import get_connection

def mostrar():
    st.title("🧾 Ventas")
    conn = get_connection()
    if conn is None:
        st.error("Error de conexión.")
        return

    # Mostrar ventas con nombres de cliente y producto
    query = """
        SELECT v.id, c.nombre AS cliente,
               p.nombre AS producto, v.cantidad, v.fecha
        FROM VENTAS v
        JOIN CLIENTES c ON v.id_cliente = c.id
        JOIN PRODUCTOS p ON v.id_producto = p.id
        ORDER BY v.fecha DESC
    """
    df = pd.read_sql(query, conn)
    st.dataframe(df, use_container_width=True)

    # Formulario para insertar
    st.subheader("Registrar venta")
    clientes  = pd.read_sql("SELECT id, nombre FROM CLIENTES", conn)
    productos = pd.read_sql("SELECT id, nombre FROM PRODUCTOS", conn)

    id_cliente  = st.selectbox("Cliente", clientes["id"],
                    format_func=lambda x: clientes[clientes["id"]==x]["nombre"].values[0])
    id_producto = st.selectbox("Producto", productos["id"],
                    format_func=lambda x: productos[productos["id"]==x]["nombre"].values[0])
    cantidad    = st.number_input("Cantidad", min_value=1, step=1)

    if st.button("Registrar venta"):
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO VENTAS (id_cliente, id_producto, cantidad) VALUES (%s, %s, %s)",
            (int(id_cliente), int(id_producto), int(cantidad))
        )
        conn.commit()
        conn.close()
        st.success("Venta registrada.")
        st.rerun()
