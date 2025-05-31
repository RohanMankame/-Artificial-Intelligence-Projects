# Python Utility Scripts and Fraction Class

This project is a collection of Python utility functions and a custom `Fraction` class. The scripts provide functionalities for sequence manipulation, list comprehensions, and other common algorithms.

---

## 🚀 Features

### 1. Sequence Manipulation
* `list_add(l1, l2)`: Returns the union of two lists.
* `dict_extend(dict1, dict2)`: Extends a dictionary with another. If a key exists in both, their values are combined into a list.
* `dict_invert(dct)`: Inverts a dictionary, swapping keys and values. If multiple keys have the same value, the new value becomes a list of those keys.
* `dict_nested(lst)`: Creates a nested dictionary from a list of keys.

---

### 2. List Comprehension and Dictionary Operations
* `list_product(l1, l2)`: Returns the Cartesian product of two lists.
* `list_flatten(list_of_seqs)`: Flattens a list of sequences into a single list.
* `nlargest(dct, n)`: Returns the `n` items with the largest values from a dictionary.
* `unique_values(list_of_dicts)`: Returns a list of unique values from a list of dictionaries.

---

### 3. Other Algorithms
* `encode(input_str)`: Performs run-length encoding on a string (e.g., "AAABBC" becomes "3A2B1C").
* `decode(input_str)`: Decodes a run-length encoded string.
* `camel_case(var_name)`: Converts a snake_case string to camelCase.

---

### 4. Fraction Class
A class to represent and perform arithmetic on fractional numbers.
* Supports addition, subtraction, multiplication, and division.
* Supports negation and comparison operators (`==`, `<`).
* Can be called as a function to return the float equivalent.
* Raises a `ZeroDivisionError` for invalid operations.

---

## ⚙️ Installation

No installation is required. Simply download the Python file and import the functions and the `Fraction` class into your project.

```python
from your_file_name import list_add, Fraction # Replace your_file_name with the actual name of your Python file
```

---

## Usage

Here are some examples of how to use the functions and the `Fraction` class:

### Sequences
```python
# list_add
print(list_add([1, 2, 3], [3, 4, 5]))
# Output: [1, 2, 3, 4, 5] (order may vary due to set conversion)

# dict_extend
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
print(dict_extend(d1, d2))
# Output: {'a': [1], 'b': [2, 3], 'c': 4}

# dict_invert
d = {'a': 1, 'b': 2, 'c': 1}
print(dict_invert(d))
# Output: {1: ['a', 'c'], 2: 'b'} (or {1: ['c', 'a'], 2: 'b'} - order of keys in list may vary)


# dict_nested
print(dict_nested(['a', 'b', 'c']))
# Output: {'a': {'b': {'c': {}}}}
```

### List Comprehension and Dictionary Operations
```python
# list_product
print(list_product([1, 2], ['a', 'b']))
# Output: [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b']]

# list_flatten
print(list_flatten([[1, 2], [3, 4]]))
# Output: [1, 2, 3, 4]

# nlargest
d = {'a': 10, 'b': 20, 'c': 5}
print(nlargest(d, 2))
# Output: {'b': 20, 'a': 10} (order might vary if values are equal)

# unique_values
list_of_dicts = [{'a': 1, 'b': 2}, {'c': 2, 'd': 3}]
print(unique_values(list_of_dicts))
# Output: [1, 2, 3] (order may vary)
```

### Other Algorithms
```python
# encode and decode
encoded = encode("AAABBC")
print(encoded)
# Output: "3A2B1C"
decoded = decode(encoded)
print(decoded)
# Output: "AAABBC"

# camel_case
print(camel_case("hello_world_example"))
# Output: "helloWorldExample"
```

### Fraction Class
```python
# Create Fractions
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

# To print the fraction nicely, you'll need to ensure the __str__ method is correctly defined within the Fraction class:
# class Fraction:
#     # ... other methods ...
#     def __str__(self):
#         return f"{self.numerator}/{self.denominator}"

# Assuming __str__ is correctly implemented:
# Addition
# print(f1 + f2) # Output: 10/8 (or simplified if you add simplification logic)

# Subtraction
# print(f1 - f2) # Output: -2/8 (or simplified)

# Multiplication
# print(f1 * f2) # Output: 3/8

# Division
# print(f1 / f2) # Output: 4/6 (or simplified)

# Equality
print(f1 == Fraction(1, 2))
# Output: True

# Less than
print(f1 < f2)
# Output: True

# Get float value
print(f1())
# Output: 0.5
