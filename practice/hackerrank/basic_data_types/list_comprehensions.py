"""
HackerRank · Basic Data Types · List Comprehensions

Given dimensions x, y, z and an integer n, print every coordinate [i, j, k]
where 0 <= i <= x, 0 <= j <= y, 0 <= k <= z and i + j + k != n.

Approach: a single nested list comprehension over the three ranges, filtered
by the sum condition.

Time:  O(x * y * z)
Space: O(x * y * z) for the result
"""

x = int(input("enter x: "))
y = int(input("enter y: "))
z = int(input("enter z: "))
n = int(input("enter n: "))

result = [
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if i + j + k != n
]
print(result)
