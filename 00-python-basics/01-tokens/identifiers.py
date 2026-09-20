# 1. CPython creates a PyLongObject containing 5 on the heap.
# 2. It binds the name tag 'a' to that object's memory address.
a = 5

# 1. CPython creates a NEW PyLongObject containing 10 on the heap.
# 2. It rips the name tag 'a' off the 5, and binds it to the 10.
# 3. The 5's refcount drops to 0, and it is garbage collected.
a = 10

# 'b' now points to the exact same PyObject as 'a'
b = a

# You can prove this using id(), which returns the underlying memory address (C pointer)
print(id(a) == id(b))  # True
