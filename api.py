from flask import Flask, jsonify, request
from db import orders_db

app = Flask(__name__)


@app.route('/orders', methods=['GET'])
def get_order():
    order_number = request.args.get('order_number')
    if not order_number:
        return jsonify({"error": "order_number query parameter is required"}), 400
        
    if order_number in orders_db:
        order = orders_db[order_number]
        return jsonify({
            "order_number": order.order_number,
            "customer_name": order.customer_name,
            "items": order.items,
            "total_amount": order.total_amount,
            "order_date": order.order_date.isoformat(),
            "status": order.status,
            "shipping_address": order.shipping_address
        })
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
