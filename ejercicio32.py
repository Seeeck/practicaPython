def modificar(lista):
   l=list(set(lista))
   l.reverse()
   for i in l:
       if i%2==1:
           l.remove(i)
   l.insert(0,sum(l))
   print(l)
   return l

lista= [1,2,2,3,4,5,6,7,8]  
nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )  
   
   
