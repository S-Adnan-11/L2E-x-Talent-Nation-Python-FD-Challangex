"""Week 8 examples, independent cross-checks, state and constraint checks."""

import ast
from contextlib import redirect_stdout
from copy import deepcopy
import importlib.util
import io
from itertools import product
from math import factorial
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
WEEK8 = ROOT / "soluxionz/week8x"


def loadx(filename):
    spec = importlib.util.spec_from_file_location(filename.removesuffix(".py"), WEEK8 / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Week8Tests(unittest.TestCase):
    def test_binary_search_examples_and_comparison_counts(self):
        module = loadx("binary_srch.py")
        for nums, target, expected in (
            ([1, 3, 3, 3, 5, 8], 3, (1, 4)), ([1, 3, 5, 8], 4, (-1, 4)),
            ([], 7, (-1, 0)), ([5], 5, (0, 1)), ([5], 4, (-1, 2)),
            ([-3, -3, -3, 0, 8], -3, (0, 2)), ([2, 2, 2, 2], 2, (0, 2)),
        ):
            original = nums.copy()
            self.assertEqual(module.binary_search(nums, target), expected)
            self.assertEqual(module.binary_search_recursive(nums, target), expected)
            self.assertEqual(nums, original)
        nums = list(range(100000))
        index, comparisons = module.binary_search(nums, 99999)
        self.assertEqual(index, 99999)
        self.assertLess(comparisons, 40)

    def test_binary_search_against_leftmost_reference(self):
        module = loadx("binary_srch.py")
        for size in range(5):
            for items in product((-1, 0, 1), repeat=size):
                nums = sorted(items)
                for target in (-2, -1, 0, 1, 2):
                    expected = nums.index(target) if target in nums else -1
                    self.assertEqual(module.binary_search(nums, target)[0], expected)
                    self.assertEqual(module.binary_search_recursive(nums, target), module.binary_search(nums, target))

    def test_rle_round_trips_and_bad_encodings(self):
        module = loadx("rle_again.py")
        for text, encoded in (("aaabbc", "a3b2c1"), ("aaaaaaaaaaaab", "a12b1"),
                              ("", ""), ("a", "a1"), ("aabbaa", "a2b2a2"),
                              ("AaAa", "A1a1A1a1"), ("z" * 120, "z120")):
            self.assertEqual(module.rle_encode(text), encoded)
            self.assertEqual(module.rle_decode(encoded), text)
            self.assertEqual(module.rle_decode(module.rle_encode(text)), text)
        self.assertEqual(module.compression_ratio("abcd"), 2)
        self.assertEqual(module.compression_ratio(""), 0.0)
        self.assertLess(module.compression_ratio("a" * 12), 1)
        for encoded in ("a", "a0", "12a", "a-2", "a2b", "a2!1"):
            with self.assertRaises(ValueError):
                module.rle_decode(encoded)
        for text in ("a1", "hi there", "!"):
            with self.assertRaises(ValueError):
                module.rle_encode(text)

    def test_max_subarray_examples(self):
        module = loadx("max_subarrayx.py")
        for nums, expected in (([-2, 1, -3, 4, -1, 2, 1, -5, 4], (6, 3, 6)),
                               ([5], (5, 0, 0)), ([-3, -1, -2], (-1, 1, 1)),
                               ([], (0, -1, -1)), ([0, 0], (0, 0, 0)),
                               ([1, -1, 1], (1, 0, 0)), ([0, 1], (1, 0, 1))):
            original = nums.copy()
            self.assertEqual(module.max_subarray_brute(nums), expected)
            self.assertEqual(module.max_subarray_fast(nums), expected)
            self.assertEqual(nums, original)

    def test_max_subarray_against_all_slice_sums(self):
        module = loadx("max_subarrayx.py")
        for size in range(1, 6):
            for items in product((-2, -1, 0, 1, 2), repeat=size):
                nums = list(items)
                candidates = [(sum(nums[start:end + 1]), start, end)
                              for start in range(size) for end in range(start, size)]
                expected = max(candidates, key=lambda row: (row[0], -row[1], -row[2]))
                self.assertEqual(module.max_subarray_brute(nums), expected)
                self.assertEqual(module.max_subarray_fast(nums), expected)

    def test_roman_examples_and_all_round_trips(self):
        module = loadx("ass_roma_back.py")
        for number, expected in ((1, "I"), (3, "III"), (4, "IV"), (9, "IX"),
                                 (40, "XL"), (58, "LVIII"), (90, "XC"), (400, "CD"),
                                 (900, "CM"), (1994, "MCMXCIV"), (3999, "MMMCMXCIX")):
            self.assertEqual(module.integer_to_roman(number), expected)
        for number in (-1, 0, 4000, 1.5):
            self.assertEqual(module.integer_to_roman(number), "")
        for number in range(1, 4000):
            self.assertEqual(module.roman_to_integer(module.integer_to_roman(number)), number)
        self.assertEqual(module.roman_to_integer("mcmxciv"), 1994)
        for roman in ("", "ABC", "IX?"):
            with self.assertRaises(ValueError):
                module.roman_to_integer(roman)

    def test_hanoi_moves_are_legal_and_complete(self):
        hanoi = loadx("hanoi_towerz.py").hanoi
        for n in range(13):
            moves = hanoi(n, "A", "C", "B")
            self.assertEqual(len(moves), 2 ** n - 1)
            rods = {"A": list(range(n, 0, -1)), "B": [], "C": []}
            for source, target in moves:
                self.assertTrue(rods[source])
                disk = rods[source].pop()
                self.assertTrue(not rods[target] or rods[target][-1] > disk)
                rods[target].append(disk)
            self.assertEqual(rods, {"A": [], "B": [], "C": list(range(n, 0, -1))})
        self.assertEqual(hanoi(1, "A", "C", "B"), [("A", "C")])
        with self.assertRaises(ValueError):
            hanoi(-1, "A", "C", "B")

    def test_bubble_sort_in_place_and_work_counts(self):
        bubble = loadx("bubble_sortx.py").bubble_sort
        for nums in ([5, 1, 4, 2, 8], [], [3], [2, 2, 1], [-4, 0, -2, -4]):
            for descending in (False, True):
                values = nums.copy()
                original_id = id(values)
                comparisons, swaps = bubble(values, descending=descending)
                self.assertEqual(values, sorted(nums, reverse=descending))
                self.assertEqual(id(values), original_id)
                self.assertGreaterEqual(comparisons, swaps)
        self.assertEqual(bubble([1, 2, 3, 4, 5]), (4, 0))
        self.assertEqual(bubble([5, 4, 3, 2, 1]), (10, 10))
        self.assertEqual(bubble([]), (0, 0))
        self.assertEqual(bubble([1]), (0, 0))

    def test_pascal_rows_and_single_list_bonus(self):
        module = loadx("pascalx.py")
        self.assertEqual(module.pascal_rows(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
        self.assertEqual(module.pascal_rows(0), [])
        self.assertEqual(module.pascal_rows(1), [[1]])
        for n in range(1, 13):
            rows = module.pascal_rows(n)
            self.assertEqual(module.pascal_row(n - 1), rows[-1])
            self.assertEqual(sum(rows[-1]), 2 ** (n - 1))
            self.assertEqual(rows[-1], rows[-1][::-1])
            self.assertEqual(len(set(map(id, rows))), n)
        for function in (module.pascal_rows, module.pascal_row):
            with self.assertRaises(ValueError):
                function(-1)

    def test_hangman_examples_repeats_and_early_stops(self):
        play = loadx("hangmanx.py").play_hangman
        cases = [
            ("apple", ["a", "z", "p", "l", "e"], 3, ("won", "apple", ["z"])),
            ("python", ["a", "b", "c", "d"], 3, ("lost", "______", ["a", "b", "c"])),
            ("python", ["p", "p", "y"], 5, ("playing", "py____", [])),
            ("a", [], 3, ("playing", "_", [])),
            ("loop", ["l", "o", "o", "p"], 3, ("won", "loop", [])),
            ("code", ["z", "z", "c", "o"], 2, ("playing", "co__", ["z"])),
            ("z", ["z", "bad"], 1, ("won", "z", [])),
            ("", ["a"], 3, ("won", "", [])),
            ("a", ["a"], 0, ("lost", "_", [])),
        ]
        for word, guesses, attempts, expected in cases:
            original = guesses.copy()
            self.assertEqual(play(word, guesses, attempts), expected)
            self.assertEqual(guesses, original)
        for word, guesses, attempts in (("a", ["aa"], 2), ("A", [], 2), ("a", [], -1)):
            with self.assertRaises(ValueError):
                play(word, guesses, attempts)

    def test_subsets_and_permutations_counts_and_fresh_lists(self):
        module = loadx("subsets_permz.py")
        for n in range(9):
            items = list(range(n))
            original = items.copy()
            subset_rows = module.subsets(items)
            permutation_rows = module.permutations(items)
            self.assertEqual(len(subset_rows), 2 ** n)
            self.assertEqual(len(permutation_rows), factorial(n))
            self.assertEqual(len(set(map(tuple, subset_rows))), 2 ** n)
            self.assertEqual(len(set(map(tuple, permutation_rows))), factorial(n))
            self.assertEqual(len(set(map(id, subset_rows))), len(subset_rows))
            self.assertEqual(len(set(map(id, permutation_rows))), len(permutation_rows))
            self.assertEqual(items, original)
        for function in (module.subsets, module.permutations):
            self.assertEqual(function([]), [[]])
            first = function([1, 2])
            second = function([1, 2])
            snapshot = deepcopy(second)
            first[0].append(99)
            self.assertEqual(second, snapshot)
        self.assertEqual({tuple(row) for row in module.subsets_with_sum([-2, 1, 2], 0)}, {(), (-2, 2)})
        self.assertEqual(module.subsets_with_sum([], 0), [[]])
        self.assertEqual(module.subsets_with_sum([], 1), [])
        self.assertEqual({tuple(row) for row in module.subsets_with_sum([1, 2, 3], 3)}, {(3,), (1, 2)})

    def test_coin_variants_examples_edges_and_input_preservation(self):
        module = loadx("performance_labx.py")
        cached = module.make_coin_counter(cached=True)
        for amount, coins, expected in (
            (5, [1, 2, 5], 4), (10, [2, 5, 3, 6], 5), (0, [1, 2], 1),
            (3, [2], 0), (100, [1, 5, 10, 25, 50], 292),
            (0, [], 1), (3, [], 0), (-1, [1, 2], 0), (4, [1, 1, 2], 3),
        ):
            original = coins.copy()
            self.assertEqual(module.count_ways(amount, coins), expected)
            self.assertEqual(cached(amount, coins), expected)
            self.assertEqual(module.count_ways_iterative(amount, coins), expected)
            self.assertEqual(coins, original)
        for coins in ([], [1], [2], [1, 2], [2, 3, 5], [5, 2, 2]):
            for amount in range(15):
                self.assertEqual(module.count_ways(amount, coins), module.count_ways_iterative(amount, coins))
                self.assertEqual(cached(amount, coins), module.count_ways_iterative(amount, coins))
        self.assertEqual(cached.stats.calls, cached.stats.hits + cached.stats.misses)
        self.assertGreater(cached.stats.hits, 0)
        for coins in ([0, 1], [-1, 2], [1.5]):
            for function in (module.count_ways, cached, module.count_ways_iterative):
                with self.assertRaises(ValueError):
                    function(3, coins)
        self.assertEqual(module.count_ways_iterative(10000, [1]), 1)

    def test_memoize_fifo_lru_stats_and_independent_caches(self):
        module = loadx("performance_labx.py")
        for lru, evicted in ((False, 1), (True, 2)):
            cached = module.memoize(max_size=3, lru=lru)(lambda value: value * value)
            for number in (1, 2, 3, 1, 4):
                self.assertEqual(cached(number), number * number)
                self.assertLessEqual(len(cached.cache), 3)
            self.assertNotIn((evicted,), cached.cache)
            self.assertEqual((cached.hits, cached.misses, cached.calls), (1, 4, 5))
            before = cached.misses
            cached(evicted)
            self.assertEqual(cached.misses, before + 1)
            self.assertEqual(cached.calls, cached.hits + cached.misses)
        uncached = module.memoize(max_size=0)(lambda n: n)
        uncached(1)
        uncached(1)
        self.assertEqual((uncached.hits, uncached.misses, uncached.calls), (0, 2, 2))
        self.assertEqual(uncached.cache, {})
        first = module.memoize()(lambda *args: args)
        second = module.memoize()(lambda *args: args)
        self.assertEqual(first("a", 2), ("a", 2))
        self.assertEqual(first("a", 2), ("a", 2))
        self.assertEqual(first(), ())
        self.assertEqual((first.hits, second.hits), (1, 0))
        self.assertEqual(second.cache, {})
        for invalid in (-1, 1.5, "3"):
            with self.assertRaises(ValueError):
                module.memoize(max_size=invalid)

    def test_lab_fibonacci_results_and_counters(self):
        module = loadx("performance_labx.py")
        for n, expected, calls in ((0, 0, 1), (1, 1, 1), (10, 55, 177), (20, 6765, 21891), (25, 75025, 242785)):
            naive = module.make_fib_naive()
            cached = module.make_fib()
            self.assertEqual(naive(n), expected)
            self.assertEqual(naive.calls, calls)
            self.assertEqual(cached(n), expected)
            self.assertEqual(cached.calls, cached.hits + cached.misses)
            self.assertLessEqual(cached.misses, n + 1)
            misses = cached.misses
            self.assertEqual(cached(n), expected)
            self.assertEqual(cached.misses, misses)
        cached = module.make_fib()
        self.assertEqual(cached(35), 9227465)
        self.assertEqual(cached(90), 2880067194370816120)
        self.assertEqual(cached.misses, 91)

    def test_dictionary_algorithms_against_small_references(self):
        module = loadx("performance_labx.py")
        for nums, expected in (([100, 4, 200, 1, 3, 2], 4), ([], 0), ([5, 5, 5], 1), ([0, -1, 1, 2, -2], 5), ([1, 1, 2, 3, 3, 4], 4)):
            original = nums.copy()
            self.assertEqual(module.longest_consecutive(nums), expected)
            self.assertEqual(nums, original)
        for nums, target, expected in (([1, 5, 7, -1, 5], 6, 3), ([1, 1, 1], 2, 3), ([], 5, 0), ([0, 0, 0, 0], 0, 6), ([-2, -1, 0, 1, 2], 0, 2)):
            self.assertEqual(module.count_pairs(nums, target), expected)
        for size in range(5):
            for items in product((-1, 0, 1), repeat=size):
                nums = list(items)
                for target in (-2, 0, 2):
                    expected = sum(1 for i in range(size) for j in range(i + 1, size) if nums[i] + nums[j] == target)
                    self.assertEqual(module.count_pairs(nums, target), expected)
        self.assertEqual(module.longest_consecutive([0] * 5000 + list(range(10000))), 10000)

    def test_required_printed_demos_and_interactive_hangman(self):
        for filename, expected in (
            ("binary_srch.py", "Match"), ("rle_again.py", "Round trip: True"),
            ("max_subarrayx.py", "Match"), ("ass_roma_back.py", "All round trips passed"),
            ("hanoi_towerz.py", "Count check 12 → True"), ("bubble_sortx.py", "Comparisons: 4 Swaps: 0"),
            ("pascalx.py", "One-list bonus, row 4: [1, 4, 6, 4, 1]"),
            ("subsets_permz.py", "Permutations: 40320 Expected: 40320"),
            ("performance_labx.py", "Memoized coin ways: 292"),
        ):
            result = subprocess.run([sys.executable, str(WEEK8 / filename)], text=True, capture_output=True, timeout=15)
            self.assertEqual(result.returncode, 0, (filename, result.stderr))
            self.assertIn(expected, result.stdout)
            self.assertNotIn("Mismatch", result.stdout)
            self.assertNotIn("Round trip: False", result.stdout)
        result = subprocess.run([sys.executable, str(WEEK8 / "hangmanx.py")], input="a\n2\nzz\nz\nz\na\n", text=True, capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("One a-z letter pls.", result.stdout)
        self.assertIn("a | Remaining: 1", result.stdout)
        self.assertTrue(result.stdout.rstrip().endswith("won"))

    def test_imports_are_silent_and_constraints_are_respected(self):
        output = io.StringIO()
        trees = {}
        with redirect_stdout(output):
            for path in WEEK8.glob("*.py"):
                loadx(path.name)
                trees[path.name] = ast.parse(path.read_text())
        self.assertEqual(output.getvalue(), "")
        forbidden = {
            "binary_srch.py": {"index", "count"},
            "max_subarrayx.py": {"max", "min", "sum"},
            "bubble_sortx.py": {"sort", "sorted", "min", "max"},
            "pascalx.py": {"center", "factorial"},
            "performance_labx.py": {"sort", "sorted", "set", "sum"},
        }
        for filename, tree in trees.items():
            for node in ast.walk(tree):
                self.assertNotIsInstance(node, (ast.Import, ast.ImportFrom), filename)
                if isinstance(node, ast.Call):
                    name = node.func.id if isinstance(node.func, ast.Name) else getattr(node.func, "attr", "")
                    self.assertNotIn(name, forbidden.get(filename, set()), filename)
            functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
            for name, function in functions.items():
                if name == "main":
                    continue
                for node in ast.walk(function):
                    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                        self.assertNotIn(node.func.id, {"print", "input"}, (filename, name))
            if filename == "binary_srch.py":
                for function in functions.values():
                    self.assertFalse(any(isinstance(node, (ast.In, ast.NotIn)) for node in ast.walk(function)))
                self.assertEqual(sum(isinstance(node, ast.While) for node in ast.walk(functions["binary_search"])), 1)
            if filename == "rle_again.py":
                self.assertFalse(any(isinstance(node, ast.For) for function in functions.values() for node in ast.walk(function)))
            if filename == "hanoi_towerz.py":
                self.assertFalse(any(isinstance(node, (ast.For, ast.While, ast.comprehension)) for node in ast.walk(functions["hanoi"])))
            if filename == "max_subarrayx.py":
                self.assertEqual(sum(isinstance(node, (ast.For, ast.While)) for node in ast.walk(functions["max_subarray_fast"])), 1)
                self.assertFalse(any(isinstance(node, ast.Slice) for function in functions.values() for node in ast.walk(function)))
            if filename == "pascalx.py":
                self.assertFalse(any(isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp)) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()
