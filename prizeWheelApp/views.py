from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Prize
from .forms import PhoneInput
from django.views.generic import View
from .models import User, Prize, Winner
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
        if User.objects.get(phoneNumber=phoneNumber):
            if User.objects.get(phoneNumber=phoneNumber).rolled == True:
                return redirect('participated')
            else:
                User.objects.filter(phoneNumber=phoneNumber).update(rolled=True)
                prize = Prize.objects.all()
                context = {'phoneNumber': phoneNumber, 'prize': prize}



                return render(request, 'prizeWheelApp/turntable.html', context)


def noPrize(request):
    return render(request, 'prizeWheelApp/noPrize.html')


def participated(request):
    return render(request, 'prizeWheelApp/participated.html')


class PrizeView(View):

    def get(self,request, prizeID):
        prize = Prize.objects.get(pk=prizeID)
        phoneNumber = request.session['phoneNumber']
        user = User.objects.get(phoneNumber=phoneNumber)

        quantityBefore = prize.quantity

        Prize.objects.filter(pk=prizeID).update(quantity= quantityBefore -1)
        winner = Winner(prizeID=prize,userID=user)
        winner.save()

        context = {'prize': prize, 'phoneNumber': phoneNumber}
        return render(request, 'prizeWheelApp/prize.html', context)

def check_prize(request, prizeID):
        prize = Prize.objects.get(pk=prizeID)
        quantity = {'quantity': prize.quantity}

        return JsonResponse(quantity)
        



