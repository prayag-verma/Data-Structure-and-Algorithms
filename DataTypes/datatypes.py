# Introduction to Data Types in Python
# Python has various built-in data types that can be used to store different kinds of data.
# The most common data types are:
# 1. Integers: Whole numbers, e.g., 1, 2, 3
# 2. Floats: Decimal numbers, e.g., 1.0, 2.5, 3.14
# 3. Strings: Text data, e.g., "Hello", "Python"
# 4. Booleans: True or False values
# 5. Lists: Ordered collections of items, e.g., [1, 2, 3], ["a", "b", "c"]
# 6. Tuples: Immutable ordered collections, e.g., (1, 2, 3), ("a", "b", "c")
# 7. Dictionaries: Key-value pairs, e.g., {"key": "value"}, {"name": "Alice", "age": 25}
# 8. Sets: Unordered collections of unique items, e.g., {1, 2, 3}, {"a", "b", "c"}



# Example of using different data types

# ===================================================================

# Integers
a = 5
b = 3
print(a + b)  # Output: 8
print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'int'>

# ===================================================================

# Floats
a = 5.0
b = 3.0
print(a + b)  # Output: 8.0
print(type(a))  # Output: <class 'float'>
print(type(b))  # Output: <class 'float'>

# ===================================================================

# Strings
a = "Hello"
b = "World"
print(a + " " + b)  # Output: Hello World
print(type(a))  # Output: <class 'str'>
print(type(b))  # Output: <class 'str'>

# ===================================================================

# Booleans
print(True)  # Output: True
print(False)  # Output: False
print(type(True))  # Output: <class 'bool'>
print(type(False))  # Output: <class 'bool'>

# ===================================================================

# Lists
a = [1, 2, 3]
b = ["a", "b", "c"]
print(a + b)  # Output: [1, 2, 3, 'a', 'b', 'c']
print(type(a))  # Output: <class 'list'>
print(type(b))  # Output: <class 'list'>
# Accessing list elements
print(a[0])  # Output: 1
print(b[1])  # Output: b

# Modifying list elements
a[0] = 10
print(a)  # Output: [10, 2, 3]

# Adding elements to a list
a.append(4)
print(a)  # Output: [10, 2, 3, 4]

# Removing elements from a list
a.remove(2)
print(a)  # Output: [10, 3, 4]

# Slicing lists
print(a[1:3])  # Output: [3, 4]

# ===================================================================

# Tuples
a = (1, 2, 3)
b = ("a", "b", "c")
print(a + b)  # Output: (1, 2, 3, 'a', 'b', 'c')
print(type(a))  # Output: <class 'tuple'>
print(type(b))  # Output: <class 'tuple'>
# Accessing tuple elements
print(a[0])  # Output: 1
print(b[1])  # Output: b
# Modifying tuple elements (not allowed)
# Adding elements to a tuple (not allowed)
# Removing elements from a tuple (not allowed)
# Slicing tuples
print(a[1:3])  # Output: (2, 3)

# ===================================================================

# Dictionaries
a = {"name": "Alice", "age": 25}
b = {"city": "New York", "country": "USA"}
print(a)  # Output: {'name': 'Alice', 'age': 25}
print(b)  # Output: {'city': 'New York', 'country': 'USA'}
print(type(a))  # Output: <class 'dict'>
print(type(b))  # Output: <class 'dict'>

# Accessing dictionary elements
print(a["name"])  # Output: Alice
print(b["city"])  # Output: New York

# Modifying dictionary elements
a["age"] = 26   
print(a)  # Output: {'name': 'Alice', 'age': 26}

# Sets
a = {1, 2, 3}
b = {"a", "b", "c"}
print(a)  # Output: {1, 2, 3}
print(b)  # Output: {'a', 'b', 'c'}
print(type(a))  # Output: <class 'set'>
print(type(b))  # Output: <class 'set'>

# Adding elements to a set
a.add(4)
print(a)  # Output: {1, 2, 3, 4}

# Removing elements from a set
a.remove(2)
print(a)  # Output: {1, 3, 4}

# Checking membership in a set
print(1 in a)  # Output: True
print(2 in a)  # Output: False

# ===================================================================
# None
a = None
print(a)  # Output: None