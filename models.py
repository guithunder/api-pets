from pydantic import BaseModel

class PetBase(BaseModel):
    nome: str
    dono: str
    telefone: str

class PetCreate(PetBase):
    pass

class Pet(PetBase):
    id: int
