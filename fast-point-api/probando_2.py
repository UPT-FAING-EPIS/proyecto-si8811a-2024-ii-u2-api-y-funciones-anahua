from fast_point_api.config import CouchDBManager

from fast_point_api.schemas import PizzaModel
from fast_point_api.crud import create_item

#uvicorn probando:app --reload

clase = CouchDBManager('http://admin:admin@localhost:5984')


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


