# flake8: noqa
from langchain.prompts import PromptTemplate

## Use a shorter template to reduce the number of tokens in the prompt
template = """
Cree una respuesta final a las preguntas dadas utilizando los fragmentos de documentos proporcionados (dados en ningún orden específico) como fuentes. SIEMPRE incluya una sección "FUENTES" en su respuesta citando solo el conjunto mínimo de fuentes necesarias para responder a la pregunta. Si no puede responder a la pregunta, simplemente indique que no tiene suficiente información para responder a la pregunta y deje la sección FUENTES vacía, y si no hay la respuesta no recree con el ejemplo siguiente. Utilice solo los documentos proporcionados y no intente fabricar una respuesta.

---------

PREGUNTA: ¿Cuál es el propósito de ARPA-H?
=========
Contenido: Más apoyo para pacientes y familias. \n\nPara llegar allí, hago un llamado al Congreso para financiar ARPA-H, la Agencia de Proyectos de Investigación Avanzada para la Salud. \n\nEstá basado en DARPA, el proyecto del Departamento de Defensa que condujo a la creación del Internet, GPS, y mucho más.  \n\nARPA-H tendrá un propósito singular: impulsar avances en cáncer, Alzheimer, diabetes, y más.
FUENTES: 1-32
Contenido: Mientras lo hacemos, asegurémonos de que todos los estadounidenses puedan obtener la atención médica que necesitan. \n\nYa hemos realizado inversiones históricas en atención médica. \n\nHemos facilitado que los estadounidenses obtengan la atención que necesitan, cuando la necesitan. \n\nHemos facilitado que los estadounidenses obtengan los tratamientos que necesitan, cuando los necesitan. \n\nHemos facilitado que los estadounidenses obtengan los medicamentos que necesitan, cuando los necesitan.
FUENTES: 1-33
Contenido: El V.A. está innovando nuevas formas de vincular exposiciones tóxicas con enfermedades, ya está ayudando a los veteranos a obtener la atención que merecen. \n\nNecesitamos extender esa misma atención a todos los estadounidenses. \n\nEs por eso que estoy pidiendo al Congreso que apruebe una legislación que establecería un registro nacional de exposiciones tóxicas y proporcionaría atención médica y asistencia financiera a los afectados.
FUENTES: 1-30
=========
RESPUESTA FINAL: El propósito de ARPA-H es impulsar avances en cáncer, Alzheimer, diabetes, y más.
FUENTES: 1-32

---------

PREGUNTA: {question}
=========
{summaries}
=========
RESPUESTA FINAL:"""


STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
