def count_profit(parsed_orders):
    profit = 0.0
    for order in parsed_orders:
        if order['tradeType'] == 'BUY':
            profit -= float(order['totalPrice'])
        else:
            profit += float(order['totalPrice'])
    return profit
def separate_buy_sell(parsed_orders):
    buy_orders = []
    sell_orders = []
    for order in parsed_orders:
        if order['tradeType'] == 'BUY':
            buy_orders.append(order)
        else:
            sell_orders.append(order)
    return buy_orders, sell_orders