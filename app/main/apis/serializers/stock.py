from flask_restplus import Namespace, fields

api = Namespace("stock", description="all the listed stock in the universe")

stock_list = api.model("stock", {
    'code': fields.String(description="the stock code"),
    'price': fields.Float(description="the stock price"),
    'update_time': fields.Date(description="the update time")
})
