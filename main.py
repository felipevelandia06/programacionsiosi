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
'''def entre(a, b):
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
operación=input('¿qué operación quiere realizar? ')
if (operación=="+"):
  suma=mas(n,f)
  print(suma)
elif (operación=="-"):
  resta=menos(n,f)
  print(resta)
elif (operación=="*"):
  multiplicacion=por(n,f)
  print(multiplicacion)
elif (operación=="/"):
  división=entre(n,f)
  print(división)
else: print('operacion no valida')'''

#ejercicio
'''def intereses(inv):
  d= inv
  if (d >0 and d<1000000):
    return 2 
  elif(d>=1000000 and d<2000000):
    return 5
  else:
    return 7

def calBalance(int, inv):
  n= int
  d= inv
  return round((d*(1+(n/100))),2)

def ctaAhorro():
  inversion = float(input('ingrese el valor de la inversion: '))
  interes= intereses(inversion)
  b1= calBalance(interes, inversion)
  b2= calBalance (interes,b1)
  b3= calBalance(interes,b2)
  print("balace año 1: "+ str(b1) + "Balance año 2: " + str(b2) + str(b3))

ctaAhorro()'''

#ejercicio 2
#'''def menu():
 #''' print('''ingrese el codigo de la figura
'''circulo 1
cuadrado 2
triangulo 3
pentagono regular 4
rombo 5)'''
'''def circulo():
  radio=float(input('igrese el valor del radio '))
  areacirculo=3.1416*radio**2
  return(areacirculo)
def cuadrado():
  lado=float(input('ingrese el valor del lado '))
  areacuadrado=lado*lado
  return(areacuadrado)
def triangulo():
  base=float(input('ingrese el valor de la base '))
  altura=float(input('ingrese el valor de la altura '))
  areatriangulo=((base*altura)/2)
  return(areatriangulo)
def pentagonoregular():
  perimetro=float(input('ingrese el valor del perimetro '))
  apotema=float(input('ingrese el valor del apotema '))
  areapentagonoregular=((perimetro*apotema)/2)
  return(areapentagonoregular)
def rombo():
  diagonalmayor=float(input('ingrese el valor de la diagonal mayor '))
  diagonalmenor=float(input('ingrese el valor de la diagoal menor '))
  if diagonalmenor>diagonalmayor:
    arearombo=print('valores no validos')
  else: arearombo=((diagonalmayor*diagonalmenor)/2)
  return(arearombo)
def areafig():
  menu()
  figura=int(input('ingrese el codigo de la figura que desee '))
  if figura==1:
    print(circulo())
  elif figura==2:
    print(cuadrado())
  elif figura==3:
    print(triangulo())
  elif figura==4:
    print(pentagonoregular())
  elif figura==5:
    print(rombo())
  else: print('coigo no valido')
#areafig()'''

#agosto 28
#ejercicio 1
'''def menu(): 
  ''''''print( ingrese el codigo de la marca de su estereo
Sonyo 1
jbl 2
samsung 3'''
'''def descuentop(a):
  descuento=(a-(a*0.1))
  return(descuento)'''
'''def descuentom(a):
  descuento=a-(a*0.05)
  return(descuento)'''
'''def descuentopm(a):
  descuento=a-(a*0.15)
  return(descuento)'''
'''def ivad(b):
  preciototal=(b+(b*0.2))
  return(preciototal)'''
'''def iva(c)
  preciototal=c+0.2*c
  return(preciototal)'''
  
'''def principal():
precio=float(input('ingrese el precio '))
  menu()
  marca=int(input('ingrese el codigo correspondiente a la marca del estereo '))
  if marca==2 or marca==3 and precio>2000000:
    ia=descuentop(precio)
    print(ivad(ia))
    elif marca==1 and precio<2000000:
    i=descuentom(precio)
    ivad(i)
  elif marca==1 and precio>2000000:'''
'''i=descuentopm(precio)
    ivad(i)
  else: print(iva(precio'''

'''principal()'''

#septiembre 11
#ejercicio1 
'''A=0
while A< 10:
  print(A)
  A=A+1'''

#ejercicio2
def menu():
  print('''ingrese el codigo respectivo a la operación que quiera realizar
  1. suma
  2. resta
  3. multiplicación
  4. división
  5. finalizar''')
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
def principal():
  n=float(input('introduzca un valor '))
  f=float(input('introduzca otro valor '))
  operación=0
  menu()
  while operación !=5:
    operación=int(input('¿qué operación quiere realizar? '))
    if operación==1:
      suma=mas(n,f)
      print(suma)
    elif operación==2:
      print('entre a la opción dos')
      resta=menos(n,f)
      print(resta)
    elif operación==3:
      multiplicacion=por(n,f)
      print(multiplicacion)
    elif operación==4:
      división=entre(n,f)
      print(división)
    elif operación==5:
      print('gracias')
      break
    else: print('operacion no valida')

principal()