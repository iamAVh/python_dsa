# Set 2

Triangles, number properties, GCD and strings.

8 problems. Solve each in `problemNN.py` in this folder.

---

### 1. Find the area of a triangle.

> `area = 0.5 * base * height`

**Function signatures**

```python
def input_triangle() -> tuple[float, float]: ...
def find_area(base: float, height: float) -> float: ...
def output(base: float, height: float, area: float) -> None: ...
```

**Input**

```
1
2
```

**Output**

```
The area of the triangle with base 1.0 and height 2.0 is 1.0
```

---

### 2. Check whether a triangle is scalene.

> A triangle is scalene when no two sides are equal.

**Function signatures**

```python
def input_side() -> int: ...
def is_scalene(a: int, b: int, c: int) -> bool: ...
def output(a: int, b: int, c: int, scalene: bool) -> None: ...
```

**Input**

```
5
4
5
```

**Output**

```
The triangle with sides 5, 4 and 5 is not scalene
```

---

### 3. Check whether a number is composite.

> A composite number has more than two factors.

**Function signatures**

```python
def input_number() -> int: ...
def is_composite(n: int) -> bool: ...
def output(n: int, result: bool) -> None: ...
```

**Input**

```
8
```

**Output**

```
8 is a composite number.
```

---

### 4. Find the sum of the composite numbers in a list.

**Function signatures**

```python
def input_size() -> int: ...
def input_list(n: int) -> list[int]: ...
def sum_composites(numbers: list[int]) -> int: ...
def output(total: int) -> None: ...
```

**Input**

```
5
1 2 7 8 12
```

**Output**

```
20
```

---

### 5. Find the GCD (HCF) of two numbers.

> Use the Euclidean algorithm. Do not use `math.gcd`.

**Function signatures**

```python
def input_number() -> int: ...
def find_gcd(a: int, b: int) -> int: ...
def output(a: int, b: int, gcd: int) -> None: ...
```

**Input**

```
12
16
```

**Output**

```
4
```

---

### 6. Reverse a string.

> Write the loop yourself rather than using `[::-1]`, then compare the two.

**Function signatures**

```python
def input_string() -> str: ...
def reverse(text: str) -> str: ...
def output(text: str, reversed_text: str) -> None: ...
```

**Input**

```
hello
```

**Output**

```
olleh
```

---

### 7. Find the area of a triangle using a class.

> The C version used a `struct`; use a `dataclass`.

**Function signatures**

```python
@dataclass
class Triangle:
    base: float
    altitude: float
    area: float = 0.0
def input_triangle() -> Triangle: ...
def find_area(t: Triangle) -> None: ...
def output(t: Triangle) -> None: ...
```

**Input**

```
2
3
```

**Output**

```
The area of the triangle with base 2.0 and altitude 3.0 is 3.0
```

---

### 8. Find the triangle with the smallest area among n triangles.

**Function signatures**

```python
@dataclass
class Triangle:
    base: float
    altitude: float
    area: float = 0.0
def input_n() -> int: ...
def input_n_triangles(n: int) -> list[Triangle]: ...
def find_areas(triangles: list[Triangle]) -> None: ...
def find_smallest(triangles: list[Triangle]) -> Triangle: ...
def output(triangles: list[Triangle], smallest: Triangle) -> None: ...
```

**Input**

```
2
2 3
4 6
```

**Output**

```
The smallest triangle out of triangles with base and height (2,3), (4,6) is the triangle having base 2.00, height 3.00 and area 3.00
```

---
