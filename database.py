import sqlite3

def init_db():
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            mac TEXT,
            name TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_all_devices():
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ip, mac, name, status FROM devices")
    rows = cursor.fetchall()
    conn.close()
    return [
        {'ip': row[0], 'mac': row[1], 'name': row[2], 'status': row[3]}
        for row in rows
    ]

def save_devices(devices):
    conn = sqlite3.connect('devices.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM devices")
    for dev in devices:
        cursor.execute("INSERT INTO devices (ip, mac, name, status) VALUES (?, ?, ?, ?)",
                       (dev['ip'], dev['mac'], dev['name'], dev['status']))
    conn.commit()
    conn.close()