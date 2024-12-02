from pydantic import BaseModel
from typing import Optional

# Schema base para cualquier colección
class BaseCollectionSchema(BaseModel):
    estado: int = 1  # 1 para activo, 0 para inactivo

# API Lugares
class LugarModel(BaseCollectionSchema):
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



# Modelo de Pizza
class PizzaModel(BaseCollectionSchema):
    name: str
    description: Optional[str] = None
    ingredients: str  # Ingredientes de la pizza
    size: str  # Tamaño de la pizza (por ejemplo, pequeña, mediana, grande)
    price: float  # Precio de la pizza
    is_vegetarian: bool  # Si la pizza es vegetariana

# Modelo de Bebida
class DrinkModel(BaseCollectionSchema):
    name: str
    description: Optional[str] = None
    type: str  # Tipo de bebida (por ejemplo, refresco, jugo, agua)
    volume_ml: int  # Volumen en mililitros
    price: float  # Precio de la bebida
    is_alcoholic: bool  # Si la bebida es alcohólica o no