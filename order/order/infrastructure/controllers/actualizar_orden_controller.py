import pika
from flask import Blueprint, request, jsonify
from order.application.usecases.actualizar_orden import UpdateOrderStatus

update_order_status_blueprint = Blueprint('update_order_status', __name__)

def send_update_stock_message(order_id):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='update_stock_queue')
    channel.basic_publish(exchange='', routing_key='update_stock_queue', body=str(order_id))
    connection.close()

def initialize_update_order_status_endpoint(order_repository):
    update_order_status_usecase = UpdateOrderStatus(order_repository)

    @update_order_status_blueprint.route('/update_status/<order_id>', methods=['PUT'])
    def update_order_status(order_id):
        new_status = request.json.get('status')
        if not new_status:
            return jsonify({"error": "Estatus es requerido"}), 400
        try:
            update_order_status_usecase.execute(order_id, new_status)
            if new_status == "Enviado":
                send_update_stock_message(order_id)
            return jsonify({"message": "Estatus actualizado exitosamente"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
