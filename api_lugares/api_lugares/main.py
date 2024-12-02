from fastapi import FastAPI, HTTPException
from .config import get_existing_collections, setup_db
from .schemas import BaseCollectionSchema
from fastapi.middleware.cors import CORSMiddleware
from .crud import (
    create_item, get_items, get_item, update_item, deactivate_item
)
import re

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración inicial (las coleecciones se crea una si no existe)
@app.on_event("startup")
async def setup():
    setup_db("lugares")  # Crear cualquier colección aquí
    
    # Obtenemos las colecciones existentes desde la base de datos
    #existing_collections = ["lugares", "categorias", "direcciones"]  # Puedes obtener esto dinámicamente
    existing_collections = get_existing_collections()

    # Registrar dinámicamente los endpoints para cada colección
    for collection_name in existing_collections:
        app.add_api_route(f"/{collection_name}/", get_items_endpoint(collection_name), methods=["GET"], tags=[collection_name.capitalize()])
        app.add_api_route(f"/{collection_name}/", create_item_endpoint(collection_name), methods=["POST"], tags=[collection_name.capitalize()])
        app.add_api_route(f"/{collection_name}/{{item_id}}", get_item_endpoint(collection_name), methods=["GET"], tags=[collection_name.capitalize()])
        app.add_api_route(f"/{collection_name}/{{item_id}}", update_item_endpoint(collection_name), methods=["PUT"], tags=[collection_name.capitalize()])
        app.add_api_route(f"/{collection_name}/{{item_id}}", deactivate_item_endpoint(collection_name), methods=["DELETE"], tags=[collection_name.capitalize()])



# Validar que el nombre de la coleccion
def validate_collection_name(collection_name: str):
    if not collection_name or collection_name.strip() == "":
        raise HTTPException(status_code=400, detail="El nombre de la colección no puede estar vacío o contener solo espacios.")

    pattern = r'^[a-z0-9_-]+$'
    if not re.match(pattern, collection_name):
        raise HTTPException(status_code=400, detail="El nombre de la colección contiene caracteres no permitidos. Solo se permiten letras, números, guiones y guiones bajos.")



# Rutas genéricas para cualquier colección
name_generic = "Todos"

@app.post("/{collection_name}/", tags=[name_generic])
async def create_new_item(collection_name: str, item: BaseCollectionSchema):
    validate_collection_name(collection_name)  # Validar el nombre de la colección
    return create_item(collection_name, item)

@app.get("/{collection_name}/", tags=[name_generic])
async def get_all_items(collection_name: str):
    validate_collection_name(collection_name)  # Validar el nombre de la colección
    return get_items(collection_name)

@app.get("/{collection_name}/{item_id}", tags=[name_generic])
async def get_single_item(collection_name: str, item_id: str):
    validate_collection_name(collection_name)  # Validar el nombre de la colección
    item = get_item(collection_name, item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"{collection_name.capitalize()} no encontrado")
    return item

@app.put("/{collection_name}/{item_id}", tags=[name_generic])
async def update_single_item(collection_name: str, item_id: str, item: BaseCollectionSchema):
    validate_collection_name(collection_name)  # Validar el nombre de la colección
    updated_item = update_item(collection_name, item_id, item.dict())
    if not updated_item:
        raise HTTPException(status_code=404, detail=f"{collection_name.capitalize()} no encontrado")
    return updated_item

@app.delete("/{collection_name}/{item_id}", tags=[name_generic])
async def deactivate_single_item(collection_name: str, item_id: str):
    validate_collection_name(collection_name)  # Validar el nombre de la colección
    item = deactivate_item(collection_name, item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"{collection_name.capitalize()} no encontrado")
    return {"detail": f"{collection_name.capitalize()} desactivado correctamente"}




# Funciones auxiliares
def get_items_endpoint(collection_name: str):
    async def endpoint():
        return get_items(collection_name)
    return endpoint

def create_item_endpoint(collection_name: str):
    async def endpoint(item: BaseCollectionSchema):
        return create_item(collection_name, item)
    return endpoint

def get_item_endpoint(collection_name: str):
    async def endpoint(item_id: str):
        item = get_item(collection_name, item_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"{collection_name.capitalize()} no encontrado")
        return item
    return endpoint

def update_item_endpoint(collection_name: str):
    async def endpoint(item_id: str, item: BaseCollectionSchema):
        updated_item = update_item(collection_name, item_id, item.dict())
        if not updated_item:
            raise HTTPException(status_code=404, detail=f"{collection_name.capitalize()} no encontrado")
        return updated_item
    return endpoint

def deactivate_item_endpoint(collection_name: str):
    async def endpoint(item_id: str):
        item = deactivate_item(collection_name, item_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"{collection_name.capitalize()} no encontrado")
        return {"detail": f"{collection_name.capitalize()} desactivado correctamente"}
    return endpoint
