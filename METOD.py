# Использование append()
my_list = []
my_list.append(5)
print(my_list)  # Выведет: [5]

# Использование extend()
my_list = [1, 2, 3]
other_list = [4, 5, 6]
my_list.extend(other_list)
print(my_list)  # Выведет: [1, 2, 3, 4, 5, 6]

# Использование insert()
my_list = [1, 2, 3]
my_list.insert(1, "a")
print(my_list)  # Выведет: [1, "a", 2, 3]

# Использование remove()
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Выведет: [1, 3]

# Использование pop()
my_list = [1, 2, 3]
popped = my_list.pop()
print(my_list)  # Выведет: [1, 2]
print(popped)   # Выведет: 3

# Использование clear()
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Выведет: []

# Использование index()
my_list = ["apple", "banana", "cherry"]
index = my_list.index("banana")
print(index)  # Выведет: 1

# Использование count()
my_list = ["apple", "banana", "cherry", "banana"]
count = my_list.count("banana")
print(count)  # Выведет: 2

# Использование sort()
my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()
print(my_list)  # Выведет: [1, 1, 2, 3, 4, 5, 9]

# Использование reverse()
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # Выведет: [5, 4, 3, 2, 1]