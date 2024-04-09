from  medicamento import Medicamento
#paso 1: crear instancia
medicamento_nuevo = Medicamento()

#paso 2: solicitud de ingreso de datos
precio = int(input("ingrese el precio del medicamento>))
                  
                  #paso 3: pasar el metodo de instancia el valor capturado
                  medicamento_nuevo.asigna_precio(precio)
                  medicamento_nuevo.precio