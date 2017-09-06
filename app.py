# flask app
from flask import Flask
from configuration.config import config

# flask app
app = Flask(__name__)

from models.sfobject.view import sfobject_blueprint
app.register_blueprint(sfobject_blueprint)

app.run(host=config['settings']["flaskhost"], port=config['settings']["flaskport"])











