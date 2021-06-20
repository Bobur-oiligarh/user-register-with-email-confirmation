from django.urls import path
from .views  import *

urlpatterns = [
    path('', index, name='home'),
    path('sign_up/', sign_up, name = 'sign_up'),
    path('activate/<str:uidb64>/<str:token>/', activate, name = 'activate'),
    path('login/', LoginView.as_view(), name='login'),

   ]


# path('sendmail/', sendmail, name='sendmail'),
# path('register/', register, name='register'),




