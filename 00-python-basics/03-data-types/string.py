import sys

# 1-byte per character (ASCII)
s1 = "hello" 
print(sys.getsizeof(s1))  # 41 bytes (Header + metadata) + 5 bytes = 46 bytes

# 2-bytes per character (Cyrillic/Greek)
s2 = "hello Δ"
print(sys.getsizeof(s2))  # Header jumps to larger size, array uses 2 bytes/char = (58 + 14) = 72 bytes

# 4-bytes per character (Emoji)
# The single rocket emoji forces the ENTIRE string array into 4-byte width!
s3 = "hello 🚀"
print(sys.getsizeof(s3))  # 88 bytes(60 + 28)