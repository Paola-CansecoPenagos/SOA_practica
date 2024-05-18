from flask import Blueprint
from product.infrastructure.controllers.crear_producto_controller import product_blueprint, initialize_product_endpoint
from product.infrastructure.controllers.listar_producto_controller import list_product_blueprint, initialize_list_product_endpoint
from product.infrastructure.controllers.eliminar_producto_controller import delete_product_blueprint, initialize_delete_product_endpoint
from product.infrastructure.controllers.buscar_producto_controller import find_product_by_name_blueprint, initialize_find_product_by_name_endpoint
from product.infrastructure.repositories.producto_repository import MongoDBProductRepository

product_router = Blueprint('product_router', __name__)

def initialize_product_endpoints(repository):
    initialize_product_endpoint(repository)
    initialize_list_product_endpoint(repository)
    initialize_delete_product_endpoint(repository)
    initialize_find_product_by_name_endpoint(repository)

repository = MongoDBProductRepository(connection_string='mongodb://localhost:27017/', database_name='213445_inventory')
initialize_product_endpoints(repository)

product_router.register_blueprint(product_blueprint,  url_prefix='/')
product_router.register_blueprint(list_product_blueprint, url_prefix='/')
product_router.register_blueprint(delete_product_blueprint, url_prefix='/')
product_router.register_blueprint(find_product_by_name_blueprint, url_prefix='/')
