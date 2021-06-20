from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not User.objects.filter(username=username).exists():     # Agar username bazada bolmasa xato chaqiradi
            raise forms.ValidationError(f" User with username {username} is not defined")
        user = User.objects.filter(username=username).first()   # agar username bazadan topilsa unda ularning birinchisini begilaydi
        if user:                        # Agar yuqoridagi tenglik bajarilsa
            if not user.check_password(password):
                raise forms.ValidationError(' Password is incorrect')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']



class ContactForm(forms.Form):
    subject = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(max_length=150, widget=forms.Textarea(attrs={'class': 'form-control', "rows":5, }))

#
# class UserLoginForm(AuthenticationForm):
#     username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
