from function import H_move,printgrid,ACTIONS,Result,Successor_function,Utility,Terminal_test,Min_value,Max_value,minimax_algorithm,alpha_beta_minimax_algorithm
import sys
from gui import drawgui
from turtle import *
import turtle
from Analyses import Option,print_analyses,Analyses_Module,precomputed
import time

def main():
	analyses_obj=Analyses_Module()
	option=0
	option=int(raw_input("Enter option:"))
	Option.opt=option
	if(option==1):
		t=Turtle()
		t.hideturtle()
		drawgui(t)
		turtle.mainloop()
		return
	if(option==2):

		Analyses_Module.start_time=time.clock()


		t=Turtle()
		t.hideturtle()
		drawgui(t)
		state=[[-1 for i in range(4)] for j in range(4)]
		Analyses_Module.R2=sys.getsizeof(state)
		h=H_move()
		H_move.h=h
		drawgui(t)
		H_move.state=minimax_algorithm(state,h)
		turtle.mainloop()

		
		return

	if option==3:

		Analyses_Module.start_time=time.clock()
		
		t=Turtle()
		t.hideturtle()
		drawgui(t)
		state=[[-1 for i in range(4)] for j in range(4)]
		Analyses_Module.R2=sys.getsizeof(state)
		h=H_move()
		H_move.h=h
		drawgui(t)
		H_move.state=alpha_beta_minimax_algorithm(state,h)
		turtle.mainloop()

		
		return

	if option==4:
		t=Turtle()
		t.hideturtle()
		drawgui(t)
		precomputed()
		analyses_obj.pre_computed_values()
		turtle.mainloop()
		return
	
main()