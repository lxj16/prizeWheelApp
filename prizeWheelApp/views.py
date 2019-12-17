from django.shortcuts import render

# Create your views here.


def start(request):
    return render(request, 'prizeWheelApp/start.html')


def index(request):
    return render(request, 'prizeWheelApp/index.html')


def noPrize(request):
    return render(request, 'prizeWheelApp/noPrize.html')


def participated(request):
    return render(request, 'prizeWheelApp/participated.html')


def prize(request):
    return render(request, 'prizeWheelApp/prize.html')


def turnTable(request):
    return render(request, 'prizeWheelApp/prize.html')
