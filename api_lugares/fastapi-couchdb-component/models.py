from pydantic import BaseModel
from typing import Optional

# Modelo base para cualquier colección
class BaseCollection(BaseModel):
    estado: int = 1  # 1 para activo, 0 para inactivo

# API Lugares
class LugarModel(BaseCollection):
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
