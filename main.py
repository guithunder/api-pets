from fastapi import FastAPI
from routers.pets import router as pets_router

app = FastAPI()

app.include_router(pets_router)

@app.get("/")
def raiz():
    return {"message": "API de Pets funcionando!"}
