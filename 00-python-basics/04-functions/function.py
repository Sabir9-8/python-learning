def compute_data(x):
    return x * 2

# compute_data is just a name tag pointing to a PyFunctionObject
print(type(compute_data))  # <class 'function'>
print(id(compute_data))    # Memory address on the heap

# You can bind another identifier to the exact same function object
alias = compute_data
print(alias(10))           # 20

def manual_sum(numbers):
    total = 0
    # Python creates a loop, fetches the iterator, evaluates bytecode for addition,
    # and re-allocates a new PyLongObject for 'total' a million times.
    for n in numbers:
        total += n
    return total

numbers = [3, 4, 5, 8, 9]
# CPython intercepts the call, sees a PyCFunctionObject, hands the list 
# directly to a native C loop, and runs hardware-level addition without 
# creating a single Python frame or evaluating any bytecode inside the loop.
total = sum(numbers)