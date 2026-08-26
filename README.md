# Python — Learning & DSA Practice

My Python journey from the fundamentals through to data structures and
algorithmic problem solving. Concepts are worked through in notebooks; solved
problems live as plain scripts. Everything here is written from scratch — the
goal is understanding the approach and its complexity, not just a passing
submission.

## Learning path

Numbered so they read in order. Each folder has its own README with a topic checklist.

| # | Module | Covers |
|---|--------|--------|
| 01 | [`01_basics/`](01_basics/) | Variables, types, operators, conditionals, loops |
| 02 | [`02_strings/`](02_strings/) | Indexing, slicing, methods, formatting |
| 03 | [`03_data_structures/`](03_data_structures/) | Lists, tuples, sets, dictionaries, comprehensions |
| 04 | [`04_functions/`](04_functions/) | Arguments, scope, lambdas, `map`/`filter`, recursion |
| 05 | [`05_oop/`](05_oop/) | Classes, inheritance, dunder methods |
| 06 | [`06_files_and_exceptions/`](06_files_and_exceptions/) | File I/O, context managers, error handling |
| 07 | [`07_modules_and_libraries/`](07_modules_and_libraries/) | `collections`, `itertools`, `math`, `datetime` |

## Practice

| Folder | Contents |
|--------|----------|
| [`practice/hackerrank/`](practice/hackerrank/) | HackerRank Python track, organised by its domains |
| [`practice/problem_solving/`](practice/problem_solving/) | Topic-wise DSA practice grouped by technique |

Every solution opens with a docstring stating the problem, the approach, and
its time/space complexity — see
[`list_comprehensions.py`](practice/hackerrank/basic_data_types/list_comprehensions.py)
for the format.

## Progress

- [x] 01 · Basics — conditionals
- [ ] 02 · Strings
- [x] 03 · Data Structures — lists, sets, dictionaries
- [ ] 04 · Functions
- [ ] 05 · OOP
- [ ] 06 · Files & Exceptions
- [ ] 07 · Modules & Standard Library

## Environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Python 3.12.11

## Branches

- **`main`** — default branch; each session's work lands here
- **`daily`** — working branch, fast-forwarded into `main` after every session
