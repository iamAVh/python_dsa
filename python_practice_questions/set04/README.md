# Set 4

Fractions, combinatorics, polynomials and word counting.

8 problems. Solve each in `problemNN.py` in this folder.

---

### 1. Find the sum of two fractions.

**Function signatures**

```python
def input_fractions() -> tuple[int, int, int, int]: ...
def add(n1: int, d1: int, n2: int, d2: int) -> tuple[int, int]: ...
def output(n1: int, d1: int, n2: int, d2: int, rn: int, rd: int) -> None: ...
```

**Input**

```
1 2
1 4
```

**Output**

```
1/2 + 1/4 = 3/4
```

---

### 2. Find the smallest of three fractions.

**Function signatures**

```python
@dataclass
class Fraction:
    num: int
    den: int
def input_fraction() -> Fraction: ...
def smallest(a: Fraction, b: Fraction, c: Fraction) -> Fraction: ...
def output(fractions: list[Fraction], smallest: Fraction) -> None: ...
```

**Input**

```
1 2
1 3
1 4
```

**Output**

```
The smallest of 1/2, 1/3 and 1/4 is 1/4
```

---

### 3. Find nCr for a given n and r.

> `nCr = n! / (r! * (n-r)!)`. Write the factorial yourself.

**Function signatures**

```python
def input_n_and_r() -> tuple[int, int]: ...
def ncr(n: int, r: int) -> int: ...
def output(n: int, r: int, result: int) -> None: ...
```

**Input**

```
6
3
```

**Output**

```
for n = 6 and r = 3, nCr = 20
```

---

### 4. Evaluate a polynomial at a given point using Horner's method.

> Horner's method rewrites the polynomial so it needs only n multiplications.

**Function signatures**

```python
def input_degree() -> int: ...
def input_coefficients(n: int) -> list[float]: ...
def input_x() -> float: ...
def evaluate(coefficients: list[float], x: float) -> float: ...
def output(coefficients: list[float], x: float, result: float) -> None: ...
```

**Input**

```
1
1 1
1
```

**Output**

```
H(1, 1, 1) = 1.00 + 1.00 * 1.00^1 = 2.0
```

---

### 5. Find the index of the largest number in a list.

**Function signatures**

```python
def input_size() -> int: ...
def input_list(n: int) -> list[int]: ...
def largest_index(numbers: list[int]) -> int: ...
def output(index: int) -> None: ...
```

**Input**

```
5
4 2 9 1 7
```

**Output**

```
The index of the largest number in the array is 2
```

---

### 6. Count the number of words in a string.

> The C version used `strtok`; in Python use `str.split()` — or write the scan yourself.

**Function signatures**

```python
def input_string() -> str: ...
def count_words(text: str) -> int: ...
def output(text: str, count: int) -> None: ...
```

**Input**

```
hello world hello
```

**Output**

```
The number of words in "hello world hello" is 3
```

---

### 7. Add two fractions and reduce the result to lowest terms.

> Reduce using the GCD.

**Function signatures**

```python
@dataclass
class Fraction:
    num: int
    den: int
def input_fraction() -> Fraction: ...
def find_gcd(a: int, b: int) -> int: ...
def add_fractions(f1: Fraction, f2: Fraction) -> Fraction: ...
def output(f1: Fraction, f2: Fraction, total: Fraction) -> None: ...
```

**Input**

```
9 6
5 6
```

**Output**

```
9/6 + 5/6 = 7/3
```

---

### 8. Add n fractions.

**Function signatures**

```python
@dataclass
class Fraction:
    num: int
    den: int
def input_n() -> int: ...
def input_n_fractions(n: int) -> list[Fraction]: ...
def find_gcd(a: int, b: int) -> int: ...
def add_n_fractions(fractions: list[Fraction]) -> Fraction: ...
def output(fractions: list[Fraction], total: Fraction) -> None: ...
```

**Input**

```
3
4 3
8 9
1 2
```

**Output**

```
4/3 + 8/9 + 1/2 = 49/18
```

---
