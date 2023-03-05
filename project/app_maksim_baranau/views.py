from django.shortcuts import render
from django.views import generic
from .city import ZoneForm
from .city import ZoneFormUSA


from django.http import HttpResponse
from django.http import HttpRequest
#from .models import selectzone
import pytz
import datetime


def index(request):
    return render(request, "index.html")

def whattimehere(request: HttpRequest) -> HttpResponse:
    return render(request, "timezone.html")

def aff(request):
    result = datetime.datetime.now()
    context = {}
    form = ZoneForm()
    context['form'] = form
    if request.POST:
        temp = request.POST['region']
        tz_city = pytz.timezone(temp)
        result = datetime.time.now(tz_city)
    return render(request, "formtimezone.html", {"result": result})

def TimeView_EUR(request: HttpRequest) -> HttpResponse:
    form = ZoneForm()
    context = {}
    context['form'] = form
    time_now = datetime.datetime.now()
    context['time_now'] = time_now.strftime("%H:%M:%S")
    if request.GET:
        temp = request.GET['region']
        tz_city = pytz.timezone(temp)
        context['tz_city'] = tz_city
        res = datetime.datetime.now(tz_city)
        result = res.strftime("%H:%M:%S")
        context['result'] = result
        raznica = time_now.hour - res.hour
        context['raznica'] = raznica
    return render(request, "formtimezone.html", context)

def TimeView_US(request: HttpRequest) -> HttpResponse:
    form = ZoneFormUSA()
    context = {}
    context['form'] = form
    time_now = datetime.datetime.now()
    context['time_now'] = time_now.strftime("%H:%M:%S")
    if request.GET:
        temp = request.GET['region_US']
        tz_city = pytz.timezone(temp)
        context['tz_city'] = tz_city
        res = datetime.datetime.now(tz_city)
        result = res.strftime("%H:%M:%S")
        context['result'] = result
        raznica = time_now.hour - res.hour
        context['raznica'] = raznica
    return render(request, "formtimezone.html", context)

def pomodoro(request: HttpRequest) -> HttpResponse:
    return render(request, "pomodoro.html")












