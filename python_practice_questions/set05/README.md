# Set 5

Points, series, list averages and the camel problems.

8 problems. Solve each in `problemNN.py` in this folder.

---

### 1. Find the distance between two points using a class.

**Function signatures**

```python
@dataclass
class Point:
    x: float
    y: float
def input_point() -> Point: ...
def dist(a: Point, b: Point) -> float: ...
def output(a: Point, b: Point, result: float) -> None: ...
```

**Input**

```
1.0 1.0
2.0 2.0
```

**Output**

```
The Distance between (1.0,1.0) and (2.0,2.0) is 1.4142
```

---

### 2. Find the weight of a camel from its height, length and stomach radius.

> `weight = pi * stomach_radius**3 * sqrt(height * length)`

**Function signatures**

```python
def input_camel_details() -> tuple[float, float, float]: ...
def find_weight(radius: float, height: float, length: float) -> float: ...
def output(radius: float, height: float, length: float, weight: float) -> None: ...
```

**Input**

```
1
1
1
```

**Output**

```
The weight of the camel with radius: 1.0, height: 1.0, length: 1.0 is 3.1415
```

---

### 3. Find the weight of a camel using a class.

> Same formula as question 2, but store the camel in a `dataclass`.

**Function signatures**

```python
@dataclass
class Camel:
    radius: float
    height: float
    length: float
    weight: float = 0.0
def input_camel() -> Camel: ...
def find_weight(c: Camel) -> None: ...
def output(c: Camel) -> None: ...
```

**Input**

```
1
1
1
```

**Output**

```
The weight of the camel with radius: 1.0, height: 1.0, length: 1.0 is 3.1415
```

---

### 4. Find the mood of a camel.

> The camel is **sick** when `radius` is less than both `height` and `length`; **happy** when `height` is less than `length` and `length` is less than `radius`; **tense** when `length` is less than both `height` and `radius`.

**Function signatures**

```python
def input_camel_details() -> tuple[float, float, float]: ...
def find_mood(radius: float, height: float, length: float) -> str: ...
def output(radius: float, height: float, length: float, mood: str) -> None: ...
```

**Input**

```
5
2
4
```

**Output**

```
The Camel is Happy
```

---

### 5. Find borga(x) for a given x.

> `borga(x) = 1 + x**1/3! + x**2/5! + x**3/7! + ...` — stop when the next term is smaller than 0.000001.

**Function signatures**

```python
def input_x() -> int: ...
def borga(x: int) -> float: ...
def output(x: int, result: float) -> None: ...
```

**Input**

```
5
```

**Output**

```
borga(5) = 2.699337
```

---

### 6. Find the average of all the odd elements in a list.

**Function signatures**

```python
def input_n() -> int: ...
def input_list(n: int) -> list[int]: ...
def odd_average(numbers: list[int]) -> float: ...
def output(average: float) -> None: ...
```

**Input**

```
5
5 4 3 8 0
```

**Output**

```
Average of all the odd elements is: 4.0
```

---

### 7. Check whether a camel has a nice name.

> A name is nice when it contains at least 2 vowels and at least 2 consonants.

**Function signatures**

```python
def input_name() -> str: ...
def has_nice_name(name: str) -> bool: ...
def output(name: str, result: bool) -> None: ...
```

**Input**

```
Conky
```

**Output**

```
The camel does not have a nice name
```

---

### 8. Find the total weight of a truck carrying n camels.

> `total = truck_weight + sum of camel weights`

**Function signatures**

```python
@dataclass
class Camel:
    radius: float
    height: float
    length: float
    weight: float = 0.0
def input_camels() -> tuple[list[Camel], float]: ...
def find_camel_weights(camels: list[Camel]) -> None: ...
def compute_total(camels: list[Camel], truck_weight: float) -> float: ...
def output(total: float) -> None: ...
```

**Input**

```
3
1 1 1
1 1 1
1 1 1
2000
```

**Output**

```
The Total weight of the truck is: 2009.4245
```

---
