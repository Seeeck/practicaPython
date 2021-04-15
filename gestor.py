import pickle
from io import open
class Personaje():

    def __init__(self,nombre,vida,ataque,defensa,alcance):
        self.nombre=nombre
        self.vida=vida
        self.ataque=ataque
        self.defensa=defensa
        self.alcance=alcance

    def __str__(self):
        return "{}{}{}{}{}".format(self.nombre,self.vida,self.ataque,self.defensa,self.alcance)

class Gestor():
    characters=[]
    def addCharacter(self,character):
        if character not in self.characters:
            self.characters.append(character)
            f=open('personajes.pkcl','wb')
            pickle.dump(self.characters,f)
            f.close()

    def showCharacter(self,characterName):
        for character in self.characters:
            if character.nombre == characterName:
                print(character)
        else:
            print('sin character')


    def deleteCharacter(self,character):
        if character in self.characters:
            self.characters.remove(character)


p1=Personaje('hola',1,2,3,4)
g1=Gestor()
g1.addCharacter(p1)
g1.deleteCharacter(p1)
g1.showCharacter('hola')


