# flake8: noqa
from langchain.prompts import PromptTemplate

template = """
Basándote en el siguiente formato de ejemplo:
---------
PREGUNTA: ¿Qué decisiones se van a tomar sobre X?
=========
Contenido: Información relevante sobre lo que se hará o acciones que se realizarán relacionadas con X.
FUENTES: Número de referencia.
=========
RESPUESTA FINAL:

---------

Por favor, crea una respuesta final a las preguntas dadas utilizando los fragmentos de documentos proporcionados. Estas preguntas pueden referirse tanto a información general como a acciones o decisiones específicas relacionadas con el tema.

SIEMPRE en todas las respuestas incluye una sección "FUENTES" en tu respuesta citando solo el conjunto mínimo de fuentes necesarias para responder a la pregunta. Si no puedes responder a la pregunta debido a falta de información, simplemente indica que no tienes suficiente información y deja la sección FUENTES vacía.

Utiliza solo los documentos proporcionados y no intente fabricar una respuesta. 

Utiliza este formato y responde a la siguiente pregunta utilizando los fragmentos de documentos proporcionados:
PREGUNTA: {question}
=========
{summaries}
=========
RESPUESTA FINAL:
"""


STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
