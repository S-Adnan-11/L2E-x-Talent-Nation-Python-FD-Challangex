"""Examples, edge cases, purity checks and the challenge restrictions."""

import ast
from contextlib import redirect_stdout
from copy import deepcopy
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]


def loadx(relative_path):
    pathx = ROOT / "soluxionz" / relative_path
    specx = importlib.util.spec_from_file_location(relative_path.replace("/", "_"), pathx)
    modulex = importlib.util.module_from_spec(specx)
    specx.loader.exec_module(modulex)
    return modulex


class SoluxionzTests(unittest.TestCase):
    def test_calculator_operations(self):
        calcx = loadx("week3x/Simple_Calculator.py").simple_calcx
        for firstx, secondx, operatorx, expectedx in (
            (0, 5, "+", 5), (5, 2, "*", 10), (5, 2, "-", 3),
            (5, 2, "/", 2.5), (1.25, 2.5, "+", 3.75),
        ):
            with self.subTest(operator=operatorx):
                self.assertEqual(calcx(firstx, secondx, operatorx), expectedx)
        self.assertIn("zero", calcx(5, 0, "/"))
        self.assertIn("Error", calcx(5, 2, "**"))

    def test_calculator_undo_and_invalid_commands(self):
        commandx = [sys.executable, str(ROOT / "soluxionz/week3x/Simple_Calculator.py")]
        sessionx = "undo\n+ 5\n* 2\n/ 0\n** 2\n+ nope\n+\n+ nan\n+ inf\nundo\nundo\nundo\n+ 2.5\n/ 2\nquit\n"
        resultx = subprocess.run(commandx, input=sessionx, text=True, capture_output=True, timeout=5)
        self.assertEqual(resultx.returncode, 0, resultx.stderr)
        self.assertIn("Division by zero", resultx.stdout)
        self.assertIn("finite number", resultx.stdout)
        self.assertEqual(resultx.stdout.count("Nothing to undo yet."), 2)
        resultsx = [linex.split("Result: ")[1] for linex in resultx.stdout.splitlines() if "Result: " in linex]
        self.assertEqual(resultsx, ["0", "5", "10", "5", "0", "2.5", "1.25"])
        eofx = subprocess.run(commandx, input="", text=True, capture_output=True, timeout=5)
        self.assertEqual(eofx.returncode, 0, eofx.stderr)

    def test_palindromes(self):
        week3x = loadx("week3x/palindromex.py")
        week4x = loadx("week4x/palindromex.py")
        self.assertTrue(week4x.is_letter("A"))
        self.assertFalse(week4x.is_letter("7"))
        self.assertFalse(week4x.is_letter("?"))
        for checkx in (week3x.palindrome_checkx, week4x.is_palindrome, week4x.is_palindrome_recursive):
            for textx, expectedx in (
                ("Was it a car or a cat I saw?", True), ("Hello, World!", False),
                ("", True), ("!? ,", True), ("A", True), ("ab", False),
                ("A man, a plan, a canal: Panama!", True), ("1a1", True),
                ("1a2", False), ("a...b...a", True),
            ):
                with self.subTest(function=checkx.__name__, text=textx):
                    self.assertEqual(checkx(textx), expectedx)

    def test_student_grades(self):
        studentsx = [
            {"name": "Sam", "scores": [80, 90]},
            {"name": "David", "scores": [55, 60]},
            {"name": "No scores", "scores": []},
            {"name": "Failed", "scores": [0, 39]},
            {"name": "Sam tie", "scores": [85]},
        ]
        originalx = deepcopy(studentsx)
        expectedx = [("Sam", 85, "A"), ("David", 57.5, "C"), ("No scores", None, "N/A"), ("Failed", 19.5, "F"), ("Sam tie", 85, "A")]
        for weekx in ("week3x", "week4x"):
            modulex = loadx(f"{weekx}/gradez.py")
            resultx = modulex.student_reportx(studentsx)
            self.assertEqual(resultx[0], expectedx)
            self.assertEqual(resultx[-2:], (expectedx[0], expectedx[3]))
            grade_fnx = modulex.letter_gradex if weekx == "week3x" else modulex.grade_for
            for averagex, gradex in ((100, "A"), (70, "A"), (69.9, "B"), (60, "B"), (59.9, "C"), (50, "C"), (49.9, "D"), (45, "D"), (44.9, "E"), (40, "E"), (39.9, "F"), (0, "F")):
                self.assertEqual(grade_fnx(averagex), gradex)
            self.assertEqual(modulex.averagex([]), None)
            self.assertEqual(modulex.student_reportx([])[-2:], (None, None))
            self.assertEqual(modulex.student_reportx([{"name": "Empty", "scores": []}])[-2:], (None, None))
            with self.assertRaises(ValueError):
                modulex.averagex([101])
            if weekx == "week4x":
                self.assertEqual(resultx[1], [expectedx[0], expectedx[1], expectedx[4]])
                self.assertEqual(modulex.rows_comprehensionx(studentsx), expectedx)
        self.assertEqual(studentsx, originalx)

    def test_second_largest(self):
        funcsx = (
            loadx("week3x/second_largest.py").second_largestx,
            loadx("week4x/second_largestx.py").second_largest,
            loadx("week4x/reduce_bonuz.py").second_largest_reduce,
        )
        for checkx in funcsx:
            for numsx, expectedx in (
                ([10, 5, 8, 20, 15], 15), ([4, 9, 2, 9, 7], 7),
                ([], None), ([9], None), ([9, 9, 9], None),
                ([-10, -2, -5, -2], -5), ([1, 0, 1], 0),
                ([2, 1, 3], 2), ([3, 2, 1], 2), ([1.5, 2.5, 2.5], 1.5),
            ):
                with self.subTest(function=checkx.__name__, numbers=numsx):
                    originalx = numsx.copy()
                    self.assertEqual(checkx(numsx), expectedx)
                    self.assertEqual(numsx, originalx)
        stepx = loadx("week4x/second_largestx.py").step
        self.assertEqual(stepx(9, 7, 9), (9, 7))
        self.assertEqual(stepx(9, 7, 10), (10, 9))

    def test_word_frequency(self):
        week3x = loadx("week3x/word_frex.py")
        week4x = loadx("week4x/word_freqx.py")
        bonusx = loadx("week4x/reduce_bonuz.py")
        for textx, expectedx, winnerx in (
            ("Python is fun, and Python is powerful!", {"python": 2, "is": 2, "fun": 1, "and": 1, "powerful": 1}, "python"),
            ("HELLO,hello. world!", {"hello": 2, "world": 1}, "hello"),
            ("  \t\n", {}, ""), ("...!?", {}, ""),
            ("a-b a; b", {"a": 2, "b": 2}, "a"),
        ):
            self.assertEqual(week3x.word_frequencyx(textx), (expectedx, winnerx))
            freqx = week4x.count_words(week4x.clean_wordsx(textx))
            originalx = freqx.copy()
            self.assertEqual(freqx, expectedx)
            self.assertEqual(week4x.most_frequent(freqx), winnerx)
            self.assertEqual(bonusx.most_frequent_reduce(freqx), winnerx)
            self.assertEqual(freqx, originalx)
        wordsx = ["Python", "PYTHON", "is"]
        self.assertEqual(week4x.count_words(wordsx), {"python": 2, "is": 1})
        self.assertEqual(wordsx, ["Python", "PYTHON", "is"])

    def test_two_sum(self):
        funcsx = (
            loadx("week3x/two_sumx.py").two_sumx,
            loadx("week4x/two_sumx.py").two_sum,
            loadx("week4x/reduce_bonuz.py").two_sum_reduce,
        )
        for checkx in funcsx:
            for numsx, targetx, expectedx in (
                ([2, 7, 11, 15], 9, [0, 1]), ([3, 3], 6, [0, 1]),
                ([3], 6, []), ([], 0, []), ([1, 2, 3], 20, []),
                ([1, 1, 4], 5, [0, 2]), ([0, 0], 0, [0, 1]),
                ([-3, 4, 1, -1], 0, [2, 3]), ([2, 4, 3, 1], 5, [0, 2]),
            ):
                originalx = numsx.copy()
                self.assertEqual(checkx(numsx, targetx), expectedx)
                self.assertEqual(numsx, originalx)
        self.assertEqual(loadx("week4x/two_sumx.py").two_sum(list(range(20000)), 39997), [19998, 19999])

    def test_anagrams(self):
        checkx = loadx("week3x/anagramz.py").anagram_checkx
        for firstx, secondx, expectedx in (
            ("listen", "silent", True), ("triangle", "integral", True),
            ("Triangle", "integral", True), ("apple", "pale", False),
            ("hello", "billion", False), ("aab", "abb", False),
            ("", "", True), ("a!", "!a", True),
        ):
            self.assertEqual(checkx(firstx, secondx), expectedx)

    def test_caesar_ciphers(self):
        for pathx in ("week3x/cipherx.py", "week4x/cipherx_again!!.py"):
            modulex = loadx(pathx)
            for textx, shiftx, modex, expectedx in (
                ("hello", 1, "encrypt", "ifmmp"), ("xyz", 2, "encrypt", "zab"),
                ("hello, world!", 3, "encrypt", "khoor, zruog!"),
                ("ifmmp", 1, "decrypt", "hello"), ("a", 1, "decrypt", "z"),
                ("Zz 123!? é", 1, "encrypt", "Aa 123!? é"),
                ("abc", -1, "encrypt", "zab"), ("abc", 53, "encrypt", "bcd"),
                ("", 9, "encrypt", ""),
            ):
                self.assertEqual(modulex.caesarx(textx, shiftx, modex), expectedx)
            messagex = "Hello, Zed! 19 😼"
            self.assertEqual(modulex.caesarx(modulex.caesarx(messagex, 17, "encrypt"), 17, "decrypt"), messagex)
            with self.assertRaises(ValueError):
                modulex.caesarx("hello", 1, "other")
        shifterx = loadx("week4x/cipherx_again!!.py").make_shifter(1)
        self.assertEqual(shifterx("Z"), "A")

    def test_number_reverser(self):
        checkx = loadx("week3x/number_reverze.py").number_reversex
        for numberx, expectedx in ((12345, 54321), (-987, -789), (1200, 21), (0, 0), (-1200, -21), (10, 1), (7, 7), (100000000000000000002, 200000000000000000001)):
            self.assertEqual(checkx(numberx), expectedx)

    def test_compose_pipe(self):
        modulex = loadx("week4x/compose_pipex.py")
        addx = lambda x: x + 1
        doublex = lambda x: x * 2
        self.assertEqual(modulex.compose(addx, doublex)(5), 11)
        self.assertEqual(modulex.pipe(addx, doublex)(5), 12)
        self.assertEqual(modulex.pipe()("same"), "same")
        self.assertEqual(modulex.pipe(addx)(5), 6)
        self.assertEqual(modulex.pipe(addx, doublex, addx)(5), 13)
        pipeline = modulex.pipe(modulex.strip, modulex.lower, modulex.remove_vowels, modulex.reverse)
        self.assertEqual(pipeline("  Hello World  "), "dlrw llh")
        for textx, expectedx in (("", ""), ("abc", "cba"), ("a", "a"), ("hi 😼", "😼 ih")):
            self.assertEqual(modulex.reverse(textx), expectedx)
            self.assertEqual(modulex.reverse_recursive(textx), expectedx)

    def test_flatten_group(self):
        modulex = loadx("week4x/flatten_groupx.py")
        for nestedx, expectedx in (
            ([1, [2, [3, [4]], 5]], [1, 2, 3, 4, 5]),
            ([], []), ([[], [[], []]], []),
            ([None, "hi", [False, (1, 2), {"a": 1}]], [None, "hi", False, (1, 2), {"a": 1}]),
        ):
            originalx = deepcopy(nestedx)
            self.assertEqual(modulex.flatten(nestedx), expectedx)
            self.assertEqual(nestedx, originalx)
        wordsx = [["apple", "avocado"], ["banana"], [["cherry"]]]
        self.assertEqual(modulex.combined(wordsx), {"a": ["apple", "avocado"], "b": ["banana"], "c": ["cherry"]})
        self.assertEqual(modulex.combined([["Apple", ""], ["avocado"]]), {"a": ["Apple", "avocado"], "": [""]})
        for groupx in (modulex.group_by, modulex.group_by_recursive):
            itemsx = [1, 2, 3, 4]
            self.assertEqual(groupx(itemsx, lambda n: n % 2), {1: [1, 3], 0: [2, 4]})
            self.assertEqual(itemsx, [1, 2, 3, 4])
            self.assertEqual(groupx([], lambda x: x), {})

    def test_memoize_fibonacci_and_stairs(self):
        modulex = loadx("week4x/fib_memoz.py")
        self.assertEqual([modulex.fib(n) for n in range(11)], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertEqual(modulex.fib(35), 9227465)
        self.assertEqual(modulex.fib(35), 9227465)
        self.assertEqual([modulex.count_ways(n) for n in range(6)], [1, 1, 2, 3, 5, 8])
        self.assertEqual(modulex.count_ways(-1), 0)
        with self.assertRaises(ValueError):
            modulex.fib(-1)
        callsx = []

        @modulex.memoize
        def joinx(*args):
            callsx.append(args)
            return "-".join(args)

        self.assertEqual(joinx("a", "b"), "a-b")
        self.assertEqual(joinx("a", "b"), "a-b")
        self.assertEqual(joinx("b", "a"), "b-a")
        self.assertEqual(callsx, [("a", "b"), ("b", "a")])
        self.assertEqual(joinx(), "")

    def test_transaction_analyzer(self):
        modulex = loadx("week4x/transactionz.py")
        transactionsx = [
            {"name": "Laptop", "amount": 250000, "type": "expense"},
            {"name": "Salary", "amount": 500000, "type": "income"},
            {"name": "Internet", "amount": 30000, "type": "expense"},
            {"name": "Freelance", "amount": 150000, "type": "income"},
            {"name": "Food", "amount": 45000, "type": "expense"},
        ]
        originalx = deepcopy(transactionsx)
        self.assertEqual(modulex.analyze(transactionsx), {
            "income": 650000, "expenses": 325000, "balance": 325000,
            "largest_expense": "Laptop", "expense_count": 3, "status": "Positive balance",
        })
        self.assertEqual(transactionsx, originalx)
        for rowsx, expectedx in (
            ([], (0, 0, 0, None, 0, "Break-even")),
            ([{"name": "Salary", "amount": 500000, "type": "income"}], (500000, 0, 500000, None, 0, "Positive balance")),
            ([{"name": "Food", "amount": 5, "type": "expense"}], (0, 5, -5, "Food", 1, "Negative balance")),
            ([{"name": "Pay", "amount": 5, "type": "income"}, {"name": "Food", "amount": 5, "type": "expense"}], (5, 5, 0, "Food", 1, "Break-even")),
            ([{"name": "Free", "amount": 0, "type": "expense"}], (0, 0, 0, "Free", 1, "Break-even")),
        ):
            self.assertEqual(tuple(modulex.analyze(rowsx).values()), expectedx)
        self.assertEqual(modulex.filter_transactions(transactionsx, lambda row: row["amount"] > 200000), transactionsx[:2])
        largestx = modulex.find_largest(modulex.get_expenses(transactionsx))
        largestx["name"] = "Changed copy"
        self.assertEqual(transactionsx, originalx)
        self.assertEqual(modulex.find_largest([]), None)

    def test_imports_and_week4_logic_are_silent(self):
        outputx = io.StringIO()
        with redirect_stdout(outputx):
            for pathx in (ROOT / "soluxionz").rglob("*.py"):
                if pathx.parent.name not in ("week3x", "week4x"):
                    continue
                loadx(str(pathx.relative_to(ROOT / "soluxionz")))
            loadx("week4x/palindromex.py").is_palindrome("aba")
            loadx("week4x/gradez.py").student_reportx([])
            loadx("week4x/word_freqx.py").count_words(["hi"])
            loadx("week4x/two_sumx.py").two_sum([1, 2], 3)
            loadx("week4x/second_largestx.py").second_largest([1, 2])
            loadx("week4x/cipherx_again!!.py").caesarx("hi", 1, "encrypt")
            loadx("week4x/compose_pipex.py").pipe()("hi")
            loadx("week4x/flatten_groupx.py").combined([["hi"]])
            loadx("week4x/fib_memoz.py").fib(35)
            loadx("week4x/transactionz.py").analyze([])
        self.assertEqual(outputx.getvalue(), "")

    def test_challenge_restrictions(self):
        restrictionsx = {
            "week3x/Simple_Calculator.py": {"eval"},
            "week3x/gradez.py": {"sum", "max", "min"},
            "week4x/gradez.py": {"sum", "max", "min"},
            "week3x/second_largest.py": {"sort", "sorted", "max", "set"},
            "week4x/second_largestx.py": {"sort", "sorted", "max", "set"},
            "week3x/word_frex.py": {"max", "sort", "sorted", "Counter"},
            "week4x/word_freqx.py": {"max", "sort", "sorted", "Counter"},
            "week3x/anagramz.py": {"sorted", "Counter"},
            "week3x/number_reverze.py": {"str"},
            "week4x/transactionz.py": {"sum", "max", "sorted"},
        }
        treesx = {}
        for pathx in (ROOT / "soluxionz").rglob("*.py"):
            relativex = str(pathx.relative_to(ROOT / "soluxionz"))
            treex = ast.parse(pathx.read_text())
            treesx[relativex] = treex
            for nodex in ast.walk(treex):
                if isinstance(nodex, (ast.Import, ast.ImportFrom)):
                    self.assertEqual(relativex, "week4x/reduce_bonuz.py")
                    self.assertIsInstance(nodex, ast.ImportFrom)
                    self.assertEqual(nodex.module, "functools")
                    self.assertEqual([aliasx.name for aliasx in nodex.names], ["reduce"])
                if isinstance(nodex, ast.Call):
                    namex = nodex.func.id if isinstance(nodex.func, ast.Name) else getattr(nodex.func, "attr", "")
                    self.assertNotIn(namex, restrictionsx.get(relativex, set()), relativex)
                if relativex.startswith("week4x/") and isinstance(nodex, ast.FunctionDef):
                    for innerx in ast.walk(nodex):
                        if isinstance(innerx, ast.Call) and isinstance(innerx.func, ast.Name):
                            self.assertNotIn(innerx.func.id, {"print", "input"}, relativex)

        for relativex in ("week3x/palindromex.py", "week4x/palindromex.py"):
            for nodex in ast.walk(treesx[relativex]):
                self.assertFalse(isinstance(nodex, ast.Subscript) and isinstance(nodex.slice, ast.Slice), relativex)
                self.assertFalse(isinstance(nodex, ast.Call) and isinstance(nodex.func, ast.Attribute) and nodex.func.attr == "reverse", relativex)

        loop_typesx = (ast.For, ast.While, ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)
        functionsx = {nodex.name: nodex for nodex in treesx["week4x/flatten_groupx.py"].body if isinstance(nodex, ast.FunctionDef)}
        for namex in ("flatten", "group_by_recursive"):
            self.assertFalse(any(isinstance(nodex, loop_typesx) for nodex in ast.walk(functionsx[namex])))
        for relativex, functionx in (
            ("week3x/two_sumx.py", "two_sumx"), ("week4x/two_sumx.py", "two_sum"),
            ("week3x/second_largest.py", "second_largestx"), ("week4x/second_largestx.py", "second_largest"),
        ):
            function_nodex = next(nodex for nodex in treesx[relativex].body if isinstance(nodex, ast.FunctionDef) and nodex.name == functionx)
            self.assertEqual(len([nodex for nodex in ast.walk(function_nodex) if isinstance(nodex, (ast.For, ast.While))]), 1)


if __name__ == "__main__":
    unittest.main()
