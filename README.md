[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17379747)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/UPT-FAING-EPIS/proyecto-si8811a-2024-ii-u2-api-y-funciones-anahua)
![Docker Image Version](https://img.shields.io/docker/v/maynerac/api-lugares?label=docker&logo=docker)

## API de Lugares

Este repositorio incluye el desarrollo y la documentación de una API diseñada para gestionar lugares, direcciones y categorías. La API utiliza FastAPI como framework y CouchDB para la base de datos. El proyecto permite realizar operaciones CRUD (crear, leer, actualizar, eliminar) sobre estos recursos mediante solicitudes HTTP, y está preparado para ser desplegado con Docker.

## Índice

- [API de Lugares](#api-de-lugares)
- [Índice](#índice)
- [Requisitos](#requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Desplegando con Docker Compose](#desplegando-con-docker-compose)
- [Instalación Local](#instalación-local)
- [Usando docker run utilizando la IP del servicio de CouchDB](#usando-docker-run-utilizando-la-ip-del-servicio-de-couchdb)
- [Usando docker run con una red personalizada](#usando-docker-run-con-una-red-personalizada)
- [Eliminar los contenedores creados](#eliminar-los-contenedores-creados)
- [Endpoints](#endpoints)
- [Diagramas](#diagramas)
- [Pruebas](#pruebas)
- [Comandos](#comandos)
- [Video](#video)

## Requisitos

- **Python 3.7+**
- **CouchDB**: Se requiere tener CouchDB corriendo para poder almacenar y recuperar la información de los lugares, direcciones y categorías.
- **FastAPI**: Framework web para construir APIs rápidas y eficientes.
- **Uvicorn**: Servidor ASGI para correr la aplicación de FastAPI.

## Estructura del Proyecto

```plaintext
api_lugares/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── crud.py
│   ├── models.py
│   ├── schemas.py
│   └── config.py
│
├── tests/
│   ├── __init__.py
│   ├── test_schemas.py
│   └── test_config.py
│
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
└── dev-requirements.txt

```

## Desplegando con Docker Compose

Para levantar los servicios definidos en el archivo docker-compose.yml, utilizamos el comando:

```bash
docker-compose up
```

Otra opcion es ejecutar los contenedores en segundo plano, evitando que los logs se muestren en la consola con la opción -d (detached mode):

```bash
docker-compose up -d
```

Puedes consultar la imagen del proyecto en Docker Hub:

🐳 [Ver imagen en Docker Hub](https://hub.docker.com/repository/docker/maynerac/api-lugares/general)

📦 [Ver imagen en GitHub Container Registry](https://github.com/users/MAYnerAC/packages/container/package/api-lugares)

## Instalación Local

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/UPT-FAING-EPIS/proyecto-si8811a-2024-ii-u2-api-y-funciones-anahua.git
   ```

2. Navegar al directorio del proyecto:

   ```bash
   cd proyecto-si8811a-2024-ii-u2-api-y-funciones-anahua/api_lugares
   ```

3. Crear un entorno virtual e instalar las dependencias:

   ```bash
   python -m venv env

   .\env\Scripts\activate

   pip install -r requirements.txt
   ```

4. Configurar las variables de entorno:

   El archivo `config.py` obtiene la URL de CouchDB de las variables de entorno. Debe seguir el formato:

   ```bash
   export COUCHDB_URL=http://usuario:contrasena@localhost:5984
   ```

5. Iniciar el servidor:

   ```bash
   uvicorn main:app --reload
   ```

## Usando docker run utilizando la IP del servicio de CouchDB

1. Iniciamos el contenedor de CouchDB

```bash
docker run -d --name couchdb -p 5984:5984 -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=admin couchdb:latest
```

2. Iniciamos el contenedor de la API Lugares, asegurarnos que "172.17.0.2" sea la IP correcta, podemos usar `docker inspect couchdb` para verificarlo

```bash
docker run -d --name fastapi -p 8000:8000 -e COUCHDB_URL=http://admin:admin@172.17.0.2:5984 maynerac/api-lugares:latest
```

## Usando docker run con una red personalizada

1. Creamos la red personalizada antes de crear los servicios por separado

```bash
docker network create apidb_network
```

2. Creamos el servicio `couchdb`, podemos cambiar las variables de entorno `COUCHDB_USER` y `COUCHDB_PASSWORD`

```bash
docker run -d --name couchdb --network apidb_network -p 5984:5984 -v couchdb_data:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=admin couchdb:latest
```

3. Creamos el servicio `fastapi`, el formato de `COUCHDB_URL` es `http://usuario:contrasena@localhost:5984`

```bash
docker run -d --name fastapi --network apidb_network -p 8000:8000 -e COUCHDB_URL=http://admin:admin@couchdb:5984 maynerac/api-lugares:latest
```

## Eliminar los contenedores creados

1. Listamos los contenedrores activos y detenidos

```bash
docker ps -a
```

2. Si estan en ejecucion, detenemos los contenedores

```bash
docker stop couchdb
docker stop fastapi
```

3. Eliminamos los contenedores

```bash
docker rm couchdb
docker rm fastapi
```

4. Verificamos su correcta eliminacion

```bash
docker ps -a
```

5. Revisamos si tenemos un volumen creado

```bash
docker volume ls
```

6. Eliminamos los volumnes en caso lo necesitemos (Opcional)

```bash
docker volume rm couchdb_data
```

7. Eliminamos la red personalizada `apidb_network` (Opcional)

```bash
docker network rm apidb_network
```

8. Verificamos que se haya eliminado `apidb_network`

```bash
docker network ls
```

## Endpoints

- **Lugares**

  - `GET /lugares/`: Obtener todos los lugares.
  - `POST /lugares/`: Crear un nuevo lugar.
  - `GET /lugares/{id_lugar}`: Obtener un lugar por su ID.
  - `PUT /lugares/{id_lugar}`: Actualizar un lugar por su ID.
  - `DELETE /lugares/{id_lugar}`: Desactivar un lugar por su ID.

- **Direcciones**

  - `GET /direcciones/`: Obtener todas las direcciones.
  - `POST /direcciones/`: Crear una nueva dirección.
  - `GET /direcciones/{id_direccion}`: Obtener una dirección por su ID.
  - `PUT /direcciones/{id_direccion}`: Actualizar una dirección por su ID.
  - `DELETE /direcciones/{id_direccion}`: Desactivar una dirección por su ID.

- **Categorías**

  - `GET /categorias/`: Obtener todas las categorías.
  - `POST /categorias/`: Crear una nueva categoría.
  - `GET /categorias/{id_categoria}`: Obtener una categoría por su ID.
  - `PUT /categorias/{id_categoria}`: Actualizar una categoría por su ID.
  - `DELETE /categorias/{id_categoria}`: Desactivar una categoría por su ID.

- **Documentación**

  - `GET /docs`: [Documentación Swagger](http://localhost:8000/docs).
  - `GET /redoc`: [Documentación ReDoc](http://localhost:8000/redoc).

- **CouchDB Dashboard**
  - `GET http://localhost:5984/_utils`: [Acceso a la interfaz de CouchDB](http://localhost:5984/_utils).

## Diagramas

- Diagrama de Clases

```mermaid

classDiagram
    class Lugar {
        +int id_lugar
        +string nombre_lugar
        +int direccion_id
        +int capacidad
        +string descripcion
        +float latitud
        +float longitud
        +int id_categoria
    }

    class Direccion {
        +int direccion_id
        +string calle
        +string numero
        +string ciudad
        +string codigo_postal
        +string pais
    }

    class Categoria {
        +int id_categoria
        +string nombre_categoria
    }

    Lugar --> Direccion : tiene
    Lugar --> Categoria : pertenece

```

Este diagrama de clases muestra la relación entre las entidades principales de la API. Cada **Lugar** está asociado con una **Dirección** y una **Categoría**.

- Diagrama de casos de uso

  ![alt text](assets/image-4.png)

- Diagrama del funcionamiento de la API Lugares

```mermaid

graph TD
    subgraph Elastika[Servidor Elastika]
        subgraph Docker[Contenedor - Docker]
            API[API de Lugares]
        end

        subgraph ElasticSearchServer[Contenedor - Docker]
            CouchDB[(CouchDB)]
        end
    end

    Cliente[Cliente - Servicio Web/Móvil]

    API --> |NoSQL| CouchDB
    Cliente --> |Métodos GET, POST, PUT, DELETE| API
    API --> |Respuestas HTTP| Cliente

    style Cliente fill:#b3d9ff,stroke:#333,stroke-width:2px
    style ElasticSearchServer fill:#ffb3b3,stroke:#333,stroke-width:2px
    style Docker fill:#d1e0e0,stroke:#333,stroke-width:2px
    style Elastika fill:#f7d794,stroke:#333,stroke-width:2px
```

## Pruebas

Las pruebas unitarias se ejecutaron correctamente utilizando `pytest`, confirmando que todos los casos de prueba para la API de lugares pasaron sin problemas.

- Se recolectaron 9 items de prueba, incluyendo pruebas para la configuración, el CRUD de lugares, direcciones y categorías.

![alt text](assets/image-6.png)

Puedes acceder a la documentación generada por Swagger en la ruta `/docs`. Esta interfaz permite probar los diferentes endpoints directamente desde el navegador. Para acceder, abre `http://localhost:8000/docs`.

![alt text](assets/image.png)

![alt text](assets/image-5.png)

![alt text](assets/image-1.png)

![alt text](assets/image-2.png)

![alt text](assets/image-3.png)

## Comandos

| **Comando**                     | **Descripción**                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------- |
| `python -m venv env`            | Crea un entorno virtual en Python.                                                |
| `.\env\Scripts\activate`        | Activa el entorno virtual en Windows.                                             |
| `deactivate`                    | Desactiva el entorno virtual.                                                     |
| `pip install fastapi uvicorn`   | Instala FastAPI y Uvicorn en el entorno actual.                                   |
| `pip install couchdb`           | Instala la librería de Python para interactuar con CouchDB.                       |
| `pip freeze > requirements.txt` | Guarda una lista de las dependencias instaladas en un archivo `requirements.txt`. |
| `pytest -v`                     | Ejecuta pruebas unitarias con un nivel detallado de salida (verbose).             |
| `docker ps`                     | Muestra una lista de los contenedores Docker que están corriendo.                 |
| `docker ps -a`                  | Muestra una lista de todos los contenedores Docker, incluyendo los detenidos.     |
| `docker-compose up`             | Levanta los servicios definidos en el archivo docker-compose.yml.                 |
| `docker-compose up -d`          | Ejecuta los servicios de Docker Compose en segundo plano (modo detached).         |
| `uvicorn main:app --reload`     | Ejecuta el servidor FastAPI con recarga automática en caso de cambios.            |

## Video

Explicacion de diferentes aspectos sobre la API de Lugares:

📂 [Ver video de la API de Lugares (Release v0.1.0) - YouTube](https://drive.google.com/file/d/13M5tyNbeWF1lK9fwnD9u-SMbgLkQa6nI/view?usp=sharing)

🎥 [Ver video de la API de Lugares (Release v0.1.0) - Google Drive](https://www.youtube.com/watch?v=_J36U9vYtoo)



## Codigo a Componentes

```mermaid

classDiagram
    class BaseCollectionSchema {
        +int estado
    }

    class LugarModel {
        +str name
        +str description
        +str direccion
        +int capacidad
        +float latitud
        +float longitud
        +str categoria
        +str codigo_postal
        +str ciudad
        +str pais
    }

    class PizzaModel {
        +str name
        +str description
        +str ingredients
        +str size
        +float price
        +bool is_vegetarian
    }

    class DrinkModel {
        +str name
        +str description
        +str type
        +int volume_ml
        +float price
        +bool is_alcoholic
    }

    BaseCollectionSchema <|-- LugarModel
    BaseCollectionSchema <|-- PizzaModel
    BaseCollectionSchema <|-- DrinkModel

```


![alt text](image.png)



![alt text](image-1.png)