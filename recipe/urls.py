from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('register_page/', views.register_page, name='register_page'),
    path('login_status/', views.login_status, name='login_status'),
    path('save_data/', views.save_data, name='save_data'),
    path('menu/', views.menu, name='menu'),
    path('<int:recipe_id>/detail/', views.detail, name='detail.html'),
    path('save_recipe/', views.save_recipe, name='save_recipe'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('logout/', views.logout_user, name='logout_user')
]