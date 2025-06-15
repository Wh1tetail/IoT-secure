from flask import Flask, render_template, jsonify
from scanner import scan_network
from security import analyze_devices
from database import get_all_devices, init_db, save_devices
from notifier import send_alert_to_telegram

app = Flask(__name__)

@app.route('/')
def dashboard():
    devices = get_all_devices()
    return render_template('dashboard.html', devices=devices)

@app.route('/scan')
def scan():
    raw_devices = scan_network()
    analyzed = analyze_devices(raw_devices)
    save_devices(analyzed) 

    suspicious = [dev for dev in analyzed if dev['status'] == 'suspicious']
    if suspicious:
        msg = "⚠️ Обнаружены подозрительные устройства:\n"
        for dev in suspicious:
            msg += f"• {dev['ip']} — {dev['mac']}\n"
        send_alert_to_telegram(msg)

    return jsonify(analyzed)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)