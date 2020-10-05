"""example_prac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from prac import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base,name='base'),
    path('order1', views.order1 ,name='order1'),
    path('transaction1', views.transaction1 ,name='transaction1'),
    path('ordertable', views.ordertable ,name='ordertable'),
    path('transactiontable', views.transactiontable ,name='transactiontable'),
    
]
