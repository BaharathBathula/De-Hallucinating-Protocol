from fastapi import FastAPI

from src.trust_engine.api.routes import router as trust_router


app = FastAPI(
    title="De-Hallucinating Protocol",
    description="Runtime Governance Framework for Enterprise AI Systems",
    version="1.0.0"
)

app.include_router(trust_router)


@app.get("/")
def root():
    return {
        "framework": "De-Hallucinating Protocol",
        "status": "runtime_governance_active"
    }
