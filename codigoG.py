from math import *



######### Seteo ############
E=0
F1=381.198
zstep = 0.2
z = 10.0
a=1
da=.01
r=11

r=110 #Radio del circulo
Ys=[250.,125.,0.,-250./3.,-500./3.,-250.]
Xs=[-750./4,-125.,-250./4]
pendientes=[]


gcode=open('gcode.txt','w')

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

######## fin de seteo ##########

layers = z/zstep

n=len(Ys)
m=len(Xs)

for i in range(int(layers)):
    z=+i*zstep
    gcode.write('G0 X0 Y0 Z'+str(z)+' F381.198'+'\n')
    gcode.write('G0 X-25 Y25 Z'+str(z)+' F381.198'+'\n')
    E=E+a*50
    gcode.write('G1 X25 Y25 Z'+str(z)+' F381.198'+' E'+str(E)+'\n')
    E=E+a*50
    gcode.write('G1 X25 Y-25 Z'+str(z)+' F381.198'+' E'+str(E)+'\n')
    E=E+a*50
    gcode.write('G1 X-25 Y-25 Z'+str(z)+' F381.198'+' E'+str(E)+'\n')
    E=E+a*50
    gcode.write('G1 X-25 Y25 Z'+str(z)+' F381.198'+' E'+str(E)+'\n')
    gcode.write('G0 X11 Y0 Z'+str(z)+' F381.198'+'\n')

    for angle in range(0,2*pi,da):
        x=r*cos(angle)
        y=r*cos(angle)
        E=a*(E+r*da)
        gcode.write('G1 X'+str(x)+' Y'+str(y)+' Z'+str(z)+' F'+str(F1)+' E'+str(E)+'\n')

   





