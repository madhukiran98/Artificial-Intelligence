import turtle
from turtle import *
from Analyses import Option,Analyses_Module



def print_message(message):
	t=Turtle()
	t.hideturtle()
	t.speed(0)
	t.color("black","white")
	t.penup()
	t.goto(-100,300)
	t.fill(True)
	t.begin_fill()
	t.pendown()
	t.goto(500,300)
	t.goto(500,200)
	t.penup()
	t.goto(400,200)
	pendown()
	t.goto(0,200)
	t.penup()
	t.goto(-100,200)
	t.pendown()
	t.goto(-100,300)
	t.end_fill()
	t.penup()
	t.goto(200,225)
	t.write(message,"True",align="center",font=("Arial",32,"bold"))




def bottom_screen():
	t=Turtle()
	t.hideturtle()
	t.speed(0)
	t.color("black","cyan")
	t.penup()
	t.goto(-45,-250)
	t.pendown()
	t.fill(True)
	t.begin_fill()
	t.goto(200,-250)
	t.goto(200,-295)
	t.goto(-45,-295)
	t.goto(-45,-250)
	t.end_fill()
	t.penup()
	t.goto(75,-290)
	t.pensize(5)
	t.color("red")
	t.penup()
	t.write("Newgame",True,align="center",font=("Arial",20,"bold"))

	t.pensize(0)
	t.color("black","cyan")
	t.penup()
	t.goto(255,-250)
	t.pendown()
	t.fill(True)
	t.begin_fill()
	t.goto(450,-250)
	t.goto(450,-295)
	t.goto(255,-295)
	t.goto(255,-250)
	t.end_fill()
	t.penup()
	t.goto(350,-290)
	t.pensize(5)
	t.color("red")
	t.penup()
	t.write("Exit",True,align="center",font=("Arial",20,"bold"))




def drawcircle(x,y,bor,col):
	t=Turtle()
	t.speed(0)
	t.penup()
	t.hideturtle()
	t.color(bor,col)
	x=x*100+50
	y=y*100
	t.goto(x,y)
	# print(x,y)
	t.pendown()
	t.fill(True)
	t.circle(50)
	t.fill(False)
	t.pendown()

def base_line():
	t=Turtle()
	t.speed(0)
	t.penup()
	t.hideturtle()
	t.penup()
	t.goto(0,250)
	t.pensize(10)
	t.color("red")
	t.pendown()
	t.goto(400,250)
	t.penup()
	t.color("grey")
	t.goto(190,275)
	t.write("BASE LINE",True,align="center",font=("Arial",14,"bold"))

def rub_top_bottom():
	t=Turtle()
	t.hideturtle()
	t.speed(0)
	t.color("black","white")
	t.penup()
	t.goto(-100,300)
	t.fill(True)
	t.begin_fill()
	t.pendown()
	t.goto(500,300)
	t.goto(500,200)
	t.penup()
	t.goto(400,200)
	pendown()
	t.goto(0,200)
	t.penup()
	t.goto(-100,200)
	t.pendown()
	t.goto(-100,300)
	t.end_fill()

	t.color("white","white")
	t.penup()
	t.goto(-45,-250)
	t.pendown()
	t.fill(True)
	t.begin_fill()
	t.goto(200,-250)
	t.goto(200,-295)
	t.goto(-45,-295)
	t.goto(-45,-250)
	t.end_fill()

	t.penup()
	t.goto(255,-250)
	t.pendown()
	t.fill(True)
	t.begin_fill()
	t.goto(450,-250)
	t.goto(450,-295)
	t.goto(255,-295)
	t.goto(255,-250)
	t.end_fill()
	t.penup()
	t.goto(350,-290)



def write_e_text():
	t=Turtle()
	t.speed(0)
	t.penup()
	t.hideturtle()
	for i in range(12):
		t.penup()
		t.goto(-460,270-i*600/12)
		t.write("R"+str(i+1)+" =",True,align="center",font=("Arial", 12,"italic") )
		t.pendown()
	
	base_line()
	
	t.color("black")
	for i in range(4):
		t.penup()
		t.goto(-35,135-i*400/4)
		t.write("R"+str(i+1),True,align="center",font=("Arial", 12,"bold") )
		t.pendown()
	for i in range(4):
		t.penup()
		t.goto(50+i*100,-235)
		t.write("C"+str(i+1),True,align="center",font=("Arial", 12,"bold") )
		t.pendown()

def printcoor(x,y):
	# print("original coordinates are ",x,y)
	x=x//100
	y=y//100
	# print("coordinates are ",x,y)
	if(x not in [0,1,2,3] or y not in [-2,-1,0,1]):
		return
	drawcircle(x,y,"black","blue")


def draw4_4():
	t=Turtle()
	t.speed(0)
	t.penup()
	t.hideturtle()
	
	for i in range(5):
		t.penup()
		t.goto(i*100,200)
		t.pendown()
		t.goto(i*100,-200)

	for i in range(5):
		t.penup()
		t.goto(0,i*100-200)
		t.pendown()
		t.goto(400,i*100-200)

def drawempty():
	t=Turtle()
	t.speed(0)
	t.penup()
	t.hideturtle()
	t.goto(-500,300)
	t.pendown()
	t.goto(500,300)
	t.goto(500,-300)
	t.goto(-500,-300)
	t.goto(-500,300)
	t.goto(-100,300)
	t.goto(-100,-300)
	draw4_4()
	write_e_text()



def drawgui(t):
	
	turtle.setup(1100,650)
	turtle.title("align3")
	t.pendown()
	drawempty()
	



