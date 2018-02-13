#Name T Naga Datta Madhu Kiran
#ID 2015A7PS0111P


import turtle
from turtle import *

var_list=[]
dimension={}
flags={}
def draw_template(l):
	global var_list
	global flags
	var_list+=sorted(l)+["~"+str(i) for i in l]
	for i in var_list:
		flags[i[-1]]=0
	t=Turtle()
	t.speed(0)
	t.hideturtle()

	draw_outer(t)
	
	xshift=200

	draw_box(t,"lightblue","Query Variables",-350-xshift,270,170)
	draw_box(t,"lightblue","Conditional Variables",-80,270,250)
	draw_allbutton(t,l)
	draw_box(t,"lightgreen","Generated Query is                                                                                ",-300-xshift,-220,750)
	draw_box(t,"lightgreen","Answer  =                                                                                         ",-300-xshift,-250,750)	
	draw_box(t,"red","Generate",270,-250,120)




def draw_outer(t):
	turtle.setup(1200,700)
	t.pensize(4)
	t.color("black",)
	t.penup() 
	t.goto(-590,340)	
	t.pendown()
	t.goto(590,340)
	t.goto(590,-300)
	t.goto(-590,-300)
	t.goto(-590,340)

def draw_allbutton(t,l):
	xshift=200
	l.sort()
	x_gap=100
	y_gap=30
	for num,i in enumerate(l):
		draw_button(t,str(i),-350-xshift,240-num*y_gap,"q")
		draw_button(t,"~"+str(i),-350+x_gap-xshift,240-num*y_gap,"q")
	for num,i in enumerate(l):
		draw_button(t,str(i),-50,240-num*y_gap,"c")
		draw_button(t,"~"+str(i),-30+x_gap,240-num*y_gap,"c")
	pass

def draw_button(t,letter,x,y,flag):
	global dimension
	length=70
	width=25
	dimension[(letter,flag)]=(x,x+length,y,y-width)
	t.pensize(2)
	t.color("grey","lightgreen")
	t.penup()
	t.goto(x,y)	
	t.pendown()
	t.fill("True")
	t.goto(x+length,y)
	t.goto(x+length,y-width)
	t.goto(x,y-width)
	t.goto(x,y)
	t.fill(False)
	t.penup()
	t.color("black")
	t.goto(x+length/2,y-width)
	t.write(letter,True,align ="center",font=("Arial",16,"bold"))

def draw_box(t,color,string,x,y,length,penc="grey"):

	t.speed(0)
	t.hideturtle()
	width=25
	t.pensize(2)
	t.color(penc,color)
	t.penup()
	t.goto(x,y)	
	t.pendown()
	t.fill(True)
	t.goto(x+length,y)
	t.goto(x+length,y-width)
	t.goto(x,y-width)
	t.goto(x,y)
	t.fill(False)
	t.penup()
	t.color("black")
	t.goto(x+length/2,y-width)
	t.write(string,True,align ="center",font=("Arial",16,"bold"))

# draw_template([chr(i) for i in range(65,65+15)])

def check_fill(x,y,letter,t):
	global dimension
	global flags
	# print dimension
	a=dimension[(letter,t)]
	if flags[letter[-1]]==1:
		return False
	if x >=a[0] and x <=a[1] and y<=a[2] and y>=a[3]:
		fill_yellow(letter,t)
		flags[letter[-1]]=1
		return True
	else:
		return False

def fill_yellow(letter,ty):
	global dimension
	a=dimension[(letter,ty)]
	x=a[0]
	y=a[2]
	length=abs(a[1]-a[0])
	width=abs(a[2]-a[3])
	t=Turtle()
	t.speed(0)
	t.hideturtle()
	t.pensize(2)
	t.color("grey","yellow")
	t.penup()
	t.goto(x,y)	
	t.pendown()
	t.fill("True")
	t.goto(x+length,y)
	t.goto(x+length,y-width)
	t.goto(x,y-width)
	t.goto(x,y)
	t.fill(False)
	t.penup()
	t.color("black")
	t.goto(x+length/2,y-width)
	t.write(letter,True,align ="center",font=("Arial",16,"bold"))

def fill_green(letter,ty):
	global dimension
	a=dimension[(letter,ty)]
	x=a[0]
	y=a[2]
	length=abs(a[1]-a[0])
	width=abs(a[2]-a[3])
	t=Turtle()
	t.speed(0)
	t.hideturtle()
	t.pensize(2)
	t.color("grey","lightgreen")
	t.penup()
	t.goto(x,y)	
	t.pendown()
	t.fill("True")
	t.goto(x+length,y)
	t.goto(x+length,y-width)
	t.goto(x,y-width)
	t.goto(x,y)
	t.fill(False)
	t.penup()
	t.color("black")
	t.goto(x+length/2,y-width)
	t.write(letter,True,align ="center",font=("Arial",16,"bold"))

def write_ans(ans):
	xshift=200
	t=Turtle()
	t.speed(0)
	t.hideturtle()
	t.penup()
	t.color("black")
	t.goto(-50-xshift,-275)
	t.write(ans,True,align ="left",font=("Arial",16,"bold"))

def refresh(lis):
	for i in ['q','c']:
		for j in lis:
			fill_green(j,i)
	return

def write_gen_query(Query_List,Conditional_List):
	xshift=200
	a="P("
	for i in Query_List[:-1]:
		a+=i
		a+=","
	a+=Query_List[-1]
	if len(Conditional_List)>=1:
		a+="|"
		for i in Conditional_List[:-1]:
			a+=i
			a+=","
		a+=Conditional_List[-1]
	a+=")"
	t=Turtle()
	t.speed(0)
	t.hideturtle()
	t.penup()
	t.pensize(2)
	t.color("black")
	t.goto(-50-xshift,-245)
	t.write(a,True,align ="left",font=("Arial",16,"bold"))
def write_string(z,x,y,header=0):
	t=Turtle()
	t.speed(0)
	t.hideturtle()
	t.penup()
	t.goto(x,y)
	if header==0:
		t.write("=>"+str(z),True,align ="left",font=("Arial",8,"bold"))
	else:
		t.write(str(z),True,align ="left",font=("Arial",8,"bold"))

def clear_mar_quer():
	t=Turtle()
	t.speed(0)
	t.hideturtle()
	t.penup()
	t.goto(-375,270)
	t.color("white","white")
	t.pendown()
	t.fill(True)
	t.goto(-90,270)
	t.goto(-90,-210)
	t.goto(-375,-210)
	t.goto(-375,270)
	t.fill(False)	

def clear_mar_cond():
	t=Turtle()
	t.speed(0)
	t.hideturtle()
	t.penup()
	t.goto(180,270)
	t.color("white","white")
	t.pendown()
	t.fill(True)
	t.goto(500,270)
	t.goto(500,-210)
	t.goto(180,-210)
	t.goto(180,270)
	t.fill(False)	

# draw_box(Turtle(),"lightgreen","Generated Query-                                             ",-300,-220,450)
# write_gen_query(["A","B","B","B","B","B","B","B","B","B"],["A","B","B","B","B","B","B","B","B","B"])
# write_ans(1.00005600000010001000)
# turtle.mainloop()