from fastapi import FastAPI

from app.routes.tarefas import router as tarefas_router

app = FastAPI(
    title="API de Tarefas",
    description="API REST para cadastrar e consultar tarefas (dados em memória).",
    version="1.0.0",
)

app.include_router(tarefas_router)


@app.get("/", tags=["Status"], summary="Health check")
def health_check() -> dict[str, str]:
    """Confirma que o servidor está no ar."""
    return {"status": "ok"}
