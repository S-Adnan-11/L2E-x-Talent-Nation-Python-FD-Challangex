# O(1) setup/space: a fresh dictionary belongs to each decorated recursive calculation.
def memoize(function):
    cache = {}

    # Average O(1) hit, plus function work on misses; O(S) entries for S visited states.
    def wrapper(*args):
        wrapper.calls += 1
        if args not in cache:
            cache[args] = function(*args)
        return cache[args]

    wrapper.calls = 0
    return wrapper


# O(3^(m+n)) time/O(m+n) stack: mismatches branch into three smaller suffix problems.
def edit_naive(a, b, counter=None):
    # O(3^(m+n)) total time/O(m+n) stack; counters are optional measurement only.
    def distance(i, j):
        if counter is not None:
            counter[0] += 1
        if i == len(a):
            return len(b) - j
        if j == len(b):
            return len(a) - i
        if a[i] == b[j]:
            return distance(i + 1, j + 1)
        return 1 + min(distance(i + 1, j), distance(i, j + 1), distance(i + 1, j + 1))

    return distance(0, 0)


# O((m+1)*(n+1)) time/space: cache index pairs rather than repeatedly hashing substrings.
def edit_memo(a, b, counter=None):
    # O((m+1)*(n+1)) total time/space: each pair of suffix indices is solved once.
    @memoize
    def distance(i, j):
        if i == len(a):
            return len(b) - j
        if j == len(b):
            return len(a) - i
        if a[i] == b[j]:
            return distance(i + 1, j + 1)
        return 1 + min(distance(i + 1, j), distance(i, j + 1), distance(i + 1, j + 1))

    result = distance(0, 0)
    if counter is not None:
        counter[0] += distance.calls
    return result


# O((m+1)*(n+1)) time/space: fill a table of prefix distances, including empty prefixes.
def edit_table(a, b):
    table = []
    for i in range(len(a) + 1):
        table.append([0] * (len(b) + 1))
    for i in range(len(a) + 1):
        table[i][0] = i
    for j in range(len(b) + 1):
        table[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
    return table[-1][-1]


# O((m+1)*(n+1)) time/O(min(m,n)+1) space: only the previous and current rows are needed.
def edit_two_rows(a, b):
    if len(b) > len(a):
        a, b = b, a
    previous = list(range(len(b) + 1))
    current = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        current[0] = i
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                current[j] = previous[j - 1]
            else:
                current[j] = 1 + min(previous[j], current[j - 1], previous[j - 1])
        previous, current = current, previous
    return previous[-1]


if __name__ == "__main__":
    cases = [("kitten", "sitting"), ("", "abc"), ("same", "same"), ("flaw", "lawn"),
             ("abcdefgh", "ijklmnop"), ("distance", "instance"), ("a", ""), ("", "")]
    for a, b in cases:
        naive_calls = [0]
        memo_calls = [0]
        first = edit_naive(a, b, naive_calls)
        second = edit_memo(a, b, memo_calls)
        third = edit_table(a, b)
        fourth = edit_two_rows(a, b)
        print("Pair:", repr(a), repr(b), "Match:", first == second == third == fourth)
        print("function".ljust(16) + " | result | calls/table cells | time complexity | space complexity")
        rows = [("edit_naive", first, naive_calls[0], "O(3^(m+n))", "O(m+n)"),
                ("edit_memo", second, memo_calls[0], "O((m+1)*(n+1))", "O((m+1)*(n+1))"),
                ("edit_table", third, (len(a) + 1) * (len(b) + 1), "O((m+1)*(n+1))", "O((m+1)*(n+1))"),
                ("edit_two_rows", fourth, (len(a) + 1) * (len(b) + 1), "O((m+1)*(n+1))", "O(min(m,n)+1)")]
        for name, result, work, time, space in rows:
            print(name.ljust(16) + " | " + str(result) + " | " + str(work).ljust(17)
                  + " | " + time + " | " + space)

# 1. Naive recursion has an O(3^(m+n)) bound: mismatches revisit the same suffix pairs.
# 2. Memo and full table use O((m+1)*(n+1)) time/space; memo also has a linear call stack.
# 3. For 5000-letter strings, use two iterative rows: no recursive depth, far less memory.
# 4. A cell needs the previous row and its left neighbour in the current row; swapping
#    those two rows gives O(min(m,n)+1) space instead of storing the entire grid.
