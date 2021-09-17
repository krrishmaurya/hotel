
from django.shortcuts import redirect, render
from django.views import View
from . import forms
from . import models

class Add_booking(View):
    def get(self,request):
        content={
            'page_tittle':'Add Booking',
            'booking_form':forms.Booking_form()
        }
        return render(request,'booking_form.html',content)    

    def post(self,request):
        customer_name=request.POST['customer_name']
        customer_age=request.POST['customer_age']
        contact_no=request.POST['contact_no']
        email=request.POST['email']
        booking_date=request.POST['booking_date']
        added_bookings=models.Booking(
            customer_name=customer_name,
            customer_age=customer_age,
            contact_no=contact_no,
            email=email,
            booking_date=booking_date
        )
        added_bookings.save()
        return redirect('/')


class Detail(View):
    def get(self,request):
        client_id=request.GET['client_id']
        print(client_id)
        content={
            'page_tittle':'Details',
            'added':models.Booking.objects.get(id=client_id)
        }
        return render(request,'client_details.html',content)