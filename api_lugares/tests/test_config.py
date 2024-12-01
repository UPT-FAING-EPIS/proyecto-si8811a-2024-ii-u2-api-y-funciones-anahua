import os
from unittest import mock
import pytest
from app.config import setup_db

# Mock para simular la conexión con CouchDB
@mock.patch('couchdb.Server')
def test_setup_db_crea_bases_de_datos(mock_couchdb_server):
    
    mock_couch_instance = mock_couchdb_server.return_value

    mock_couch_instance.__contains__.side_effect = lambda db_name: db_name == "_users"
    
    setup_db()

    mock_couch_instance.create.assert_any_call('lugares')
    mock_couch_instance.create.assert_any_call('direcciones')
    mock_couch_instance.create.assert_any_call('categorias')
