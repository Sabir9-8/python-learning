def calculate_throughput(data_size, time_seconds):
    """
    Calculates network throughput in MB/s.
    
    Args:
        data_size (int): Total bytes transferred.
        time_seconds (float): Duration of transfer.
    """
    return (data_size / 1024 / 1024) / time_seconds

# The documentation exists at RUNTIME as an attribute on the PyFunctionObject
print(calculate_throughput.__doc__)

# This is how the built-in help() function actually works
help(calculate_throughput)