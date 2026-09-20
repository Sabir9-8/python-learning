In C, C++, and Java, a variable is a memory box with a fixed size and type. When you write int a = 5;, the compiler allocates 4 bytes of memory, labels that exact physical address as a, and drops the binary value of 5 inside it. If you later write a = 10;, the CPU overwrites those exact 4 bytes with the new value.
In Python, this concept does not exist. Python does not have variables; it has Identifiers (name tags) and Objects (memory).
1. Identifiers (The Name Tags)
An identifier is simply a string name used to point to a PyObject on the heap.
Syntax Rules:
    Must start with a letter (A-Z, a-z) or an underscore (_).
    Can be followed by letters, numbers, or underscores.
    Case-sensitive (Data and data are different tags).
    Cannot be a reserved keyword (like if, def, class).
The Architectural Reality:
When you assign a value to an identifier, CPython does not put the value into the identifier. Instead, it adds an entry to a namespace dictionary (PyDictObject). The dictionary key is the identifier's name (e.g., "a"), and the value is a C-pointer to the PyObject on the heap.
# 1. CPython creates a PyLongObject containing 5 on the heap.
# 2. It binds the name tag 'a' to that object's memory address.
a = 5

# 1. CPython creates a NEW PyLongObject containing 10 on the heap.
# 2. It rips the name tag 'a' off the 5, and binds it to the 10.
# 3. The 5's refcount drops to 0, and it is garbage collected.
a = 10

# 'b' now points to the exact same PyObject as 'a'
b = a

# You can prove this using id(), which returns the underlying memory address (C pointer)
print(id(a) == id(b))  # True

In C++, b = a copies the value into a new memory box. In Python, b = a simply attaches a second name tag to the exact same object.

2. Literals (The Heap Objects)
A literal is the raw data value written directly into your source code. Whenever the CPython interpreter encounters a literal during the evaluation loop, it instantiates the corresponding PyObject.
Common Literals & Their Underlying C-Types:
# Literal Type	            Example	                    Underlying CPython Type
# Integer	            42, -10, 0xFF (Hex)	        PyLongObject (Arbitrary precision, never overflows)
# Float	                3.14, 1.5e2	                PyFloatObject (Standard C double, 64-bit IEEE 754)
# Complex	            2 + 3j	                    PyComplexObject (Two C doubles for real/imaginary)
# String	            "text", 'text', """multi""" PyUnicodeObject (Handles UTF-8/16/32 dynamically)
# Boolean	            True, False	                PyBoolObject (A subclass of integer where True=1, False=0)
# None	                None	                    PyNoneObject (A true singleton, equivalent to null)
# Collections	        [1, 2], (1, 2), {"x": 1}	PyListObject, PyTupleObject, PyDictObject
The Architectural Reality (Interning & Singletons):
Because creating PyObject structs is expensive, CPython optimizes certain literals at startup:
Singletons: True, False, and None are created exactly once when the VM boots. Whenever you type True, CPython just returns a pointer to that single eternal object.
String Interning: For short strings that look like identifiers (e.g., "hello"), Python often reuses the same memory address rather than creating duplicates, to speed up dictionary lookups.