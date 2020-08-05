# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.classe_controller import api as classe_ns
from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(classe_ns, path='/classe')
api.add_namespace(user_ns, path='/user')
