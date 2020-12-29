import os

from dotenv import load_dotenv
from flask import Flask

# load dotenv in the base root
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')  # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

from config import Config

app = Flask(__name__)
# to encrypt the data
app.config.from_object(Config)

from app import routes
