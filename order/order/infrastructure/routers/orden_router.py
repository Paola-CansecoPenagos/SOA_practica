from flask import Blueprint
from order.infrastructure.controllers.crear_orden_controller import order_blueprint, initialize_order_endpoint
from order.infrastructure.controllers.listar_orden_controller import list_order_blueprint, initialize_list_order_endpoint
from order.infrastructure.controllers.actualizar_orden_controller import update_order_status_blueprint, initialize_update_order_status_endpoint
from order.infrastructure.repositories.orden_repository import MongoDBOrderRepository

order_router = Blueprint('order_router', __name__)

def initialize_order_endpoints():
    order_repository = MongoDBOrderRepository(connection_string='mongodb://localhost:27017/', database_name='213445_order')
    initialize_order_endpoint(order_repository)
    initialize_list_order_endpoint(order_repository)
    initialize_update_order_status_endpoint(order_repository)

initialize_order_endpoints()

order_router.register_blueprint(order_blueprint, url_prefix='/')
order_router.register_blueprint(list_order_blueprint, url_prefix='/')
order_router.register_blueprint(update_order_status_blueprint, url_prefix='/')