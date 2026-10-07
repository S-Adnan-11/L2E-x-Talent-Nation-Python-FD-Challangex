# challangex → soluxionz 😼

Weeks 1,2,3 + Week 4, with the optional bonuses too! lol.
Wasn't aware before. srsly

No dependencies; use Python 3.9 or newer.

The calculator keeps the original file and `simple_calcx` name. Everything else lives in `week3x` or `week4x`. Week 4 keeps the function names the questions explicitly ask for; the helper names still get a lil x/z treatment.

## Run a soluxion

From the repo folder:

```bash
python3 soluxionz/Simple_Calculator.py
python3 soluxionz/week3x/anagramz.py
python3 soluxionz/week4x/transactionz.py
```

Each challenge file runs on its own. Text/number challenges ask for input; grades, flattening, Fibonacci and transactions use the supplied examples. For different student or transaction data, change the example under `if __name__ == "__main__":` or call the functions with your own data. Importing a file never starts its prompts or prints its examples.

## Week 3

| Question | File | Main function |
| --- | --- | --- |
| 1. Simple Calculator | [Simple_Calculator.py](soluxionz/Simple_Calculator.py) | `simple_calcx` |
| 2. Palindrome | [palindromex.py](soluxionz/week3x/palindromex.py) | `palindrome_checkx` |
| 3. Student Grades | [gradez.py](soluxionz/week3x/gradez.py) | `student_reportx` |
| 4. Second Largest | [second_largestx.py](soluxionz/week3x/second_largestx.py) | `second_largestx` |
| 5. Word Frequency | [word_freqx.py](soluxionz/week3x/word_freqx.py) | `word_frequencyx` |
| 6. Two Sum | [two_sumx.py](soluxionz/week3x/two_sumx.py) | `two_sumx` |
| 7. Anagram Finder | [anagramz.py](soluxionz/week3x/anagramz.py) | `anagram_checkx` |
| 8. Caesar Cipher | [cipherx.py](soluxionz/week3x/cipherx.py) | `caesarx` |
| 9. Number Reverser | [number_reversez.py](soluxionz/week3x/number_reversez.py) | `number_reversex` |

The Week 3 sheet labels its final three questions “7.” They're listed above as 7–9 in their original order.

## Week 4

| Question | File | Main functions |
| --- | --- | --- |
| 1. Palindrome | [palindromex.py](soluxionz/week4x/palindromex.py) | `is_letter`, `is_palindrome` |
| 2. Student Grades | [gradez.py](soluxionz/week4x/gradez.py) | `grade_for`, `student_reportx` |
| 3. Word Frequency | [word_freqx.py](soluxionz/week4x/word_freqx.py) | `count_words`, `most_frequent` |
| 4. Two Sum | [two_sumx.py](soluxionz/week4x/two_sumx.py) | `two_sum` |
| 5. Second Largest | [second_largestx.py](soluxionz/week4x/second_largestx.py) | `step`, `second_largest` |
| 6. Caesar Cipher | [cipherx.py](soluxionz/week4x/cipherx.py) | `make_shifter`, `caesarx` |
| 7. Compose and Pipe | [compose_pipex.py](soluxionz/week4x/compose_pipex.py) | `compose`, `pipe`, text helpers |
| 8. Recursive Flatten and Group | [flatten_groupx.py](soluxionz/week4x/flatten_groupx.py) | `flatten`, `group_by`, `combined` |
| 9. Memoized Fibonacci | [fib_memoz.py](soluxionz/week4x/fib_memoz.py) | `memoize`, `fib`, `count_ways` |
| 10. Transaction Analyzer | [transactionz.py](soluxionz/week4x/transactionz.py) | required helpers, `analyze` |

Recursive palindrome, comprehension grades, uppercase cipher, recursive reverse/grouping, stairs, and both transaction bonuses live with their questions. Q3–Q5's `reduce` variants live in [reduce_bonusx.py](soluxionz/week4x/reduce_bonusx.py). Only that optional file imports `functools.reduce`; the main challenge files import nothing.

```bash
python3 soluxionz/week4x/reduce_bonusx.py
python3 -m unittest discover -s tests -v
```

## Small decisions that matter

- Ties keep the first encountered student, word or expense. Two Sum returns the first pair completed while scanning left to right, keeping the earliest index for repeated numbers.
- Second-largest returns `None` when fewer than two unique numbers exist. Two Sum returns `[]` when no pair exists. Empty word counts return `{}` and their most frequent word is `""`.
- Empty scores mean average `None`, grade `N/A`, and no place in the highest/lowest ranking. Scores outside 0–100 raise `ValueError`. Decimal grade boundaries use lower thresholds: 69.9 is B, 59.9 is C, etc.
- Palindromes compare letters and digits, skipping punctuation/spaces. Week 4's required `is_letter` identifies letters; the pointer checks also retain numeric characters so digits aren't silently removed. Empty or punctuation-only text is a palindrome.
- Word counting treats the explicitly listed punctuation as separators. `hello,hello` becomes two words; contractions and hyphenated words split at their punctuation. Anagrams compare every character after lowercasing; their task is words, so spaces/punctuation aren't discarded.
- Both ciphers shift English A–Z/a–z, preserving case and every other character. Negative shifts and shifts larger than 26 work.
- Flatten expands lists only; tuples and other non-list values stay as elements. The combined word example groups case-insensitively, using `""` as the key for empty words. `group_by` accepts any key function returning hashable keys.
- Recursive solutions stop at their base cases, but very long/deep inputs can reach Python's recursion limit. Memoization speeds up repeated Fibonacci work; it doesn't remove that limit. `memoize` accepts positional, hashable arguments to functions with stable results.
- Transactions use the question's schema: `name`, numeric `amount`, and `type` (`income` or `expense`). An empty expense list has largest expense `None`; exactly zero balance is `Break-even`.

[StudyCase](StudyCase) tells the constraint stories. The personal walkthrough lives locally in `.private_soluxionz/soluxionz_explained.md`; `.gitignore` excludes that folder from normal commits. It's a local note, not encrypted storage.

