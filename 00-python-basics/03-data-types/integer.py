import sys

# A small integer (fits in a single 30-bit chunk)
# Header (24 bytes) + 1 chunk (4 bytes) = 28 bytes total
x = 100
print(sys.getsizeof(x))  # 28 bytes

# A massive integer (requires multiple 30-bit chunks)
# As the number grows, CPython dynamically allocates more array slots!
y = 10 ** 100
print(sys.getsizeof(y))  # 72 bytes!