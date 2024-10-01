from django.urls import path
from Mobileapp import views


urlpatterns =[
    path('index_page/',views.index_page,name="index_page"),
    path('Add_company/',views.Add_company,name="Add_company"),
    path('save_company/',views.save_company,name="save_company"),
    path('display_company/',views.display_company,name="display_company"),
    path('Edit_company/<int:mob_id>/',views.Edit_Company,name="Edit_company"),
    path('update_company/<int:mob_id>/',views.update_comapny,name="update_company"),
    path('delete_company/<int:mob_id>/',views.delete_company,name="delete_company"),
    path('Add_mobile/',views.Add_mobile,name="Add_mobile"),
    path('save_mobile/',views.save_mobile,name="save_mobile"),
    path('display_mobile/',views.display_mobile,name="display_mobile"),
    path('edit_mobile/<int:mob_id>/',views.edit_mobile,name="edit_mobile"),
    path('delete_mobile/<int:mob_id>/',views.delete_mobile,name="delete_mobile"),
    path('update_mobile/<int:mob_id>/',views.update_mobile,name="update_mobile"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_page/',views.admin_page,name="admin_page"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('contact_details/',views.contact_details,name="contact_details"),
    path('delete_contact/<int:cnt_id>/',views.delete_contact,name="delete_contact"),
    path('register_details/',views.register_details,name="register_details"),
    path('delete_register/<int:cn_id>/',views.delete_register,name="delete_register")
]