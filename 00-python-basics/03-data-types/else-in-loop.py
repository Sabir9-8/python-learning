server_ports = [80, 443, 8080]
target_port = 8080

for port in server_ports:
    if port == target_port:
        print("Port found! Breaking loop.")
        break
else:
    # This executes ONLY because the loop finished without breaking.
    # No "bool found" flag needed!
    print("Target port is not in the list.")

def fetch_user_data():
    # TODO: Implement database connection later
    pass  # Satisfies the parser, does absolutely nothing at runtime

status = 200

if status == 500:
    print("Server Error")
elif status == 200:
    # We want to explicitly ignore 200s, but we MUST put something here
    pass 
else:
    print("Unknown state")