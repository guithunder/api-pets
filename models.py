from pydantic import BaseModel

class Pet(BaseModel):
    id: int | None = None
    nome: str
    dono: str
    telefone: str
