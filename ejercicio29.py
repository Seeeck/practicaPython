class Punto:
    #Constructor
    def __init__(self,cord_x=0,cord_y=0):
        self.cord_x=cord_x
        self.cord_y=cord_y
    #self es el propio objeto creado
    def __str__(self):
        print(f"({self.cord_x},{self.cord_y})")
    
    def cuadrante(self):
        
        if self.cord_x==0 and self.cord_y!=0:
            print("El punto se situa sobre el eje Y")
        elif self.cord_x!=0 and self.cord_y==0:
            print("El punto se situa sobre el eje X")
        elif self.cord_x==0 and self.cord_y==0:
            print("El punto se situa sobre el Origen")
        elif self.cord_x>=1 and self.cord_y>=1:
            print("El punto se situa sobre el primer cuadrante")
        elif self.cord_x<=-1 and self.cord_y>=1:
            print("El punto se situa sobre el segundo cuadrante")
        elif self.cord_x<=-1 and self.cord_y<=-1:
            print("El punto se situa sobre el tercer cuadrante")
        elif self.cord_x>=1 and self.cord_y<=-1:
            print("El punto se situa sobre el cuarto cuadrante")




    
    def vector(self,x,y):
        print(f"El vector es:({x-self.cord_x},{y-self.cord_y})")
    
class Rectangulo:

    def __init__(self,punto1=Punto(0,0),punto2=Punto(0,0)):
        self.punto1=punto1
        self.punto2=punto2
    
    def base(self):
        print("La base es:",abs(self.punto2.cord_x-self.punto1.cord_x))
    
    def altura(self):
        print("La altura es:",abs(self.punto2.cord_y-self.punto1.cord_y))
    
    def area(self):
        print("El area es:",abs(self.punto2.cord_x-self.punto1.cord_x)*abs(self.punto2.cord_y-self.punto1.cord_y))

pa=Punto(2,3)
pb=Punto(5,5)
pc=Punto(-3,-1)
pd=Punto(0,0)

#Impresion
""" pa.__str__()
pb.__str__()
pc.__str__()
pd.__str__() """

#Cuadrantes
""" pa.cuadrante()
pc.cuadrante()
pd.cuadrante()
 """
r1=Rectangulo(pa,pc)
r1.base()
r1.altura()
r1.area()




     
