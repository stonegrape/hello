from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("weekday", views.weekday, name="weekday"),
    path("ctime", views.ctime, name="ctime")
]
