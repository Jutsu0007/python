#espiral1.py

import turtle
p=turtle.Pen()
p.speed(50)

turtle.bgcolor("black")
cores=["red","yellow","blue","green","orange","purple"]
lados=int(turtle.numinput("escolha entre 2 e 6", "Numero de dados"))
for x in range(1000):
    resto= x % 4 #devolve 0,1,2 ou 3
    cor=cores[resto]
    p.pencolor(cor)
    p.forward(x*5)
    p.left(360/(lados+1))
    p.width(x*lados/200)        
    
