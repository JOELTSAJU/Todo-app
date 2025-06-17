from django.urls import path
from list_app import views


urlpatterns =[
    path('register/',views.register_view,name='register'),
    path('',views.login_view,name='login'),
    path('home/<str:username>/', views.homepage_view, name='home')
]

