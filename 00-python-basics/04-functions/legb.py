network_status = "Offline"  # Global (Module-level)

def attempt_connection():
    # This does NOT change the global. It creates a brand NEW Local tag.
    # The moment the function returns, this local tag is destroyed.
    network_status = "Online"  

def force_connection():
    # Tells the compiler: "Route all assignments to the Global dict"
    global network_status 
    network_status = "Online"  

def outer_wrapper():
    retries = 3  # Enclosing variable
    
    def inner_worker():
        # Tells the compiler: "Route this to the Enclosing closure cell"
        nonlocal retries 
        retries -= 1     
        
    inner_worker()
    print(f"Retries left: {retries}") # Prints 2