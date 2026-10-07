def memoize(funcx):
    cachex = {}

    def cachedx(*args):
        if args not in cachex:
            cachex[args] = funcx(*args)
        return cachex[args]

    # Each decorated function gets its own cache. No global stash 😼
    return cachedx


@memoize
def fib(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Fibonacci needs a non-negative whole number.")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@memoize
def count_ways(n):
    if not isinstance(n, int):
        raise ValueError("Step count must be a whole number.")
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_ways(n - 1) + count_ways(n - 2)


if __name__ == "__main__":
    print("fib(35):", fib(35))
    print("Ways to climb 5 steps:", count_ways(5))
