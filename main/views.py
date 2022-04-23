from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@login_required(login_url='/main/login/')
def bookTripBus(request, id):
    if request.method == "POST":
        tripid = request.POST['id']
        date = request.POST['date']
        adult = request.POST['adult']
        child = request.POST['child']
        # baby = request.POST['baby']
        if date and adult and child :
            adult = int(adult)
            # baby = int(baby)
            child = int(child)
            if not adult == 0:
                trip = BusChart.objects.get(id=tripid)
                adultcost = trip.adultcost
                childcost = trip.childcost
                total = (adult * adultcost) + (child * childcost)
                user = User.objects.get(id=request.user.id)
                bustrip = BusTrip.objects.create(user=user, bus=trip, adult=adult, child=child, departureDate=date, totalcost=total, payment="Incomplete")
                context = {
                    'bus': bustrip,
                    'trip': trip,
                    'user': user,
                    'tripby': "Bus"
                }
                return render(request, 'main/checkout.html', context)
            else:
                context = {
                    'error': "Trip can't be booked without any Adult Member!"
                }
                return render(request, 'main/error.html', context)
        else:
            context = {
                'error': "Please fill up all the fields (Date, Adult, Child) and try again!"
            }
            return render(request, 'main/error.html', context)
    trip = BusChart.objects.get(id=id)
    context = {
        'trip': trip,
        'tripby': "Bus",
    }
    return render(request, 'main/tripform.html', context)

@login_required(login_url='/main/login/')
def payBus(request, id):
    context = {
        'id': id,
    }
    if request.method == "POST":
        id = request.POST['id']
        bustrip = BusTrip.objects.get(id=id)
        bustrip.payment = "Complete"
        bustrip.save()
        return redirect(mytripBus)
    return render(request, 'main/pay.html', context)

@login_required(login_url='/main/login/')
def mytripBus(request, *args, **kwargs):
    uid = request.user.id
    user = User.objects.get(id=uid)
    trip = BusTrip.objects.filter(user=user).order_by('departureDate')

    context = {
        'trip': trip,
        'tripby': "Bus"
    }

    return render(request, 'main/mytrip.html', context)

login_required(login_url='/main/login/')
def incompleteBus(request, *args, **kwargs):
    uid = request.user.id
    user = User.objects.get(id=uid)
    trip = BusTrip.objects.filter(payment="Incomplete", user=user).order_by('departureDate')

    context = {
        'trip': trip,
        'tripby': "Bus"
    }

    return render(request, 'main/incompletepay.html', context)

@login_required(login_url='/main/login/')
def busticket(request, id):
    uid = request.user.id
    user = User.objects.get(id=uid)
    bustrip = BusTrip.objects.get(id=id)
    context = {
            'bus': bustrip,
            'trip': bustrip.bus,
            'user': user,
            'tripby': "Bus"
        }
    return render(request, 'main/ticket.html', context)

@login_required(login_url='/main/login/')
def businvoice(request, id):
    uid = request.user.id
    user = User.objects.get(id=uid)
    bustrip = BusTrip.objects.get(id=id)
    context = {
            'bus': bustrip,
            'trip': bustrip.bus,
            'user': user,
            'tripby': "Bus"
        }
    return render(request, 'main/invoice.html', context)

@login_required(login_url='/main/login/')
def logOut(request, *args, **kwargs):
    logout(request)
    return redirect(userLogin)

def userLogin(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'main/login.html')

def userRegistration(request, *args, **kwargs):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if first_name and last_name and username and email and password:
            user = User.objects.create_user(email=email, username=username, first_name=first_name, last_name=last_name, password=password)

            if user:
                login(request, user)
                return redirect("/")
            else:
                context = {
                    'error': "Username is already taken, please choose another username and try again!"
                }
                return render(request, 'main/error.html', context)
        else:
            context = {
                'error': "Please fill up all the fields and try again!"
            }
            return render(request, 'main/error.html', context)
    return render(request, 'main/registration.html')

@login_required(login_url='/main/login/')
def charts(request, *args, **kwargs):
    buschart = BusChart.objects.all()
    context = {
        'buschart': buschart,
    }
    return render(request, 'main/charts.html', context)