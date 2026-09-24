print(issubclass(bool, int))  # True

# Because they are just 1 and 0 under the hood:
print(True + True)            # 2
print(False * 50)             # 0

# Pointer identity check confirms they are singletons
x = (5 > 3)
print(x is True)              # True