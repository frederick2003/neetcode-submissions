# Python Lists / Arrays — DSA Interview Cheatsheet

## 1. Creating Lists

```python
a = []                          # empty list
a = [1, 2, 3]
a = list(range(5))              # [0, 1, 2, 3, 4]
a = [0] * 5                      # [0, 0, 0, 0, 0]
a = [x for x in range(10)]       # list comprehension
a = [[0]*cols for _ in range(rows)]   # 2D grid — CORRECT way (independent rows)
# a = [[0]*cols]*rows            # WRONG — all rows are the same object (aliasing bug!)
a, b = [1, 2], [3, 4]
a = list("hello")                # ['h','e','l','l','o']
a = list(some_iterable)
```

**Common interview trap:** `[[0]*n]*m` creates `m` references to the *same* inner list.
Mutating one row mutates all of them. Always use a comprehension for 2D arrays.

---

## 2. Indexing & Slicing

```python
a[0]           # first element
a[-1]          # last element
a[-2]          # second to last

a[1:3]         # elements at index 1,2 (end exclusive)
a[:3]          # first 3 elements
a[3:]          # from index 3 to end
a[:]           # shallow copy of whole list
a[::-1]        # reversed copy
a[::2]         # every 2nd element
a[1:5:2]       # start:stop:step

a[-3:]         # last 3 elements
a[:-1]         # all but last element
```

Slicing never throws `IndexError` (out-of-range bounds are just clipped);
direct indexing (`a[i]`) *does* throw `IndexError`.

---

## 3. Insertion

```python
a.append(x)          # add x to end                          O(1) amortized
a.insert(i, x)        # insert x at index i (shifts right)     O(n)
a.extend([x, y, z])   # append multiple elements               O(k)
a += [x, y]           # same as extend
a[len(a):] = [x, y]   # same as extend, via slice assignment

a[1:1] = [10, 20]     # insert multiple elements at index 1    O(n)
a.insert(0, x)         # insert at front (expensive, O(n))
```

For frequent front-insertions, prefer `collections.deque` (O(1) `appendleft`).

---

## 4. Deletion / Removal

```python
a.pop()            # remove & return last element              O(1)
a.pop(i)           # remove & return element at index i        O(n)
a.remove(x)        # remove FIRST occurrence of value x         O(n) (ValueError if missing)
del a[i]           # delete element at index i                 O(n)
del a[i:j]         # delete a slice
a.clear()          # remove everything                          O(n)

# remove all occurrences of a value
a = [x for x in a if x != val]

# safe pop (avoid IndexError)
x = a.pop() if a else None
```

**Removing while iterating — classic bug:**
```python
# WRONG: mutating list while iterating over it skips elements
for x in a:
    if x == 3:
        a.remove(x)

# RIGHT: iterate over a copy, or build a new list, or go backwards
for x in a[:]:
    if x == 3:
        a.remove(x)

for i in range(len(a) - 1, -1, -1):   # iterate backwards, safe for in-place deletes
    if a[i] == 3:
        del a[i]
```

---

## 5. Iteration Patterns

```python
# forward
for x in a:
    ...

for i in range(len(a)):
    ...

for i, x in enumerate(a):
    ...

# backward
for x in reversed(a):
    ...

for i in range(len(a) - 1, -1, -1):
    ...

for i, x in reversed(list(enumerate(a))):
    ...

# two lists in parallel
for x, y in zip(a, b):
    ...

# with index, in parallel
for i, (x, y) in enumerate(zip(a, b)):
    ...

# two-pointer (very common in DSA)
left, right = 0, len(a) - 1
while left < right:
    # process a[left], a[right]
    left += 1
    right -= 1

# sliding window
left = 0
for right in range(len(a)):
    # expand window with a[right]
    while <condition to shrink>:
        # shrink from left
        left += 1
```

---

## 6. Searching

```python
x in a                  # membership test         O(n)
a.index(x)               # first index of x        O(n), raises ValueError if absent
a.index(x, start, end)   # search within a slice

import bisect
bisect.bisect_left(a, x)    # leftmost insertion point (a must be sorted) O(log n)
bisect.bisect_right(a, x)   # rightmost insertion point
bisect.insort(a, x)         # insert x keeping a sorted, O(n) due to shift
```

---

## 7. Sorting

```python
a.sort()                          # in-place, ascending, O(n log n), stable (Timsort)
a.sort(reverse=True)              # in-place, descending
b = sorted(a)                     # returns NEW sorted list, leaves a untouched
b = sorted(a, reverse=True)

# custom key
a.sort(key=lambda x: abs(x))
a.sort(key=len)                    # e.g. sort strings by length

# multi-criteria sort (primary, then secondary)
a.sort(key=lambda x: (x[0], -x[1]))   # ascending on x[0], descending on x[1]

# sorting list of tuples/lists (very common)
pairs = [(3, 'c'), (1, 'a'), (2, 'b')]
pairs.sort()                       # sorts by first elem, then second (lexicographic)
pairs.sort(key=lambda p: p[1])     # sort by second element only

# sorting list of lists by a specific column
matrix = [[3, 9], [1, 5], [2, 7]]
matrix.sort(key=lambda row: row[0])          # by column 0
matrix.sort(key=lambda row: (row[0], row[1]))# by column 0, tie-break column 1

# sort with a separate index (get sorted order without losing original indices)
idx = sorted(range(len(a)), key=lambda i: a[i])

# reverse stability trick: sort ascending on secondary key only
# (use negative for numeric descending; for strings, sort twice — Timsort is stable)
```

Python's `sort`/`sorted` is **stable**: equal elements keep their relative order.
That means for tie-breaking by "sort A, then sort B" you can do two passes,
last sort = primary key (relies on stability), instead of a tuple key.

---

## 8. Reversing

```python
a.reverse()          # in-place                    O(n)
b = a[::-1]          # new reversed list
b = list(reversed(a))# new reversed list (iterator-based, memory efficient)
```

---

## 9. Copying (shallow vs deep — huge interview gotcha)

```python
b = a                 # SAME object — mutating b mutates a
b = a[:]              # shallow copy — new outer list, same inner references
b = a.copy()          # same as a[:]
b = list(a)           # same as a.copy()

import copy
b = copy.deepcopy(a)  # fully independent copy, needed for nested lists/objects
```

```python
matrix = [[1, 2], [3, 4]]
shallow = matrix.copy()
shallow[0][0] = 99      # ALSO changes matrix[0][0]! (inner lists shared)

deep = copy.deepcopy(matrix)
deep[0][0] = 99          # matrix unaffected
```

---

## 10. Useful Built-ins & Functions

```python
len(a)
sum(a)
sum(a, start=0)
max(a); min(a)
max(a, key=lambda x: x[1])
min(a, default=None)             # avoid error on empty list

any(x > 0 for x in a)
all(x > 0 for x in a)

a.count(x)                        # count occurrences of x     O(n)

list(map(str, a))                  # apply function to each elem
list(filter(lambda x: x > 0, a))   # keep elements matching predicate
from functools import reduce
reduce(lambda acc, x: acc + x, a, 0)

a.index(x)

# unpacking
first, *rest = a
*init, last = a
first, *mid, last = a

# flattening a list of lists (one level)
flat = [x for row in matrix for x in row]
import itertools
flat = list(itertools.chain.from_iterable(matrix))

# unique values, order not preserved
uniq = list(set(a))
# unique values, order preserved (Python 3.7+)
uniq = list(dict.fromkeys(a))
```

---

## 11. Common Two-List / Matrix Idioms

```python
# transpose a matrix
transposed = [list(row) for row in zip(*matrix)]

# rotate matrix 90 deg clockwise
rotated = [list(row) for row in zip(*matrix[::-1])]

# element-wise combine two lists
combined = [x + y for x, y in zip(a, b)]

# pairwise adjacent elements
for x, y in zip(a, a[1:]):
    ...

# chunk a list into groups of n
chunks = [a[i:i+n] for i in range(0, len(a), n)]

# prefix sums (common for range-sum problems)
prefix = [0] * (len(a) + 1)
for i, x in enumerate(a):
    prefix[i+1] = prefix[i] + x
# sum of a[i:j] == prefix[j] - prefix[i]
```

---

## 12. Swapping & In-place Tricks

```python
a[i], a[j] = a[j], a[i]         # swap without temp variable

# reverse a sub-range in place
def reverse_range(a, i, j):
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

# rotate array left by k (in place, O(n), O(1) extra space)
def rotate_left(a, k):
    n = len(a)
    k %= n
    a[:] = a[k:] + a[:k]
```

---

## 13. Complexity Cheat-Sheet (CPython list = dynamic array)

| Operation                  | Complexity          |
|-----------------------------|----------------------|
| Index access `a[i]`         | O(1)                 |
| Index assignment `a[i]=x`   | O(1)                 |
| `append`                    | O(1) amortized       |
| `pop()` (from end)          | O(1)                 |
| `pop(i)` / `insert(i, x)`   | O(n)                 |
| `remove(x)`                 | O(n)                 |
| slicing `a[i:j]`            | O(j-i)               |
| `x in a`                    | O(n)                 |
| `len(a)`                    | O(1)                 |
| `sort()` / `sorted()`       | O(n log n)           |
| `reverse()`                 | O(n)                 |
| copy (`a[:]`, `.copy()`)    | O(n)                 |

---

## 14. Gotchas Checklist (skim before an interview)

- `[[0]*n]*m` → aliased rows. Use `[[0]*n for _ in range(m)]`.
- Mutating a list while iterating over it → skipped elements / bugs. Iterate over a copy or go backwards.
- `sorted(a)` returns a new list; `a.sort()` mutates in place and returns `None`.
- Shallow copy (`a.copy()`, `a[:]`) does **not** deep-copy nested lists.
- `a.remove(x)` removes by **value**, `a.pop(i)` / `del a[i]` remove by **index** — easy to mix up.
- Negative indices wrap around (`a[-1]` is last); slicing with out-of-range bounds does NOT raise.
- Python sort is **stable** — exploit this for multi-key sorts.
- `list.index()` and `list.remove()` raise `ValueError` if not found (not `None`/`False`).
- Default mutable argument bug: `def f(a=[]):` — the same list persists across calls. Use `def f(a=None): a = a or []`.
- `+=` on a list mutates in place (calls `__iadd__`); `a = a + [x]` creates a new list — matters when the list is shared/passed around.