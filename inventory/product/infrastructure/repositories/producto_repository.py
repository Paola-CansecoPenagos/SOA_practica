from pymongo import MongoClient
from bson import ObjectId
from product.domain.entities.producto import Product

class MongoDBProductRepository:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.product_collection = self.db['productos']
    
    def find_by_name(self, name):
        products = list(self.product_collection.find({"name": {"$regex": name, "$options": "i"}}))
        if not products:
            raise ValueError("No se encontraron productos con ese nombre")
        return [{**product, "_id": str(product["_id"])} for product in products]

    def save(self, product: Product):
        try:
            existing_product = self.find_by_name(product.name)
            if existing_product:
                raise ValueError("Producto ya existente")
        except ValueError as e:
            if str(e) == "No se encontraron productos con ese nombre":
                pass 
            else:
                raise
        product_data = product.__dict__
        self.product_collection.insert_one(product_data)


    def find_all(self):
        products = self.product_collection.find({})
        return [{**product, "_id": str(product["_id"])} for product in products]
    
    def delete_by_id(self, product_id):
        result = self.product_collection.delete_one({"_id": ObjectId(product_id)})
        if result.deleted_count == 0:
            raise ValueError("Producto no encontrado")