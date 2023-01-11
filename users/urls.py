from django.urls import path
from . import views

urlpatterns = [
    path('cadastros/', views.cadastro, name="cadastro"),
    path('login/', views.logar, name="login"),
    path('sair/', views.sair, name="logout"),
]