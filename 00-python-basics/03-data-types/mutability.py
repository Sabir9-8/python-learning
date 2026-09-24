# CPython allocates a PyUnicodeObject. Let's look at its C pointer address.
name = "Logic"
print(id(name))  # e.g., 4321000112

# We try to "change" the string
name = name + " Loops"

# The original string was destroyed. 'name' now points to a completely new object.
print(id(name))  # e.g., 4321000955 (Different address!)

# CPython allocates a PyListObject.
team = ["Sabir"]
print(id(team))  # e.g., 4322000500

# We mutate the list in place
team.append("Ahamed")

# The pointer hasn't changed. The underlying C-array simply expanded.
print(id(team))  # e.g., 4322000500 (Exact same address!)