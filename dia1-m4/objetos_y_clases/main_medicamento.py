#import medicamento#en minuscula para idefernciar que es una importacio
#desde el archivo medicamento importame Medicamento
from medicamento import Medicamento

#instancia de la clase o creacion de un objeto
paracetamol = Medicamento()
#creamos otro objeto que pertenece a la misma clase
aspirina = Medicamento()

print(paracetamol.descuento) 
print(aspirina.descuento) 
print()
#le asignamos un nuevo valor a ese atributo
paracetamol.descuento = 0.06
print(paracetamol.descuento)
print(aspirina.descuento) 