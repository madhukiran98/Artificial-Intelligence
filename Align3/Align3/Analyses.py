from turtle import *
import turtle
class Option:
	opt=0

def print_analyses():
	print "printed analyses"
	print Analyses_Module.R1
	print Analyses_Module.R2
	print Analyses_Module.R3
	print Analyses_Module.R4
	print Analyses_Module.R5
	print Analyses_Module.R6
	print Analyses_Module.R7
	print Analyses_Module.R8
	print Analyses_Module.R9
	print Analyses_Module.R10
	print Analyses_Module.R11
	print Analyses_Module.R12

def precomputed():
	Analyses_Module.R1=503589
	Analyses_Module.R2=104
	Analyses_Module.R3=16
	Analyses_Module.R4=4.872414
	Analyses_Module.R5=0.1300452379
	Analyses_Module.R6=19519
	Analyses_Module.R7=float(float(503589-19519)/float(503589))
	Analyses_Module.R8=0.489393
	Analyses_Module.R9="In Minimax  "+str(503589*104)+"Bytes"+"\n"+"In Alpha-Beta "+str(19519*104)+"Bytes"
	Analyses_Module.R10=4.977
	Analyses_Module.R11="10 wins for Machine"
	Analyses_Module.R12="(Average)10 wins for Machine"


class Analyses_Module:
	R1=0
	R2=0
	R3=0
	R4=0
	R5=0
	R6=0
	R7=0
	R8=0
	R9=0
	R10=0
	R11=0
	R12=0
	start_time=0
	end_time=0
	r1_tur=None
	r2_tur=None
	r3_tur=None
	r4_tur=None
	r5_tur=None
	r6_tur=None
	r7_tur=None
	r8_tur=None
	r9_tur=None
	r10_tur=None
	r11_tur=None
	r12_tur=None

	def pre_computed_values(self):
		self.write_r1()
		self.write_r2()
		self.write_r3()
		self.write_r4()
		self.write_r5()
		self.write_r6()
		self.write_r7()
		self.write_r8()
		self.write_r9()
		self.write_r10()
		self.write_r11()
		self.write_r12()


	def clear_minimax(self):
		Analyses_Module.r1_tur.clear()
		Analyses_Module.r2_tur.clear()
		Analyses_Module.r3_tur.clear()
		Analyses_Module.r4_tur.clear()
		Analyses_Module.r5_tur.clear()

	def clear_AB(self):
		Analyses_Module.r6_tur.clear()
		Analyses_Module.r7_tur.clear()
		Analyses_Module.r8_tur.clear()

	def write_minimax_fgame(self):
		self.write_r1()
		self.write_r2()
		self.write_r3()

	def write_minimax(self):
		self.write_r1()
		self.write_r2()
		self.write_r3()
		self.write_r4()
		self.write_r5()

	def write_AB(self):
		self.write_r6()
		self.write_r7()
		self.write_r8()

	def write_r1(self):
		if(Analyses_Module.r1_tur!=None):
			Analyses_Module.r1_tur.clear()
		t=Turtle()
		t.hideturtle()
		t.speed(0)
		t.pensize(2)
		t.penup()
		t.goto(-275,270-0*600/12)
		t.write(str(Analyses_Module.R1)+" Nodes",True,align ="center",font=("Arial",12,"bold"))
		Analyses_Module.r1_tur=t
		pass
	def write_r2(self):
		if(Analyses_Module.r2_tur!=None):
			Analyses_Module.r2_tur.clear()
		t=Turtle()
		t.hideturtle()
		t.speed(0)
		t.pensize(2)
		t.penup()
		t.goto(-275,270-1*600/12)
		t.write(str(Analyses_Module.R2)+" Bytes",True,align ="center",font=("Arial",12,"bold"))
		Analyses_Module.r2_tur=t		
		pass
	def write_r3(self):
		if(Analyses_Module.r3_tur!=None):
			Analyses_Module.r3_tur.clear()
		t=Turtle()
		t.hideturtle()
		t.speed(0)
		t.pensize(2)
		t.penup()
		t.goto(-275,270-2*600/12)
		t.write("16"+ "(max size of implicit stack)",True,align ="center",font=("Arial",12,"bold"))
		Analyses_Module.r3_tur=t
		pass

	def write_r4(self):
		if(Analyses_Module.r4_tur!=None):
			Analyses_Module.r4_tur.clear()
		t=Turtle()
		t.hideturtle()
		t.speed(0)
		t.pensize(2)
		t.penup()
		t.goto(-275,270-3*600/12)
		t.write(str(Analyses_Module.R4)+" seconds",True,align ="center",font=("Arial",12,"bold"))
		Analyses_Module.r4_tur=t
		pass
	
	def write_r5(self):
		if(Analyses_Module.r5_tur!=None):
			Analyses_Module.r5_tur.clear()
		t=Turtle()
		t.hideturtle()
		t.speed(0)
		t.pensize(2)
		t.penup()
		t.goto(-275,270-4*600/12)
		t.write(str(Analyses_Module.R5)+" nodes/microsecond",True,align ="center",font=("Arial",12,"bold"))
		Analyses_Module.r5_tur=t
		pass
	
	def write_r6(self):
		if(Analyses_Module.r6_tur!=None):
			Analyses_Module.r6_tur.clear()
		t=Turtle()
		t.hideturtle()
		t.speed(0)
		t.pensize(2)
		t.penup()
		t.goto(-275,270-5*600/12)
		t.write(str(Analyses_Module.R6)+" nodes",True,align ="center",font=("Arial",12,"bold"))
		Analyses_Module.r6_tur=t
		pass
	
	def write_r7(self):
		if(Analyses_Module.r7_tur!=None):
			Analyses_Module.r7_tur.clear()
		t=Turtle()
		t.hideturtle()
		t.speed(0)
		t.pensize(2)
		t.penup()
		t.goto(-275,270-6*600/12)
		t.write(str(Analyses_Module.R7)+"(Ratio)",True,align ="center",font=("Arial",12,"bold"))
		Analyses_Module.r7_tur=t
		pass
	
	def write_r8(self):
		if(Analyses_Module.r8_tur!=None):
			Analyses_Module.r8_tur.clear()
		t=Turtle()
		t.hideturtle()
		t.speed(0)
		t.pensize(2)
		t.penup()
		t.goto(-275,270-7*600/12)
		t.write(str(Analyses_Module.R8)+" seconds",True,align ="center",font=("Arial",12,"bold"))
		Analyses_Module.r8_tur=t
		pass
	
	def write_r9(self):
		if(Analyses_Module.r9_tur!=None):
			Analyses_Module.r9_tur.clear()
		t=Turtle()
		t.hideturtle()
		t.speed(0)
		t.pensize(2)
		t.penup()
		t.goto(-275,270-8*600/12-10)
		t.write(str(Analyses_Module.R9),True,align ="center",font=("Arial",12,"bold"))
		Analyses_Module.r9_tur=t
		pass
	
	def write_r10(self):
		if(Analyses_Module.r10_tur!=None):
			Analyses_Module.r10_tur.clear()
		t=Turtle()
		t.hideturtle()
		t.speed(0)
		t.pensize(2)
		t.penup()
		t.goto(-275,270-9*600/12)
		t.write(str(Analyses_Module.R10)+" seconds",True,align ="center",font=("Arial",12,"bold"))
		Analyses_Module.r10_tur=t
		pass
	
	def write_r11(self):
		if(Analyses_Module.r11_tur!=None):
			Analyses_Module.r11_tur.clear()
		t=Turtle()
		t.hideturtle()
		t.speed(0)
		t.pensize(2)
		t.penup()
		t.goto(-275,270-10*600/12)
		t.write(str(Analyses_Module.R11),True,align ="center",font=("Arial",12,"bold"))
		Analyses_Module.r11_tur=t
		pass
	
	def write_r12(self):
		if(Analyses_Module.r12_tur!=None):
			Analyses_Module.r12_tur.clear()
		t=Turtle()
		t.hideturtle()
		t.speed(0)
		t.pensize(2)
		t.penup()
		t.goto(-275,270-11*600/12)
		t.write(str(Analyses_Module.R12),True,align ="center",font=("Arial",12,"bold"))
		Analyses_Module.r12_tur=t
		pass
