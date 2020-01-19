# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from app.main.apis.controllers.stock import api as Stock

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(Stock, path='/stock')