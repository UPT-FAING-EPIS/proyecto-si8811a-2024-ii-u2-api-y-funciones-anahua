import couchdb
import os

# Obtener la URL de CouchDB del entorno
COUCHDB_URL = os.getenv('COUCHDB_URL', 'http://admin:admin@localhost:5984')

def setup_db():
    couch = couchdb.Server(COUCHDB_URL)
    db_names = ["lugares", "direcciones", "categorias", "_users"]# _users para la auth interna de CouchDB / Evitar logs sobre eso
    
    # Crear las bases de datos si no existen
    for db_name in db_names:
        if db_name not in couch:
            couch.create(db_name)
    return couch
