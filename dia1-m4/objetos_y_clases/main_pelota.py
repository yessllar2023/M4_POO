#import pelota #en minuscula por importacion
from objetos_y_clases.pelota import Pelota
#INSTANCIAR O CREAR OBJETO
#pelota_de_andy = pelota.Pelota()
pelota_de_andy = Pelota()#de esta forma es la mas comun

print(pelota_de_andy)
print(type(pelota_de_andy))#<class "pelota.Pelota">
print(pelota_de_andy.forma)#redondeada
print()

pelota_de_andy.material = "Plastico"
print(pelota_de_andy.material)
    
pelota_tenis = Pelota()
print(pelota_tenis)