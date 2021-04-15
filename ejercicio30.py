class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

class Camioneta(Vehiculo):
    
    def __init__(self,color,ruedas,carga):
        Vehiculo.__init__(self,color,ruedas)
        self.carga=carga
    
    def __str__(self):
        return Vehiculo.__str__(self) + ",{} ".format(self.carga)

class Bicicleta(Vehiculo):

    def __init__(self,color,ruedas,tipo):

        Vehiculo.__init__(self,color,ruedas)
        self.tipo=tipo

    def __str__(self):
        return Vehiculo.__str__(self) + ",{}".format(self.tipo)

class Motocicleta(Vehiculo):

    def __init__(self,color,ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h  {} cc".format(self.velocidad,self.cilindrada)

moto=Motocicleta("rojo",2,200,2000)
bici=Bicicleta('negra',2,"urbana")
camioneta=Camioneta('azul',4,500)
auto=Coche('verde',4,300,2000)
vehiculos=[moto,bici,camioneta,auto]

def Catalogar(lista,ruedas=0):

    if ruedas>0:
        veh=0
        for a in lista:
            if a.ruedas==ruedas:
               veh=veh+1
        print("Se han encontrado {} con {}".format(veh,ruedas))
    else:

        for i in lista:
            print(type(i).__name__)
            print(i.__str__())

Catalogar(vehiculos,0) 

