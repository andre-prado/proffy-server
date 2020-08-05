from flask import request
from flask_restplus import Resource

from ..util.dto import ClasseDto
from ..service.classe_service import (save_new_classe, get_all_classes,
                                      get_a_classe)

api = ClasseDto.api
_classe = ClasseDto.classe


@api.route('/')
class ClassList(Resource):
    @api.doc('list_of_registered_classes')
    @api.marshal_list_with(_classe, envelope='data')
    def get(self):
        """List of all registered classes"""
        return get_all_classes()

    @api.response(201, 'Classe sucessfully created.')
    @api.doc('create a new classe')
    @api.expect(_classe, validade=True)
    def post(self):
        """Creates a new classe """
        data = request.json
        return save_new_classe(data=data)


@api.route('/<id>')
@api.param('id', 'The Classe Identifier')
class Classe(Resource):
    @api.doc('get a classe')
    @api.marshal_with(_classe)
    def get(self, id):
        """ get a user given its identifier """
        classe = get_a_classe(id)
        if not classe:
            api.abort(404)
        else:
            return classe
