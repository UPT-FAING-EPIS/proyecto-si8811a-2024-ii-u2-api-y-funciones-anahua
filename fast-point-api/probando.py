from fast_point_api.config import CouchDBManager

from fast_point_api.schemas import PizzaModel
from fast_point_api.crud import create_item

#uvicorn probando:app --reload

clase = CouchDBManager('http://admin:admin@localhost:5984')


# INSTANCIAS DE COUCHDB
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


# Crear el paquete
# pip install build

# Verificar que todo este en orden
# tar -tf dist/fast_point_api-0.1.0.tar.gz


# Probar intalar el paquete generado
# pip install dist/fast_point_api-0.1.0-py3-none-any.whl


#
# pip install twine
#
# twine upload dist/*
