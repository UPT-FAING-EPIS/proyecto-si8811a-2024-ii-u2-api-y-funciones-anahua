from fastapi import FastAPI, HTTPException
from .config import setup_db
from .schemas import BaseCollectionSchema, LugarCreate, DireccionCreate, CategoriaCreate
from fastapi.middleware.cors import CORSMiddleware

from .crud import (
    create_item, get_items, get_item, update_item, deactivate_item
)


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración inicial de la base de datos (se crea una si no existe)
@app.on_event("startup")
async def setup():
    setup_db("lugares")  # Puedes crear cualquier colección aquí

# Rutas genéricas para cualquier colección

@app.post("/{collection_name}/")
async def create_new_item(collection_name: str, item: BaseCollectionSchema):
    return create_item(collection_name, item)

@app.get("/{collection_name}/")
async def get_all_items(collection_name: str):
    return get_items(collection_name)

@app.get("/{collection_name}/{item_id}")
async def get_single_item(collection_name: str, item_id: str):
    item = get_item(collection_name, item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"{collection_name.capitalize()} no encontrado")
    return item

@app.put("/{collection_name}/{item_id}")
async def update_single_item(collection_name: str, item_id: str, item: BaseCollectionSchema):
    updated_item = update_item(collection_name, item_id, item.dict())
    if not updated_item:
        raise HTTPException(status_code=404, detail=f"{collection_name.capitalize()} no encontrado")
    return updated_item

@app.delete("/{collection_name}/{item_id}")
async def deactivate_single_item(collection_name: str, item_id: str):
    item = deactivate_item(collection_name, item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"{collection_name.capitalize()} no encontrado")
    return {"detail": f"{collection_name.capitalize()} desactivado correctamente"}
