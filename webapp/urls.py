from django.urls import path
from webapp import views



urlpatterns=[
    path('Home/',views.Home_page,name="Home"),
    path('About_Us/',views.About_page,name="About_Us"),
    path('Contact/',views.Contact_page,name="Contact"),
    path('save_contact',views.save_contact,name="save_contact"),
    path('All_products/',views.All_products,name="All_products"),
    path('mobile_details/<int:pro_id>/',views.mobile_details,name="mobile_details"),
    path('filtered_product/<mob_name>/',views.filtered_product,name="filtered_product"),
    path('',views.Register_page,name="Register"),
    path('save_register/',views.save_register,name="save_register"),
    path('User_login/',views.User_login,name="User_login"),
    path('User_logout/',views.User_logout,name="User_logout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart/',views.cart_page,name="cart"),
    path('delete_cart/<int:cart_id>/',views.delete_cart,name="delete_cart"),
    path('checkout/',views.checkout_page,name="checkout"),
    path('Payment/',views.Payment_page,name="Payment"),
    path('save_checkout/',views.save_checkout,name="save_checkout"),


    # path('whishlist/',views.whishlist,name="whishlist"),
    # path('save_whishlist/',views.save_whishlist,name="save_whishlist")
]