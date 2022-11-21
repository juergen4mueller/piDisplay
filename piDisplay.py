import eel
import time
import threading
import sys
import os
import requests
import json
import pprint
from datetime import datetime
import socket


def get_ip_address():
    """Ermittlung der IP-Adresse im Netzwerk

    Returns:
        str: lokale IP-Adresse
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    socket_ip = s.getsockname()[0]
    s.close()
    return socket_ip

eel.init(os.path.join(sys.path[0], "web"))


app_running = False

@eel.expose  # Expose this function to Javascript
def startApp():
    global app_running
    app_running = True
    print("start App")

@eel.expose
def say_hello_py(x):
    print("Hello from", x)

sensors = []


def close_callback(page, openSocks):
    print("Window "+page+" closed")
    for sock in openSocks:
        print("remaining socket: ", sock)
    
def update_sensors():
    global sensors
    url = "http://192.168.55.220/addons/red/sensors"
    response  = requests.get( url=url)
    sensors.clear()
    data = json.loads(response.content)
    for sensor in data:
        if sensor.startswith("T_"):
            name = sensor.split("_")
            data[sensor]["name"]= name[-1:][0]
            sensors.append(data[sensor])
    
    
    for sensor in sensors:
        name = sensor.get("name", "unnamed")
        temperature = round(sensor.get("temperature", 100),1)
        humidity = round(sensor.get("humidity", 0),0)
        battery = sensor.get("battery", 100)
        timeout = False
        eel.update_values(name, temperature, humidity, battery, timeout)

def run_eel():
    print("starting eel ...")
    eel.start(
        "index.html", 
        host=get_ip_address(),
        mode="None",
        shutdown_delay = 1000000,
        close_callback=close_callback,
        port=8080, 
    )
    
    
def update_time():
    while True:
        timestring = str(datetime.now())[:-7]
        eel.updateTime(timestring)
        time.sleep(1)
        
        
def main():
    
            
    eel_worker = threading.Thread(None, run_eel).start()
    time_updater = threading.Thread(None, update_time, daemon=True).start()
    
    while True:
        try:
            time.sleep(5)
            update_sensors()
        except:
            break
            
    


if __name__ == "__main__":
    main()