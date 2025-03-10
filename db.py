from typing import Dict, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Order:
    order_number: str
    customer_name: str
    items: list
    total_amount: float
    order_date: datetime
    status: str
    shipping_address: str


orders_db: Dict[str, Order] = {
    "101": Order(
        order_number="101",
        customer_name="John Doe",
        items=[
            {"product": "Laptop", "quantity": 1, "price": 999.99},
            {"product": "Mouse", "quantity": 1, "price": 29.99}
        ],
        total_amount=1029.98,
        order_date=datetime(2024, 3, 15, 14, 30),
        status="Delivered",
        shipping_address="123 Main St, New York, NY 10001"
    ),
    "102": Order(
        order_number="102",
        customer_name="Jane Smith",
        items=[
            {"product": "Headphones", "quantity": 2, "price": 79.99},
            {"product": "Phone Case", "quantity": 1, "price": 19.99}
        ],
        total_amount=179.97,
        order_date=datetime(2024, 3, 16, 9, 15),
        status="Processing",
        shipping_address="456 Oak Ave, Los Angeles, CA 90001"
    ),
    "103": Order(
        order_number="103",
        customer_name="Bob Johnson",
        items=[
            {"product": "Smart Watch", "quantity": 1, "price": 299.99},
            {"product": "Charger", "quantity": 1, "price": 24.99}
        ],
        total_amount=324.98,
        order_date=datetime(2024, 3, 17, 11, 45),
        status="Shipped",
        shipping_address="789 Pine Rd, Chicago, IL 60601"
    )
}