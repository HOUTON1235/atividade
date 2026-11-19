from fastapi import APIRouter, HTTPException

from app.models import Tarefa, TarefaEntrada
from app.store import store

router = APIRouter(prefix="/tarefas", tags=["Tarefas"])


@router.post(
    "/",
    response_model=Tarefa,
    status_code=201,
    summary="Cadastrar tarefa",
    description="Cria uma nova tarefa e a armazena em memória.",
)
def cadastrar(entrada: TarefaEntrada) -> Tarefa:
    return store.criar(entrada)


@router.get(
    "/",
    response_model=list[Tarefa],
    summary="Listar tarefas",
    description="Retorna todas as tarefas cadastradas.",
)
def listar() -> list[Tarefa]:
    return store.listar_todas()


@router.get(
    "/{tarefa_id}",
    response_model=Tarefa,
    summary="Consultar tarefa por ID",
    description="Retorna uma única tarefa a partir do seu identificador.",
)
def buscar_por_id(tarefa_id: int) -> Tarefa:
    tarefa = store.buscar_por_id(tarefa_id)
    if tarefa is None:
        raise HTTPException(status_code=404, detail=f"Tarefa {tarefa_id} não encontrada.")
    return tarefa
