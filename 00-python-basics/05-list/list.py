# CPython allocates the dynamic array of pointers and sets the initial ob_size
data = ["Sabir", "Anuj", "Abhilash"]

# Creating a pre-sized list (useful for dynamic programming matrices)
dp_table = [0] * 100  # Creates an array of 100 pointers, all pointing to the '0' singleton
print(len(dp_table))

# 'enumerate' dynamically tracks the index for you
for index, value in enumerate(data):
    print(f"Position {index} holds {value}")


    original = [10, 20, 30, 40, 50]

# Extract from index 1 up to (but not including) 4
sub_list = original[1:4]  
print(sub_list)  # [20, 30, 40]

# Memory Proof: The lists are different objects...
print(original is sub_list)  # False

# ...but they point to the EXACT SAME integers in memory!
print(original[1] is sub_list[0])  # True
