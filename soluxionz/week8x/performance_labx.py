# O(1) setup: the dictionary starts empty; cached calls pay for hashing their keys.
def memoize(max_size=None, lru=False):
    if max_size is not None and (not isinstance(max_size, int) or max_size < 0):
        raise ValueError("Cache size must be None or a non-negative integer.")

    # O(1) setup and space before any results are stored.
    def decorate(function):
        cache = {}

        # Hit O(K), miss O(K + F); O(C) cache entries, plus their key/result sizes.
        def wrapper(*args):
            hash(args)
            wrapper.calls += 1
            if args in cache:
                wrapper.hits += 1
                result = cache[args]
                if lru:
                    del cache[args]
                    cache[args] = result
                return result
            wrapper.misses += 1
            result = function(*args)
            if max_size == 0:
                return result
            if max_size is not None and len(cache) >= max_size:
                oldest = next(iter(cache))
                del cache[oldest]
            cache[args] = result
            return result

        wrapper.hits = 0
        wrapper.misses = 0
        wrapper.calls = 0
        wrapper.cache = cache
        return wrapper

    return decorate


# O(1) setup/extra space; each counted call adds O(1) overhead to the function work.
def track_calls(function):
    # O(F) time/O(1) extra per frame: count the call, then do the original work.
    def wrapper(*args):
        wrapper.calls += 1
        return function(*args)

    wrapper.calls = 0
    return wrapper


# O(m) time/space: validate denominations and keep each one once.
def prepare_coins(coins):
    values = {}
    for coin in coins:
        if not isinstance(coin, int) or coin <= 0:
            raise ValueError("Coins must be positive integers.")
        values[coin] = True
    return tuple(values)


# O(1) factory setup; the recursive work happens when the returned counter runs.
def make_coin_counter(cached=False, max_size=None):
    # Naive O(2^D) time/O(D) stack; memo stores O(A*m) states. D = A/c + m.
    def ways(amount, coins, index):
        if amount == 0:
            return 1
        if amount < 0 or index == len(coins):
            return 0
        return (ways(amount - coins[index], coins, index)
                + ways(amount, coins, index + 1))

    if cached:
        ways = memoize(max_size=max_size)(ways)
    else:
        ways = track_calls(ways)

    # Memo O(A*m^2) time/O(A*m + D + m) space here: hashing the coin tuple costs O(m).
    def counter(amount, coins):
        if not isinstance(amount, int):
            raise ValueError("Amount must be an integer.")
        values = prepare_coins(coins)  # lists can't be dictionary keys; tuples can 😼
        return ways(amount, values, 0)

    counter.stats = ways
    return counter


# O(2^D) time/O(D + m) space: take or skip a coin, with no cached answers.
def count_ways(amount, coins):
    counter = make_coin_counter()
    return counter(amount, coins)


# Average O(n) time/O(n) space: only run starts walk forward through unique values.
def longest_consecutive(nums):
    values = {}
    for number in nums:
        values[number] = True
    longest = 0
    for number in values:
        if number - 1 not in values:
            length = 1
            while number + length in values:
                length += 1
            if length > longest:
                longest = length
    return longest


# Average O(n) time/O(n) space: add the number of earlier complements in one pass.
def count_pairs(nums, target):
    counts = {}
    pairs = 0
    for number in nums:
        pairs += counts.get(target - number, 0)
        counts[number] = counts.get(number, 0) + 1
    return pairs


# O(1) factory setup; the returned function has its own call counter.
def make_fib_naive():
    # O(2^n) time/O(n) stack: both branches repeat the smaller problems.
    @track_calls
    def fib(n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Fibonacci needs a non-negative integer.")
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    return fib


# O(1) factory setup; each returned Fibonacci function gets a fresh cache.
def make_fib():
    # O(n) cold time/O(n) space: each n is computed once, counting arithmetic as O(1).
    @memoize()
    def fib(n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Fibonacci needs a non-negative integer.")
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    return fib


# O(A*m) time/O(A + m) space: one totals list, updated once per denomination.
def count_ways_iterative(amount, coins):
    if not isinstance(amount, int):
        raise ValueError("Amount must be an integer.")
    values = prepare_coins(coins)
    if amount < 0:
        return 0
    totals = [0] * (amount + 1)
    totals[0] = 1
    for coin in values:
        for number in range(coin, amount + 1):
            totals[number] += totals[number - coin]
    return totals[amount]


if __name__ == "__main__":
    print("Fibonacci calls, with a fresh cache for each row:")
    for n in (10, 20, 25):
        naive = make_fib_naive()
        fib = make_fib()
        first = naive(n)
        second = fib(n)
        print("n:", n, "Match:", first == second, "Naive calls:", naive.calls,
              "Cached calls:", fib.calls, "Hits:", fib.hits, "Misses:", fib.misses)
    for n in (35, 90):
        fib = make_fib()
        print("fib(" + str(n) + "):", fib(n), "Misses:", fib.misses)

    coins = [1, 5, 10, 25, 50]
    naive = make_coin_counter()
    fast = make_coin_counter(cached=True)
    print("Naive coin ways:", naive(100, coins), "Calls:", naive.stats.calls)
    print("Memoized coin ways:", fast(100, coins), "Hits:", fast.stats.hits,
          "Misses:", fast.stats.misses, "Calls:", fast.stats.calls)
    for amount, coins in ((5, [1, 2, 5]), (10, [2, 5, 3, 6]), (0, [1, 2]),
                          (3, [2]), (-1, [1]), (4, [1, 1, 2])):
        print("Coin check:", amount, coins, "→", count_ways(amount, coins),
              "Iterative:", count_ways_iterative(amount, coins))

    for nums in ([100, 4, 200, 1, 3, 2], [], [5, 5, 5], [0, -1, 1, 2, -2]):
        print("Longest consecutive:", nums, "→", longest_consecutive(nums))
    for nums, target in (([1, 5, 7, -1, 5], 6), ([1, 1, 1], 2), ([], 5)):
        print("Pair count:", nums, target, "→", count_pairs(nums, target))

    # O(1) time/space per calculation; the decorator holds at most three results.
    @memoize(max_size=3)
    def square(number):
        return number * number

    for number in (1, 2, 3, 4, 5):
        print("FIFO:", number, "→", square(number), "Cache size:", len(square.cache))
    before = square.misses
    square(1)
    print("Evicted 1 is a miss again:", square.misses == before + 1)

    # O(1) calculation; LRU changes cache order on a hit, FIFO leaves it alone.
    @memoize(max_size=3, lru=True)
    def identity(number):
        return number

    for number in (1, 2, 3, 1, 4):
        identity(number)
    print("LRU keeps recently used 1:", (1,) in identity.cache)
    print("LRU evicts 2:", (2,) not in identity.cache)
    print("Iterative amount 10000:", count_ways_iterative(10000, [1, 5, 10, 25, 50]))

    print("A = amount, m = coin types, c = smallest coin, D = A/c + m.")
    print("K = key-hashing work, F = function work, C = stored cache entries.")
    print("Bounds assume average dictionary operations and unit-cost arithmetic.")
    rows = [
        ("memoize / decorate setup", "O(1)", "O(1)"),
        ("wrapper: hit / miss", "O(K) / O(K + F)", "O(C) entries + results"),
        ("track_calls / counted wrapper", "O(1) setup / O(F) call", "O(1) extra per frame"),
        ("prepare_coins", "O(m)", "O(m)"),
        ("make_coin_counter setup", "O(1)", "O(1)"),
        ("count_ways / naive ways", "O(2^D)", "O(D + m)"),
        ("counter / memoized ways", "O(A*m^2)", "O(A*m + D + m)"),
        ("longest_consecutive", "O(n)", "O(n)"),
        ("count_pairs", "O(n)", "O(n)"),
        ("make_fib_naive / make_fib setup", "O(1)", "O(1)"),
        ("naive fib", "O(2^n)", "O(n)"),
        ("memoized fib: cold / cached", "O(n) / O(1)", "O(n)"),
        ("count_ways_iterative", "O(A*m)", "O(A + m)"),
        ("square / identity body", "O(1)", "O(1)"),
    ]
    print("function name".ljust(34) + " | " + "time complexity".ljust(20)
          + " | space complexity")
    for name, time, space in rows:
        print(name.ljust(34) + " | " + time.ljust(20) + " | " + space)

# 1. Naive fib is O(2^n); memoized is O(n), cos repeated n values reuse results.
# 2. longest_consecutive is already linear; caching helps only an identical repeat.
#    A list can't be a cache key without conversion, which itself takes O(n).
# 3. Hashes locate dictionary slots in O(1) average; collisions can force O(n) work.
# 4. Caching huge changing inputs wastes memory; side effects may be skipped on hits.
# 5. A three-entry cache uses O(1) entries, but frequent evictions repeat calculations.
#    Bytes still depend on key/result sizes; FIFO is insertion order, not recent use.
# Bonus: amount 10000 favours bottom-up: O(A + m) space and no recursion-depth limit.
# Coin memo has O(A*m) states; tuple hashing adds O(m) work per lookup in this version.
