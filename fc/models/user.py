from models import db


class User(db.Model):
    """
    User Model

    """
    __tablename__ = 'users'

    id = db.Column(db.BigInteger(), primary_key=True)

    def __repr__(self):
        return '{}<{}>'.format(self.nickname, self.id)
