from django.shortcuts import render
import datetime
# Create your views here.


def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {"newyear": now.month == 1 and now.day == 1})
    # return render(request, "newyear/index.html", {"newyear": True})


def weekday(request):
    now = datetime.datetime.now()
    if now.isoweekday() == 1:
        weekday = "Monday"
    elif now.isoweekday() == 2:
        weekday = "Tuesday"
    elif now.isoweekday() == 3:
        weekday = "Wednesday"
    elif now.isoweekday() == 4:
        weekday = "Thursday"
    elif now.isoweekday() == 5:
        weekday = "Friday"
    elif now.isoweekday() == 6:
        weekday = "Saturday"
    else:
        weekday = "Sunday"
    return render(request, "day/weekday.html", {"weekday": weekday})


def ctime(request):
    now = datetime.datetime.now()
    ctime = now.ctime()
    return render(request, "day/ctime.html", {"ctime": ctime})
