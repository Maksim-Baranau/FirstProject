from django.contrib import admin
from django.urls import path
from app_maksim_baranau import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('time/', views.whattimehere, name='time'),
    path('time/EUR/', views.TimeView_EUR, name='timeform_EUR'),
    path('time/US/', views.TimeView_US, name='timeform_US'),
    path('pomodoro/', views.pomodoro, name='pomodoro'),
]
