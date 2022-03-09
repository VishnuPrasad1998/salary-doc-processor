from flask import Flask, jsonify
from flask_restx import Api
from flask_pymongo import PyMongo
from .response import Response


mongo_db = PyMongo()
app = Flask(__name__)


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app.config.from_object(config_by_name[env or 'dev'])
    mongo_db.init_app(app)
    from flask import Blueprint

    api_v1 = Blueprint('api_v1', __name__)

    api = Api(api_v1,
              title="PDF Extractor Api",
              version="0.1.0", description="API to extract pdf data and return as json")

    register_routes(api, app)

    app.register_blueprint(api_v1, url_prefix="/pdf")
    
    @app.route("/health")
    def health():
        return Response.success({"status": "Running"}, 200, "Successfully working")

    return app, mongo_db

