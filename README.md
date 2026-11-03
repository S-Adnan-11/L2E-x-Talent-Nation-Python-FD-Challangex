# challangex → soluxionz 😼

Python foundation challangex from Weeks 3–8, including the Week 1/2 revision and optional stretches. Loops, dictionaries, functional thinking, then more loops lol. The later weeks add matrix work, backtracking and a performance lab with actual call counts.

No dependencies. Python 3.9 or newer.

## Run a soluxion

From the repo folder:

```bash
python3 soluxionz/week3x/Simple_Calculator.py
python3 soluxionz/week4x/transactionz.py
python3 soluxionz/week5x/List_Analyxer.py
python3 soluxionz/week6x/List_analyxer_againn_wtf.py
python3 'soluxionz/week6x/balance().py'
python3 soluxionz/week7x/prime.py
python3 soluxionz/week7x/matrixx_rtx.py
python3 soluxionz/week8x/binary_srch.py
python3 soluxionz/week8x/performance_labx.py
```

Weeks 3, 4 and 8 keep prompts/examples under `if __name__ == "__main__":`, so their functions can also be imported without starting a session. Weeks 5–7 mostly run directly: some prompt for input, others use a starting list or matrix near the top of the file.

Week 5's `balanced_px.py` defines a function without calling it. Example:

```bash
python3 -c 'from soluxionz.week5x.balanced_px import balanced_px; balanced_px("(a+b) * (c-d)")'
```

## Week 3

| Question | File | Main function |
| --- | --- | --- |
| 1. Simple Calculator | [Simple_Calculator.py](soluxionz/week3x/Simple_Calculator.py) | `simple_calcx` |
| 2. Palindrome | [palindromex.py](soluxionz/week3x/palindromex.py) | `palindrome_checkx` |
| 3. Student Grades | [gradez.py](soluxionz/week3x/gradez.py) | `student_reportx` |
| 4. Second Largest | [second_largest.py](soluxionz/week3x/second_largest.py) | `second_largestx` |
| 5. Word Frequency | [word_frex.py](soluxionz/week3x/word_frex.py) | `word_frequencyx` |
| 6. Two Sum | [two_sumx.py](soluxionz/week3x/two_sumx.py) | `two_sumx` |
| 7. Anagram Finder | [anagramz.py](soluxionz/week3x/anagramz.py) | `anagram_checkx` |
| 8. Caesar Cipher | [cipherx.py](soluxionz/week3x/cipherx.py) | `caesarx` |
| 9. Number Reverser | [number_reverze.py](soluxionz/week3x/number_reverze.py) | `number_reversex` |

The Week 3 sheet labels its final three questions “7.” well, they're listed above as 7–9 in their original order.

## Week 4

| Question | File | Main functions |
| --- | --- | --- |
| 1. Palindrome | [palindromex.py](soluxionz/week4x/palindromex.py) | `is_letter`, `is_palindrome` |
| 2. Student Grades | [gradez.py](soluxionz/week4x/gradez.py) | `grade_for`, `student_reportx` |
| 3. Word Frequency | [word_freqx.py](soluxionz/week4x/word_freqx.py) | `count_words`, `most_frequent` |
| 4. Two Sum | [two_sumx.py](soluxionz/week4x/two_sumx.py) | `two_sum` |
| 5. Second Largest | [second_largestx.py](soluxionz/week4x/second_largestx.py) | `step`, `second_largest` |
| 6. Caesar Cipher | [cipherx_again!!.py](soluxionz/week4x/cipherx_again!!.py) | `make_shifter`, `caesarx` |
| 7. Compose and Pipe | [compose_pipex.py](soluxionz/week4x/compose_pipex.py) | `compose`, `pipe`, text helpers |
| 8. Recursive Flatten and Group | [flatten_groupx.py](soluxionz/week4x/flatten_groupx.py) | `flatten`, `group_by`, `combined` |
| 9. Memoized Fibonacci | [fib_memoz.py](soluxionz/week4x/fib_memoz.py) | `memoize`, `fib`, `count_ways` |
| 10. Transaction Analyzer | [transactionz.py](soluxionz/week4x/transactionz.py) | required helpers, `analyze` |

Recursive palindrome, comprehension grades, uppercase cipher, recursive reverse/grouping, stairs, and both transaction bonuses live with their questions. Q3–Q5's `reduce` variants live in [reduce_bonuz.py](soluxionz/week4x/reduce_bonuz.py). That's the only solution file with an import: the permitted `functools.reduce`.

```bash
python3 soluxionz/week4x/reduce_bonuz.py
```

## Week 5

Five practical problems using loops, counters and a small menu-driven project.

| Question | File | Approach |
| --- | --- | --- |
| 1. List Analyser | [List_Analyxer.py](soluxionz/week5x/List_Analyxer.py) | `ListAnalyzer`: track `minn`, `maxx`, total and average |
| 2. Linear Search | [LIneeer_srch.py](soluxionz/week5x/LIneeer_srch.py) | first matching index, then stop |
| 3. Matrix Row Sums | [matrixx.py](soluxionz/week5x/matrixx.py) | nested loops, fresh total for each row |
| 4. Balanced Parentheses | [balanced_px.py](soluxionz/week5x/balanced_px.py) | `balanced_px`: counter for round parentheses |
| 5. To-Do List | [mini_todo_lixt_lol.py](soluxionz/week5x/mini_todo_lixt_lol.py) | add, view, remove, quit |

The to-do menu takes a choice first, then prompts for task text or a removal number.

## Week 6

The same five problems with extra requirements, followed by leap years, duplicates and run-length encoding.

| Question | File | Added logic |
| --- | --- | --- |
| 1. List Analyser — Extended | [List_analyxer_againn_wtf.py](soluxionz/week6x/List_analyxer_againn_wtf.py) | first min/max indices, second pass for above-average count |
| 2. Linear Search — All Occurrences | [lin_srch.py](soluxionz/week6x/lin_srch.py) | all indices, count, first and last |
| 3. Matrix Sums — Extended | [matrix_sum.py](soluxionz/week6x/matrix_sum.py) | column totals and row averages |
| 4. Balanced Brackets | [balance().py](<soluxionz/week6x/balance().py>) | stack for `()`, `[]`, `{}` |
| 5. To-Do List — Extended | [todo_lisit.py](soluxionz/week6x/todo_lisit.py) | `[text, done]` records and a done command |
| 6. Leap Year Checker | [lip_year.py](soluxionz/week6x/lip_year.py) | century rules, plus next three leap years |
| 7. Find Duplicates | [duplicatez.py](soluxionz/week6x/duplicatez.py) | each duplicate once, plus frequency dictionary |
| 8. Run-Length Encoding | [decode_encode.py](soluxionz/week6x/decode_encode.py) | `encode` and multi-digit-count `decode` |

The extended to-do menu accepts commands on one line: `add Study Python`, `view`, `done 1`, `remove 1`, `quit`. Tasks stay in memory for that session.

## Week 7

Square-root checks, Fibonacci without a stored list, manual base conversion and more matrix work. The anagram dictionary makes another appearance too lol.

| Question | File | Approach |
| --- | --- | --- |
| 1. Prime Number Checker | [prime.py](soluxionz/week7x/prime.py) | `is_prime`: while-loop divisors up to the square root; manually total primes through N |
| 2. Fibonacci — Even Sum | [even_fibonacci.py](soluxionz/week7x/even_fibonacci.py) | loop with two sequence values; even total and forward/reverse strings |
| 3. Decimal to Binary | [10_to_01.py](soluxionz/week7x/10_to_01.py) | divide by 2 and prepend each remainder |
| 4. Matrix Multiplication | [matrix_mx.py](soluxionz/week7x/matrix_mx.py) | dimension check and three nested loops |
| 5. Remove Spaces & Capitalize | [capitalize.py](soluxionz/week7x/capitalize.py) | word-start flag and ASCII conversion; build both strings manually |
| 6. Anagram Checker | [Anagramm!.py](soluxionz/week7x/Anagramm!.py) | `count_letters`: compare lowercase character-frequency dictionaries |
| 7. Roman to Integer | [ass_roma.py](soluxionz/week7x/ass_roma.py) | symbol dictionary and while-loop look-ahead for subtraction |
| 8. Matrix Rotation | [matrixx_rtx.py](soluxionz/week7x/matrixx_rtx.py) | transpose and manually reverse rows in place |

The two matrix scripts use the matrices near the top of each file; the other six prompt for input. No imports or added dependencies.

## Week 8

Revision with more edge cases, then Hanoi, Pascal, Hangman, backtracking and the full performance lab. All ten questions and their bonuses are included.

| Question | File | Main functions |
| --- | --- | --- |
| 1. Binary Search | [binary_srch.py](soluxionz/week8x/binary_srch.py) | `binary_search`, `binary_search_recursive` |
| 2. RLE Round Trip | [rle_again.py](soluxionz/week8x/rle_again.py) | `rle_encode`, `rle_decode`, `compression_ratio` |
| 3. Maximum Subarray | [max_subarrayx.py](soluxionz/week8x/max_subarrayx.py) | `max_subarray_brute`, `max_subarray_fast` |
| 4. Integer to Roman | [ass_roma_back.py](soluxionz/week8x/ass_roma_back.py) | `integer_to_roman`, `roman_to_integer` |
| 5. Tower of Hanoi | [hanoi_towerz.py](soluxionz/week8x/hanoi_towerz.py) | `hanoi` |
| 6. Bubble Sort | [bubble_sortx.py](soluxionz/week8x/bubble_sortx.py) | `bubble_sort`, including `descending=True` |
| 7. Pascal's Triangle | [pascalx.py](soluxionz/week8x/pascalx.py) | `pascal_rows`, single-list `pascal_row` |
| 8. Hangman | [hangmanx.py](soluxionz/week8x/hangmanx.py) | `play_hangman`, interactive `main` |
| 9. Subsets & Permutations | [subsets_permz.py](soluxionz/week8x/subsets_permz.py) | `subsets`, `permutations`, `subsets_with_sum` |
| 10. Performance Lab | [performance_labx.py](soluxionz/week8x/performance_labx.py) | coin counters, `memoize`, `longest_consecutive`, `count_pairs`, Fibonacci factories |

Each file prints its checks when run. That includes the recursive/loop search comparison, RLE round trips, brute/fast subarray comparison, all 1–3999 Roman round trips, Hanoi move counts and subset/permutation counts through n=8. The Roman inverse wraps Week 7's existing look-ahead logic locally; the earlier script stays as it is.

`hangmanx.py` prints its examples, then asks for a word, an attempt limit and one letter at a time. The interactive part calls the same pure game function after each guess.

The lab prints naive/cached Fibonacci calls, both coin results, cache hits/misses, a three-entry FIFO eviction demo, the LRU bonus and the complexity table. Its code comments include the five written-analysis answers required by the sheet. The coin recurrence is shared by both versions; only the counting/cache wrapper changes.

For the 100-unit coin example, both versions return 292. The naive version makes 38,901 calls; the cached one makes 1,001 calls (310 hits, 691 misses). The bottom-up bonus handles amount 10000 without recursive calls. The report distinguishes the O(A×m) cached states from the O(m) cost of hashing the coin tuple on each lookup; with m coin types, that implementation has an O(A×m²) time bound.

## Small decisions that matter

- Binary search assumes ascending input and returns `(leftmost_index, comparisons)`. Each target equality counts once; a non-match also counts its direction comparison. Pointer bounds aren't included.
- Week 8 RLE accepts letters only, reads whole positive counts, and raises `ValueError` for malformed encodings. Empty input round-trips as `""`; its compression ratio is defined as `0.0`. Single-letter runs can make encoding longer.
- Maximum subarray returns `(sum, start, end)` with inclusive indices; empty input returns `(0, -1, -1)`. Equal sums keep the earliest start, then earliest end. All-negative input still picks a real element.
- Integer-to-Roman returns `""` for values outside 1–3999 or non-integer inputs. Hanoi accepts zero disks as no moves and rejects negative counts. Pascal accepts zero rows as `[]`; its single-row bonus counts rows from zero. Negative row counts/indices raise `ValueError`.
- Bubble sort intentionally modifies the supplied list and returns `(comparisons, swaps)`. The other Week 8 analysis functions leave input lists unchanged. Hangman's empty word is already won; a non-empty word with zero attempts is already lost. Guesses use lowercase a–z; repeats cost nothing, and guesses after an ending are ignored.
- Permutations assume distinct items. Subsets treat positions as choices, so repeated input values can produce equal-looking subsets. Returned result rows are fresh lists. Sum-filtered subsets allow negative values and include the empty subset when the target is zero.
- Coin amounts below zero return zero ways; amount zero has one empty combination. Duplicate denominations count once. Zero/negative/non-integer coin values raise `ValueError`. Cache size `None` is unlimited, zero disables storage, and positive sizes bound the entry count. `lru=True` refreshes order on hits; the default is FIFO.

- Week 7's prime checker rejects numbers below 2. Divisor checks stop at `i * i <= num`, and the prime list/total includes N when N itself is prime.
- Fibonacci starts with 0, 1 and builds the reversed output by prepending each generated value. It uses strings rather than a sequence list, slicing or `.reverse()`. The binary converter uses remainders rather than `bin()` and also handles zero as `"0"`.
- Matrix multiplication assumes non-empty rectangular inputs and checks that A's column count equals B's row count. Rotation assumes a square matrix and modifies the existing rows directly.
- Capitalization treats literal spaces as word boundaries and converts only ASCII a–z at a word's start. The no-spaces output is built from those same converted characters. Roman conversion rejects empty input/unknown symbols and applies the exercise's look-ahead rule; it doesn't validate every rule of canonical Roman notation.

- List analysers assume at least one number. Starting the trackers at the first value handles negative-only lists too. Week 6 keeps the first index on ties and counts above-average numbers only after calculating the average.
- Matrix scripts expect non-empty numeric rows; Week 6 expects a rectangular matrix. Its column accumulators work with different row/column counts.
- Week 5's bracket counter handles `()` only. Week 6 checks bracket types and nesting with a stack, ignoring non-bracket characters.
- Duplicate output follows each value's first position in the input, matching the sheet's examples. The wording “first appears as a duplicate” could imply second-occurrence order; this implementation follows the examples. The count dictionary uses the same order.
- Run-length encoding counts consecutive runs and keeps case distinct: `aabbaa` becomes `a2b2a2`. Decoding reads all digits in a count, so `a12b2` works. This unescaped format assumes non-digit source characters for round trips; digit characters would be ambiguous with counts.
- Ties keep the first encountered student, word or expense. Two Sum returns the first pair completed while scanning left to right, keeping the earliest index for repeated numbers.
- Second-largest returns `None` when fewer than two unique numbers exist. Two Sum returns `[]` when no pair exists. Empty word counts return `{}` and their most frequent word is `""`.
- Empty scores mean average `None`, grade `N/A`, and no place in the highest/lowest ranking. Scores outside 0–100 raise `ValueError`. Decimal grade boundaries use lower thresholds: 69.9 is B, 59.9 is C, etc.
- Palindromes compare letters and digits, skipping punctuation/spaces. Week 4's required `is_letter` identifies letters; the pointer checks also retain numeric characters so digits aren't silently removed. Empty or punctuation-only text is a palindrome.
- Word counting treats the explicitly listed punctuation as separators. `hello,hello` becomes two words; contractions and hyphenated words split at their punctuation. Anagrams compare every character after lowercasing; their task is words, so spaces/punctuation aren't discarded.
- Both ciphers shift English A–Z/a–z, preserving case and every other character. Negative shifts and shifts larger than 26 work.
- Flatten expands lists only; tuples and other non-list values stay as elements. The combined word example groups case-insensitively, using `""` as the key for empty words. `group_by` accepts any key function returning hashable keys.
- Recursive solutions stop at their base cases, but very long/deep inputs can reach Python's recursion limit. Memoization speeds up repeated Fibonacci work; it doesn't remove that limit. `memoize` accepts positional, hashable arguments to functions with stable results.
- Transactions use the question's schema: `name`, numeric `amount`, and `type` (`income` or `expense`). An empty expense list has largest expense `None`; exactly zero balance is `Break-even`.

## Checks and notes

The automated suite covers Weeks 3, 4 and 8, including examples, edge cases and the required restrictions. Week 8 also checks input preservation, independent reference results, legal Hanoi moves and cache behaviour:

```bash
python3 -m unittest discover -s tests -v
```

Weeks 5–7 run as the scripts listed above. Week 8's printed checks run alongside its examples. The question sheets live in [challangex](challangex). [StudyCase](StudyCase) walks through the constraints and the reasoning behind each soluxion.

