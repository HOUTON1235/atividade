from enum import Enum
from pydantic import BaseModel, Field


class Prioridade(str, Enum):
    baixa = "baixa"
    media = "media"
    alta  = "alta"


class TarefaEntrada(BaseModel):
    """Dados enviados pelo cliente para criar uma tarefa."""

    titulo:     str        = Field(..., description="Título da tarefa")
    descricao:  str        = Field(..., description="Descrição detalhada")
    prioridade: Prioridade = Field(..., description="Prioridade: baixa, media ou alta")


class Tarefa(TarefaEntrada):
    """Tarefa completa — herda os campos de TarefaEntrada e adiciona o id."""

    id: int = Field(..., description="Identificador único gerado pelo servidor")
