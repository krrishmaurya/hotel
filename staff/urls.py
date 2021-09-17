from django.urls import path
from client.views import Add_booking,Detail
from . import views

urlpatterns=[
    path('',views.Home.as_view(),name='home'),
    path('booking',Add_booking.as_view(),name='add'),
    path('client_details/',Detail.as_view(),name='details'),
    path('login',views.Login.as_view(),name='login'),
    path('logout',views.Logout.as_view(),name='logout')
]