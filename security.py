KNOWN_MACS = {
    "00:41:0E:D1:27:A1": "Probook",
    "CE:1C:E6:D2:AB:D5": "Roma"
}

def analyze_devices(devices):
    analyzed = []
    for dev in devices:
        mac = dev['mac'].upper()
        status = "safe" if mac in KNOWN_MACS else "suspicious"
        name = KNOWN_MACS.get(mac, "Unknown Device")
        analyzed.append({
            'ip': dev['ip'],
            'mac': dev['mac'],
            'name': name,
            'status': status
        })
    return analyzed


