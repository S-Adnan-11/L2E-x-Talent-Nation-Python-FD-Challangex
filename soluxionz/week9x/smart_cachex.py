# O(1) setup/space: choose policy and limits before creating any entries.
def make_cache(max_size, recent, max_age=None):
    if max_size is not None and (type(max_size) is not int or max_size < 0):
        raise ValueError("Cache size must be None or a non-negative integer.")
    if max_age is not None and (type(max_age) is not int or max_age < 0):
        raise ValueError("Call age must be None or a non-negative integer.")

    # O(1) setup/space: each decorated function gets independent dictionaries.
    def decorate(function):
        cache = {}
        inserted = {}

        # O(e+1) expected time/O(1) extra: remove only the e expired entries at the front.
        def expire(now):
            if max_age is None:
                return
            while inserted:
                oldest = next(iter(inserted))
                if now - inserted[oldest] <= max_age:
                    break
                del inserted[oldest]
                del cache[oldest]

        # Hit O(H+e+1), miss adds function work; O(C) entries, H=key hashing, e=expirations.
        def wrapper(*args):
            hash(args)
            wrapper.calls += 1
            expire(wrapper.calls)
            if args in cache:
                wrapper.hits += 1
                result = cache[args]
                if recent:
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
                if max_age is not None:
                    del inserted[oldest]
            cache[args] = result
            if max_age is not None:
                inserted[args] = wrapper.calls
            return result

        # O(C) time/space: return a fresh list of keys without exposing the dictionary.
        def keys():
            return list(cache)

        # O(C) time/O(1) extra: discard entries and reset the wrapper's counters.
        def clear():
            cache.clear()
            inserted.clear()
            wrapper.hits = 0
            wrapper.misses = 0
            wrapper.calls = 0

        wrapper.hits = 0
        wrapper.misses = 0
        wrapper.calls = 0
        wrapper.keys = keys
        wrapper.clear = clear
        return wrapper

    return decorate


# O(1) setup/space: hits move their dictionary key to the newest position.
def lru_cache(max_size, max_age=None):
    return make_cache(max_size, recent=True, max_age=max_age)


# O(1) setup/space: hits leave insertion order alone.
def fifo_cache(max_size, max_age=None):
    return make_cache(max_size, recent=False, max_age=max_age)


if __name__ == "__main__":
    for name, factory in (("LRU", lru_cache), ("FIFO", fifo_cache)):
        # O(1) time/space for the calculation; cache bookkeeping belongs to the wrapper.
        @factory(max_size=2)
        def square(x):
            return x * x

        for number in (1, 2, 1, 3, 2, 1):
            print(name, number, "→", square(number), "Keys:", square.keys())
        print(name, "hits:", square.hits, "misses:", square.misses, "calls:", square.calls)
        square.clear()
        print("Cleared:", square.keys(), square.hits, square.misses, square.calls)

    # O(1) time/space: demonstrate keys with several positional arguments.
    @lru_cache(max_size=None)
    def add(a, b):
        return a + b

    print("Several args:", add(2, 3), add(2, 3), add.keys())
    for size in (0, None):
        # O(1) time/space calculation, without another cache underneath this demo.
        function = fifo_cache(size)(lambda a, b: a + b)
        function(1, 2)
        function(1, 2)
        print("Size:", size, "Hits:", function.hits, "Keys:", function.keys())

    # O(1) time/space calculation; birth age uses call count and is not refreshed by hits.
    @lru_cache(max_size=2, max_age=2)
    def identity(x):
        return x

    for number in (1, 2, 1, 1, 3):
        print("Call-age bonus:", number, "→", identity(number),
              "Hits:", identity.hits, "Misses:", identity.misses, "Keys:", identity.keys())

# 1. FIFO wins this sequence; LRU favours repeated hot keys, while FIFO can survive scans
#    that temporarily push hot keys aside. Neither policy wins every access pattern.
# 2. A fixed-size hashable key gives an average O(1) hit without expiry: delete/reinsert
#    replaces an O(C) list search. Expiry costs O(e+1), amortized over expired entries.
#    Collisions and large key hashes can still cost more than constant time.
# 3. A cache of recently opened image thumbnails can evict images nobody uses anymore.
# Bonus: age means calls since insertion, not last use; expire only when age > max_age.
