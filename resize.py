import PIL
from PIL import Image
import os

################# Funciones ################3

#Funcion que cambia el tamaño de la fotografia
def resize_ancho(fotografias, tamaño):
    #Recorremos cada fotografia de la lista
    for imagen in fotografias:

        print("Fotografia:",imagen,"\n")
        
        #Se abre la imagen
        img = Image.open(imagen)
        #Se calcula el porcentaje de reduccion
        porcentaje_ancho = tamaño / float(img.size[0])
        #Se especifica el acho y alto de la fotografia
        ancho = tamaño
        alto = int(float(img.size[1]) * float(porcentaje_ancho))
        #Se aplica el resize y se guarda la imagen
        img = img.resize((ancho, alto),PIL.Image.ANTIALIAS )
        img.save(imagen)
        
def resize_altura(fotografias, tamaño):
    for imagen in fotografias:
        
        print("Fotografia:",imagen,"\n")
        
        #Se abre la imagen
        img = Image.open(imagen)
        #Se calcula el porcentaje de reduccion
        porcentaje_alto = tamaño / float(img.size[1])
        #Se especifica el acho y alto de la fotografia
        ancho = int(float(img.size[0]) * float(porcentaje_alto))
        alto = tamaño
        #Se aplica el resize y se guarda la imagen
        img = img.resize((ancho, alto),PIL.Image.ANTIALIAS )
        img.save(imagen)


#Se obtiene el nombre del directorio y se cargan las imágenes a una lista
nombre_directorio = os.path.dirname(os.path.abspath(__file__))
fotografias = [archivo for archivo in os.listdir(nombre_directorio) if '.png' in archivo or '.jpg' in archivo or '.jpeg' in archivo]


#Especificacion del tamaño de la imagen
print("\n########## RESIZER DE FOTOGRAFIAS #############\n")

print("")

if len(fotografias) == 0:
    print("\n¡No hay fotografías en la carpeta, por favor, añade algunas")
    
else:
    opcion = int(input("¿Qué quieres hacer? 1- Cambiar el tamaño en función de la anchura | 2- Cambiar tamaño en función de la altura | 3- Salir: " ))
    
    while opcion != 1 and opcion != 2 and opcion != 3:    
        opcion = int(input("Entrada incorrecta, vuelve a intentarlo: "))
        
    if opcion == 1:
        print("")
        tamaño = int(input("Introduce la medida del ancho que deseas: "))
        print("")

        resize_ancho(fotografias, tamaño)
        
        print("\nTODAS LAS FOTOGRAFIAS MODIFICADAS CON EXITO\n")
    
        
    elif opcion == 2:
        print("")
        tamaño = int(input("Introduce la medida de la altura que deseas: "))
        print("")
        
        resize_altura(fotografias, tamaño)
 
        print("\nTODAS LAS FOTOGRAFIAS MODIFICADAS CON EXITO\n")

    
    elif opcion == 0:
        exit
    
    

