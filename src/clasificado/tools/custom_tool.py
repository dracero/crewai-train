from crewai_tools import BaseTool, tool
from typing import Type
from pydantic import BaseModel, Field

# Tool para procesar tópicos administrativos
class ProcesarAdministrativoInput(BaseModel):
    """Input schema for ProcesarAdministrativo."""
    topico: dict = Field(..., description="El tópico administrativo a procesar.")

@tool
class ProcesarAdministrativoTool(BaseTool):
    """
    Procesa un tópico administrativo e imprime el resultado.
    Args:
        topico: El tópico a procesar
    Returns:
        str: Mensaje de confirmación
    """
    name: str = "procesar_administrativo"
    description: str = "Procesa tópicos administrativos y devuelve un mensaje de confirmación."
    args_schema: Type[BaseModel] = ProcesarAdministrativoInput

    def _run(self, topico: dict) -> str:
        return f"Agente Administrativo: Procesando tópico administrativo - '{topico}'"

# Tool para procesar tópicos técnicos
class ProcesarTecnicoInput(BaseModel):
    """Input schema for ProcesarTecnico."""
    topico: dict = Field(..., description="El tópico técnico a procesar.")

@tool
class ProcesarTecnicoTool(BaseTool):
    """
    Procesa un tópico técnico e imprime el resultado.
    Args:
        topico: El tópico a procesar
    Returns:
        str: Mensaje de confirmación
    """
    name: str = "procesar_tecnico"
    description: str = "Procesa tópicos técnicos y devuelve un mensaje de confirmación."
    args_schema: Type[BaseModel] = ProcesarTecnicoInput

    def _run(self, topico: dict) -> str:
        return f"Agente Técnico: Procesando tópico técnico - '{topico}'"
