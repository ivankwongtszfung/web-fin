from flask import abort
from flask_restplus import Resource

from app.main.apis.serializers.stock import (api, stock_list)
from app.main.resources.stock import Stock
from app.main.services.data_fetcher import DataFetcher


@api.route("/")
class StockList(Resource):
    @api.doc('get the whole list of stock')
    @api.marshal_with(stock_list, envelope='data')
    def get(self, **kwargs):
        return DataFetcher(resource=Stock).all()


@api.route("/<code>")
@api.param('code', 'The Stock Code')
class StockDetail(Resource):
    @api.doc('get the whole list of stock')
    @api.marshal_with(stock_list)
    def get(self, code):
        stock = DataFetcher(resource=Stock).first(**{"code": code})
        if not stock:
            abort(404, f'stock {code} is not found')
        else:
            return stock
