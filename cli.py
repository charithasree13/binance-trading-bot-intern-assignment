import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        client = get_client()

        order = place_order(
            client,
            args.symbol.upper(),
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price
        )

        print("\n✅ Order Placed Successfully!")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice", "N/A"))

    except Exception as e:
        print("\n❌ Error:", str(e))

if __name__ == "__main__":
    main()