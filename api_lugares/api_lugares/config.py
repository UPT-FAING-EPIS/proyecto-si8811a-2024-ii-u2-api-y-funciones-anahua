import couchdb
import os

# Obtener la URL de CouchDB del entorno
COUCHDB_URL = os.getenv('COUCHDB_URL', 'http://admin:admin@localhost:5984')

def setup_db(collection_name: str):
    try:
        # Conectarse al servidor CouchDB
        couch = couchdb.Server(COUCHDB_URL)
        
        # Intentar acceder a la base de datos dada
        try:
            db = couch[collection_name]
        except couchdb.http.ResourceNotFound:
            # Si la base de datos no existe, crearla
            db = couch.create(collection_name)
            print(f"Base de datos '{collection_name}' creada.")
        
        return db
    
    except couchdb.http.ServerError as e:
        print(f"Error de conexión con CouchDB: {e}")
        raise  # Re-lanzar la excepción para que se maneje en otro lugar si es necesario

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        raise

#-----------------------------------------------------------------------------------#

def get_existing_collections():
    try:
        # Conectarse al servidor CouchDB
        couch = couchdb.Server(COUCHDB_URL)
        
                
        response = couch.resource.get('_all_dbs')

        # Acceder al cuerpo de la respuesta (el tercer elemento en la tupla)
        response_body = response[2].read().decode('utf-8')

        # Convertirlo de JSON a una lista de bases de datos
        import json
        db_names = json.loads(response_body)

        print(db_names)

        # Devuelve la lista de nombres de las bases de datos
        return db_names
    
    except couchdb.http.ServerError as e:
        print(f"Error al conectar con CouchDB: {e}")
        return []

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        return []