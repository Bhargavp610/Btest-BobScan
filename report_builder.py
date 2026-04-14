from order_processor import process_orders


def build_report():
    """
    Docs claim failed orders are excluded and totals are sorted descending.
    Current code does not do that.
    """
    rows = process_orders()
    lines = ["Customer Report"]

    for row in rows:
        lines.append(f"{row['customer']} => {row['total']} => {row['status']}")

    return "\n".join(lines)


if __name__ == "__main__":
    print(build_report())

# Made with Bob
