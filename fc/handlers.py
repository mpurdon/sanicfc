import logging

from sanic import Sanic
from sanic.exceptions import ServerError, NotFound
from sanic.response import json
from sanic.views import HTTPMethodView

from models.user import User

logger = logging.getLogger(__name__)


def init_handlers(app: Sanic):
    """
    Add the handlers to the app.

    """
    app.add_route(TestView.as_view(), '/')
    app.add_route(ErrorView.as_view(), '/error')
    app.add_route(TeapotView.as_view(), '/teapot')
    app.add_route(UserDetailView.as_view(), '/users/<user_id>/')

    @app.exception(NotFound)
    async def ignore_404s(request, exception):
        return json({'status': 404, 'message': f'{request.path} was not found', 'data': None}, status=404)

    @app.exception(ServerError)
    async def handle_500s(request, exception):
        return json({'status': 500, 'message': str(exception), 'data': None}, status=500)


class ErrorView(HTTPMethodView):
    async def get(self, request):
        raise ServerError('Something bad happened, freak out dude!', status_code=500)


class TeapotView(HTTPMethodView):
    async def get(self, request):
        return json({'status': 418, 'message': 'I am a teapot'}, status=418)


class TestView(HTTPMethodView):
    """
    Test Views

    """
    async def get(self, request):
        logger.debug('Getting some fucking thing')
        return json({'hello': 'world'})

    async def post(self, request):
        logger.debug('Posting some fucking thing')
        return json(request.json)


class UserDetailView(HTTPMethodView):
    """
    User Details

    """
    async def get(self, request, user_id):
        logger.debug(f'Getting details for user {user_id}')
        user = await User.get_or_404(int(user_id))
        logger.debug(f'Found user with id: {user.id}')
        return json(user.to_dict())
