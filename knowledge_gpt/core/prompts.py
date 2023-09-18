# flake8: noqa
from langchain.prompts import PromptTemplate

template = """
Basándote en el siguiente formato de ejemplo:
---------
PREGUNTA: ¿Cuál es el propósito de X?
=========
Contenido: Información relevante sobre X.
FUENTES: Número de referencia.
=========
RESPUESTA FINAL:

---------

Por favor, cree una respuesta final a las preguntas dadas utilizando los fragmentos de documentos proporcionados (dados en ningún orden específico) como fuentes. SIEMPRE incluya una sección "FUENTES" en su respuesta citando solo el conjunto mínimo de fuentes necesarias para responder a la pregunta. Si no puede responder a la pregunta, simplemente indique que no tiene suficiente información para responder a la pregunta y deje la sección FUENTES vacía. Utilice solo los documentos proporcionados y no intente fabricar una respuesta. Utiliza este formato y responde a la siguiente pregunta utilizando los fragmentos de documentos proporcionados:
PREGUNTA: {question}
=========
{summaries}
=========
RESPUESTA FINAL:
"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
