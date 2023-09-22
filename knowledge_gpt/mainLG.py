import streamlit as st
from io import BytesIO
import os
from PIL import Image


from components.sidebar import sidebar

from ui import (
    wrap_doc_in_html,
    is_query_valid,
    is_file_valid,
    is_open_ai_key_valid,
    display_file_read_error,
)

from core.caching import bootstrap_caching

from core.parsing import read_file
from core.chunking import chunk_file
from core.embedding import embed_files
from core.qa import query_folder
from core.utils import get_llm


EMBEDDING = "openai"
VECTOR_STORE = "faiss"
MODEL_LIST = ["gpt-3.5-turbo"]#, "gpt-4"]

# Uncomment to enable debug mode
# MODEL_LIST.insert(0, "debug")



st.set_page_config(page_title="Plan de Gobierno de Luisa González", page_icon="📖", layout="centered",initial_sidebar_state="expanded")
st.markdown(" ### 🤖PoliChatBot: Preguntas al Plan de Gobierno de Luisa González")


# Utilizar columnas para centrar la imagen
col1, col2, col3 = st.columns([4,8,1])

with col2:
    file_path_img= os.path.join(os.path.dirname(os.path.abspath(__file__)), "Luisa.jpg")
    image = Image.open(file_path_img)
    st.image(image)




# Enable caching for expensive functions
bootstrap_caching()

#sidebar()

openai_api_key = st.session_state.get("OPENAI_API_KEY")

# if not openai_api_key:
#     st.warning(
#         "Ingrese sus preguntas"
#     )

############################## Read PDF #######################################
# Define la ruta al archivo que deseas leer
file_path= os.path.join(os.path.dirname(os.path.abspath(__file__)), "Luisa.pdf")


# Asegúrate de que el archivo exista
if not os.path.exists(file_path):
    st.error(f"El archivo {file_path} no se encuentra en el directorio.")
    st.stop()

# Si el archivo existe, lee su contenido y crea un objeto BytesIO
with open(file_path, "rb") as f:
    file_content = f.read()
    uploaded_file = BytesIO(file_content)
    uploaded_file.name = file_path



# uploaded_file = st.file_uploader(
#     "Upload a pdf, docx, or txt file",
#     type=["pdf", "docx", "txt"],
#     help="Scanned documents are not supported yet!",
# )




#################################
#model: str = st.selectbox("Modelo", options=MODEL_LIST)  # type: ignore


if not uploaded_file:
    st.stop()

try:
    file = read_file(uploaded_file)
except Exception as e:
    display_file_read_error(e)

chunked_file = chunk_file(file, chunk_size=300, chunk_overlap=0)

if not is_file_valid(file):
    st.stop()


###############

openai_api_key = st.secrets["OPENAI_API_KEY"]

model="gpt-3.5-turbo"
if not is_open_ai_key_valid(openai_api_key, model):
    st.stop()


with st.spinner("Analizando el Plan de Gobierno⏳"):
    folder_index = embed_files(
        files=[chunked_file],
        embedding=EMBEDDING if model != "debug" else "debug",
        vector_store=VECTOR_STORE if model != "debug" else "debug",
        openai_api_key=openai_api_key,
    )

with st.form(key="qa_form"):
    query = st.text_area("Realice sus preguntas al Plan de Gobierno")
    submit = st.form_submit_button("Consulta")


st.markdown("Made by  [Jhon Glidden](https://jhonglidden.netlify.app) -  [LinkedIn](https://www.linkedin.com/in/jhon-glidden/) ")

with st.expander("Opciones avanzadas"):
    return_all_chunks = st.checkbox("Mostrar todos los chunks recuperados de la búsqueda vectorial")
    show_full_doc = st.checkbox("Mostrar el contenido analizado del documento")

if show_full_doc:
    with st.expander("Document"):
        # Hack to get around st.markdown rendering LaTeX
        st.markdown(f"<p>{wrap_doc_in_html(file.docs)}</p>", unsafe_allow_html=True)


if submit:
    if not is_query_valid(query):
        st.stop()

    # Output Columns
    answer_col, sources_col = st.columns(2)

    llm = get_llm(model=model, openai_api_key=openai_api_key, temperature=0)
    result = query_folder(
        folder_index=folder_index,
        query=query,
        return_all=return_all_chunks,
        llm=llm,
    )

    with answer_col:
        st.markdown("####  Respuesta")
        st.markdown(result.answer)

    with sources_col:
        st.markdown("#### Fuentes")
        for source in result.sources:
            st.markdown(source.page_content)
            st.markdown(source.metadata["source"])
            st.markdown("---")


