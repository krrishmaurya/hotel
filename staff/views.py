

from django.shortcuts import render ,redirect
from client.models import Booking
from  django.views  import View
from django.contrib.auth.models import auth
from . import forms

class Home (View):
    def get(self,request):
        content={
            'page_tittle':'Home',
            'bookings':Booking.objects.all()
        }
        return render(request,'index.html',content)

class Login(View):
    def get(self,request):
        content={
            'page_tittle':'Login Here',
            'login_form':forms.Login_form()
        }
        return render(request,'login.html',content)
    
    def post(self,request):
        user_name=request.POST['user_name']
        password=request.POST['password']
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
        return redirect('/')


class  Logout(View):
    def get(self,request):
        auth.logout(request)
        return redirect('/')        
