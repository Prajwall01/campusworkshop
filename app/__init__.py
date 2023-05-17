"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7jem4dadc9vltn09g-a.oregon-postgres.render.com",
        database="todo_data",
        user="root",
        password="hHlVbgMtP2AsN9LwkwgaHwpmYFXIMWSr")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
