from venv import create
from django.urls import path
from .views import index, logout_view, sobre, cadastro, login, list_resgates, create_resgates, update_resgates, delete_resgates, list_denuncias, create_denuncias, update_denuncias, delete_denuncias

urlpatterns = [
    path('', index, name = 'index'),
    path('resgates', list_resgates, name = 'list_resgates'),
    path('sobre/', sobre, name = 'sobre'),
    path('cadastro/', cadastro, name = 'cadastro'),
    path('login/', login, name = 'login'),
    path('new', create_resgates, name = 'create_resgates'),
    path('update/<int:codResgate>/', update_resgates, name = 'update_resgates'),
    path('delete/<int:codResgate>/', delete_resgates, name = 'delete_resgates'),
    path('denuncias', list_denuncias, name = 'list_denuncias'),
    path('novadenuncia', create_denuncias, name = 'create_denuncias'),
    path('updatedenuncia/<int:codDenuncia>/', update_denuncias, name = 'update_denuncias'),
    path('deletedenuncia/<int:codDenuncia>/', delete_denuncias, name = 'delete_denuncias'),
    path('logout', logout_view, name = 'logout_view')
]