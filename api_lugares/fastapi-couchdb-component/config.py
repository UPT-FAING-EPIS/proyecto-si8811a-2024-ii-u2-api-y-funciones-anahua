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
    


def delete_single_collection(collection_name: str):
    try:
        # Conectarse al servidor CouchDB
        couch = couchdb.Server(COUCHDB_URL)
        
        # Obtener todas las bases de datos existentes
        db_names = get_existing_collections()

        if collection_name in db_names:
            try:
                couch.delete(collection_name)
                print(f"Base de datos '{collection_name}' eliminada.")
            except couchdb.http.ResourceNotFound:
                print(f"La base de datos '{collection_name}' no se pudo encontrar para eliminar.")
        else:
            print(f"La base de datos '{collection_name}' no existe.")

    except couchdb.http.ServerError as e:
        print(f"Error al conectar con CouchDB: {e}")

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")


def delete_all_collections():
    try:
        # Conectarse al servidor CouchDB
        couch = couchdb.Server(COUCHDB_URL)
        
        # Obtener todas las bases de datos existentes
        db_names = get_existing_collections()

        for db_name in db_names:
            if db_name not in ["_replicator", "_users"]:  # No borrar bases de datos del sistema
                try:
                    couch.delete(db_name)
                    print(f"Base de datos '{db_name}' eliminada.")
                except couchdb.http.ResourceNotFound:
                    print(f"La base de datos '{db_name}' no se pudo encontrar para eliminar.")
    
    except couchdb.http.ServerError as e:
        print(f"Error al conectar con CouchDB: {e}")
    
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
