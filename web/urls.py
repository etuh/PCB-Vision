from django.urls import path
from django.contrib.auth import views

from . import views as tempview

from web.views import frontpage, signup

urlpatterns = [
    path("",tempview.index, name="index"),
    path("fp/",frontpage, name="frontpage"),
    path("signup/",signup, name="signup"),
    path("login/",views.LoginView.as_view(template_name='web/login.html'), name="login"),
    path("logout/",views.LogoutView.as_view(), name="logout")    
]