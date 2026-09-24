import sys

# Stored as two C doubles (16 bytes) + standard 16-byte object header = 32 bytes
z = 3 + 4j
print(type(z))           # <class 'complex'>
print(sys.getsizeof(z))  # 32 bytes

# You can access the underlying floats directly
print(z.real)            # 3.0
print(z.imag)            # 4.0