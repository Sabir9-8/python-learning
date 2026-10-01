In Python, a function is a first-class object (PyFunctionObject) allocated dynamically on the heap, possessing state, attributes, and a memory address exactly like an integer or a string.

When the CPython Virtual Machine encounters a def block during top-to-bottom execution, it performs three operations in real-time:

* It compiles the internal block of code into a bytecode structure called a PyCodeObject.

* It wraps that bytecode inside a new PyFunctionObject, which tracks metadata like default arguments, closures, and the global namespace.

* It binds the resulting object pointer to the identifier name in the current dictionary namespace.

Because functions are just objects on the heap, you can pass them around exactly like C function pointers, but with the full flexibility of object-oriented memory.

When you invoke a function using parentheses (), CPython halts the current execution flow and pushes a PyFrameObject onto the execution stack.

Isolated Namespaces: The frame contains its own local PyDictObject. Any variable you assign inside the function lives exclusively in this local dictionary, protecting the global state.

Garbage Collection Hooks: When the function hits a return statement, the PyFrameObject is popped off the stack and destroyed. CPython instantly decrements the reference count (Py_refcnt) of every local variable created inside that frame. If those counts hit zero, the memory is immediately reclaimed.

Without functions, all variables would dump into the global namespace, keeping their memory locked indefinitely and destroying application performance.

1. Built-In Functions: The Native C Fast-Path (PyCFunctionObject)When you call a built-in function like len(), sum(), or print(), you are not executing Python code. You are executing pre-compiled, highly optimized C code embedded directly within the CPython runtime.The Architecture:Built-in functions are instantiated in memory as PyCFunctionObject structs. These objects contain a direct C-pointer to the underlying C implementation.For example, when you call len(my_list):The VM does not create a new execution frame.It does not iterate over the list.It directly executes a C macro that reads the ob_size property of the PyVarObject C-struct.This means len() executes in true $O(1)$ time, taking barely a fraction of a microsecond, bypassing the Python evaluation loop entirely.

2. User-Defined Functions: The Bytecode Engine (PyFunctionObject)When you use the def keyword to create your own function, CPython compiles your logic into custom bytecode and wraps it in a PyFunctionObject.The Architecture:When you call a user-defined function, the CPython interpreter (ceval.c) must do significant architectural work:It halts current execution.It dynamically allocates a new PyFrameObject on the heap to track local variables and scope.It maps the arguments you passed into the frame's local dictionary (PyDictObject).It starts a new iteration of the massive switch statement inside the CPython evaluation loop to interpret your bytecode instruction by instruction.Upon return, it destroys the frame and garbage-collects variables.

3. Default Arguments: The "Mutable Default" Trap
This is the single most common bug for C++ and Java developers moving to Python, rooted directly in how CPython compiles the def statement.

In C++, default arguments are evaluated every single time the function is called.
In Python, default arguments are evaluated exactly ONCE, at the exact moment the CPython compiler executes the def statement and allocates the PyFunctionObject. It stores a pointer to the default object inside a tuple (__defaults__) directly on the function struct.

If you use an immutable default (like an integer or string), it behaves normally. But if you use a mutable default (like a list or dictionary), that exact same heap object is shared across every single function call.

1. *args: Packing Positional Overflow (PyTupleObject)
When you prefix a parameter with a single asterisk *, you are instructing the CPython evaluation frame to intercept any "leftover" positional arguments that don't match explicitly defined parameters.

The Architecture:
CPython dynamically allocates a Tuple (PyTupleObject) on the heap, dumps all the extra arguments into it, and binds it to the identifier. (Note: args is just a naming convention; *data works exactly the same).

Because tuples are strictly immutable, this operation is fast and memory-safe.

2. **kwargs: Packing Keyword Overflow (PyDictObject)
If a user passes keyword arguments (e.g., timeout=5) that are not explicitly defined in your function signature, CPython will crash with a TypeError—unless you use the double asterisk **.

The Architecture:
The ** operator intercepts overflow keyword arguments, dynamically allocates a Dictionary (PyDictObject), uses the parameter names as string keys, and binds the values to them.

The Ordering Rule: Because of how the CPython parser scans syntax, parameters must strictly follow this order: Standard parameters $\rightarrow$ *args $\rightarrow$ Standard keyword-only parameters $\rightarrow$ **kwargs.