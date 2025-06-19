from email.message import EmailMessage
from smtplib import SMTPException
from django.conf import settings
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from theme.forms import ContactForm
from theme.models import *
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'hero.html')

def documents_view(request):
    documents = Document.objects.all()
    return render(request, 'document.html', {'documents': documents})

def view(request):
    return render(request, 'view.html')

# def news(request):
#     return render(request, 'news.html')

def news(request):
    news_list = NewsItem.objects.order_by('-published_date')
    return render(request, 'news.html', {'news_list': news_list})

def news_detail(request, id):
    news_item = get_object_or_404(NewsItem, id=id)
    return render(request, 'readmore.html', {'news_item': news_item})


def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def contact(request):
    if request.method == 'POST':
        # Create a mutable copy of POST data so we can modify it
        post_data = request.POST.copy()
        country_code = post_data.get('country_code', '').strip()
        contact_number = post_data.get('contact_Number', '').strip()
        # Combine the country code and contact number
        full_contact_number = f"{country_code}{contact_number}" if country_code and contact_number else contact_number
        # Update the POST data so the form receives the combined phone number
        post_data['contact_Number'] = full_contact_number

        # Initialize the form with the modified POST data
        contactform = ContactForm(post_data)

        # Honeypot check (case insensitive)
        if post_data.get('Subject', ''):
            return JsonResponse({'success': False, 'errors': {'bot': ['Form submission rejected.']}}, status=400)

        # Custom field validation
        name = post_data.get('name', '').strip()
        email = post_data.get('email', '').strip()
        message = post_data.get('message', '').strip()

        custom_errors = {}
        if not name:
            custom_errors['name'] = ['Name is required.']
        if not full_contact_number:
            custom_errors['contact_Number'] = ['Contact number is required.']
        if not email:
            custom_errors['email'] = ['Email is required.']
        elif '@' not in email or '.' not in email:  # Basic email validation
            custom_errors['email'] = ['Enter a valid email address.']
        if not message:
            custom_errors['message'] = ['Message is required.']

        if custom_errors:
            return JsonResponse({'success': False, 'errors': custom_errors}, status=400)

        # Validate the form with the updated data
        if contactform.is_valid():
            try:
                name = contactform.cleaned_data['name']
                message_phone_number = contactform.cleaned_data['contact_Number']
                message_email = contactform.cleaned_data['email']
                message_message = contactform.cleaned_data['message']

                # Prepare the email body using a template
                email_body = render_to_string('emails/sendContact.html', {
                    'name': name,
                    'message_phone_number': message_phone_number,
                    'message_email': message_email,
                    'message_message': message_message,
                })

                email_msg = EmailMultiAlternatives(
                subject='Contact Us Message from Gorkha-Hills website',
                body='This is a fallback plain text version.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['gamejoker388@gmail.com'],
            )
                email_msg.attach_alternative(email_body, "text/html")
                email_msg.send()

                # Save the form data to the database
                contactform.save()
                return JsonResponse({'success': True})
            except SMTPException as e:
                print(f"SMTPException: {e}")
                return JsonResponse({'success': False, 'errors': ['Email sending failed. Please try again later.']}, status=500)
            except Exception as e:
                print(f"Exception here: {e}")
                return JsonResponse({'success': False, 'errors': ['An unexpected error occurred.']}, status=500)
        else:
            
            print(contactform.errors)
            # Return form errors if validation fails
            return JsonResponse({'success': False, 'errors': contactform.errors}, status=400)
    else:
        contactform = ContactForm()
        return render(request, 'contact.html', {'contactform': contactform})

