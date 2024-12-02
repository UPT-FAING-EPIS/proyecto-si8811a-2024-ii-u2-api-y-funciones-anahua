import couchdb
import os
import json

# Obtener la URL de CouchDB del entorno
COUCHDB_URL = os.getenv('COUCHDB_URL', 'http://admin:admin@localhost:5984')

def setup_db(collection_name: str):
    try:
        # Conectarse al servidor CouchDB
        couch = couchdb.Server(COUCHDB_URL)
        
        # Acceder a la db del parametro
        try:
            db = couch[collection_name]
        except couchdb.http.ResourceNotFound:
            # Si no existe, crearla
            db = couch.create(collection_name)
            print(f"Base de datos '{collection_name}' creada.")
        
        return db
    
    except couchdb.http.ServerError as e:
        print(f"Error de conexión con CouchDB: {e}")
        raise

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        raise

#-----------------------------------------------------------------------------------#

def get_existing_collections():
    try:
        # Conectarse al servidor CouchDB
        couch = couchdb.Server(COUCHDB_URL)
        
        response = couch.resource.get('_all_dbs')
        response_body = response[2].read().decode('utf-8')
        db_names = json.loads(response_body)
        print(db_names)

        return db_names
    
    except couchdb.http.ServerError as e:
        print(f"Error al conectar con CouchDB: {e}")
        return []

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        return []