import turtle             # nos permite usar as tartarugas (turtles)

jn = turtle.Screen()      # Abre uma janela onde as tartarugas vão caminhar
jn.bgcolor(input('Coloque a cor da janela ''\n'))      # Definir a cor de fundo da janela
joana = turtle.Turtle()    # Cria uma tartaruga, atribui a joana

cores= ['yellow','red','blue','purple']

for i in [0,1,2,3]:
	joana.color(cores[i])
	joana.forward(50)
	joana.left(90)        
