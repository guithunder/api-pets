from fastapi import APIRouter, HTTPException
from database import supabase
from models import PetCreate, Pet

router = APIRouter(prefix="/pets", tags=["Pets"])


@router.get("/")
def listar_pets():
    result = supabase.table("pets").select("*").execute()
    return result.data


@router.get("/{pet_id}")
def buscar_pet(pet_id: int):
    result = supabase.table("pets").select("*").eq("id", pet_id).single().execute()

    if result.data is None:
        raise HTTPException(status_code=404, detail="Pet não encontrado")

    return result.data


@router.post("/")
def criar_pet(pet: PetCreate):
    data = pet.dict()  # garante que não inclui "id"

    result = supabase.table("pets").insert(data).execute()

    if not result.data:
        raise HTTPException(500, "Erro ao inserir Pet")

    return result.data


@router.put("/{pet_id}")
def atualizar_pet(pet_id: int, pet: PetCreate):
    exists = supabase.table("pets").select("*").eq("id", pet_id).single().execute()

    if exists.data is None:
        raise HTTPException(404, "Pet não encontrado")

    data = pet.dict()

    result = supabase.table("pets").update(data).eq("id", pet_id).execute()

    return result.data


@router.delete("/{pet_id}")
def deletar_pet(pet_id: int):
    exists = supabase.table("pets").select("*").eq("id", pet_id).single().execute()

    if exists.data is None:
        raise HTTPException(404, "Pet não encontrado")

    supabase.table("pets").delete().eq("id", pet_id).execute()
    return {"message": "Pet deletado com sucesso!"}
