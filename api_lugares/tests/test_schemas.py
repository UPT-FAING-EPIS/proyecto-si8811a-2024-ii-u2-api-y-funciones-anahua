# tests/test_schemas.py
from pydantic import ValidationError
from app.schemas import LugarCreate, DireccionCreate, CategoriaCreate
import pytest

# Pruebas para LugarCreate
def test_valid_lugar_create():
    lugar = LugarCreate(
        nombre_lugar="Parque Central",
        direccion_id="001",
        capacidad=200,
        descripcion="Un parque en el centro de la ciudad.",
        latitud=40.7128,
        longitud=-74.0060,
        id_categoria="cat_001"
    )
    assert lugar.nombre_lugar == "Parque Central"
    assert lugar.capacidad == 200

def test_invalid_lugar_create_missing_fields():
    with pytest.raises(ValidationError):
        LugarCreate(
            nombre_lugar="Parque Central",
            # Faltan varios campos requeridos
        )

def test_invalid_lugar_create_wrong_types():
    with pytest.raises(ValidationError):
        LugarCreate(
            nombre_lugar="Parque Central",
            direccion_id="001",
            capacidad="doscientos",  # Debería ser un entero
            descripcion="Un parque en el centro de la ciudad.",
            latitud="incorrecto",    # Debería ser un float
            longitud=-74.0060,
            id_categoria="cat_001"
        )

# Pruebas para DireccionCreate
def test_valid_direccion_create():
    direccion = DireccionCreate(
        calle="Av. Siempre Viva",
        numero="742",
        ciudad="Springfield",
        codigo_postal="12345",
        pais="USA"
    )
    assert direccion.calle == "Av. Siempre Viva"
    assert direccion.pais == "USA"

def test_optional_pais():
    direccion = DireccionCreate(
        calle="Av. Siempre Viva",
        numero="742",
        ciudad="Springfield",
        codigo_postal="12345"
    )
    assert direccion.pais is None

def test_invalid_direccion_missing_fields():
    with pytest.raises(ValidationError):
        DireccionCreate(
            calle="Av. Siempre Viva"
            # Faltan número, ciudad, código postal
        )

# Pruebas para CategoriaCreate
def test_valid_categoria_create():
    categoria = CategoriaCreate(nombre_categoria="Museo")
    assert categoria.nombre_categoria == "Museo"

def test_invalid_categoria_create_missing_name():
    with pytest.raises(ValidationError):
        CategoriaCreate()  # Falta el nombre de la categoría
