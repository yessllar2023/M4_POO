"""Introducción a la programación orientada a objetos con Python
Métodos (Parte II)"""

#METODO NO ESTATICO

#los metodos estaticos no puede modificar los atributod
#  INVESTIGACION DE "SELF"()metodo parametro
#MAS "CLASS METODOS"

from pelota import Pelota
#traer solo clase(molde).
#creacion de objeto o instancia de la clase(es lo mismo)
    #RECORDAR instancia: es crear una variable que le asingna la clase que se transforma en una variable...
pelota_multicolor = Pelota()  
 # print(pelota_multicolor.color)
 # #ERROR: unexpected indent(no existe ese atributo)
 #se vusualiza cuando llame el metodo asigna_color la instancia va a tener ese Attributo.

 #"aqui recien asigna el atributo y existe"}

print(pelota_multicolor.color)
pelota_multicolor.asigna_color("rojo")
pelota_multicolor.lee_color()
print(lee_color)

pelota_multicolor.asigna_color("verde")

pelota_multicolor.lee_color_local_atributo("amarillo")

#error: self color
#....


   
   