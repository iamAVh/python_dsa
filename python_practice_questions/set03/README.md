# Set 3

Geometry, primes, Fibonacci and substrings.

8 problems. Solve each in `problemNN.py` in this folder.

---

### 1. Find the distance between two points.

> `distance = sqrt((x2-x1)**2 + (y2-y1)**2)`

**Function signatures**

```python
def input_points() -> tuple[float, float, float, float]: ...
def find_distance(x1: float, y1: float, x2: float, y2: float) -> float: ...
def output(x1: float, y1: float, x2: float, y2: float, distance: float) -> None: ...
```

**Input**

```
1 1
2 2
```

**Output**

```
The distance between point (1.0, 1.0) and (2.0, 2.0) is 1.4142
```

---

### 2. Check whether three points form a triangle.

> They form a triangle only if the three points are not collinear and no two coincide.

**Function signatures**

```python
def input_triangle() -> tuple[float, ...]: ...
def is_triangle(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> bool: ...
def output(points: tuple[float, ...], result: bool) -> None: ...
```

**Input**

```
1 1
0 0
1 1
```

**Output**

```
The points (1.0, 1.0), (0.0, 0.0) and (1.0, 1.0) do not form a triangle
```

---

### 3. Check whether a number is prime.

**Function signatures**

```python
def input_number() -> int: ...
def is_prime(n: int) -> bool: ...
def output(n: int, result: bool) -> None: ...
```

**Input**

```
3
```

**Output**

```
3 is a prime number
```

---

### 4. Find the nth number in the Fibonacci sequence.

> `0, 1, 1, 2, 3, 5, 8, 13, ...`

**Function signatures**

```python
def input_n() -> int: ...
def find_fib(n: int) -> int: ...
def output(n: int, value: int) -> None: ...
```

**Input**

```
5
```

**Output**

```
fibo(5) = 5
```

---

### 5. Find all prime numbers from 2 to n using the Sieve of Eratosthenes.

**Function signatures**

```python
def input_n() -> int: ...
def sieve(n: int) -> list[int]: ...
def output(primes: list[int]) -> None: ...
```

**Input**

```
35
```

**Output**

```
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31
```

---

### 6. Find the index of a substring within a string.

> Write the search yourself — do not use `str.find` or `in`.

**Function signatures**

```python
def input_strings() -> tuple[str, str]: ...
def substring_index(text: str, sub: str) -> int: ...
def output(text: str, sub: str, index: int) -> None: ...
```

**Input**

```
helloworldhello
world
```

**Output**

```
The index of 'world' in 'helloworldhello' is 5
```

---

### 7. Find the length of a line using classes.

> Model `Point` and `Line` as dataclasses.

**Function signatures**

```python
@dataclass
class Point:
    x: float
    y: float
@dataclass
class Line:
    p1: Point
    p2: Point
    distance: float = 0.0
def input_point() -> Point: ...
def input_line() -> Line: ...
def find_length(line: Line) -> None: ...
def output(line: Line) -> None: ...
```

**Input**

```
1 1
2 2
```

**Output**

```
The distance between the points (1.0, 1.0) and (2.0, 2.0) is 1.4142
```

---

### 8. Find the perimeter of a polygon.

**Function signatures**

```python
@dataclass
class Point:
    x: float
    y: float
@dataclass
class Polygon:
    points: list[Point]
    perimeter: float = 0.0
def input_n() -> int: ...
def input_polygon(n: int) -> Polygon: ...
def find_distance(a: Point, b: Point) -> float: ...
def find_perimeter(p: Polygon) -> None: ...
def output(p: Polygon) -> None: ...
```

**Input**

```
4
0 0
1 0
1 1
0 1
```

**Output**

```
The perimeter of the polygon is 4.0
```

---
