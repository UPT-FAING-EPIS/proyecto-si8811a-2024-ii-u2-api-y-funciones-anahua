from fast_point_api.config import CouchDBManager

from fast_point_api.schemas import PizzaModel
from fast_point_api.crud import create_item


clase = CouchDBManager('http://admin:admin@localhost:5984')

'''


a = clase.get_existing_collections()

b = clase.get_db('_users')
b = clase.get_db('vdfveee')
d = clase.get_db('asasas')
e = clase.get_db('rerfer')

c= clase.delete_collection('vfveee')

#f1 = clase.delete_all_collections(exclude_system_dbs = True)
#f2 = clase.delete_all_collections(exclude_system_dbs = False)

g = clase.get_existing_collections()

#print(a)
#print(b)


pizza_data = PizzaModel(name="Margarita", description="Pizza clásica", ingredients="Tomate, queso", size="Mediana", price=12.99, is_vegetarian=True)
#new_item = create_item(clase, "pizzas", pizza_data)
#print(new_item)

from fast_point_api.crud import update_item

updated_data = {"price": 99.99}
updated_item = update_item(clase, "pizzas", "8468bc67-d09f-4e73-981b-061783ff44a6", updated_data)
print(updated_item)


'''


# FUNCION CREAR_BD_COUCHDB() ???
#docker run -d -p 5984:5984 -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=admin couchdb
#docker run -d -p 5985:5984 -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=admin couchdb
#docker run -d -p 5986:5984 -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=admin couchdb



# uvicorn api_lugares.main:app --reload
# uvicorn fastapi-couchdb-component.main:app --reload



from fast_point_api.app_factory import create_app
from fast_point_api.schemas import PizzaModel, DrinkModel
from fast_point_api.endpoints import generar_endpoints_genericos

#Evitar que use "_users" u otra db del sistema de couchdb
#app = create_app(connection_url="http://admin:admin@localhost:5984")



collections = {
    "pizzas": PizzaModel,
    "bebidas": DrinkModel,
}
#Endpoints con la conexion 85
app = create_app(
    connection_url="http://admin:admin@localhost:5985",
    models_dict=collections
    )


#Endpoints con la conexion 84
a = generar_endpoints_genericos(app,clase)


#Asi la api funcionara con la bd segun la conexion que se desee como puede ser una 86 y etc