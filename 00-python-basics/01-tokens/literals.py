# 'None' is a singleton. Always compare against it using 'is' (pointer comparison), not '=='
x = None
print(x is None)  # Extremely fast pointer check

# Small string interning in action
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True (CPython reused the string literal)

s3 = "hello world!"
s4 = "hello world!"
print(s3 is s4)  # True/False (Spaces/punctuation often defeat the basic intern cache in the REPL)
