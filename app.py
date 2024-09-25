from flask import Flask, render_template, request
import json
import urllib.request

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'London'

    source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key).read()

    data=json.loads(source)
    print(data)
    weather_data = {"country_code": data['sys']['country'], "coordinate": data['coord']['lon'], "coordinate": data['coord']['lat'], "temp": data['main']['temp'], "pressure": data['main']['pressure'], "humidity": data['main']['humidity'], "weather": data['weather'][0]['description'], "icon": data['weather'][0]['icon']}
    return render_template('index.html', data=weather_data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
