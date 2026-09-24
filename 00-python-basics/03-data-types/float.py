import sys

# A PyFloatObject contains the standard 16-byte object header + an 8-byte C double.
# It will ALWAYS be exactly 24 bytes, no matter how large the number is.
pi = 3.14159
print(sys.getsizeof(pi)) # 24 bytes

# It suffers from standard IEEE 754 binary fraction representation errors
print(0.1 + 0.2 == 0.3)  # False (It actually equals 0.30000000000000004)
print(type(pi))