1. Variables: Mutability and Pass-by-Object-Reference
Since we established that variables are just name tags attached to memory, the critical behavior you must understand coming from C++ is mutability. When you pass a variable into a function, Python uses "pass-by-object-reference" (similar to Java's object references, but applied universally to everything, including integers).

# Immutable Types (Integers, Strings, Tuples): If you try to modify an immutable object inside a function, CPython allocates a brand new object and moves the local name tag to it. The original object outside the function remains unchanged.

# Mutable Types (Lists, Dictionaries, Sets): If you modify a mutable object in place (e.g., using .append()), the underlying memory is mutated. All other variables pointing to that object will immediately see the change.

# In CPython, constants do not exist at the runtime level.

# Reading Input:
The input() function halts the VM and reads from sys.stdin until it hits a newline character. Just like command-line arguments in sys.argv, it always returns a string (PyUnicodeObject). You are responsible for instantiating new types if you need them.

# Writing Output:
The print() function is a wrapper around sys.stdout.write(). It automatically handles converting objects to strings (via their internal __str__ method), separates multiple arguments with spaces, and appends a newline at the end. You can override this behavior using keyword arguments.