#Name T Naga Datta Madhu Kiran
#ID 2015A7PS0111P

from gui import draw_template,dimension
from turtle import *
import turtle
from gui import var_list,check_fill,write_gen_query,write_ans,refresh,draw_box,flags,clear_mar_cond,clear_mar_quer,write_string
import copy

class node:

	def __init__(self):
		self.par=[]
		self.child=[]
		self.name=""
		self.cpt={}
		self.num_par=0

	def __repr__(self):
		# return str([i.name for i in self.par])+"-parents."+str([i.name for i in self.child])+"-children.\n"
		return str(self.cpt)

	def get_cp(self,lis):
		if len(lis)==0:
			return self.cpt
		else:
			# print self.cpt,lis
			return self.cpt[tuple(sorted(lis))]





def cpt_tru_dict(lis,cpt):
	par_com=all_combination(lis)
	d={}
	for i in range(len(cpt)):
		d[tuple(sorted(par_com[i]))]=cpt[i]
	return d

def createBayesianNetwork(cause_effect_file):
	BayesianNetwork={}
	with open (cause_effect_file,"r+") as data:
		for row in data:
			if row =='$$':
				break
			temp=row[:-1].split(">>")
			temp2=temp[1].strip(" ")[1:-1]
			cpt=[float(i) for i in temp[2].strip(" ").split(" ")]
			if(temp2==""):
				par=[]
				num_par=0
			else:
				par=temp2.split(",")
				par=[i.strip(" ") for i in par]
				num_par=len(par)
			node_name=temp[0].strip(" ")
			if node_name in BayesianNetwork:
				cur_node=BayesianNetwork[node_name]
			else:
				cur_node=node()
				BayesianNetwork[node_name]=cur_node			
			for i in par:
				if i in BayesianNetwork:
					cur_node.par.append(BayesianNetwork[i])
				else:
					new_node=node()
					BayesianNetwork[i]=new_node
					cur_node.par.append(new_node)
			cur_node.name=node_name
			if len(par)==0:
				cur_node.cpt=cpt[0]
			else:
				cur_node.cpt=cpt_tru_dict(par,cpt)
			cur_node.num_par=num_par
			for i in par:
				if i in BayesianNetwork:
					BayesianNetwork[i].child.append(cur_node)
				else:
					new_node=node()
					BayesianNetwork[i]=new_node
					new_node.child=[cur_node]
	return BayesianNetwork

class Markov_Blanket:
	def __init__(self):
		self.child=[]
		self.par=[]
		self.childpar=[]
		self.name=""
		self.M_Blanket=[]

	def get_child(self):
		l=[]
		for i in self.child:
			l.append(i.name)
		return l

	def get_par(self):
		l=[]
		for i in self.par:
			l.append(i.name)
		return l

	def get_childpar(self):
		l=[]
		for i in self.childpar:
			l.append(i.name)
		return l

	def __repr__(self):
		return str([i.name  for i in self.M_Blanket])

# def computeMarkovBlanket(B, str_A):
	
# 	A=B[str_A]
# 	MarkovBlanket=[]
# 	MarkovBlanket+=A.par
# 	child=A.child
# 	MarkovBlanket+=child
# 	for i in child:
# 		MarkovBlanket+=i.par
# 	return list(set(MarkovBlanket))


def computeMarkovBlanket(B, str_A):
	A=B[str_A]
	MarkovBlanket=Markov_Blanket()
	MarkovBlanket.name=str_A
	MarkovBlanket.par+=A.par
	MarkovBlanket.child=A.child
	child=A.child
	for i in child:
		MarkovBlanket.childpar+=i.par
	MarkovBlanket.childpar=list(set(MarkovBlanket.childpar))
	MarkovBlanket.M_Blanket=list(set(MarkovBlanket.par+MarkovBlanket.child+MarkovBlanket.childpar))

	mar=[]
	for i in MarkovBlanket.M_Blanket:
		mar.append(i.name)
	mar.append(MarkovBlanket.name)
	mar=list(set(mar))
	return mar

class expression:
	def __init__(self):
		self.conditional=[]
		self.query=[]

def createExpression(query_variables,conditional_variables):
	exp=expression()
	exp.query=copy.deepcopy(query_variables)
	exp.conditional=copy.deepcopy(conditional_variables)
	return exp

def all_chars(expression):
	temp=[]
	for i in expression.conditional:
		temp.append(i[-1])
	for i in expression.query:
		temp.append(i[-1])
	return temp

# def inc_one(lis,lit):
# 	temp=[]
# 	for i in lis:
# 		temp.append(i+[lit])
# 	for i in lis:
# 		temp.append(i+["~"+lit])
# 	return temp

# def all_combination(lis):
# 	ans=[[]]
# 	temp=
# 	for i in lis:
# 		ans=inc_one(ans,i)
# 	return ans

def inc_one(lis,lit):
	temp=[]
	for i in lis:
		temp+=[(i+["~"+lit])]
	for i in lis:
		temp+=[(i+[lit])]	
	return temp

def all_combination(lis):
	ans=[[]]
	for i in range(len(lis)-1,-1,-1):
		ans=inc_one(ans,lis[i])
	ans2=[]
	for i in ans:
		ans2+=[i[::-1]]
	return ans2

def make_a_dict(lis):
	dictionary={}
	for i in lis:
		dictionary[i[-1]]=i
	return dictionary

def calculateind(lis,bayesian):
	# print "start"
	# print lis
	d=make_a_dict(lis)
	# print d
	ans=1
	for i in d.keys():
		par=bayesian[i].par
		par_name=[]
		for k in par:
			par_name.append(k.name)
		par=par_name
		l=[]
		for j in par:
			if j in d:
				l.append(d[j])
			else:
				l.append(j)
		# print i,l
		num=bayesian[i].get_cp(l)
		if(d[i]==i):
			ans*=num
		else:
			ans*=(1-num)
	# print ans

	# print "end"
	return ans

def full_set(bayesian,temp):
	mar=[]
	while(True):
		for i in temp:
			mar+=computeMarkovBlanket(bayesian,i)
		mar=list(set(mar))
		if(len(mar)==len(temp)):
			break
		temp=mar
		mar=[]
	return mar

def computeProbability(expression):
	global filename
	bayesian=createBayesianNetwork(filename[0])
	orichars=expression.conditional+expression.query
	temp=all_chars(expression)
	# mar=[]
	# for i in temp:
	# 	mar+=computeMarkovBlanket(bayesian,i)
	mar=full_set(bayesian,temp)
	mar=list(set(mar))
	excl=subtract(mar,temp)
	all_excl=all_combination(excl)
	# print "all_excl",len(all_excl)
	ans=0
	for i in all_excl:
		ans+=calculateind(orichars+i,bayesian)
	orichars=expression.conditional
	temp=[i[-1] for i in orichars]
	# mar=[]
	# for i in temp:
	# 	mar+=computeMarkovBlanket(bayesian,i)
	mar=full_set(bayesian,temp)
	mar=list(set(mar))
	excl=subtract(mar,temp)
	all_excl=all_combination(excl)
	
	ans2=0
	for i in all_excl:
		ans2+=calculateind(orichars+i,bayesian)
	# print ans,ans2
	write_ans(ans/ans2)
	# print ans/ans2




def subtract(big,small):
	ans=[]
	for i in big:
		if i not in small:
			ans.append(i)
	return ans

Query_list=[]
Conditional_list=[]
global var_list

def new_query(x,y):
	global Query_list
	global Conditional_list
	global flags
	xshift=200
	if x>=315 and x<=495 and y>=-240 and y<=-215:
		
		draw_box(Turtle(),"white","",315,-220,180,"white")
		draw_box(Turtle(),"white","",410,-250,120,"white")
		refresh(Query_list+Conditional_list)
		draw_box(Turtle(),"lightgreen","Generated Query is                                                                                ",-300-xshift,-220,760)
		draw_box(Turtle(),"lightgreen","Answer  =                                                                                         ",-300-xshift,-250,760)	
		clear_mar_cond()
		clear_mar_quer()

		for i in flags:
			flags[i]=0
		del Query_list[:]
		del Conditional_list[:]
		screen=turtle.Screen()
		screen.onclick(take_input)
		return 

	if x>=410 and x<=530 and y>=-270 and y<=-245:
		turtle.bye()



def write_markov_query(l):
	global dimension
	global filename
	bayesian=createBayesianNetwork(filename[0])
	write_string("MarkovBlanket of Query Variables\n      (for corresponding nodes)",-350,245,1)
	for i in l:
		a=computeMarkovBlanket(bayesian,i[-1])
		write_string(a,-370,dimension[(i,'q')][2]-18.5)



def write_conditional_query(l):
	global dimension
	global filename
	bayesian=createBayesianNetwork(filename[0])
	write_string("MarkovBlanket of Conditional Variables\n      (for corresponding nodes)",190,245,1)
	for i in l:
		a=computeMarkovBlanket(bayesian,i[-1])
		write_string(a,190,dimension[(i,'q')][2]-18.5)


	


def take_input(x,y):
	screen=turtle.Screen()
	screen.onclick(None)
	global var_list
	global Query_list
	global Conditional_list
	types=["q","c"]
	# print Query_list,Conditional_list
	if x>=270 and x<=390 and y>=-270 and y<=-245: 
		draw_box(Turtle(),"red","Process is going on",220,320,240)
		# print "generated"
		if len(Query_list)==0:
			print "invalid query--'atleast one query_variable needs to be selected'"
			turtle.bye()
			# screen=turtle.Screen()
			# screen.onclick(take_input)
			return
		else:
			write_gen_query(Query_list,Conditional_list)
			write_markov_query(Query_list)
			write_conditional_query(Conditional_list)
			exp=createExpression(Query_list,Conditional_list)
			ans=computeProbability(exp)
			draw_box(Turtle(),"white","",220,320,240,"white")
			draw_box(Turtle(),"red","New Query",315,-220,180)
			draw_box(Turtle(),"red","Exit",410,-250,120)
			screen=turtle.Screen()
			screen.onclick(new_query)
		
		return

	for t in types:
		for v in var_list:
			if (len(Query_list)>=10 and t=='q') or (len(Conditional_list)>=10 and t=='c'):
				continue
			if check_fill(x,y,v,t)==True:
				if t =='q':
					Query_list.append(v)	
				if t =='c':
					Conditional_list.append(v)
					
	screen=turtle.Screen()
	screen.onclick(take_input)



filename=[]
def main():
	global Query_list
	global Conditional_list
	cause_effect_file=raw_input("Enter name input file - ")
	# cause_effect_file="input2.txt"
	filename.append(cause_effect_file)
	# print cause_effect_file
	BayesianNetwork =createBayesianNetwork(cause_effect_file)
	draw_template(BayesianNetwork.keys())	
	screen=turtle.Screen()
	screen.onclick(take_input)	
	turtle.mainloop()

main()
