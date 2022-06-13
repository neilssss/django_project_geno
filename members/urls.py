from django.urls import path
from . import views
from django.urls import include,path
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('buy/', views.buy, name='buy'),
    path('buy/addfish/', views.addfish, name='addfish'),
    path('buy/addfish/addfishrecord/', views.addfishrecord, name='addfishrecord'),
    path('buy/deletefish/<int:id>', views.deletefish, name='deletefish'),
    path('buy/updatefish/<int:id>', views.updatefish, name='updatefish'),
    path('buy/updatefish/updatefishrecord/<int:id>', views.updatefishrecord, name='updatefishrecord'),
    path('user/add/', views.add, name='add'),
    path('user/home/', views.home, name='home'),
    path('user/display/home/', views.home, name='home'),
    path('user/add/home/', views.home, name='home'),
    path('user/add/addrecord/', views.addrecord, name='addrecord'),
    path('user/delete/<int:id>', views.delete, name='delete'),
    path('user/update/<int:id>', views.update, name='update'),
    path('user/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('user/display/',views.display,name='display'),
    path('user/searchbar/',views.searchbar,name='searchbar')

]