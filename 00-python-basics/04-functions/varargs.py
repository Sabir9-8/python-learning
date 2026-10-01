# 'host' gets the first string. 
# '*' packs everything else into a PyTupleObject named 'ports'
def ping_servers(host, *ports):
    print(f"Target: {host}")
    print(f"Tuple of ports: {ports}") 
    print(type(ports)) # <class 'tuple'>

    # You can safely iterate without worrying about stack memory boundaries
    for p in ports:
        print(f"Pinging {host}:{p}...")

ping_servers("192.168.1.1", 80, 443, 8080)