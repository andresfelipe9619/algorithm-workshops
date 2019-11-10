#ALGORITMIA GRUPO 03
#LABORATORIO 1 - PUNTO 1
#NOVIEMBRE 10 2019
#PROF: DIANA LOZANO

#AURA JULIETH HINOJOSA MUÑOZ – 1626392-3752
################################################################

# Defino funciones

# En donde: 
# Pp: Punto de pedido
# Tr: Tiempo de reposición de inventario (en días)
# Cp: Consumo medio diario
# Cmx: Consumo máximo diario
# Cmn: Consumo mínimo diario
# Emx: Existencia máxima
# Emn: Existencia mínima (Inventario de seguridad)
# CP: Cantidad de pedido
# E: Existencia actual

def calculaExistenciaMinima(cmn, tr):   
   emn = cmn * tr
   return emn

def calculaExistenciaMaxima(cmx, tr, emn):   
   emx =  (cmx * tr) + emn
   return emx

def calculaCantidadPedido(emx, e):   
   cp =  emx - e
   return cp

def calculaPuntoPedido(cp, tr, emn):   
   pp =  (cp * tr) + emn
   return pp

#Leo entradas:
consumoMinimo = float(input("Consumo minimo diario ................. : "))
consumoMaximo = float(input("Consumo maximo diario ................. : "))
consumoMedio = float(input("Consumo medio diario .................. : "))
tiempoReposicion = float(input("Tiempo de reposicion de inventario .... : "))
existenciaActual = float(input("Existencia actual ..................... : "))


#Proceso datos:
existenciaMinima = calculaExistenciaMinima(consumoMinimo, tiempoReposicion)
existenciaMaxima = calculaExistenciaMaxima(consumoMaximo, tiempoReposicion, existenciaMinima)
cantidadPedido = calculaCantidadPedido(existenciaMaxima, existenciaActual)
puntoPedido = calculaPuntoPedido(consumoMedio, tiempoReposicion, existenciaMinima)

#Muestro resultados:
print("==========================================================")
print("=                                                         ")
print("=                       RESULTADOS                       =")
print("=                                                         ")
print("==========================================================")
print("Existencia minima .... :  " + str(existenciaMinima))
print("Existencia maxima .... :  " + str(existenciaMaxima))
print("Punto de pedido ...... :  " + str(puntoPedido))
print("Cantidad de pedido ... :  " + str(cantidadPedido))
print("==========================================================")
