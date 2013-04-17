from flask import Flask
from forecastio.forecast import Forecast

# configuration
WEATHER_CONF='general.conf'

app = Flask(__name__)
app.config.from_envvar('WEATHER_CONF', silent=True)

@app.route('/')
def index():
    #lat long from easton - should be loaded from db (i guess?)
    forecast = Forecast(key='5730376531f05188e85f80cf342ec8f5',units='us',latitude=40.049820,longitude=-82.91367)
    if forecast.get_forecast():
        return 'The value of forecast {!r}.'.format(forecast.current)
    else:
        print 'FORECAST FAILED BRO'
        return 'womp womp'


if __name__ == '__main__':
    app.run()
