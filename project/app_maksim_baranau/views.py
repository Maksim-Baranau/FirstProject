from django.shortcuts import render, redirect
from django.views import generic
from .city import ZoneForm
from .city import ZoneFormUSA


from django.http import HttpResponse
from django.http import HttpRequest
import pytz
import datetime
import time
from .models import ycity
from django import forms
from .bob import usecases
from .scheme.ycity import ycitySchema


def index(request):
    return render(request, "index.html")

def whattimehere(request: HttpRequest) -> HttpResponse:
    return render(request, "timezone.html")

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
    context = {}
    remember = str("Тут появится ваш текст")
    context['remember'] = remember
    current_date_time = datetime.datetime.now()
    time_now = current_date_time.time()
    context["time_now"] = time_now
    if request.POST:
        remember = str(request.POST["rem"])
        when = float(request.POST["when"])
        result = when
        context['result'] = result
        time.sleep(when)
        context['remember'] = remember
    return render(request, "pomodoro.html", context)

class ycityForm(forms.Form):
    model = ycity
    name = forms.CharField(label="Имя:")
    about = forms.CharField(label="Фамилия:")
    age = forms.IntegerField(label="Возраст:")
    img = forms.ImageField(label='Photo')


class ycityView(generic.FormView):
    form_class = ycityForm
    success_url = "/ycity/"
    template_name = "ycity.html"

    def get_context_data(self, **kwargs: dict) -> dict:
        ctx = super().get_context_data(**kwargs)

        get_all_city = usecases.GetAllycityUseCase()
        ctx["object_list"] = get_all_city()

        return ctx

    def form_valid(self, form: forms.Form) -> HttpResponse:
        ycity = ycitySchema.parse_obj(form.cleaned_data)

        save_city = usecases.SaveycityUseCase(ycity)
        save_city()

        return super().form_valid(form)

class ycitycreateCreateView(generic.CreateView):
    model = ycity
    fields = "__all__"
    success_url = "/ycity/"
    template_name = "ycity_form.html"

class ycityDetail(generic.DetailView):
    model = ycity
    template_name = "ycity_detail.html"

class ycityUpdate(generic.UpdateView):
    template_name = "ycity_update.html"
    fields = ["name", "about", "age"]
    model = ycity

    def get_success_url(self) -> str:
        return f"/ycity/{self.object.pk}/"

class ycityDel(generic.DeleteView):
    model = ycity
    template_name = "ycity_del.html"
    success_url = "/ycity/"


def upload_image_view(request):
    if request.method == 'POST':
        form = ycity(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ycityForm()
    return render(request, 'ycity_detail.html', {'form': form})
