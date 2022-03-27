from django.urls import path
from pages.views import *

app_name='pages'

urlpatterns = [
    path('', Main.as_view(), name='main')
]
