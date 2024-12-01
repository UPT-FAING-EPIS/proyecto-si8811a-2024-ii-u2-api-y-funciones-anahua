from setuptools import setup, find_packages

setup(
    name="api_lugares",
    version="0.1.0",
    description="Paquete reutilizable para gestionar colecciones en CouchDB con FastAPI",
    author="maynerac",
    author_email="ma2020067145@virtual.upt.pe",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "couchdb",
        "pydantic"
    ],
    entry_points={
        'console_scripts': [
            'api_lugares = api_lugares.main:app',  # Comando para ejecutar la API
        ],
    },
)
