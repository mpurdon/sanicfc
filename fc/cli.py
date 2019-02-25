from sanic import Sanic
from sanic_pw import Peewee


app = Sanic('fc_cli')
app.db = Peewee(app)


if __name__ == "__main__":
    app.db.cli()
