from django.urls import path, include

from .views import *

urlpatterns = [
    path('login/', APILoginView.as_view(), name='api_login'), 
    path('logout/', APILogoutView.as_view(), name='api_logout'), 
    path('update_password/', APIPasswordUpdateView.as_view(), name='api_update_password'), 
]