from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="loginPage"),
    path('logout/', views.logoutPage, name="logoutPage"),
    path('', views.index, name= "index"),
    path('user/', views.userPage, name= "userPage"),
    path('account/', views.accountSettings, name= "accountSettings"),
    path('products/', views.products, name= "products"),
    path('customer/<str:pk>/', views.customer, name= "customer"),
    path('create_order/<str:pk>', views.create_order, name= "create_order"),
    path('update_order/<str:pk>', views.update_order, name= "update_order"),
    path('delete_order/<str:pk>', views.delete_order, name= "delete_order"),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/form.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/complete.html'), name='password_reset_complete'),
]