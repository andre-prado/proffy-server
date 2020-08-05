from flask import Flask
from flask_restplus import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, help='Your name')
    name = parser.parse_args()

    def get(self):
        return {'hello': 'mr {name}'}


if __name__ == '__main__':
    app.run(debug=True)
