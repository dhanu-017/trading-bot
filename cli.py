import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        # Validate inputs
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.price, args.type)

        client = get_client()

        print("\n--- Order Request ---")
        print(vars(args))

        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n--- Order Response ---")
        print({
            "orderId": order.get("orderId"),
            "status": order.get("status"),
            "executedQty": order.get("executedQty"),
            "avgPrice": order.get("avgPrice", "N/A")
        })

        print("\n✅ Order placed successfully!")

    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()