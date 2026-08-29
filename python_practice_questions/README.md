# Python Practice Questions

A set-based question bank, adapted from a C activity-set course into Python.
44 problems across 5 sets, working up from basic functions to classes,
geometry, fractions and series.

| Set | Problems | Focus |
|-----|----------|-------|
| [`set01/`](set01/) | 12 | Functions, loops, strings, complex numbers |
| [`set02/`](set02/) | 8 | Triangles, number properties, GCD, strings |
| [`set03/`](set03/) | 8 | Geometry, primes, Fibonacci, substrings |
| [`set04/`](set04/) | 8 | Fractions, combinatorics, polynomials |
| [`set05/`](set05/) | 8 | Points, series, list averages, camel problems |

## How to use this

Each set folder has a `README.md` listing its problems, with suggested function
signatures and sample input/output. Solve one per file:

```
set01/problem01.py
set01/problem02.py
```

The signatures are a guide, not a rule — they mirror the original C function
breakdown so each problem stays split into input, compute and output steps.

## Notes on the C → Python translation

- **`struct` → `dataclass`.** Where the original used a C struct, use
  `from dataclasses import dataclass`.
- **Pass by reference.** C used `int *sum` to return values through parameters.
  Python has no equivalent for immutable types — either return the value, or
  pass a mutable object (list, dict, dataclass) and write into it.
- **Build it yourself.** Where a problem is *about* an algorithm — square roots,
  GCD, substring search, string reversal — write the loop rather than calling
  the standard library. Compare with the built-in afterwards.
