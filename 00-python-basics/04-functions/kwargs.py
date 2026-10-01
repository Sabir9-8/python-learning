def configure_router(ip, **kwargs):
    print(f"Configuring {ip}")
    print(type(kwargs)) # <class 'dict'>
    
    # CPython packed the extra keyword arguments into a hash map
    if "timeout" in kwargs:
        print(f"Timeout set to {kwargs['timeout']} seconds.")
    if "protocol" in kwargs:
        print(f"Protocol: {kwargs['protocol']}")

configure_router("10.0.0.1", timeout=30, protocol="TCP", retries=3)