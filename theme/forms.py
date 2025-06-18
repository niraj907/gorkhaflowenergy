# forms.py
from django import forms
from .models import ContactMessage
from django_recaptcha.fields import ReCaptchaField
from phonenumber_field.formfields import PhoneNumberField
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.utils import timezone
# from .models import Schedule

class ContactForm(forms.ModelForm):
    contact_Number=PhoneNumberField(
                region='NP',        
                
)
    

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message','contact_Number']
        # widgets = {
        #     'contact_Number' : PhoneNumberPrefixWidget(initial='NP', )}
        error_messages = {
            'name': {
                'required': "Please enter your name."
            },
            'email': {
                'required': "Please enter your email address.",
                'invalid': "Please enter a valid email address."
            },
            'message': {
                'required': "Please enter your message."
            },
            'contact_Number': {
                'required': "Please enter your phone number.",
                'invalid': "Please enter a valid phone number."
            }
            
        }
        
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox,
        error_messages={'required': 'Please complete the captcha.'})
    
# class ScheduleForm(forms.ModelForm):
#     start_time=forms.TimeField(
#         widget=forms.TimeInput(attrs={
#             'type': 'time'
#             })
#     )  
#     end_time=forms.TimeField(
#         widget=forms.TimeInput(attrs={
#             'type': 'time',
#             })
#     ) 
#     class Meta:
#         model = Schedule
#         fields = ['Name', 'locationName', 'date', 'start_time', 'end_time', 'location']
#         widgets = {
#             'Name': forms.TextInput(attrs={'placeholder': 'Enter Event Name'}),
#             'locationName': forms.TextInput(attrs={'placeholder': 'Enter Location Name'}),
#             'location': forms.TextInput(attrs={'placeholder': 'Enter Google Location Code'}),
#             'date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()})
#         }
    