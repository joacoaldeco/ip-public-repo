# capa de servicio/lógica de negocio

from ..transport import transport
from ..dao import repositories
from ..generic import mapper
from django.contrib.auth import get_user
from ..transport.transport import getAllImages as getAllImages2
from ..generic.mapper import fromRequestIntoNASACard,fromTemplateIntoNASACard,fromRepositoryIntoNASACard
from nasa_image_gallery.models import Favourite
from nasa_image_gallery.layers.dao import repositories
from nasa_image_gallery.layers.generic.mapper import fromRepositoryIntoNASACard


def getAllImages(input=None):
    # obtiene un listado de imágenes desde transport.py y lo guarda en un json_collection.
    # ¡OJO! el parámetro 'input' indica si se debe buscar por un valor introducido en el buscador.
    json_collection = getAllImages2(input)

    images = []
    for im in json_collection: 
        image=fromRequestIntoNASACard(im)
        images.append(image)

    # recorre el listado de objetos JSON, lo transforma en una NASACard y lo agrega en el listado de images. Ayuda: ver mapper.py.

    return images


def getImagesBySearchInputLike(input):
    return getAllImages(input)


# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = fromTemplateIntoNASACard(request) # transformamos un request del template en una NASACard.
    fav.user = get_user(request) # le seteamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.


# usados en el template 'favourites.html'
def getAllFavouritesByUser(request):
    if not request.user.is_authenticated:
        return []
    else:
        user =  get_user(request)
        favourite_list= Favourite.objects.filter(user=user)
        mapped_favourites = []
        
        for favourite in favourite_list:#convertimos el objeto Favourite en un diccionario.
            fav_dict = {
                'id': favourite.id,
                'title': favourite.title,
                'description': favourite.description,
                'image_url': favourite.image_url, #formateamos la fecha como una cadena.
                'date': favourite.date.strftime('%Y-%m-%d')
            }
            nasa_card = fromRepositoryIntoNASACard(fav_dict) #convertimos el diccionario en un objeto NASACard.
            mapped_favourites.append(nasa_card)
        
        return mapped_favourites



def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.