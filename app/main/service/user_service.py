from app.main import db
from app.main.model.user import User


def get_all_users():
    users = User.query.all()
    print(users)
    return users


def get_a_user(id):
    return User.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
    return data.id
