import pika
from pymongo import MongoClient
from bson import ObjectId

def update_product_stock(order_id):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['213445_inventory']
    order_db = client['213445_order']

    order = order_db.order.find_one({"_id": ObjectId(order_id)})
    if order:
        for product in order['order_products']:
            product_id = product['product_id']
            quantity = product['quantity']
            # Actualiza el stock en la base de datos de inventario
            db.productos.update_one(
                {"_id": ObjectId(product_id)},
                {"$inc": {"stock": -quantity}}
            )

def callback(ch, method, properties, body):
    order_id = body.decode()
    update_product_stock(order_id)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='update_stock_queue')
    channel.basic_consume(queue='update_stock_queue', on_message_callback=callback, auto_ack=False)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()
