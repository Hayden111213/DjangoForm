from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('end.html', views.end, name='end')
]