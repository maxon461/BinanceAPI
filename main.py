

from request import *
from preparing_to_upload import *
from save_excel import *
from load_keys import *
from datetime import datetime


def main():
    # Replace with your API key and secret key
    api_key, secret_key = load_api_keys()
    # Get c2c order history
    c2c_order_history = get_binance_c2c_order_history(api_key, secret_key)
    # print(c2c_order_history)
    if c2c_order_history:
        # Parse orders
        c2c_order_data = c2c_order_history.get("data", [])
        parsed_orders = []
        for order_info in c2c_order_data:
            create_time_milliseconds = order_info.get("createTime")
            create_time_seconds = create_time_milliseconds / 1000
            create_time = datetime.utcfromtimestamp(create_time_seconds + 3600)


            # Check if the day in the date is the 13th
            if create_time.day == 12 and order_info.get("orderStatus") == "COMPLETED":
                parsed_order = {
                    "orderStatus": order_info.get("orderStatus"),
                    "totalPrice": order_info.get("totalPrice"),
                    "tradeType": order_info.get("tradeType"),
                    "createTime": create_time.strftime('%Y-%m-%d %H:%M:%S')  # Convert to human-readable format
                }
                parsed_orders.append(parsed_order)
        profit = count_profit(parsed_orders)
        # Save parsed orders to Excel file
        buy_orders, sell_orders = separate_buy_sell(parsed_orders)
        save_to_excel(buy_orders, sell_orders, profit, "parsed_orders.xlsx")
        print("Parsed orders saved to parsed_orders.xlsx")
    else:
        print("Failed to retrieve c2c order history.")


if __name__ == "__main__":
    main()