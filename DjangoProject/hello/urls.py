import django
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path("<str:name>", views.greet, name="greet"),
    path("brain", views.brain, name='brain'),
    path("david", views.david, name="david")
]


# from . : from the current directory:view.py 和 urls.py 在同一个文件夹hello 下
# which will be a list of all of the allowable URLs that can be accessed for this
# particular app.
# and the way we create a URL is by first importing form django.urls import path
# first argument : empty string; no additional argument
# meaning nothing at the end of the route.
# second argument is what view should be rendered  when this URL is visited.
# import index from view
