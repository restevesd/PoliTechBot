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

Por favor, utiliza este formato y responde a la siguiente pregunta utilizando los fragmentos de documentos proporcionados:
PREGUNTA: {question}
=========
{summaries}
=========
RESPUESTA FINAL:
"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
