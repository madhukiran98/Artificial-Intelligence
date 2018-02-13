from copy import *
import sys
from gui import draw4_4,rub_top_bottom,base_line,drawcircle,printcoor,print_message,bottom_screen,rub_top_bottom,base_line
import thread
import time
import turtle
from turtle import *
import random as rand
from Analyses import Option,Analyses_Module

sys.setrecursionlimit(40000)

analyses_obj=Analyses_Module()

def printgrid(state):
	print("-----------------------------")
	for i in range(4):
		for j in range(4):
			sys.stdout.write(str(state[i][j])+" ")
		print(" ")
	print("-----------------------------")

#probabilistic

def ACTIONS(state):
	# printgrid(state)
	a=[]
	for j in range(4):
		for i in range(4):
			if(state[i][j]==-1):
				a.append([i,j])
				break
	# print(a)
	b=[]
	while(len(a)!=0):
		z=rand.randint(0,len(a)-1)
		b.append(a[z])
		a.pop(z)
	return b

#deterministic

# def ACTIONS(state):
# 	# printgrid(state)
# 	a=[]
# 	for j in range(4):
# 		for i in range(4):
# 			if(state[i][j]==-1):
# 				a.append([i,j])
# 				break
# 	# print(a)
# 	return a

def Result(state,a,turn):
	# printgrid(state)
	Analyses_Module.R1+=1
	Analyses_Module.R6+=1
	new_state=[[state[i][j] for j in range(4)] for i in range(4)]
	new_state[a[0]][a[1]]=turn
	# printgrid(new_state)
	return new_state

def Alpha_Beta_Successor_function(state):
	# print("ab_succ")
	alpha=-sys.maxint-1
	beta=sys.maxint
	max_value=-sys.maxint-1
	max_action=[]
	v=0
	# printgrid(state)
	acts=ACTIONS(state)
	# print(acts)
	for a in acts:
		v=AB_Min_value(Result(state,a,1),alpha,beta,a)
		# print("here")
		if(v > max_value):
			max_action=a
			max_value=v
		alpha=max(alpha,v)
	return max_action

def Successor_function(state):
	max_action=[]
	max_value=-sys.maxint-1
	v=0
	# printgrid(state)
	acts=ACTIONS(state)
	# print(acts)
	for a in acts:
		v=Min_value(Result(state,a,1),a)
		# print("here")
		if(v > max_value):
			max_action=a
			max_value=v

	return max_action

def Utility(state,a,turn):
	i=a[0]
	j=a[1]
	if(i!=0 and j!=0 and i!=3 and j!=3):
		if (state[i][j+1]==turn and state[i][j-1]==turn or 
		state[i+1][j]==turn and state[i-1][j]==turn  or
		state[i+1][j+1]==turn and state[i-1][j-1]==turn or
		state[i-1][j+1]==turn and state[i+1][j-1]==turn ):
			if(turn == 1):
				return 1
			if(turn==2):
				return -1
		if(i==1 and j==1):
			if(state[2][2]==turn and state[3][3]==turn or
				state[1][2]==turn and state[1][3]==turn or
				state[2][1]==turn and state[3][1]==turn):
				if(turn == 1):
					return 1
				elif(turn==2):
					return -1
		if(i==2 and j==2):
			if(state[0][0]==turn and state[1][1]==turn or
				state[2][0]==turn and state[2][1]==turn or
				state[1][2]==turn and state[0][2]==turn):
				if(turn == 1):
					return 1
				elif(turn==2):
					return -1
		if(i==1 and j==2):
			if(state[2][1]==turn and state[3][0]==turn or
				state[1][0]==turn and state[1][1]==turn or
				state[2][2]==turn and state[3][2]==turn):
				if(turn == 1):
					return 1
				elif(turn==2):
					return -1
		if(i==2 and j==1):
			if(state[0][3]==turn and state[1][2]==turn or
				state[1][1]==turn and state[0][1]==turn or
				state[2][3]==turn and state[2][2]==turn):
				if(turn == 1):
					return 1
				elif(turn==2):
					return -1
	if(i==0):
		if(j==0):
			if( state[1][0]==turn and state[2][0]==turn or
				state[0][1]==turn and state[0][2]==turn or
				state[1][1]==turn and state[2][2]==turn ):
				if(turn==1):
					return 1
				elif(turn==2):
					return -1
		if(j==3):
			if( state[1][3]==turn and state[2][3]==turn or
				state[0][1]==turn and state[0][2]==turn or
				state[1][2]==turn and state[2][1]==turn ):
				if(turn==1):
					return 1
				elif(turn==2):
					return -1
	if(i==3):
		if(j==0):
			if( state[1][0]==turn and state[2][0]==turn or
				state[3][1]==turn and state[3][2]==turn or
				state[1][2]==turn and state[2][1]==turn ):
				if(turn==1):
					return 1
				elif(turn==2):
					return -1
		if(j==3):
			if( state[1][3]==turn and state[2][3]==turn or
				state[3][1]==turn and state[3][2]==turn or
				state[1][1]==turn and state[2][2]==turn ):
				if(turn==1):
					return 1
				elif(turn==2):
					return -1
	if(i==0):
		if(j==1 or j==2):
			if(state[0][j-1]==turn and state[0][j+1]==turn or
				state[1][j]==turn and state[2][j]==turn):
				if(turn==1):
					return 1
				elif(turn==2):
					return -1
			if(j==1):
				if(state[1][2]==turn and state[2][3]==turn or
					state[0][2]==turn and state[0][3]==turn):
					if(turn==1):
						return 1
					elif(turn==2):
						return -1
			if(j==2):
				if(state[1][1]==turn and state[2][0]==turn or
					state[0][0]==turn and state[0][1]==turn):
					if(turn==1):
						return 1
					elif(turn==2):
						return -1
	if(i==3):
		if(j==1 or j==2):
			if(state[3][j-1]==turn and state[3][j+1]==turn or
				state[1][j]==turn and state[2][j]==turn):
				if(turn==1):
					return 1
				elif(turn==2):
					return -1
			if(j==1):
				if(state[2][2]==turn and state[1][3]==turn or 
					state[3][2]==turn and state[3][3]==turn):
					if(turn==1):
						return 1
					elif(turn==2):
						return -1
			if(j==2):
				if(state[1][0]==turn and state[2][1]==turn or
					state[3][0]==turn and state[3][1]==turn):
					if(turn==1):
						return 1
					elif(turn==2):
						return -1
	if(j==0):
		if(i==1 or i==2):
			if(state[i-1][0]==turn and state[i+1][0]==turn or
				state[i][1]==turn and state[i][2]==turn):
				if(turn==1):
					return 1
				elif(turn==2):
					return -1
			if(i==1):
				if(state[2][1]==turn and state[3][2]==turn or
					state[2][0]==turn and state[3][0]==turn):
					if(turn==1):
						return 1
					elif(turn==2):
						return -1
			if(i==2):
				if(state[1][1]==turn and state[0][2]==turn or
					state[0][0]==turn and state[1][0]==turn):
					if(turn==1):
						return 1
					elif(turn==2):
						return -1
	if(j==3):
		if(i==1 or i==2):
			if(state[i-1][3]==turn and state[i+1][3]==turn or
				state[i][1]==turn and state[i][2]==turn):
				if(turn==1):
					return 1
				elif(turn==2):
					return -1
			if(i==1):
				if(state[2][2]==turn and state[3][1]==turn or
					state[2][3]==turn and state[3][3]==turn):
					if(turn==1):
						return 1
					elif(turn==2):
						return -1
			if(i==2):
				if(state[0][1]==turn and state[1][2]==turn or
					state[0][3]==turn and state[1][3]==turn):
					if(turn==1):
						return 1
					elif(turn==2):
						return -1
	return 0
def Terminal_test(state,a,turn):
	u=Utility(state,a,turn)
	if(u!=0):
		return True
	else:
		for i in range(4):
			for j in range(4):
				if(state[i][j]==-1):
					return False
		return True
r3=0
def Min_value(state,a):
	# printgrid(state)
	global r3
	r3+=1
	if(Terminal_test(state,a,1)):
		# print("------------''''''''''''''''''''''''''''''''''''''''''''''''-----------------'''''''''''----------")
		# printgrid(state)
		# print(a,1)
		if(r3>Analyses_Module.R3):
			Analyses_Module.R3=r3
		r3=0
		z=Utility(state,a,1)
		# print("min = ",z)
		return z
	v=sys.maxint
	acts=ACTIONS(state)
	for i,a in enumerate(acts):
		# print(i)
		v=min(v,Max_value(Result(state,a,2),a))
		# if(v==1):
		# 	print(i)
	return v

def AB_Min_value(state,alpha,beta,a):
	# print("ab_min")
	# printgrid(state)
	global r3
	r3+=1
	if(Terminal_test(state,a,1)):
		# print("------------''''''''''''''''''''''''''''''''''''''''''''''''-----------------'''''''''''----------")
		# printgrid(state)
		# print(a,1)
		if(r3>Analyses_Module.R3):
			Analyses_Module.R3=r3
		r3=0
		z=Utility(state,a,1)
		# print("min = ",z)
		return z
	v=sys.maxint
	acts=ACTIONS(state)
	for i,a in enumerate(acts):
		# print(i)
		v=min(v,AB_Max_value(Result(state,a,2),alpha,beta,a))
		if(v <=alpha):
			return v
		beta=min(beta,v)
		# if(v==1):
		# 	print(i)
	return v

def Max_value(state,a):
	# printgrid(state)
	global r3
	r3+=1
	if(Terminal_test(state,a,2)):
		# printgrid(state)
		# print(a,2)
		if(r3>Analyses_Module.R3):
			Analyses_Module.R3=r3
		r3=0
		z=Utility(state,a,2)
		# print("max = ",z)
		return z
	v=-1*sys.maxint-1
	acts=ACTIONS(state)
	for a in acts:
		v=max(v,Min_value(Result(state,a,1),a))
	return v

def AB_Max_value(state,alpha,beta,a):
	# print("ab_max")

	# printgrid(state)
	global r3
	r3+=1
	if(Terminal_test(state,a,2)):
		# printgrid(state)
		# print(a,2)
		if(r3>Analyses_Module.R3):
			Analyses_Module.R3=r3
		r3=0
		z=Utility(state,a,2)
		# print("max = ",z)
		return z
	v=-1*sys.maxint-1
	acts=ACTIONS(state)
	for a in acts:
		v=max(v,AB_Min_value(Result(state,a,1),alpha,beta,a))
		if v >=beta:
			return v
		alpha=max(alpha,v)
	return v

def get_gui_coor(x,y):
	dic={(0,0):[0,1],(0,1):[1,1],(0,2):[2,1],(0,3):[3,1],
	     (1,0):[0,0],(1,1):[1,0],(1,2):[2,0],(1,3):[3,0],
	     (2,0):[0,-1],(2,1):[1,-1],(2,2):[2,-1],(2,3):[3,-1],
	     (3,0):[0,-2],(3,1):[1,-2],(3,2):[2,-2],(3,3):[3,-2],}
	return dic[(x,y)]

def get_real_coor(x,y):
 	dic={(0,1):[0,0],(1,1):[0,1],(2,1):[0,2],(3,1):[0,3],
	     (0,0):[1,0],(1,0):[1,1],(2,0):[1,2],(3,0):[1,3],
	     (0,-1):[2,0],(1,-1):[2,1],(2,-1):[2,2],(3,-1):[2,3],
	     (0,-2):[3,0],(1,-2):[3,1],(2,-2):[3,2],(3,-2):[3,3],}
	return dic[(x,y)]


li=[]

def minimax_algorithm(state,h):
	initial_pos=[[0,0],[0,1],[0,2],[0,3]]
	global li
	# a=Successor_function(state)
	screen=turtle.Screen()
	screen.onclick(standstill)
	a=initial_pos[rand.randint(0,len(initial_pos)-1)]
	state[a[0]][a[1]]=1
	li.append(get_gui_coor(a[0],a[1]))
	x,y=get_gui_coor(a[0],a[1])
	drawcircle(x,y,"black","green")
	if(Terminal_test(state,a,1)):
		option_exit()
	screen=turtle.Screen()
	screen.onclick(h.print_coor)
	return state

# def alpha_beta_minimax_algorithm(state,h):
# 	initial_pos=[[0,0],[0,1],[0,2],[0,3]]
# 	global li
# 	# a=Successor_function(state)
# 	screen=turtle.Screen()
# 	screen.onclick(standstill)
# 	a=initial_pos[rand.randint(0,len(initial_pos)-1)]
# 	state[a[0]][a[1]]=1
# 	li.append(get_gui_coor(a[0],a[1]))
# 	x,y=get_gui_coor(a[0],a[1])
# 	drawcircle(x,y,"black","green")
# 	if(Terminal_test(state,a,1)):
# 		option_exit()
# 	screen=turtle.Screen()
# 	screen.onclick(h.print_coor)
# 	return state


def alpha_beta_minimax_algorithm(state,h):
	screen=turtle.Screen()
	screen.onclick(standstill)
	a=Alpha_Beta_Successor_function(state)
	state[a[0]][a[1]]=1
	li.append(get_gui_coor(a[0],a[1]))
	x,y=get_gui_coor(a[0],a[1])
	drawcircle(x,y,"black","green")
	if(Terminal_test(state,a,1)):
		option_exit()
	screen=turtle.Screen()
	screen.onclick(h.print_coor)
	return state

# def minimax_algorithm(state,h):
# 	screen=turtle.Screen()
# 	screen.onclick(standstill)
# 	a=Successor_function(state)
# 	state[a[0]][a[1]]=1
# 	li.append(get_gui_coor(a[0],a[1]))
# 	x,y=get_gui_coor(a[0],a[1])
# 	drawcircle(x,y,"black","green")
# 	if(Terminal_test(state,a,1)):
# 		option_exit()
# 	screen=turtle.Screen()
# 	screen.onclick(h.print_coor)
# 	return state

class H_move:
	state=None
	Hx=0
	Hy=0
	h=None
	def __init(self):
		pass
	def print_coor(self,x,y):
		global li
		# print("original coordinates are ",x,y)
		x=x//100
		y=y//100	
		if([x,y] in li):
			return
		if(x not in [0,1,2,3] or y not in [-2,-1,0,1]):
			return
		H_move.Hx=x
		H_move.Hy=y
		li.append([x,y])
		drawcircle(x,y,"black","blue")
		a=get_real_coor(H_move.Hx,H_move.Hy)
		H_move.state[a[0]][a[1]]=2
		# printgrid(H_move.state)
		if(Terminal_test(H_move.state,a,2)):
			screen=turtle.Screen()
			screen.onclick(do_nothing)
			prompt(2)
			return
		screen=turtle.Screen()
		screen.onclick(standstill)
		if Option.opt ==2:
			a=Successor_function(H_move.state)
			analyses_obj.write_minimax_fgame()
		elif Option.opt ==3:
			a=Alpha_Beta_Successor_function(H_move.state)
			analyses_obj.write_r6()
		H_move.state[a[0]][a[1]]=1
		# printgrid(H_move.state)
		x,y=get_gui_coor(a[0],a[1])
		li.append(get_gui_coor(a[0],a[1]))
		drawcircle(x,y,"black","green")
		if(Terminal_test(H_move.state,a,1)):
			screen=turtle.Screen()
			screen.onclick(do_nothing)
			prompt(1)
			return
		screen=turtle.Screen()
		screen.onclick(H_move.h.print_coor)

def ask_option(x,y):
	print("ask_option")
	pass

def decide(x,y):
	if(x>-45 and x <200 and y>-295 and y<-250):
		option_newgame()
	elif(x>225 and x <450 and y>-295 and y<-250):
		option_exit()


def do_nothing(x,y):
	pass	

def standstill(x,y):
	print("Machine is Thinking !!")

def prompt(turn):
	if turn==1:
		message= "Machine Won!"
		print("Machine Won!")
		Analyses_Module.end_time=time.clock()
		if Option.opt==2:
			Analyses_Module.R4=Analyses_Module.end_time-Analyses_Module.start_time
			Analyses_Module.R5=Analyses_Module.R1/(Analyses_Module.R4*1000000)
			analyses_obj.write_minimax()
			Analyses_Module.start_time=time.clock()
			Analyses_Module.R1=0
		if Option.opt==3:
			Analyses_Module.end_time=time.clock()
			Analyses_Module.R8=Analyses_Module.end_time-Analyses_Module.start_time
			Analyses_Module.R7=float(float(503589-Analyses_Module.R6)/float(503589))
			analyses_obj.write_AB()
			Analyses_Module.start_time=time.clock()
			Analyses_Module.R6=0
	else:
		message= "You won!"
		print ("You won!")
	print_message(message)
	choice=bottom_screen()
	screen=turtle.Screen()
	screen.onclick(decide)
	# print("here")

def option_exit():
	print("exited")
	turtle.bye()

def option_newgame():
	rub_top_bottom()
	base_line()

	global li
	for i in li:
		x,y=i
		drawcircle(x,y,"white","white")
	draw4_4()
	li=[]
	state=[[-1 for i in range(4)] for j in range(4)]
	h=H_move()
	H_move.h=h
	if Option.opt ==2:
		analyses_obj.clear_minimax()
		H_move.state=minimax_algorithm(state,h)
	elif Option.opt ==3:
		analyses_obj.clear_AB()
		Analyses_Module.R6=0
		H_move.state=alpha_beta_minimax_algorithm(state,h)