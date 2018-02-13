#Name T Naga Datta Madhu Kiran
#ID 2015A7PS0111P

from pre_module import generate_packages,constraint_graph,printdict,course_data,prof_data,course_ltp,printlist,print_constraint_matrix,CSP
from constraint import DFS_BT,node,get_slots,DFS_BT_propagate,degree_heuristic,without_degree_heuristic,print_timetable
import copy,sys

def main():
	inp=int(input("Enter the Option "))
	if inp==1:
		output_package=generate_packages("testcase1")
		printlist(output_package[0])
		printdict (output_package[1][0])
	elif inp==2:
		output_package=generate_packages("testcase1")
		constraint_list,constraint_matrix=constraint_graph(output_package)
		printdict (constraint_list)
	elif inp==3:
		output_package=generate_packages("testcase1")
		constraint_list,constraint_matrix=constraint_graph(output_package)
		slots=get_slots()
		csp=CSP()
		course_ltp=csp.course_ltp
		init_state={}
		domain={}

		while(True):
			heur=int(input("Enter '1' for with heuristic \n   or '2' for without a heuristic (1 or 2)-"))
			if heur==1:
				varlist=degree_heuristic(csp.CG)
				break
			elif heur ==2:
				varlist=without_degree_heuristic(csp.CG)
				break
			else:
				print "1 or 2  only!"

		# stdout=sys.stdout
		# sys.stdout=open("output.txt","w+")

		for i in course_ltp:
			if course_ltp[i][0]>6:
				print("Time table is not Possible!!!!")
				return
			if course_ltp[i][1]>6:
				print("Time table is not Possible!!!!")
				return
			if course_ltp[i][2]>3:
				print("Time table is not Possible!!!!")
				return
				
			init_state[i]=[[],[],[[],[]],0]
			domain[i]=copy.deepcopy(slots)
		n=node(init_state,domain,'')
		node.slots={i:[0,0] for i in slots}
		answer=DFS_BT(csp,varlist,n,csp.CG)
		# print "true"+str(answer[1].state)
		# print csp.CG
		# sys.stdout=stdout

	elif inp==4:
		output_package=generate_packages("testcase1")
		constraint_list,constraint_matrix=constraint_graph(output_package)
		slots=get_slots()
		csp=CSP()
		course_ltp=csp.course_ltp
		init_state={}
		domain={}
		# print (without_degree_heuristic(csp.CG))

		# print (degree_heuristic(csp.CG))
		while(True):
			heur=int(input("Enter '1' for with heuristic \n   or '2' for without a heuristic (1 or 2)-"))
			if heur==1:
				varlist=degree_heuristic(csp.CG)
				break
			elif heur ==2:
				varlist=without_degree_heuristic(csp.CG)
				break
			else:
				print "1 or 2  only!"



		# stdout=sys.stdout
		# sys.stdout=open("output.txt","w+")

		for i in course_ltp:
			if course_ltp[i][0]>6:
				print("Time table is not Possible!!!!")
				return
			if course_ltp[i][1]>6:
				print("Time table is not Possible!!!!")
				return
			if course_ltp[i][2]>3:
				print("Time table is not Possible!!!!")
				return
				
			init_state[i]=[[],[],[[],[]],0]
			domain[i]=copy.deepcopy(slots)
		n=node(init_state,domain,'')
		node.slots={i:[0,0] for i in slots}



		answer=DFS_BT_propagate(csp,varlist,n,csp.CG)
		# print str(answer)
		# print csp.CG
		# sys.stdout=stdout
	

main()