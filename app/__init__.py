import os

from dotenv import load_dotenv
from flask import Flask

from config import Config

# load dotenv in the base root
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
# to encrypt the data
app.config.from_object(Config)

# to avoid circular import
from app import routes
