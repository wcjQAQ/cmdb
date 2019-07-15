from flask import Flask
from flask_restful import Api
from api.show import ShowCron, ShowUsers, ShowCabinets, ShowHosts, ShowHostInfo
from flask_cors import CORS
from api.add import AddCron
app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

###### show  #######
api.add_resource(ShowCron, '/api/show/<hostname>/<users>')
api.add_resource(ShowUsers, '/api/show/cabinet/<hostname>')
api.add_resource(ShowHostInfo, '/api/show/<cabinet>/<host>/info')
api.add_resource(ShowCabinets,'/api/show/cabinet')
api.add_resource(ShowHosts,'/api/show/<cabinet>')

###### add  #######
api.add_resource(AddCron,'/api/add/crontab')


if __name__ == '__main__':
    app.run()