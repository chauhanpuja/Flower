from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path('',views.index,name="index"),
    path('quickview/<int:id>',views.quickview,name="quickview"),
    path('contact',views.contact,name="contact"),
    path('search',views.search,name="search"),
    path('about',views.about,name="about"),
    # reset password
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    # shopping cart
    
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
#     end cart

    path('handlelogin',views.handlelogin,name="handlelogin"),
    path('handlelogout',views.handlelogout,name="handlelogout"),
    path('signup',views.register,name="register"),
    path('handlelogin1',views.handlelogin1,name="handlelogin1"),
   
    path('checkout',views.checkout,name="checkout"),
    path('placeorder',views.placeorder,name="placeorder"),
    path('thankyou',views.thankyou,name="thankyou"),
    path('myorder',views.myorder,name="myorder"),
    # path('category/<str:slug>',views.category,name="category")
    # path('verify_payment',views.verifypayment,name="verifypayment"),

]
