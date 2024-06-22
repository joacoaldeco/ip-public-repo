from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('login/', views.index_page, name='login'),
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),
    path('register/', views.register_view, name="register"),
    path('index', views.exit, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),

    path('exit/', views.exit, name='exit'),
]