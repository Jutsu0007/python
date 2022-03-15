 
#textos.py


import turtle
turtle.bgcolor("black")
p=turtle.Pen()

#        0      1       2       3       4        5         6       7       8      9
cores=["red","yellow","blue","green","orange","purple","white","brown","gray","pink"]

#              0        1         2          3        4          5         6         7          8        9
animais = ["cachorro","gato,","calopsita","coelho","passaro","elefante","camelo","tartaruga","jacarè","cavalo"]

for x in range(100):
    p.penup()
    p.forward(x*3)
    resto=x%len(animais)
    p.pencolor(cores[resto])
    animal=animais[resto] #0 a 9
    p.write(animal,font=("arial",int(x*0.6),'bold'))
    p.left(360/(len(animais)+2))
