from django import forms

class Booking_form(forms.Form):
    customer_name=forms.CharField(max_length=20,required=False)
    customer_age=forms.IntegerField(required=False)
    contact_no=forms.CharField(max_length=12,required=False)
    email=forms.EmailField(required=False)
    booking_date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),required=False)
