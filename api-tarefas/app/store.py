from app.models import Tarefa, TarefaEntrada


class TarefaStore:
    """Repositório em memória de tarefas.

    Encapsular o estado numa classe elimina variáveis globais e
    facilita substituir por um banco de dados no futuro — basta
    trocar a implementação desta classe sem tocar nas rotas.
    """

    def __init__(self) -> None:
        self._tarefas: list[Tarefa] = []
        self._proximo_id: int = 1

    def listar_todas(self) -> list[Tarefa]:
        return self._tarefas

    def buscar_por_id(self, tarefa_id: int) -> Tarefa | None:
        return next((t for t in self._tarefas if t.id == tarefa_id), None)

    def criar(self, entrada: TarefaEntrada) -> Tarefa:
        tarefa = Tarefa(id=self._proximo_id, **entrada.model_dump())
        self._tarefas.append(tarefa)
        self._proximo_id += 1
        return tarefa


# Instância única compartilhada pela aplicação (injetada nas rotas via dependência)
store = TarefaStore()
