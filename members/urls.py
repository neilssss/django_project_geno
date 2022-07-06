from django.urls import path
from . import views
from django.urls import include,path
from django.contrib import admin



urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user, name='user'),
    #path('cart/checkout/myorder/myorderview/<int:id>', views.updatefish, name='updatefish'),
    path('myorderview/<str:t_no>',views.myorderview, name="myorderview"),
    path('cart/checkout/myorder/', views.myorder, name='myorder'),
    path('cart/checkout/proceedtopay/', views.proceedtopay, name='proceedtopay'),
    path('cart/checkout/placeorder/', views.placeorder, name='placeorder'),
    path('cart/', views.cart, name='cart'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('wishlist/',views.wishlist, name='wishlist'),
    path('wishlist/deletewishlist/', views.deletewishlist, name='deletewishlist'),
    path('buy1/', views.buy1, name='buy1'),
    path('buy1/addtocart1/addtocart/', views.addtocart, name='addtocart'),
    path('buy1/addtocart1/addtowishlist/', views.addtowishlist, name='addtowishlist'),
    path('cart/updatecart/', views.updatecart, name='updatecart'),
    path('cart/deletecart/', views.deletecart, name='deletecart'),
    
    path('buy1/addtocart1/<int:id>', views.addtocart1, name='addtocart1'),
    path('buy1/searchbarfishbuy', views.searchbarfishbuy, name='searchbarfishbuy'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('registeruser/', views.registeruser, name='registeruser'),
    path('buy/addfish2/', views.addfish2, name='addfish2'),
    path('buy/searchbarfish/', views.searchbarfish, name='searchbarfish'),
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


    #facebook login
    path('oauth/', include('social_django.urls', namespace='social')),

    path('user/searchbar/',views.searchbar,name='searchbar')

]