from io import open
fichero=open('personas.txt','r',encoding="utf8")
lista=fichero.readlines()
fichero.close()
for linea in lista:
    linea=linea.split(';')
    print('Identificador:{} Nombre:{} Apellido:{} fecha de nacimiento:{} '.format(linea[0],linea[1],linea[2],linea[3]))