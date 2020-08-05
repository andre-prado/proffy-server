from .. import db


class User(db.Model):
    """ User Model for storing user related deatails """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    avatar = db.Column(db.String(255), nullable=False)
    whatsapp = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.String(255), nullable=False)

    classe = db.relationship('Classe', backref="user", lazy="dynamic")
    classe = db.relationship('Connection', backref="user", lazy="dynamic")

    def __repr__(self):
        return f"<User '{self.name}'>"
