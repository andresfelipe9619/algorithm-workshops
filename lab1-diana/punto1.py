#ALGORITMIA GRUPO 03
#LABORATORIO 1 - PUNTO 1
#NOVIEMBRE 10 2019
#PROF: DIANA LOZANO

#AURA JULIETH HINOJOSA MUÑOZ – 1626392-3752
################################################################

#Defino funciones
def calculaPotencia(voltaje, rt):   
   potencia = (voltaje * voltaje) / rt
   return potencia

def calculaCorriente(voltaje, rt):   
   corriente =  voltaje / rt
   return corriente

def calculaResitenciaTotal(r1,r2,r3,r4,r5):   
   rt = 1/((1/r1)+(1/r2)+(1/r3)+(1/r4) +(1/r5))
   return rt

#Leo entradas:
voltaje = float(input("Ingrese el voltaje en voltios...........: "))
r1 = float(input("Ingrese el valor en ohmios de la resistencia 1: "))
r2 = float(input("Ingrese el valor en ohmios de la resistencia 2: "))
r3 = float(input("Ingrese el valor en ohmios de la resistencia 3: "))
r4 = float(input("Ingrese el valor en ohmios de la resistencia 4: "))
r5 = float(input("Ingrese el valor en ohmios de la resistencia 5: "))

#Proceso datos:
resistenciaTotal = calculaResitenciaTotal(r1,r2,r3,r4,r5)
corriente = calculaCorriente(voltaje, resistenciaTotal)
potencia = calculaPotencia(voltaje, resistenciaTotal)

#Muestro resultados:
print("==========================================================")
print("=                                                         ")
print("=                       RESULTADOS                       =")
print("=                                                         ")
print("==========================================================")
print("Resistencia total del circuito :  " + str(resistenciaTotal))
print("Corriente en el circuito :  " + str(corriente))
print("Potencia en el circuito :  " + str(potencia))
print("==========================================================")
