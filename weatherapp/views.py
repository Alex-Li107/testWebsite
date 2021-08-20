from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == "POST":
        cityCode = request.POST["cityCode"]
        result = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + cityCode + "&appid=29614eb5a95803ddc52b19e778214b82&units=metric").read()
        jsonData = json.loads(result)
        weatherData = {
            "country": str(jsonData['sys']['country']),
            "currentTemp": str(jsonData["main"]["feels_like"]),
            #"feels": str(jsonData["main"]["temp"]),
            "tempH": str(jsonData['main']['temp_max']),
            "tempL": str(jsonData['main']['temp_min']),
            "weather": str(jsonData['weather'][0]["main"]),
            "city": str(jsonData["name"])
        }
    else: 
        weatherData = {}
    return render(request, 'index.html', weatherData)
