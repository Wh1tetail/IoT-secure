import nmap

def scan_network(subnet="192.168.110.0/24"):
    nm = nmap.PortScanner()
    nm.scan(hosts=subnet, arguments="-sP")  # Ping scan
    print("[DEBUG] Найдено хостов:", nm.all_hosts())

    devices = []
    for host in nm.all_hosts():
        mac = nm[host]['addresses'].get('mac', 'unknown')
        print(f"[DEBUG] {host} => MAC: {mac}")
        devices.append({
            'ip': host,
            'mac': mac
        })
    return devices
