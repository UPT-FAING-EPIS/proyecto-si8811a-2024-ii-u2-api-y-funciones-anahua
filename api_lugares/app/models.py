from pydantic import BaseModel
from uuid import uuid4

class Lugar(BaseModel):
    id_lugar: str
    nombre_lugar: str
    direccion_id: str
    capacidad: int
    descripcion: str
    latitud: float
    longitud: float
    id_categoria: str
    estado: int = 1  # 1 para activo, 0 para inactivo (default: activo)

class Direccion(BaseModel):
    direccion_id: str
    calle: str
    numero: str
    ciudad: str
    codigo_postal: str
    pais: str | None = None
    estado: int = 1  # 1 para activo, 0 para inactivo

class Categoria(BaseModel):
    id_categoria: str
    nombre_categoria: str
    estado: int = 1  # 1 para activo, 0 para inactivo
