import requests
import json
import unittest

class Forecast():

    def __init__(self, key, units, latitude, longitude, time = None):
        self.key = key
        self.units = units
        self.lat = latitude
        self.lon = longitude
        self.timestamp = time

        if time:
            self.url = 'https://api.forecast.io/forecast/{key}/{latitude},{longitude},{time}?{units}'.format(key=key,latitude=latitude,longitude=longitude,time=time,units=units)
        else:
            self.url = 'https://api.forecast.io/forecast/{key}/{latitude},{longitude}?{units}'.format(key=key,latitude=latitude,longitude=longitude,time=time,units=units)

    def get_forecast(self):
        try:
            r = requests.get(self.url)
        except:
            return False
        else:
            if int(r.status_code) != 200:
                print
                return False
            else:
                self.forecast = json.loads(r.content)
                self.current = self.forecast['currently']
                self.daily = self.forecast['daily']
                self.daily_data = self.daily['data']
        return True

# MAIN
if __name__ == "__main__":
    unittest.main()