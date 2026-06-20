import streamlit as st
from modulos import clientes, productos, ventas

def mostrar_menu():
    st.sidebar.title("📋 Menú principal")
    st.sidebar.write(f"👤 Usuario: {st.session_state['usuario']}")
    st.sidebar.divider()

    opcion = st.sidebar.radio(
        "Secciones",
        ["Clientes", "Productos", "Ventas"]
    )

    if st.sidebar.button("🚪 Cerrar sesión"):
        st.session_state["autenticado"] = False
        st.rerun()

    if opcion == "Clientes":
        clientes.mostrar()
    elif opcion == "Productos":
        productos.mostrar()
    elif opcion == "Ventas":
        ventas.mostrar()
