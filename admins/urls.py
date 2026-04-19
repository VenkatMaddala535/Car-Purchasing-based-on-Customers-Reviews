from django.urls import path
from . import views

app_name = 'admins_'

urlpatterns = [

    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('users_list/', views.users_list, name='users_list'),
    path('activate_user/<str:id>', views.activate_user, name='activate_user'),
    path('admin_results/', views.admin_results, name='admin_results'),

]
