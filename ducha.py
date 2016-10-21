from turtle import *
from math import *


r=110 #Radio del circulo
Ys=[250.,125.,0.,-250./3.,-500./3.,-250.]
Xs=[-750./4,-125.,-250./4]
pendientes=[]

#Calcula la pendiente de una recta
def pendiente(x,y):

    return y/x

#Pendientes de todas las rectas a dibujar
for y in Ys:
    pend=pendiente(-250.,y)
    pendientes.append(pend)

for x in Xs:
    pend=pendiente(x,-250)
    pendientes.append(pend)

#intersecciones con el circulo interior
xpos=[]
ypos=[]

for p in pendientes:
    x=-r/sqrt(1+p**2)
    y=p*x
    xpos.append(x)
    ypos.append(y)


setup(1000, 1000, 0, 0)

#ir a esquina superior izuqierda
pu()
goto(-250,250)
pd()
#hacer cuadrado
goto(-250,-250)
goto(250,-250)
goto(250,250)
goto(-250,250)
pu()

#Hacer circulo
goto(0,-110)
pd()
circle(110)
pu()

n=len(Ys)
m=len(Xs)
#Comienzo recorrido

for i in range(n):
    goto(-250,Ys[i])
    pd()
    goto(xpos[i],ypos[i])
    pu()

for i in range(m):
    goto(Xs[i],-250)
    pd()
    goto(xpos[i+n],ypos[i+n])
    pu()

goto(0,-250)
pd()
goto(0,-r)
pu()

for i in range(m):
    goto(-Xs[m-1-i],-250)
    pd()
    goto(-xpos[m+n-i-1],ypos[m+n-i-1])
    pu()

for i in range(n):
    goto(250,Ys[n-1-i])
    pd()
    goto(-xpos[n-i-1],ypos[n-i-1])
    pu()

goto(0,250)
pd()
goto(0,r)
pu()
goto(0,0)

showturtle()
done()
