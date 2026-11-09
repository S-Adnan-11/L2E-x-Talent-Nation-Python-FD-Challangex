# O(m) time/space: validate and keep each denomination once, in input order.
def coin_values(coins):
    values = {}
    for coin in coins:
        if type(coin) is not int or coin <= 0:
            raise ValueError("Coins must be positive whole numbers.")
        values[coin] = True
    return list(values)


# O(A*m + A + m) time/O(A + m) space: initialize the table, then update per coin type.
def count_ways_dp(amount, coins):
    if type(amount) is not int:
        raise ValueError("Amount must be a whole number.")
    values = coin_values(coins)
    if amount < 0:
        return 0
    totals = [0] * (amount + 1)
    totals[0] = 1
    for coin in values:
        for number in range(coin, amount + 1):
            totals[number] += totals[number - coin]
    return totals[amount]


# O(A*m + A + m) time/O(A + m) space: build minimum counts and optional predecessor choices.
def min_coins(amount, coins, with_coins=False):
    if type(amount) is not int:
        raise ValueError("Amount must be a whole number.")
    values = coin_values(coins)
    if amount < 0:
        return (-1, []) if with_coins else -1
    totals = [amount + 1] * (amount + 1)
    chosen = [None] * (amount + 1)
    totals[0] = 0
    for number in range(1, amount + 1):
        for coin in values:
            if coin <= number and totals[number - coin] + 1 < totals[number]:
                totals[number] = totals[number - coin] + 1
                chosen[number] = coin
    if totals[amount] == amount + 1:
        return (-1, []) if with_coins else -1
    if not with_coins:
        return totals[amount]
    used = []
    number = amount
    while number > 0:
        coin = chosen[number]
        used.append(coin)
        number -= coin
    return totals[amount], used


# The tables don't grow a recursive call stack, so amount 10000 doesn't hit that limit.
if __name__ == "__main__":
    for amount, values in ((5, [1, 2, 5]), (100, [1, 5, 10, 25, 50]), (0, [1, 2]),
                           (3, [2]), (0, []), (7, []), (6, [1, 3, 4]),
                           (4, [1, 1, 2]), (-1, [1, 2]), (3, [5])):
        print("Amount:", amount, "Coins:", values,
              "Ways:", count_ways_dp(amount, values),
              "Minimum:", min_coins(amount, values),
              "Bonus:", min_coins(amount, values, with_coins=True))
    print("Minimum for 11:", min_coins(11, [1, 2, 5]))
    print("Ways for 10000:", count_ways_dp(10000, [1, 5, 10, 25, 50]))
