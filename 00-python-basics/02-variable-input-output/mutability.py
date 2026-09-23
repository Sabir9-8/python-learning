def modify_data(num, items):
    num += 10          # Creates a NEW PyLongObject. The outer 'x' is unaffected.
    items.append(4)    # Mutates the EXISTING PyListObject. The outer 'y' changes!

x = 5
y = [1, 2, 3]
modify_data(x, y)

print(x)  # Output: 5 (Immutable)
print(y)  # Output: [1, 2, 3, 4] (Mutable)