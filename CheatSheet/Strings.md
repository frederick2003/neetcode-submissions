# Python Strings — DSA Interview Cheatsheet

Strings in Python are **immutable** sequences of characters. This one fact drives
almost every gotcha below — every "modification" actually creates a new string.

---

## 1. Creating & Basic Properties

```python
s = "hello"
s = 'hello'
s = """multi
line"""
s = ""                      # empty string
len(s)                       # length
s[0]                          # first char
s[-1]                         # last char

# strings are immutable — this raises TypeError
# s[0] = 'H'

# to "modify" a string, build a new one
s = 'H' + s[1:]
```

---

## 2. Indexing & Slicing (same rules as lists)

```python
s[1:4]        # substring, end exclusive
s[:3]          # first 3 chars
s[3:]          # from index 3 to end
s[::-1]        # reversed string — the classic Python reverse idiom
s[::2]         # every 2nd char
s[-3:]         # last 3 chars

# slicing never raises IndexError, even out of range
s[100:200]     # returns ''
```

---

## 3. String <-> List Conversion (needed because strings are immutable)

```python
chars = list(s)              # ['h','e','l','l','o']
s = ''.join(chars)            # back to string — the idiomatic way to build strings

# building a string efficiently in a loop
parts = []
for x in items:
    parts.append(str(x))
result = ''.join(parts)       # O(n) — MUCH better than repeated s += x in a loop

# NEVER do this in a hot loop:
# s = ""
# for c in chars:
#     s += c                  # O(n) per concat -> O(n^2) total, creates new string each time
```

---

## 4. Insertion / "Modification" (build new strings)

```python
s = s + "!"                     # concatenation -> new string
s = f"{s}!"                      # f-string, often cleanest
s = "%s!" % s                    # old-style formatting

s = s[:i] + "X" + s[i:]          # insert "X" at index i
s = s[:i] + s[i+1:]               # delete char at index i
s = s[:i] + "X" + s[i+1:]         # replace char at index i (since can't do s[i]='X')

s.replace(old, new)               # replace ALL occurrences, returns new string
s.replace(old, new, 1)            # replace only first occurrence
```

---

## 5. Iteration Patterns

```python
# forward
for c in s:
    ...

for i in range(len(s)):
    ...

for i, c in enumerate(s):
    ...

# backward
for c in reversed(s):
    ...

for i in range(len(s) - 1, -1, -1):
    ...

# two-pointer (palindrome checks, etc.)
left, right = 0, len(s) - 1
while left < right:
    if s[left] != s[right]:
        return False
    left += 1
    right -= 1

# sliding window (longest substring problems)
left = 0
seen = set()
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    # window is s[left:right+1]
```

---

## 6. Searching

```python
"lo" in s                     # membership test          O(n)
s.find("lo")                  # first index, or -1 if not found
s.rfind("lo")                 # last index, or -1 if not found
s.index("lo")                  # like find, but raises ValueError if not found
s.rindex("lo")

s.count("l")                   # count non-overlapping occurrences
s.startswith("he")
s.endswith("lo")
s.startswith(("he", "wo"))     # tuple of prefixes — matches any
```

---

## 7. Splitting & Joining

```python
s.split()                      # split on any whitespace, drops empty strings
s.split(",")                    # split on exact delimiter
s.split(",", 1)                 # split at most once (maxsplit)
s.rsplit(",", 1)                # split from the right
s.splitlines()                   # split on line boundaries, no trailing '\n'

",".join(["a", "b", "c"])        # 'a,b,c'
"".join(chars)                    # concatenate list of chars back into a string

s.partition("=")                  # ('before', '=', 'after') — always 3-tuple
s.rpartition("=")                 # split from the right
```

---

## 8. Stripping & Padding

```python
s.strip()                      # remove leading/trailing whitespace
s.strip("xy")                   # remove leading/trailing chars in the set {x,y}
s.lstrip(); s.rstrip()

s.zfill(5)                      # pad with leading zeros to length 5 ("42" -> "00042")
s.ljust(10, '-')                # pad right to width 10
s.rjust(10, '-')                 # pad left to width 10
s.center(10, '-')                 # center-pad to width 10
```

---

## 9. Case & Character Checks

```python
s.lower(); s.upper()
s.title()                       # "hello world" -> "Hello World"
s.capitalize()                   # "hello world" -> "Hello world"
s.swapcase()

c.isalpha()
c.isdigit()                      # note: '②'.isdigit() -> True; use isdecimal() for stricter check
c.isalnum()
c.isspace()
c.isupper(); c.islower()
c.isascii()
```

---

## 10. Sorting Strings

```python
sorted(s)                        # returns a LIST of chars, sorted
''.join(sorted(s))                 # sorted string
''.join(sorted(s, reverse=True))    # sorted descending

# check anagram
sorted(s1) == sorted(s2)

# sort list of strings
words = ["banana", "apple", "cherry"]
words.sort()                        # lexicographic
words.sort(key=len)                  # by length
words.sort(key=lambda w: (len(w), w))# by length, then lexicographic
words.sort(key=str.lower)            # case-insensitive sort
```

---

## 11. Character <-> Code Point (ASCII/Unicode tricks)

```python
ord('a')                     # 97 — char to code point
chr(97)                       # 'a' — code point to char

# common trick: map 'a'..'z' to 0..25
idx = ord(c) - ord('a')
c = chr(idx + ord('a'))

# check if char is a lowercase letter without .isalpha()
'a' <= c <= 'z'
```

---

## 12. Formatting

```python
name, age = "Ann", 30
f"{name} is {age}"                     # f-string (preferred)
f"{value:.2f}"                          # 2 decimal places
f"{value:>10}"                          # right-align, width 10
f"{value:05d}"                          # zero-pad int to width 5
"{} is {}".format(name, age)
"%s is %d" % (name, age)
```

---

## 13. Regex (`re` module) — common interview needs

```python
import re

re.search(r"\d+", s)              # first match object, or None
re.findall(r"\d+", s)              # list of all matches (strings)
re.sub(r"\s+", " ", s)             # replace all matches with a string
re.split(r"[,;]", s)                # split on multiple delimiters
re.match(r"^\d+", s)                 # match only at start of string
bool(re.fullmatch(r"[a-z]+", s))     # entire string must match
```

---

## 14. Common String Algorithm Idioms

```python
# palindrome check
def is_palindrome(s):
    return s == s[::-1]

# palindrome check ignoring non-alphanumerics, case-insensitive
def is_palindrome_clean(s):
    filtered = [c.lower() for c in s if c.isalnum()]
    return filtered == filtered[::-1]

# reverse words in a sentence
def reverse_words(s):
    return " ".join(s.split()[::-1])

# check anagram
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
    # or: from collections import Counter; Counter(s1) == Counter(s2)

# character frequency count
from collections import Counter
freq = Counter(s)                    # dict-like {char: count}
freq.most_common(3)                   # top 3 most frequent chars

# first non-repeating character
def first_unique(s):
    freq = Counter(s)
    for i, c in enumerate(s):
        if freq[c] == 1:
            return i
    return -1

# check if s2 is a rotation of s1
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)

# longest common prefix among a list of strings
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix

# check if t is a subsequence of s
def is_subsequence(t, s):
    it = iter(s)
    return all(c in it for c in t)
```

---

## 15. Complexity Cheat-Sheet

| Operation                   | Complexity                                                               |
| --------------------------- | ------------------------------------------------------------------------ |
| Index access `s[i]`         | O(1)                                                                     |
| Slicing `s[i:j]`            | O(j-i)                                                                   |
| `len(s)`                    | O(1)                                                                     |
| `s + t` (concatenation)     | O(len(s)+len(t))                                                         |
| `s in t` (substring search) | O(n·m) worst case (CPython uses an optimized algorithm, ~O(n+m) typical) |
| `s.find(t)` / `s.index(t)`  | same as above                                                            |
| `s.split()` / `.join()`     | O(n)                                                                     |
| `sorted(s)`                 | O(n log n)                                                               |
| repeated `s += c` in a loop | O(n) per op -> **O(n²) total** — avoid! Use a list + `''.join()`         |

---

## 16. Gotchas Checklist (skim before an interview)

- Strings are **immutable** — any "in place" modification (`s[i] = 'x'`) raises `TypeError`. Convert to `list(s)`, mutate, then `''.join()`.
- Building a string with repeated `+=` in a loop is O(n²). Collect pieces in a list and `''.join()` at the end — O(n).
- `s.find(x)` returns `-1` when not found; `s.index(x)` raises `ValueError`. Don't mix them up.
- `.split()` (no args) splits on **any whitespace and drops empty strings**; `.split(" ")` splits on a literal space and _keeps_ empty strings between consecutive spaces.
- `sorted(s)` returns a **list of characters**, not a string — wrap with `''.join(...)` if you need a string back.
- `c.isdigit()` is true for some non-ASCII digit-like characters (e.g. superscripts); use `c.isdecimal()` for strict `0-9` checks in edge-case-sensitive problems.
- Comparing strings (`<`, `>`) is lexicographic by Unicode code point — uppercase letters sort before lowercase (`'Z' < 'a'`).
- `s * n` repeats a string — handy but easy to forget (`"ab" * 3 == "ababab"`).
- f-strings evaluate expressions at the time of formatting; watch out for mutable defaults inside them just like anywhere else in Python.
- `in` on a string checks for a **substring**, not a single element like it might imply with lists — `"ell" in "hello"` is `True`.
