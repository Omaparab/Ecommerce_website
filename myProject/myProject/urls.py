"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('proceed/', views.proceed, name='proceed'),
    path('buy/', views.buy, name='buy'),
    path('logout_confirmation/', views.logout_confirmation, name='logout_confirmation'),

    path('calci/', views.calci, name='calci'),
    path('drafter/', views.drafter, name='drafter'),
    path('folder/', views.folder, name='folder'),
    path('geometry/', views.geometry, name='geometry'),
    path('punch/', views.punch, name='punch'),
    path('raspberry/', views.raspberry, name='raspberry'),
    path('sheetholder/', views.sheetholder, name='sheetholder'),
    path('stapler/', views.stapler, name='stapler'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
