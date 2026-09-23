# Coming from C++ cin >> age, you must explicitly cast in Python
raw_age = input("Enter your age: ") 
age = int(raw_age)  # Parses the string and allocates a new PyLongObject on the heap