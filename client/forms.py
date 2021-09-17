from django import forms

class Booking_form(forms.Form):
    customer_name=forms.CharField(max_length=20)
    customer_age=forms.IntegerField()
    contact_no=forms.CharField(max_length=12)
    email=forms.EmailField()
    booking_date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
