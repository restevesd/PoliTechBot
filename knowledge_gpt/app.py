# import streamlit as st

# # Funciones para cada página:
# def show_home():
#     st.title("Página de Inicio")
#     st.write("Bienvenido a la página de inicio!")

# def show_page1():
#     st.title("Página 1")
#     st.write("Estás en la página 1.")

# def show_page2():
#     st.title("Página 2")
#     st.write("Estás en la página 2.")

# # Navegación lateral:
# choice = st.sidebar.radio("Elije una página:", ["Inicio", "Página 1", "Página 2"])

# # Lógica para mostrar la página seleccionada:
# if choice == "Inicio":
#     show_home()
# elif choice == "Página 1":
#     show_page1()
# elif choice == "Página 2":
#     show_page2()





from st_pages import Page, Section, add_page_title, show_pages
import st_pages
import os
import streamlit as st
st.markdown("""
            ## 🤖PoliChatBot: ¡Descubre, Compara y Decide!

            __¿Sabias qué?__ De acuerdo con el Artículo 278 de nuestra Constitución:

            > Artículo 278.- El programa presentado por el candidato ganador a la Presidencia de la República será de obligatorio cumplimiento y servirá como instrumento de fiscalización ciudadana.
            
            Por lo tanto, no te dejes engañar con propuestas demagógicas y sin sentido. Realiza preguntas como:

            ¿Qué propone para mejorar el sistema de salud? 
            
            ¿Cuál es su plan para la educación? 

            ¿Cómo combatirá la delincuencia? 


            ¡Descubre esto y más ahora!

            Funciones Destacadas:

            - 🔍 Búsqueda Instantánea: Encuentra propuestas específicas en segundos.
            - 🔄 Comparador: Sitúa lado a lado las ideas de tus candidatos favoritos.
            """)
st.markdown("Made by   [Jhon Glidden](https://jhonglidden.netlify.app)")


show_pages(
    [
        Page(os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.py"), "Inicio", "🏠"),
        Page(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mainLG.py"), "Luisa González", "👩‍💼"),
        Page(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mainDN.py"), "Daniel Noboa", "👨‍💼"),
       
       
    ]
)

#add_page_title()  # Optional method to add title and icon to current page