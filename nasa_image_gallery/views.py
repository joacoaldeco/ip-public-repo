# capa de vista/presentación
# si se necesita algún dato (lista, valor, etc), esta capa SIEMPRE se comunica con services_nasa_image_gallery.py

from django.shortcuts import redirect, render
from .layers.services import services_nasa_image_gallery
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from nasa_image_gallery.layers.services.services_nasa_image_gallery import getAllImages,saveFavourite as saveFavourite2,getAllFavouritesByUser as getAllFavouritesByUser2,deleteFavourite as deleteFavourite2
from googletrans import Translator
from nasa_image_gallery.palBuscables import palIngles
from .models import CustomUserCreationForm
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from main import settings


# función que invoca al template del índice de la aplicación.
def index_page(request):
    return render(request, 'index.html')


# auxiliar: retorna 2 listados -> uno de las imágenes de la API y otro de los favoritos del usuario.
def getAllImagesAndFavouriteList(request):
    images = getAllImages()
    favourite_list = getAllFavouritesByUser(request)
    return images, favourite_list


# función principal de la galería.

def home(request):
    # llama a la función auxiliar getAllImagesAndFavouriteList() y obtiene 2 listados: uno de las imágenes de la API y otro de favoritos por usuario*.
    # (*) este último, solo si se desarrolló el opcional de favoritos; caso contrario, será un listado vacío [].
    images=getAllImages()
    favourite_list = getAllFavouritesByUser2(request)
    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list} )


# función utilizada en el buscador.
def search(request):
    if request.method == 'POST':    
        search_msg = request.POST.get('query', '')
        if search_msg:
            #evita que se rompa si buscan apretando la tecla espacio
            if(search_msg in "                 "):
                images= getAllImages()
                return render(request,"home.html",{"images":images})
            # Traduce la palabra del español al ingles
            translator = Translator()
            translatedSearch_mgs = translator.translate(search_msg, src='es', dest='en').text
            #si es una de las palabras de la lista de palbuscables.py entra
            if(search_msg in palIngles):
                images= getAllImages(search_msg)
                return render(request,"home.html",{"images":images})
            else:
                #si esta en español la traduce y si está en la lista de palbuscables.py entra
                #para el traslate ejecutar como admin el visual y en la terminal poner: pip install googletrans==4.0.0-rc1
                if(translatedSearch_mgs.lower() in palIngles):
                    images= getAllImages(translatedSearch_mgs)
                    return render(request,"home.html",{"images":images})
                # si no está en la lista,busca por default "space"
                else:
                    images= getAllImages()
                    return render(request,"home.html",{"images":images})
        #si no pusieron nada busca por default "space"                    
        else:
            images= getAllImages()
            return render(request,"home.html",{"images":images})

    # si el usuario no ingresó texto alguno, debe refrescar la página; caso contrario, debe filtrar aquellas imágenes que posean el texto de búsqueda.


# Crear / registrar cuenta
def register_view(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            subject = 'verificación'
            message = f'¡Hola {form.cleaned_data.get("first_name")}!\n\n' \
                      f'Gracias por registrarte en nuestro sitio. A continuación, encontrarás tus credenciales de acceso:\n\n' \
                      f'Nombre de usuario: {form.cleaned_data.get("username")}\n' \
                      f'Contraseña: {form.cleaned_data.get("password1")}\n\n' \
                      f'¡Bienvenido y disfruta de nuestra plataforma!\n\n' \
                      f'Saludos,\n' \
                      f'El equipo de Introducción a la Programación Número 3'
            recipient = form.cleaned_data.get('email')
            print("Se envió el correo")
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            form.save()
            print("REGISTRADO EXITOSAMENTE")
            return redirect('login')
    return render(request, 'register.html', {'form': form})


# las siguientes funciones se utilizan para implementar la sección de favoritos: traer los favoritos de un usuario, guardarlos, eliminarlos y desloguearse de la app.
@login_required
def getAllFavouritesByUser(request): 
    favourite_list = getAllFavouritesByUser2(request)
    return render(request, 'favourites.html', {'favourite_list': favourite_list})


@login_required
def saveFavourite(request):
    if request.method=='POST':
        saveFavourite2(request)
        return redirect('/home')


@login_required
def deleteFavourite(request):
    if request.method=='POST':
        deleteFavourite2(request)
        return redirect('/favourites')


def exit(request):
    print("salió")
    return index_page(request)