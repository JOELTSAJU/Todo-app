from django.urls import path
from list_app import views


urlpatterns =[
    path('register/',views.register_view,name='register'),
    path('',views.login_view,name='login'),
    path('home/<str:username>/', views.homepage_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
  

    # path('create_list/<str:username>/', views.task_list_view, name='create_list'),
]

