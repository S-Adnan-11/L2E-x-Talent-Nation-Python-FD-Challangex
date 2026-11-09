def fresh_stock(stock):
    new_stock = {}
    for item in stock:
        new_stock[item] = stock[item]
    return new_stock


def restock(stock, item, qty):
    new_stock = fresh_stock(stock)
    if type(qty) is int and qty > 0:
        new_stock[item] = new_stock.get(item, 0) + qty
    return new_stock


def sell(stock, item, qty):
    new_stock = fresh_stock(stock)
    if type(qty) is not int or qty <= 0:
        return new_stock, False
    if item not in stock or stock[item] < qty:
        return new_stock, False
    new_stock[item] -= qty  # zero stays in the shop, it isn't deleted 😼
    return new_stock, True


def low_stock(stock, limit):
    items = []
    for item in stock:
        if stock[item] < limit:
            items.append(item)
    return items


def total_items(stock):
    total = 0
    for item in stock:
        total += stock[item]
    return total


def inventory_value(stock, prices):
    total = 0
    for item in stock:
        if item in prices:
            total += stock[item] * prices[item]
    return total


if __name__ == "__main__":
    stock = {"rice": 10, "beans": 5}
    print("Before success:", stock)
    print("Sell rice:", sell(stock, "rice", 4))
    print("After success:", stock)
    print("Before failure:", stock)
    print("Sell too much:", sell(stock, "beans", 9))
    print("After failure:", stock)
    print("New item:", restock(stock, "gari", 8))
    print("More rice:", restock(stock, "rice", 5))
    for item, qty in (("beans", 5), ("yam", 1), ("rice", 0), ("rice", -2), ("rice", 1.5)):
        print("Sell:", item, qty, "→", sell(stock, item, qty))
    print("Low stock:", low_stock(stock, 6))
    print("Total:", total_items(stock))
    print("Value (unpriced beans skipped):", inventory_value(stock, {"rice": 250, "gari": 100}))
