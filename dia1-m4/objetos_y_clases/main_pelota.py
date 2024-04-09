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

#Metodos estaticos
#no se necesita crear un objeto para invocar al metodo
print()
print(Pelota.crear_rebote())#[5,0,4,0,3,0,2,0,1,]


print()
pelota_futbol = Pelota()
print(pelota_futbol)

