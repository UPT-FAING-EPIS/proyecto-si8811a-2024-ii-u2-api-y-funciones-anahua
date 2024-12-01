import couchdb
from uuid import uuid4
from .config import setup_db
from .models import Lugar, Direccion, Categoria

# Conectar con CouchDB
couch = setup_db()

lugares_db = couch['lugares']
direcciones_db = couch['direcciones']
categorias_db = couch['categorias']



# CRUD Lugares
def create_lugar(lugar):
    lugar_data = lugar.dict()
    lugar_data['_id'] = str(uuid4())
    lugar_data['estado'] = 1
    lugares_db.save(lugar_data)
    return lugar_data

def get_lugares():
    return [lugares_db[lugar.id] for lugar in lugares_db.view('_all_docs', include_docs=True) if lugares_db[lugar.id]['estado'] == 1]

def get_lugar(id_lugar):
    lugar_id = str(id_lugar)
    try:
        lugar = lugares_db[lugar_id]
        if lugar['estado'] == 1:
            return lugar
        else:
            return None
    except couchdb.http.ResourceNotFound:
        return None

def deactivate_lugar(id_lugar):
    lugar_id = str(id_lugar)
    try:
        lugar = lugares_db[lugar_id]
        lugar['estado'] = 0
        lugares_db.save(lugar)
        return lugar
    except couchdb.http.ResourceNotFound:
        return None


def update_lugar(id_lugar, lugar_data):
    lugar_id = str(id_lugar)
    try:
        lugar = lugares_db[lugar_id]
        for key, value in lugar_data.items():
            if key in lugar:
                lugar[key] = value
        lugares_db.save(lugar)
        return lugar
    except couchdb.http.ResourceNotFound:
        return None





# CRUD Direcciones
def create_direccion(direccion):
    direccion_data = direccion.dict()
    direccion_data['_id'] = str(uuid4())
    direccion_data['estado'] = 1
    direcciones_db.save(direccion_data)
    return direccion_data

def get_direcciones():
    return [direcciones_db[direccion.id] for direccion in direcciones_db.view('_all_docs', include_docs=True) if direcciones_db[direccion.id]['estado'] == 1]

def get_direccion(id_direccion):
    direccion_id = str(id_direccion)
    try:
        direccion = direcciones_db[direccion_id]
        if direccion['estado'] == 1:
            return direccion
        else:
            return None
    except couchdb.http.ResourceNotFound:
        return None
    
def deactivate_direccion(id_direccion):
    direccion_id = str(id_direccion)
    try:
        direccion = direcciones_db[direccion_id]
        direccion['estado'] = 0
        direcciones_db.save(direccion)
        return direccion
    except couchdb.http.ResourceNotFound:
        return None


def update_direccion(id_direccion, direccion_data):
    direccion_id = str(id_direccion)
    try:
        direccion = direcciones_db[direccion_id]
        for key, value in direccion_data.items():
            if key in direccion:
                direccion[key] = value
        direcciones_db.save(direccion)
        return direccion
    except couchdb.http.ResourceNotFound:
        return None
    




# CRUD Categorías
def create_categoria(categoria):
    categoria_data = categoria.dict()
    categoria_data['_id'] = str(uuid4())
    categoria_data['estado'] = 1
    categorias_db.save(categoria_data)
    return categoria_data

def get_categorias():
    return [categorias_db[categoria.id] for categoria in categorias_db.view('_all_docs', include_docs=True) if categorias_db[categoria.id]['estado'] == 1]

def get_categoria(id_categoria):
    categoria_id = str(id_categoria)
    try:
        categoria = categorias_db[categoria_id]
        if categoria['estado'] == 1:
            return categoria
        else:
            return None
    except couchdb.http.ResourceNotFound:
        return None
    
    
def deactivate_categoria(id_categoria):
    categoria_id = str(id_categoria)
    try:
        categoria = categorias_db[categoria_id]
        categoria['estado'] = 0
        categorias_db.save(categoria)
        return categoria
    except couchdb.http.ResourceNotFound:
        return None


def update_categoria(id_categoria, categoria_data):
    categoria_id = str(id_categoria)
    try:
        categoria = categorias_db[categoria_id]
        for key, value in categoria_data.items():
            if key in categoria:
                categoria[key] = value
        categorias_db.save(categoria)
        return categoria
    except couchdb.http.ResourceNotFound:
        return None