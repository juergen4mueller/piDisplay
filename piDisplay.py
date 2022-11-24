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


class WebData():
    def __init__(self) -> None:
        self._active_page = ""
        self.weatherData = []
        self.homeSensors = []
        self.holfuyData = None
        self.energySystem = {}
        self.init()
        
    def init(self):
        self.read_home_sensors()
        self.read_weather_data()
        self.read_holfuy_data()
        
        
    def set_page(self, page):
        self._active_page = page
    
    def send_home_sensors_to_js(self):
        for sensor in self.homeSensors:
            name = sensor.get("name", "unnamed")
            temperature = round(sensor.get("temperature", 100),1)
            humidity = round(sensor.get("humidity", 0),0)
            battery = sensor.get("battery", 100)
            timeout = False
            eel.update_home_sensors(
                name, 
                temperature, 
                humidity, 
                battery, 
                timeout)
        
    
    def send_weather_data_to_js(self):
        for i, day in enumerate(self.weatherData):
            time = day.get("time")
            temperature_2m_min = day.get("temperature_2m_min")
            temperature_2m_max = day.get("temperature_2m_max")
            sunrise = day.get("sunrise")
            sunset = day.get("sunset")
            rain_sum = day.get("rain_sum")
            windspeed_10m_max = day.get("windspeed_10m_max")
            windgusts_10m_max = day.get("windgusts_10m_max")
            windgusts_10m_max = day.get("windgusts_10m_max")
            winddirection_10m_dominant = day.get("winddirection_10m_dominant")
            shortwave_radiation_sum = day.get("shortwave_radiation_sum")
            eel.update_weather_data(
                i,
                time, temperature_2m_min, 
                temperature_2m_max, 
                sunrise, 
                sunset, 
                rain_sum, 
                windspeed_10m_max, 
                windgusts_10m_max, 
                winddirection_10m_dominant, 
                shortwave_radiation_sum)
    
    
    def send_holfuy_data_to_js(self):
        for holfuy in self.holfuyData:
            name,_,_ = holfuy.get("stationName").partition(" ")
            updateTime = holfuy.get("dateTime")
            wind = holfuy.get("wind")
            wSpeed = wind.get("speed")
            wGust = wind.get("gust")
            wMin = wind.get("min")
            wUnit = wind.get("unit")
            wDirection = wind.get("direction")
            pressure = holfuy.get("pressure")
            temperature = holfuy.get("temperature")
            eel.update_holfuy_data(
                name,
                updateTime,
                wSpeed,
                wGust,
                wMin,
                wUnit,
                wDirection,
                pressure,
                temperature
            )
    
    def send_data_to_js(self):
        if self._active_page == "index":
            print("send home sensor data")
            self.send_home_sensors_to_js()
        elif self._active_page == "flugwetter":
            print("send holfuy data")
            #self.send_weather_data_to_js()
            self.send_holfuy_data_to_js()
            
            
    def read_holfuy_data(self):
        pwd = "2N8aox0vMzpZS51"
        stations = "400,407,1561"
        url = "http://api.holfuy.com/live/?s="+stations+"&pw="+pwd+"&m=JSON&tu=C&su=km/h"    
        response = requests.get(url)    
        self.holfuyData = json.loads(response.content).get("measurements") #list mit 3 Stationen die Angefragt wurden
    
    def read_home_sensors(self):
        url = "http://192.168.55.220/addons/red/sensors"
        response  = requests.get(url)
        self.homeSensors.clear()
        data = json.loads(response.content)
        for sensor in data:
            if sensor.startswith("T_"):
                name = sensor.split("_")
                data[sensor]["name"]= name[-1:][0]
                self.homeSensors.append(data[sensor])
    
    def read_weather_data(self):
        url="https://api.open-meteo.com/v1/forecast?latitude=48.97&longitude=11.06&models=icon_mix&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,rain_sum,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant,shortwave_radiation_sum&current_weather=true&timezone=Europe%2FBerlin"
        r = requests.get(url)    
        dataWeather = json.loads(r.content)
        units = dataWeather.get("daily_units")
        daily = dataWeather.get("daily")
        weather_per_day = []
        weather_per_day.clear()
        day_info = {}
        day_info.clear()
        units = dataWeather.get("daily_units")
        daily = dataWeather.get("daily")
        _time = daily.get("time")
        _temperature_2m_min = daily.get("temperature_2m_min")
        _temperature_2m_max = daily.get("temperature_2m_max")
        _sunrise = daily.get("sunrise")
        _sunset = daily.get("sunset")
        _rain_sum = daily.get("rain_sum")
        _windspeed_10m_max = daily.get("windspeed_10m_max")
        _windgusts_10m_max = daily.get("windgusts_10m_max")
        _winddirection_10m_dominant = daily.get("winddirection_10m_dominant")
        _shortwave_radiation_sum = daily.get("shortwave_radiation_sum")
        self.weatherData.clear()
        for i, t in enumerate(_time):
            day_info["time"] = t[-2:] +"."+t[-5:-3]+"."
            day_info["temperature_2m_min"] = str(_temperature_2m_min[i] ) + " " +units.get("temperature_2m_min")
            day_info["temperature_2m_max"] = str(_temperature_2m_max[i] ) + " " +units.get("temperature_2m_max")
            day_info["sunset"] = str(_sunset[i] )
            day_info["sunrise"] = str(_sunrise[i] )
            day_info["rain_sum"] = str(_rain_sum[i] ) + " " +units.get("rain_sum")
            day_info["windspeed_10m_max"] = str(_windspeed_10m_max[i] ) + " " +units.get("windspeed_10m_max")
            day_info["windgusts_10m_max"] = str(_windgusts_10m_max[i] ) + " " +units.get("windgusts_10m_max")
            day_info["winddirection_10m_dominant"] = str(_winddirection_10m_dominant[i] ) + " " +units.get("winddirection_10m_dominant")
            day_info["shortwave_radiation_sum"] = str(_shortwave_radiation_sum[i] ) + " " +units.get("shortwave_radiation_sum")
            self.weatherData.append(day_info)
            
            
webData = WebData()

        
        
        
@eel.expose
def request_data(page):
    print("Seite: ", page)
    webData.set_page(page)
    webData.send_data_to_js()
    

def close_callback(page, openSocks):
    pass
    #print("Window "+page+" closed")
    #for sock in openSocks:
    #    print("remaining socket: ", sock)
    

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
    update_counter = 0
    while True:
        try:
            time.sleep(1)
            update_counter +=1
            if (update_counter % 5) == 0:
                #alle 5s
                webData.read_home_sensors()
                webData.send_data_to_js()
                
            if (update_counter % 60) == 0:
                webData.read_holfuy_data()
                
            if (update_counter % 3600) == 0:
                #alle 1h
                webData.read_weather_data()
        except:
            break
            
    


if __name__ == "__main__":
    main()