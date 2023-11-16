import socket

def find_available_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    _, port = s.getsockname()
    s.close()
    return port

# Voorbeeldgebruik
available_port = find_available_port()
print(f"Een beschikbare poort gevonden: {available_port}")
