#hola
#Ejercicio 1
'''print('hola mundo')'''

#ejercicio 2
'''palabra=('Hola Mundo')
print(palabra)
print('¿cómo te llamas?')'''

'''#ejercicio 3
nombre=input()
print('es un placer,'+nombre)'''

#ejercicio 4
'''print(((3+2)/(2*5))**2)'''

#ejercicio 5 
'''print('horas trabajadas')
horas=float(input())
print('cuanto es el costo por hora')
costo=float(input())
print(costo*horas)'''

#ejercicio 6
'''print('introducir un entero positivo')
N=int(input())
print((N*(N+1))/2)'''

#ejercicio 7
'''print('Cual es su peso(kg)')
peso=float(input())
print('cual es su estatura (en metros)')
estatura=float(input())
im=((peso/estatura)**2) 
imc=round(im, 2)
print('su imc es', imc)'''

#ejercicio 8
'''print('escriba un numero entero')
N=int(input())
print('escriba un numero entero')
M=int(input())
C=(N//M)
R=(N%M)
print('el cociente es', C)
print('el residuo es', R)'''

#ejercicio 9
'''print('escriba una cantidad a invertir')
c=float(input())
print('escriba su interes anual')
i=float(input())
print('escriba el numero de años')
años=float(input())
f=(c*(i/100+1)**años)
print('inversion')
print(f)'''

#ejercicio 10
'''print('numero de payasos')
p=int(input())
print('numero de muñecas')
m=int(input())
pg=(p*112)
print('peso total de payasos', pg)
mg=(m*75)
print('peso total de muñecas', mg)
pgmg=(pg+mg)
print('peso total de payasos y muñecas', pgmg)'''

#ejercicio 11
'''print('cantidad de dinero primer año')
primer=float(input())
porcentajeaumento=float(4)
porcentaje1=(primer*(porcentajeaumento/100))
print('aumento primer año', porcentaje1)
print('cantidad de dinero segundo año')
segundo=float(input())
porcentaje2=(segundo*(porcentajeaumento/100))
print('aumento segundo año', porcentaje2)
print('cantidad tercer año')
tercer=float(input())
porcentaje3=(tercer*(porcentajeaumento/100))
print('aumento tercer año', porcentaje3)
total=(porcentaje1+porcentaje2+porcentaje3)
print('aumento de los tres años en total', total)'''

#PRACTICA 2
#ejercicio 1
'''print('introducir un numero')
n=int(input())
s=((n*(n+1))/2)
if s>20:print(s,'es un gran numero!')
else: print('suma de todos los enteros desde 1 hasta', n, 'es', s)'''

 #ejercicio 2
'''print('escriba un numero')
n=int(input())
print('escriba otro numero')
m=int(input())
c=(n/m)
r=(n%m)
print('el cociente es', c)
print('el residuo es', r)
if c<1: print('el divisor es mayor al dividendo')
if c>1: print('el divisor es menor que el dividendo')
if c==1: print('el divisor y el dividendo son iguales')'''

#ejercicio 3
'''print('cantidad a invertir')
ci=float(input())
print('interes anual')
ia=float(input())
print('numero de años')
na=int(input())
capital=(ci*(ia/100+1)**na)
if capital<100000: print('el valor de', capital, 'tiene baja rentabilidad')
if 100000>capital>1000000:print('el valor de', capital, 'tiene rentabilidad moderada')'''

#ejercicio 3
'''print('numero de payasos vendidos')
p=int(input())
print('numero de muñescas vendidas')
m=int(input())
pg=(112*p)
mg=(75*m)
s="sí"
pesototal=(pg+mg)
print('peso total', pesototal)
if pesototal>3000000:
  print('desea enviarlo?')
  i=input()
  if i==s:
    print('contenedor enviado')
  else: print('contendor no enviado')
else: print('el peso total del pedido es', pesototal)'''

#Practica 3
#ejercicio 1
'''def numeros(a, b):
  s=a+b
  return s
d=int(input('introduzca un número '))
c=int(input('introduzca otro número '))
suma=numeros(c,d)
print(suma)'''

#ejercicio 2
'''def numeros(a,b):
  r=a-b
  return r
c=int(input('introduzca un número '))
d=int(input('introduzca otro número '))
resta=numeros(c,d)
print(resta)'''

#ejercicio 3
'''def numeros(a,b):
  m=a*b
  return m
c=int(input('introduzca un números '))
d=int(input('introduzca otro número '))
multiplicación=numeros(c,d)
print(multiplicación)'''

#ejercicio 4
'''def numeros(a, b):
  if b==0:
    print('no es posible realizar la división')
  d=a/b 
  return d
n=int(input('introduzca un número '))
m=int(input('introduzca otro número '))
división=numeros(n,m)
print(división)'''

#ejercicio 5
def entre(a, b):
  d=a/b 
  return d
def por(a,b):
    m=a*b
    return m
def menos(a,b):
  r=a-b
  return r
def mas(a, b):
  s=a+b
  return s
n=int(input('introduzca un valor '))
f=int(input('introduzca otro valor '))
división=entre(n,f)
multiplicacion=por(n,f)
resta=menos(n,f)
suma=mas(n,f)
operación=input('¿qué operación quiere realizar? ')
if (operación=="+"):
  print(suma)
elif (operación=="-"):
  print(resta)
elif (operación=="*"):
  print(multiplicacion)
elif (operación=="/"):
  print(división)