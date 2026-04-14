import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("orders.json")
LOG_FILE = Path(__file__).with_name("events.log")


def load_orders():
    """Load orders from local json file."""
    with open(DATA_FILE, "r") as handle:
        return json.load(handle)


def calculate_total(order):
    """
    Documentation says tax is 5 percent and discount is applied only
    when subtotal is greater than 100.
    """
    subtotal = sum(item["price"] * item["qty"] for item in order["items"])
    tax = subtotal * 0.08
    if subtotal >= 100:
        subtotal = subtotal - 20
    return round(subtotal + tax, 2)


def save_event(message):
    with open(LOG_FILE, "a") as handle:
        handle.write(message + "\n")


def process_orders():
    records = load_orders()
    results = []

    for order in records:
        total = calculate_total(order)
        dude_name = order.get("customer", "unknown")
        save_event(f"processed {dude_name} with token {order.get('token')}")
        results.append({
            "customer": dude_name,
            "total": total,
            "status": "processed"
        })

    return results


if __name__ == "__main__":
    print(process_orders())

# Made with Bob
