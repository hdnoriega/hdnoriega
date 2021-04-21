from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "This is a demo of what i can do with python!"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

class get_resource(Resource, datos):
    def get(self):        
        r = usuarios(datos)
        return r, 200
        pass

class post_resource(Resource, datos):
    def post(self):        
        r = usuarios(datos)
        return r, 200
        pass

api.add_resource(ConsultaNOC, "/consultanoc", "/consultanoc/", "/consultanoc/<int:id>")

if __name__ == '__main__':
    app.run(debug=True, host = '127.0.0.1', port = 8080)

        
