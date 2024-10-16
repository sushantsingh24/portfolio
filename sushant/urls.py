"""
URL configuration for sushant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sushant1 import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('achivement/', views.achivement, name='achivement'),
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('resume/', views.resume, name='resume'),
    path('About/', views.about, name='about'),
    path('logout/', views.logoutPage, name='logout'),
    
   


]
urlpatterns+=staticfiles_urlpatterns()
