from pydantic import BaseModel
from typing import Optional

class BaseCollectionSchema(BaseModel):
    name: str
    description: Optional[str] = None
    direccion: str
    capacidad: int
    latitud: float
    longitud: float
    categoria: str
    codigo_postal: str
    ciudad: str
    pais: Optional[str] = None

    estado: int = 1

# Crear las clases para las colecciones específicas
class LugarCreate(BaseCollectionSchema):
    direccion_id: str
    capacidad: int
    latitud: float
    longitud: float
    id_categoria: str

class DireccionCreate(BaseCollectionSchema):
    calle: str
    numero: str
    ciudad: str
    codigo_postal: str
    pais: Optional[str] = None

class CategoriaCreate(BaseCollectionSchema):
    pass
