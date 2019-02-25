import logging

from functools import wraps

from sanic.response import json
from sanic_jwt import exceptions

logger = logging.getLogger('fc')

users = {
    'matthew': {
        'id': 1,
        'password': 'password',
    }
}


async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user = users.get(username, None)
    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user.get('password'):
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return users.get(username)
