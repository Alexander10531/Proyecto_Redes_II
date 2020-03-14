import re

def conversionBinario(num):
    num = bin(num)
    num = num.split('b')
    num = num[1]

    
    if len(num) < 8:
        ceros = 8 - len(num)
        num = (ceros * '0') + num

    return num

def verificacionIp(direccion):
    direccionTotal = ''
    direccion = direccion.split('.')

    for x in direccion:
        direccionTotal = direccionTotal + '.' + str(conversionBinario(int(x)))
    direccionTotal = direccionTotal[1:len(direccionTotal)]
    
    if(len(direccionTotal)) != 35:
        return 'direccion Erronea'
    else:
        return direccionTotal  

def arregloDeDirecciones(listaDirecciones):
    listaBinaria = []
    for x in listaDirecciones:
        
        listaBinaria.append(verificacionIp(x))
    return listaBinaria

def formatoRutaSumarizada(direccion):
    if direccion[8] == '0':
        direccion = direccion[0:7] + '.' + direccion[9:len(direccion)]
    if direccion[17] == '0':
            direccion = direccion[0:16] + '.' + direccion[16:len(direccion)]
    if direccion[26] == '0':
                direccion = direccion[0:25] + '.' + direccion[27:len(direccion)]
    return direccion

def rutaSumarizada(listaDirecciones):
    
    for x in listaDirecciones:
        for y in range(0,len(listaDirecciones[0])):
            if(listaDirecciones[0][y] != x[y]):
                coincidencia = listaDirecciones[0][0:y]
                faltante = 35 - len(coincidencia)
                coincidencia += '0' * faltante
                return formatoRutaSumarizada(coincidencia)



 

         