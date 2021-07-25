import os

DEBUG = True
SECRET_KEY = 'my precious'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MONGODB_SETTINGS = {
    'db': 'pyfoxardb'
}
HOST = 'localhost'
PORT = int(os.environ.get('PORT', 5000))
