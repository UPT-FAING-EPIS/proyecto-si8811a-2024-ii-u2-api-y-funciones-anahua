import couchdb
from uuid import uuid4
from .config import setup_db
from .schemas import BaseCollectionSchema

# CRUD Genérico
def create_item(collection_name: str, item: BaseCollectionSchema):
    db = setup_db(collection_name)
    item_data = item.dict()
    item_data['_id'] = str(uuid4())
    item_data['estado'] = 1  # Por defecto, el item está activo
    db.save(item_data)
    #print(item_data)
    #print(item)
    return item_data

#print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

def get_items(collection_name: str):
    db = setup_db(collection_name)
    items = []
    for doc in db.view('_all_docs', include_docs=True):
        if doc['doc'].get('estado') == 1:
            items.append(doc['doc'])
        else:
            print(f"Documento sin estado o inactivo: {doc['doc']}")
    return items

def get_item(collection_name: str, item_id: str):
    db = setup_db(collection_name)
    try:
        item = db[item_id]
        if item.get('estado') == 1:
            return item
        else:
            return None
    except couchdb.http.ResourceNotFound:
        return None


def update_item(collection_name: str, item_id: str, item_data: dict):
    db = setup_db(collection_name)
    try:
        item = db[item_id]
        for key, value in item_data.items():
            if key in item:
                item[key] = value
        db.save(item)
        return item
    except couchdb.http.ResourceNotFound:
        return None

def deactivate_item(collection_name: str, item_id: str):
    db = setup_db(collection_name)
    try:
        item = db[item_id]
        item['estado'] = 0  # Cambiar estado a inactivo
        db.save(item)
        return item
    except couchdb.http.ResourceNotFound:
        return None
