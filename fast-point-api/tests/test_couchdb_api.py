import pytest
import warnings
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "fast_point_api"))

from fast_point_api.config import CouchDBManager
from fast_point_api.schemas import PizzaModel
from fast_point_api.crud import create_item, deactivate_item, get_item, get_items, update_item

warnings.filterwarnings("ignore", category=DeprecationWarning, module="pydantic")

# Configuración para pruebas
@pytest.fixture
def test_db_manager():
    """Crea un gestor de base de datos para pruebas y asegura que '_users' existe."""
    db_manager = CouchDBManager('http://admin:admin@localhost:5984')
    db_manager.get_db('_users')
    return db_manager

@pytest.fixture
def test_pizza_data():
    """Datos de ejemplo para PizzaModel."""
    return PizzaModel(
        name="Test Pizza",
        description="Pizza de prueba",
        ingredients="Tomate, queso",
        size="Mediana",
        price=10.99,
        is_vegetarian=True
    )

# Pruebas de bases de datos
def test_get_existing_collections(test_db_manager):
    """Prueba para obtener bases de datos existentes."""
    collections = test_db_manager.get_existing_collections()
    assert isinstance(collections, list), "El resultado debe ser una lista."

def test_create_and_delete_database(test_db_manager):
    """Prueba para crear y eliminar una base de datos."""
    db_name = "test_db"
    test_db_manager.get_db(db_name)
    assert db_name in test_db_manager.get_existing_collections(), "La base de datos debería existir."
    test_db_manager.delete_collection(db_name)
    assert db_name not in test_db_manager.get_existing_collections(), "La base de datos debería haber sido eliminada."

# Pruebas CRUD
def test_create_item(test_db_manager, test_pizza_data):
    collection_name = "test_collection"
    new_item = create_item(test_db_manager, collection_name, test_pizza_data)
    assert new_item['_id'] is not None, "El ID único debe ser generado"
    assert new_item['estado'] == 1, "El estado por defecto debe ser 1"

def test_get_items(test_db_manager, test_pizza_data):
    collection_name = "test_collection"
    create_item(test_db_manager, collection_name, test_pizza_data)
    items = get_items(test_db_manager, collection_name)
    assert len(items) > 0, "Debe haber al menos un elemento activo en la colección"

def test_get_item(test_db_manager, test_pizza_data):
    collection_name = "test_collection"
    new_item = create_item(test_db_manager, collection_name, test_pizza_data)
    fetched_item = get_item(test_db_manager, collection_name, new_item['_id'])
    assert fetched_item is not None, "Debe devolver el elemento solicitado si está activo"
    assert fetched_item['_id'] == new_item['_id'], "El ID del elemento devuelto debe coincidir"

def test_update_item(test_db_manager, test_pizza_data):
    collection_name = "test_collection"
    new_item = create_item(test_db_manager, collection_name, test_pizza_data)
    updated_data = {"price": 19.99}
    updated_item = update_item(test_db_manager, collection_name, new_item['_id'], updated_data)
    assert updated_item is not None, "Debe devolver el elemento actualizado"
    assert updated_item['price'] == 19.99, "El precio debe actualizarse correctamente"

def test_deactivate_item(test_db_manager, test_pizza_data):
    collection_name = "test_collection"
    new_item = create_item(test_db_manager, collection_name, test_pizza_data)
    deactivated_item = deactivate_item(test_db_manager, collection_name, new_item['_id'])
    assert deactivated_item is not None, "Debe devolver el elemento desactivado"
    assert deactivated_item['estado'] == 0, "El estado del elemento debe ser 0 tras la desactivación"


# Limpieza después de pruebas
@pytest.fixture(scope="function", autouse=True)
def cleanup(test_db_manager):
    """Limpia las bases de datos de prueba después de cada ejecución."""
    yield
    dbs_to_clean = ["test_db", "test_pizzas"]
    for db in dbs_to_clean:
        if db in test_db_manager.get_existing_collections():
            test_db_manager.delete_collection(db)
