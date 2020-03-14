import Binario as bi

listaDirecciones = []
listaDirecciones.append('192.168.40.0')
listaDirecciones.append('192.168.40.32')

print(bi.arregloDeDirecciones(listaDirecciones))
print(bi.rutaSumarizada(bi.arregloDeDirecciones(listaDirecciones)))
