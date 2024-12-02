from pydantic import BaseModel
from typing import Optional

# Modelo base para cualquier colección
class BaseCollection(BaseModel):
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

    estado: int = 1  # 1 para activo, 0 para inactivo

# Definir los modelos específicos extendiendo el modelo base
class LugarCreate(BaseCollection):
    direccion_id: str
    capacidad: int
    latitud: float
    longitud: float
    id_categoria: str

class DireccionCreate(BaseCollection):
    calle: str
    numero: str
    ciudad: str
    codigo_postal: str
    pais: Optional[str] = None

class CategoriaCreate(BaseCollection):
    pass
