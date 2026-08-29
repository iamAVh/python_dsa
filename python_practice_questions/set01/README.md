# Set 1

Basics, functions, loops, strings and complex numbers.

12 problems. Solve each in `problemNN.py` in this folder.

---

### 1. Print your name.

**Function signatures**

```python
def print_name(name: str) -> None: ...
```

**Input**

```
Ajay
```

**Output**

```
Ajay
```

---

### 2. Add two numbers.

**Function signatures**

```python
def add(a: int, b: int) -> int: ...
```

**Input**

```
1
2
```

**Output**

```
3
```

---

### 3. Add two numbers, passing values into a function.

> In Python every argument is passed the same way — this is the plain, value-style version.

**Function signatures**

```python
def input_number() -> int: ...
def add(a: int, b: int) -> int: ...
def output(a: int, b: int, total: int) -> None: ...
```

**Input**

```
1
2
```

**Output**

```
The sum of 1 and 2 is 3
```

---

### 4. Add two numbers, returning the result through a mutable container.

> Python has no pass-by-reference for `int`. Emulate C's `int *sum` by passing a mutable object (a one-element list or a dict) and writing into it.

**Function signatures**

```python
def input_number() -> int: ...
def add(a: int, b: int, result: list) -> None: ...
def output(a: int, b: int, total: int) -> None: ...
```

**Input**

```
1
2
```

**Output**

```
The sum of 1 and 2 is 3
```

---

### 5. Find the largest of three numbers.

**Function signatures**

```python
def input_number() -> int: ...
def compare(a: int, b: int, c: int) -> int: ...
def output(a: int, b: int, c: int, largest: int) -> None: ...
```

**Input**

```
1
2
3
```

**Output**

```
The largest of 1,2 and 3 is 3.
```

---

### 6. Find the largest of three numbers, writing the result into a mutable container.

> Same idea as question 4 — the C version used `int *largest`.

**Function signatures**

```python
def input_number() -> int: ...
def compare(a: int, b: int, c: int, largest: list) -> None: ...
def output(a: int, b: int, c: int, largest: int) -> None: ...
```

**Input**

```
3
1
2
```

**Output**

```
The largest of 3,1 and 2 is 3.
```

---

### 7. Find the sum of all natural numbers up to n.

**Function signatures**

```python
def input_n() -> int: ...
def sum_n(n: int) -> int: ...
def output(n: int, total: int) -> None: ...
```

**Input**

```
5
```

**Output**

```
The sum of natural numbers up to 5 is 15
```

---

### 8. Find the sum of n numbers entered by the user.

**Function signatures**

```python
def input_size() -> int: ...
def input_list(n: int) -> list[int]: ...
def sum_list(numbers: list[int]) -> int: ...
def output(numbers: list[int], total: int) -> None: ...
```

**Input**

```
3
1 7 11
```

**Output**

```
1+7+11 is 19
```

---

### 9. Find the square root of a number using the Babylonian method.

> Iterate `guess = (guess + n / guess) / 2` until it stops changing. Do not use `math.sqrt`.

**Function signatures**

```python
def input_number() -> float: ...
def square_root(n: float) -> float: ...
def output(n: float, root: float) -> None: ...
```

**Input**

```
49
```

**Output**

```
Square root of 49.0 is 7.0
```

---

### 10. Compare two strings character by character.

> `Hello` equals `Hello` but not `hello`. `Hello` is less than `Hellw` alphabetically. Do not use `<` on the whole string — compare character by character.

**Function signatures**

```python
def input_two_strings() -> tuple[str, str]: ...
def string_compare(a: str, b: str) -> int: ...
def output(a: str, b: str, result: int) -> None: ...
```

**Input**

```
hello
world
```

**Output**

```
world is greater than hello
```

---

### 11. Add two complex numbers.

> Model the complex number yourself with a `dataclass` or a tuple — do not use Python's built-in `complex` type.

**Function signatures**

```python
@dataclass
class Complex:
    real: float
    imaginary: float
def input_complex() -> Complex: ...
def add_complex(a: Complex, b: Complex) -> Complex: ...
def output(a: Complex, b: Complex, total: Complex) -> None: ...
```

**Input**

```
2 3
4 5
```

**Output**

```
The sum of 2+3i and 4+5i is 6+8i
```

---

### 12. Add n complex numbers.

**Function signatures**

```python
@dataclass
class Complex:
    real: float
    imaginary: float
def input_n() -> int: ...
def input_n_complex(n: int) -> list[Complex]: ...
def add_n_complex(numbers: list[Complex]) -> Complex: ...
def output(numbers: list[Complex], total: Complex) -> None: ...
```

**Input**

```
3
2 3
4 5
6 7
```

**Output**

```
2+3i + 4+5i + 6+7i is 12+15i
```

---
