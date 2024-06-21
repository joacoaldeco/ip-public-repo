# capa de vista/presentación
# si se necesita algún dato (lista, valor, etc), esta capa SIEMPRE se comunica con services_nasa_image_gallery.py

from django.shortcuts import redirect, render
from .layers.services import services_nasa_image_gallery
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from nasa_image_gallery.layers.services.services_nasa_image_gallery import getAllImages
from googletrans import Translator
from nasa_image_gallery.palBuscables import palIngles

# función que invoca al template del índice de la aplicación.
def index_page(request):
    return render(request, 'index.html')

# auxiliar: retorna 2 listados -> uno de las imágenes de la API y otro de los favoritos del usuario.
def getAllImagesAndFavouriteList(request):
    images = getAllImages()
    favourite_list = []

    return images, favourite_list

# función principal de la galería.
def home(request):
    # llama a la función auxiliar getAllImagesAndFavouriteList() y obtiene 2 listados: uno de las imágenes de la API y otro de favoritos por usuario*.
    # (*) este último, solo si se desarrolló el opcional de favoritos; caso contrario, será un listado vacío [].
    images,favourite_list=getAllImagesAndFavouriteList(request)
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
    pass


# las siguientes funciones se utilizan para implementar la sección de favoritos: traer los favoritos de un usuario, guardarlos, eliminarlos y desloguearse de la app.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', {'favourite_list': favourite_list})


@login_required
def saveFavourite(request):
    pass


@login_required
def deleteFavourite(request):
    pass


@login_required
def exit(request):
    pass