from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('about/',views.about,name="About"),
    path('menu/',views.menu,name="Menu"),
    path('contact/',views.contact,name="Contact"),
    path('login/',views.login,name="Login"),
    path('signup',views.handleSignup,name="handleSignup"),
    path('signin',views.handleLogin,name="handleLogin")
]
