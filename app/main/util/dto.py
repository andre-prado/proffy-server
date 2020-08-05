from flask_restplus import Namespace, fields


class ClasseDto:
    api = Namespace('classe', description='classe related operations')
    classe = api.model('classe', {
        'subject': fields.String(required=True, description='classe subject'),
        'cost': fields.Float(required=True, description='classe cost')
    })
