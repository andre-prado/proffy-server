from flask_restplus import Namespace, fields


class ClasseDto:
    api = Namespace("classe", description="classe related operations")
    classe = api.model("classe", {
        "id": fields.Integer(require=True, description="Class id"),
        "subject": fields.String(required=True, description="classe subject"),
        "cost": fields.Float(required=True, description="classe cost"),
        "user_id": fields.Integer(require=True, description="user id"),
    })


class UserDto:
    api = Namespace("user", description="user related operations")
    user = api.model("user", {
        "id": fields.Integer(require=True, description="User Id"),
        "name": fields.String(require=True, description="User name"),
        "avatar": fields.String(require=True, description="User avatar"),
        "whatsapp": fields.String(require=True, description="User whatsapp"),
        "bio": fields.String(require=True, description="User bio")
    })
