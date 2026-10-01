# WARNING: 'cache' is instantiated ONCE when this line compiles.
def add_user(user, cache=[]):
    cache.append(user)
    return cache

# First call works as expected
print(add_user("Alice"))  # Output: ['Alice']

# Second call mutates the EXACT SAME PyListObject from the first call!
print(add_user("Bob"))    # Output: ['Alice', 'Bob'] 

# Proof: We can inspect the function's internal C-struct
print(add_user.__defaults__)  # Output: (['Alice', 'Bob'],)