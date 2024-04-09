




def asigna_precio(self,precio_entregado: int):
    es_valido = self.validar_mayor_a_cero(precio_entregado)
    if es_valido: 
        #self = ser
        self.precio = precio_entregado
    # podria poner def directamente y es validoif es_valido: asigna_precio(self,precio_entregado)
    else:
        print(f."el precio (precio_entregado), no es un valor valido"
              #validacio y resultado)
        