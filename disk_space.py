import psutil # pip install psutil

def get_disk_usage(path='/'):
    disk_info = psutil.disk_usage(path)
    return disk_info

def main():
    disk_info = get_disk_usage()

    print(f"Totale schijfruimte: {disk_info.total / (1024 ** 3):.2f} GB")
    print(f"Gebruikte schijfruimte: {disk_info.used / (1024 ** 3):.2f} GB")
    print(f"Beschikbare schijfruimte: {disk_info.free / (1024 ** 3):.2f} GB")
    print(f"Percentage gebruikte schijfruimte: {disk_info.percent}%")

if __name__ == "__main__":
    main()
