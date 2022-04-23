from django.urls import path
from django.views.generic import TemplateView
from .views import *
urlpatterns = [
    path('<int:id>/',bookTripBus, name='book trip'),
    path('pay/<int:id>/', payBus, name="paybus"),
    path('mytrips/', mytripBus, name="mytrip-bus"),
    path('incomplete-bus/', incompleteBus, name="incomplete-bus"),
    path('ticket/<int:id>/', busticket, name="busticket"),
    path('invoice/<int:id>/', businvoice, name="busticket"),
    path('log-out/', logOut, name="log-out"),
    path('login/', userLogin, name="user-login"),
    path('registration/', userRegistration, name='user-registration'),
    path('charts/', charts, name='charts'),


]