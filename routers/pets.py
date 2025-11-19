from fastapi import APIRouter, HTTPException
from database import supabase
from models import Pet

router = APIRouter(prefix="/pets", tags=["Pets"])


# -------------------------------
# LISTAR TODOS OS PETS
# -------------------------------
@router.get("/")
def listar_pets():
    result = supabase.table("pets").select("*").execute()
    return result.data


# -------------------------------
# BUSCAR PET POR ID
# -------------------------------
@router.get("/{pet_id}")
def buscar_pet(pet_id: int):
    result = supabase.table("pets").select("*").eq("id", pet_id).single().execute()

    if result.data is None:
        raise HTTPException(status_code=404, detail="Pet não encontrado")

    return result.data


# -------------------------------
# CRIAR PET
# -------------------------------
@router.post("/")
def criar_pet(pet: Pet):
    data = {
        "nome": pet.nome,
        "dono": pet.dono,
        "telefone": pet.telefone
    }

    result = supabase.table("pets").insert(data).execute()
    return result.data


# -------------------------------
# ATUALIZAR PET
# -------------------------------
@router.put("/{pet_id}")
def atualizar_pet(pet_id: int, pet: Pet):
    # verificar se existe
    exists = supabase.table("pets").select("*").eq("id", pet_id).single().execute()

    if exists.data is None:
        raise HTTPException(status_code=404, detail="Pet não encontrado")

    # atualização
    data = {
        "nome": pet.nome,
        "dono": pet.dono,
        "telefone": pet.telefone
    }

    result = supabase.table("pets").update(data).eq("id", pet_id).execute()
    return result.data


# -------------------------------
# DELETAR PET
# -------------------------------
@router.delete("/{pet_id}")
def deletar_pet(pet_id: int):
    # verificar se existe
    exists = supabase.table("pets").select("*").eq("id", pet_id).single().execute()

    if exists.data is None:
        raise HTTPException(status_code=404, detail="Pet não encontrado")

    result = supabase.table("pets").delete().eq("id", pet_id).execute()
    return {"message": "Pet deletado com sucesso!"}
