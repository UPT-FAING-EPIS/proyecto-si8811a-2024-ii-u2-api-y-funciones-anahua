from pydantic import BaseModel
from typing import Optional

#Lugares
class LugarBase(BaseModel):
    nombre_lugar: str
    direccion_id: str
    capacidad: int
    descripcion: Optional[str]
    latitud: float
    longitud: float
    id_categoria: str

class LugarCreate(LugarBase):
    pass

#Direcciones
class DireccionBase(BaseModel):
    calle: str
    numero: str
    ciudad: str
    codigo_postal: str
    pais: Optional[str] = None  # Opcional

class DireccionCreate(DireccionBase):
    pass

#Categorias
class CategoriaBase(BaseModel):
    nombre_categoria: str

class CategoriaCreate(CategoriaBase):
    pass
