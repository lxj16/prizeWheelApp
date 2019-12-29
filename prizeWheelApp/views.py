from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Prize
from .forms import PhoneInput
from django.views.generic import View
from .models import User, Prize, Winner

import random
# Create your views here.


def start(request):
    Prize_list = list(Prize.objects.all())
    context = {'prizes': Prize_list}
    return render(request, 'prizeWheelApp/start.html', context)


class Index(View):

    def get(self, request):
        phoneInput = PhoneInput()
        context = {'form': phoneInput}
        return render(request, 'prizeWheelApp/index.html', context)

    def post(self, request):
        if request.method == 'POST':
            form = PhoneInput(request.POST)

            if form.is_valid():
                phoneNumber = form.cleaned_data['phone']
                # phoneNumber = request.POST.get['phone']
                print(phoneNumber)

                if User.objects.filter(phoneNumber=phoneNumber).exists():
                    return redirect('participated')
                else:
                    newUser = User(phoneNumber=phoneNumber)
                    newUser.save()
                    request.session['phoneNumber'] = phoneNumber

                    return redirect('turnTable', phoneNumber=phoneNumber)

        return redirect('index')


class TurnTable(View):

    def get(self, request, phoneNumber):
        try:
            phoneNumber = request.session['phoneNumber']

            if User.objects.get(phoneNumber=phoneNumber):
                if User.objects.get(phoneNumber=phoneNumber).rolled == True:
                    return redirect('participated')
                else:
                    User.objects.filter(
                        phoneNumber=phoneNumber).update(rolled=True)
                    prize = Prize.objects.all()
                    context = {'phoneNumber': phoneNumber, 'prize': prize}

                    return render(request, 'prizeWheelApp/turntable.html', context)
        except:
            return redirect('participated')


def noPrize(request):
    try:
        phoneNumber = request.session['phoneNumber']
        clearSession(request)

        return render(request, 'prizeWheelApp/noPrize.html')
    except:
        return redirect('participated')


def participated(request):
    clearSession(request)
    return render(request, 'prizeWheelApp/participated.html')


class PrizeView(View):

    def get(self, request, prizeID):
        try:

            prize = Prize.objects.get(pk=prizeID)
            phoneNumber = request.session['phoneNumber']
            user = User.objects.get(phoneNumber=phoneNumber)

            quantityBefore = prize.quantity

            Prize.objects.filter(pk=prizeID).update(
                quantity=quantityBefore - 1)
            winner = Winner(prize=prize, user=user, phoneNumber=phoneNumber)
            winner.save()

            clearSession(request)

            context = {'prize': prize, 'phoneNumber': phoneNumber}
            return render(request, 'prizeWheelApp/prize.html', context)
        except:
            return redirect('index')


def getResult(request):

    result = random.random()

    if result > 0.05 and result < 0.08:
        prizeID = 2
    elif (result > 0.25 and result < 0.28):
        prizeID = 2
    elif (result > 0.15 and result < 0.18):
        prizeID = 2
    elif (result > 0.35 and result < 0.38):
        prizeID = 4
    elif (result > 0.55 and result < 0.57):
        prizeID = 5
    elif (result > 0.65 and result < 0.66):
        prizeID = 6
    else:
        prizeID = 2

    prize = Prize.objects.get(pk=prizeID)

    if prize.quantity <= 0:
        prizeID = 7
    print(prizeID)
    prizeID = {'prizeID': prizeID}
    request.session['rolled'] = True
    request.session.save()
    return JsonResponse(prizeID)


def clearSession(request):
    for key in list(request.session.keys()):
        del request.session[key]
