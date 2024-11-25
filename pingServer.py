import ping3

def ping_server(host):
    response = ping3.ping(host)
    if response is None:
        print(f"Failed to ping {host}")
    else:
        print(f"Ping to {host} successful in {response} seconds")

# Example usage:
host = "google.com"
ping_server(host)