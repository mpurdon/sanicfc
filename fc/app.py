import logging

from sanic import Sanic
from sanic_jwt import Initialize as init_jwt

from authentication import authenticate
from config import LOGGING_CONFIG
from handlers import init_handlers
from models import db

logger = logging.getLogger('fc')

api = Sanic('fc', log_config=LOGGING_CONFIG)
api.config.REQUEST_MAX_SIZE = 1_000_000
api.config.REQUEST_TIMEOUT = 5

api.config.DB_HOST = 'localhost'
api.config.DB_DATABASE = 'fc'
api.config.DB_USER = 'fc'
api.config.DB_PASSWORD = 'fcpass'

init_jwt(
    api,
    secret='secretdev',
    authenticate=authenticate
)

db.init_app(api)

init_handlers(api)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8000, debug=True, workers=2)
