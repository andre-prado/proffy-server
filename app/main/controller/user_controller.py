from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import get_a_user, get_all_users

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        return get_all_users()


@api.route('/<id>')
@api.param('id', 'The User Identifier')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, id):
        """ get a classe given its identifier """
        user = get_a_user(id)
        if not user:
            api.abort(404)
        else:
            return user
