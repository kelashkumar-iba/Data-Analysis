# Creating a new List:
# Empty list
empty_list = []

# List of integers
int_list = [1, 2, 3, 4, 5]

# List of strings
str_list = ["apple", "banana", "cherry"]

# Mixed data types
mixed_list = [1, "hello", 3.14, True]

# List of lists (nested list)
nested_list = [[1, 2], [3, 4], [5, 6]]

# ---------------------------------------------
# Accessing elements
print(int_list[0])  # Output: 1
print(str_list[1])  # Output: banana

# Negative indexing
print(int_list[-1])  # Output: 5
print(str_list[-2])  # Output: banana

# ----------------------------------------------
# Slicing lists
print(int_list[1:3])  # Output: [2, 3]
print(str_list[:2])   # Output: ['apple', 'banana']
print(int_list[2:])   # Output: [3, 4, 5]

# Step slicing
print(int_list[::2])  # Output: [1, 3, 5]

# -----------------------------------------------
# Changing elements
int_list[0] = 10
print(int_list)  # Output: [10, 2, 3, 4, 5]

# Changing a range of elements
int_list[1:3] = [20, 30]
print(int_list)  # Output: [10, 20, 30, 4, 5]

# -------------------------------------------------
# Append: adds a single element to the end
int_list.append(6)
print(int_list)  # Output: [10, 20, 30, 4, 5, 6]

# Extend: adds multiple elements to the end
int_list.extend([7, 8])
print(int_list)  # Output: [10, 20, 30, 4, 5, 6, 7, 8]

# Insert: adds an element at a specific position
int_list.insert(2, 25)
print(int_list)  # Output: [10, 20, 25, 30, 4, 5, 6, 7, 8]
