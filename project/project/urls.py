from django.contrib import admin
from django.urls import path
from app_maksim_baranau import views
from app_maksim_baranau import wiki
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('time/', views.whattimehere, name='time'),
    path('time/EUR/', views.TimeView_EUR, name='timeform_EUR'),
    path('time/US/', views.TimeView_US, name='timeform_US'),
    path('pomodoro/', views.pomodoro, name='pomodoro'),
    path('ycity/', views.ycityView.as_view(), name='ycity'),
    path('ycity/create/', views.ycitycreateCreateView.as_view(), name='ycitycreate'),
    path("ycity/<int:pk>/", views.ycityDetail.as_view()),
    path("ycity/<int:pk>/update/", views.ycityUpdate.as_view()),
    path("ycity/<int:pk>/del/", views.ycityDel.as_view()),
    path('image_upload/', views.upload_image_view, name ='image_upload'),
    path('wiki/',wiki.wikiped),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)