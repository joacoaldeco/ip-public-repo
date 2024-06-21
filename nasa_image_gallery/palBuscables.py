#posiblesBusquedas=["sol","luna","Estrellas", "Planetas", "Galaxias", "Nebulosas", "Agujeros negros", "Supernovas", "Constelaciones", "Satélites", "Cometas", "Meteoritos", "Cinturón de asteroides", "Vía Láctea", "Espacio interestelar", "Radiación cósmica de fondo", "Gravedad", "Telescopios", "Exploración espacial", "Estación Espacial Internacional", "Viajes espaciales tripulados", "Cohetes", "Sondas espaciales", "Órbita geosincrónica", "Cinturones de Van Allen", "Nave espacial", "Cosmonauta", "Astronauta", "Eclipses", "Transbordador espacial", "Estación del espacio", "Auroras", "Campo magnético de la tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno", "Plutón", "Exoplanetas", "Nave espacial no tripulada", "Sistema solar", "Nave espacial robótica", "Cohete pesado SpaceX Falcon", "Cinturón de Kuiper", "Nave espacial Voyager", "Nube de Oort", "Estrella enana blanca", "Estrella enana roja", "Estrella gigante", "Estrella de neutrones", "Estrella binaria", "Estrella variable", "Estrella fugaz"]
traduccionXBusqueda=["sun","moon","Stars", "Planets", "Galaxies", "Nebulae", "Black holes", "Supernovas", "Constellations", "Satellites", "Comets", "Meteorites", "Asteroid belt", "Milky Way", "Interstellar space", "Cosmic background radiation", "Gravity", "Telescopes", "Space exploration", "International Space Station", "Manned space travel", "Rockets", "Space probes", "Geosynchronous orbit", "Van Allen belts", "Spacecraft", "Cosmonaut", "Astronaut", "Eclipses", "Space shuttle", "space station", "Auroras", "Earth's magnetic field", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Exoplanets", "Unmanned spacecraft", "Solar system", "Robotic spacecraft", "SpaceX Falcon Heavy rocket", "Kuiper Belt", "Voyager spacecraft", "Oort Cloud", "White dwarf star", "Red dwarf star", "Giant star", "Neutron star", "Binary star", "Variable star", "Shooting star"]
#palabrasEspañol=[]
palIngles=[]
#for palabras in posiblesBusquedas:
    #palabrasEspañol.append(palabras.lower())
for words in traduccionXBusqueda:
    palIngles.append(words.lower())
#print(traduccionXBusqueda[0])

#por si no anda el traductor agregar a views:
                #if(search_msg in palabrasEspañol):
                    #print("si lee")
                    #for pal in range(len(palabrasEspañol)):
                        #if(palabrasEspañol[pal]==search_msg):
                            #images= getAllImages(palIngles[pal])
                            #return render(request,"home.html",{"images":images})