import requests

from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy


#Creating your home route

app = Flask(__name__)
app.config['DEBUG'] = True


#Forms an endpoint to (HOME) and calls the index function that implents everything and returns it via the html file
@app.route('/')
def index():

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=6373d366847603ddf8bcc2cafb87ce81'
    city = 'Toronto'

    r = requests.get(url.format(city)).json()

    weather = {
        'city': city,
        'temprature' :  r['main']['temp'],
        'description':  r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
         }

    print(weather)

    return render_template('weather.html',weather=weather)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')