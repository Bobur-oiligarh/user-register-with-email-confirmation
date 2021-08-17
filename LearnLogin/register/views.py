from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.views import View

from . import forms
from .forms import UserRegisterForm, LoginForm, ContactForm
from .models import Person
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .tokens import account_activation_token



def index(request):
    return render(request, 'index.html')


def sign_up(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False
            user.save()


            current_site = get_current_site(request)
            subject = 'Activate Your Mysite Account'
            message = render_to_string('activate_your_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
                })
            user.email_user(subject, message,  from_email= 'boburjon@thinkland.uz')
            return redirect('sign_up')
    else:
        form = UserRegisterForm()
    return render(request, 'registration.html', {'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.person.email_confirmed = True
        user.save()

        new_user = Person(username=user.username, password=user.password)
        new_user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')

class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {"form":form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return redirect('/')
        return render(request, 'login.html', {'form':form})



