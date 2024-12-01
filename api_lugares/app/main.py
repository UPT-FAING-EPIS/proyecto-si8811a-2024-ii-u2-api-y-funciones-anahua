from fastapi import FastAPI, HTTPException
from .schemas import LugarCreate, DireccionCreate, CategoriaCreate
from fastapi.middleware.cors import CORSMiddleware

from .crud import (
    create_lugar, get_lugares, get_lugar, update_lugar, deactivate_lugar, 
    create_direccion, get_direcciones, get_direccion, update_direccion, deactivate_direccion, 
    create_categoria, get_categorias, get_categoria, update_categoria, deactivate_categoria
)

from .config import setup_db

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración inicial de la base de datos
setup_db()



# Endpoints para Lugares
@app.post("/lugares/")
async def create_new_lugar(lugar: LugarCreate):
    return create_lugar(lugar)

@app.get("/lugares/")
async def get_all_lugares():
    return get_lugares()

@app.get("/lugares/{id_lugar}")
async def get_single_lugar(id_lugar: str):
    lugar = get_lugar(id_lugar)
    if not lugar:
        raise HTTPException(status_code=404, detail="Lugar no encontrado")
    return lugar

@app.delete("/lugares/{id_lugar}")
async def deactivate_single_lugar(id_lugar: str):
    lugar = deactivate_lugar(id_lugar)
    if not lugar:
        raise HTTPException(status_code=404, detail="Lugar no encontrado o ya desactivado")
    return {"detail": "Lugar desactivado correctamente"}

@app.put("/lugares/{id_lugar}")
async def update_lugar_endpoint(id_lugar: str, lugar: LugarCreate):
    lugar_data = lugar.dict()
    updated_lugar = update_lugar(id_lugar, lugar_data)
    if not updated_lugar:
        raise HTTPException(status_code=404, detail="Lugar no encontrado")
    return updated_lugar





# Endpoints para Direcciones
@app.post("/direcciones/")
async def create_new_direccion(direccion: DireccionCreate):
    return create_direccion(direccion)

@app.get("/direcciones/")
async def get_all_direcciones():
    return get_direcciones()

@app.get("/direcciones/{id_direccion}")
async def get_single_direccion(id_direccion: str):
    direccion = get_direccion(id_direccion)
    if not direccion:
        raise HTTPException(status_code=404, detail="Dirección no encontrada")
    return direccion


@app.delete("/direcciones/{id_direccion}")
async def deactivate_single_direccion(id_direccion: str):
    direccion = deactivate_direccion(id_direccion)
    if not direccion:
        raise HTTPException(status_code=404, detail="Dirección no encontrada o ya desactivada")
    return {"detail": "Dirección desactivada correctamente"}

@app.put("/direcciones/{id_direccion}")
async def update_direccion_endpoint(id_direccion: str, direccion: DireccionCreate):
    direccion_data = direccion.dict()
    updated_direccion = update_direccion(id_direccion, direccion_data)
    if not updated_direccion:
        raise HTTPException(status_code=404, detail="Dirección no encontrada")
    return updated_direccion




# Endpoints para Categorías
@app.post("/categorias/")
async def create_new_categoria(categoria: CategoriaCreate):
    return create_categoria(categoria)

@app.get("/categorias/")
async def get_all_categorias():
    return get_categorias()

@app.get("/categorias/{id_categoria}")
async def get_single_categoria(id_categoria: str):
    categoria = get_categoria(id_categoria)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@app.delete("/categorias/{id_categoria}")
async def deactivate_single_categoria(id_categoria: str):
    categoria = deactivate_categoria(id_categoria)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada o ya desactivada")
    return {"detail": "Categoría desactivada correctamente"}

@app.put("/categorias/{id_categoria}")
async def update_categoria_endpoint(id_categoria: str, categoria: CategoriaCreate):
    categoria_data = categoria.dict()
    updated_categoria = update_categoria(id_categoria, categoria_data)
    if not updated_categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return updated_categoria