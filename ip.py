import socket

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except socket.error:
        return "Kon het lokale IP-adres niet verkrijgen"

local_ip_address = get_local_ip()
print(f"Het lokale IP-adres is: {local_ip_address}")
