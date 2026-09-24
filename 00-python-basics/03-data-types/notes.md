# int
How CPython Implements int (The PyLongObject):
Because a massive number cannot fit into a standard 64-bit CPU register, CPython implements integers as "bignums" (a dynamic array of digits).

# bool The Integer Subclass
In Java, boolean is a distinct primitive. In C, it's often a macro for an integer. In Python, the bool type is strictly a subclass of int.

The Architecture (PyBoolObject):
There are only two boolean objects in existence: True and False. They are immortal singletons allocated when the VM boots. Because bool inherits from int, True is mathematically evaluated as 1 and False as 0.

You can literally perform arithmetic with them, which is heavily utilized in data science (like NumPy) for counting occurrences in boolean masks.

# complex: Built-in Engineering Mathematics
Unlike C++ (which requires #include <complex>) or Java (which lacks a standard complex primitive), Python treats complex numbers as a first-class core data type. This is a primary reason Python dominated scientific computing and electrical engineering early on.

The Architecture (PyComplexObject):
A complex object is a fixed-size C struct containing exactly two double (64-bit float) values: ob_real and ob_imag. Python uses the electrical engineering convention of j instead of the mathematical i to denote the imaginary part.

# str: The Memory-Morphing Array (PyUnicodeObject)
In C, a string is a char array terminated by \0. In Java, a string is backed by a UTF-16 array. Python strings are fundamentally different: they are immutable sequences of Unicode code points.
The Architecture (PEP 393 Flexible String Representation):Before Python 3.3, if your string had even one emoji or obscure character, CPython forced the entire string into 4-bytes-per-character (UTF-32) to maintain $O(1)$ indexing, wasting massive amounts of RAM.
Modern CPython uses a dynamic memory layout. When you create a string, the interpreter scans the characters:
* If every character is standard ASCII, the string uses 1 byte per character (Latin-1).
* If the largest character fits in 16 bits (e.g., most common language scripts), the entire string uses 2 bytes per character (UCS-2).
* If there is a massive code point (like an emoji 🚀), the entire string expands to 4 bytes per character (UCS-4).
This guarantees fast $O(1)$ index lookups (my_string[500]) without sacrificing memory efficiency for standard English text.

# Core Immutable Types: int, float, bool, complex, str, tuple, frozenset.

# Core Mutable Types: list, dict, set, bytearray, user-defined classes.

# Implicit Coercion (Type Promotion)
Python will never implicitly coerce a string to an integer or a list to a boolean. It strictly limits implicit coercion to mathematical operations between numeric types where no data loss occurs.

If you add a PyLongObject (int) and a PyFloatObject (float), CPython's evaluation loop recognizes the type mismatch. Instead of crashing, it temporarily promotes the integer to a float, performs C-level double-precision arithmetic, and returns a new PyFloatObject.

# Explicit Coercion (Object Factories)
When you write int("42"), you are not casting a pointer. You are calling the int class constructor.

CPython routes this call to a C-function that parses the string character-by-character, calculates the base-10 value, allocates a new PyLongObject in memory, and returns its pointer. The original string object is left completely untouched.

Python
# C++ style casting does not exist in Python
# val = (int)"42";  // SyntaxError

# Calling the constructor to allocate a new object
text = "42"
val = int(text)