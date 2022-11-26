from django.shortcuts import render, get_object_or_404
from django.http.request import HttpRequest
from .models import Measurement
from .forms import MeasurementModelForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo
import folium
# Create your views here.


def calculate_distance_view(request: HttpRequest):
    obj = get_object_or_404(Measurement, id=7)
    print(obj.id)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Nominatim(user_agent="measurements")

    ip = '87.237.232.87'  # Enter your IP address here
    country, city, lat, lon = get_geo(ip)
    print(city['city'])
    location = geolocator.geocode(city)

    # location coordinates
    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)

    # inital folium map
    m = folium.Map(width=800, height=500, location=pointA)

    # location marker
    # folium.Marker(
    #     [l_lat, l_lon], tooltip='click here for more', popup=city['city'],
    #     icon=folium.Icon(color='purple').add_to(m)
    # )

    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)

        # destination coordinates
        d_lat = destination.latitude
        d_long = destination.longitude

        pointB = (d_lat, d_long)

        # distance calculation
        distance = round(geodesic(pointA, pointB).km, 2)

        # folium map modification

        instance.location = location
        instance.distance = distance
        instance.save()

    m = m._repr_html_()

    context = {
        'distance': obj,
        'form': form,
        'map': m,
    }

    return render(request=request, template_name='measurements/main.html', context=context)