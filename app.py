from flask import Flask
from flask_restful import Api
from api.showCrontab import Show, ShowUsers, ShowCabinet,ShowHost
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

api.add_resource(Show, '/api/show/<hostname>/<users>')
api.add_resource(ShowUsers, '/api/show/<hostname>')
api.add_resource(ShowCabinet,'/api/show/cabinet')
api.add_resource(ShowHost,'/api/show/hosts')

if __name__ == '__main__':
    app.run()