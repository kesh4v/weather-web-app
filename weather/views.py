from django.shortcuts import render, redirect
import json
import urllib.request
from weather.models import TempHistory
from django.utils import timezone

# Create your views here.
def index(request):
    city = None
    data = None
    history = None

    if request.method == 'POST':
        city = request.POST['city']
        try:
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' +
                str(json_data['coord']['lat']),
                "temp": str(round(json_data['main']['temp']-273.15, 2)),
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }

            history = TempHistory.objects.filter(city__iexact=city, coordinate=str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat'])).order_by("-id")[1:]

            if not TempHistory.objects.filter(city__iexact=city, date__date=timezone.now(), temperature=round(json_data['main']['temp']-273.15, 2), pressure=json_data['main']['pressure'], humidity=json_data['main']['humidity']):
                temp = TempHistory()
                temp.city = city
                temp.coordinate = str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat'])
                temp.temperature = round(json_data['main']['temp']-273.15, 2)
                temp.pressure = json_data['main']['pressure']
                temp.humidity = json_data['main']['humidity']
                temp.save()
        except:
            return redirect("index")

    else:
        city = ''
        data = {}

    return render(request, 'index.html', {'city': city, 'data': data, 'historys': history})