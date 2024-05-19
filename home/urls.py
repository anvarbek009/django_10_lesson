from django.urls import path
from .views import home_page, Analaze

app_name = 'home'
urlpatterns = [
    path('',home_page, name='home_page'),
    path('analaze/', Analaze.as_view(), name='analaze'),
]