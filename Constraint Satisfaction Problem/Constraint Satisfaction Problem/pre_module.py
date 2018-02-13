#Name T Naga Datta Madhu Kiran
#ID 2015A7PS0111P

import csv
import sys
import copy 

class CSP():
	course_data=[]
	prof_data={}
	constraint_adj_matrix=[]
	course_ltp={}
	program_data={}
	output_package=[]
	CG=[]
	varlist=[]

	def __init(self):
		pass
	def __repr__(self):
		return  "class"+str(CSP.course_data)+'\n'+str(CSP.prof_data)+'\n'+str(CSP.constraint_adj_matrix)+'\n'+str(CSP.course_ltp)+'\n'+str(CSP.program_data)+'\n'+str(CSP.output_package)+'\n'





course_data=[]
prof_data={}
constraint_adj_matrix=[]
course_ltp={}
program_data={}
def generate_packages(input):
	global course_data
	global prof_data
	global course_ltp
	global program_data
	with open(input+".csv","r") as file:
		data =csv.reader(file,delimiter=",")
		course=[]
		prof=[]
		flag=0
		for i in data:
			if i[0]=='$COURSES$':
				name=1
				flag=2
			if i[0]=='$PROF$':
				name=2
				flag=2
			if flag!=0:
				flag-=1
				continue
			if name==1:
				i[4]=list(i[4].split())
				course.append(i)
			elif name==2:
				prof.append(i)
			# print(i)
		# print(course)
		# print(prof)
	course_data=copy.deepcopy(course)
	# print course
	# prof_data=copy.deepcopy(prof)
	


	for i in course:
		course_ltp[i[0]]=[int(j) for j in i[4]]
		CSP.varlist.append(i[0])
	prof_courses={}
	for i in prof:
		temp=[]
		for j in i[1:]:
			if j!='NA':
				temp.append(j)
		prof_courses[i[0]]=temp
	for i in prof_courses:
		prof_data[i]=prof_courses[i]

	prof_package=[prof_courses,course_ltp]
	# print prof_package
	progA={'DC':[],'DE':[],'GE':[],'NA':[]}
	progB={'DC':[],'DE':[],'GE':[],'NA':[]}
	progC={'DC':[],'DE':[],'GE':[],'NA':[]}
	for i in course:
		progA[i[1]].append(i[0])
		progB[i[2]].append(i[0])
		progC[i[3]].append(i[0])

	program_data['progA']=copy.deepcopy(progA)
	program_data['progB']=copy.deepcopy(progB)
	program_data['progC']=copy.deepcopy(progC)
	
	# print program_data

	student_packages=[]
	# print(progA)
	student_packages+=possible_combinations(progA)
	# print(progB)
	student_packages+=possible_combinations(progB)
	# print(progC)
	student_packages+=possible_combinations(progC)
	
	output_package=[student_packages,prof_package]
	
	# print(output_package)
	CSP.course_data=course_data
	CSP.prof_data=prof_data

	CSP.course_ltp=course_ltp
	CSP.program_data=program_data
	CSP.output_package=output_package

	return output_package
	

def possible_combinations(program):
	packages=[]
	possible_DC=[]
	DC_num=len(program['DC'])
	for i in range(0,DC_num):
		for j in range(i+1,DC_num):
			for k  in range(j+1,DC_num):
				possible_DC.append([program['DC'][i],program['DC'][j],program['DC'][k]])
	possible_DE=[]
	DE_num=len(program['DE'])
	for i in range(0,DE_num):
		for j in range(i+1,DE_num):
			possible_DE.append([program['DE'][i],program['DE'][j]])
	possible_GE=[]
	GE_num=len(program['GE'])
	for i in range(0,GE_num):
		possible_GE.append([program['GE'][i]])
	# print(possible_DC)
	# print(possible_DE)
	# print(possible_GE)
	for i in possible_DC:
		for j in possible_DE:
			for k in possible_GE:
				packages.append([i,j,k])
	# printlist(packages)
	return packages
def printdict(dic):
	for i in dic:
		print i+" : "+str(dic[i])
def constraint_graph(package):
	student_packages=package[0]
	prof_package=package[1]
	prof_data=prof_package[0]

	# printlist(student_packages)
	# print prof_package
	# print prof_data

	global course_data
	global constraint_adj_matrix

	# print("\n\n"+str(course_data)+"\n\n\n")

	num_courses=len(course_data)
	constraint_matrix= [[0 for i in range(0,num_courses+1)] for j in range(0,num_courses+1)]
	constraint_list={i[0]:[] for i in course_data}
	
	for i in student_packages:
		i_cour=i[0]+i[1]+i[2]
		for j in range(0,len(i_cour)):
			for k in range(j+1,len(i_cour)):
				constraint_matrix[int(i_cour[j][2:])][int(i_cour[k][2:])]=1
				constraint_matrix[int(i_cour[k][2:])][int(i_cour[j][2:])]=1
				if i_cour[k] not in constraint_list[i_cour[j]]:
					constraint_list[i_cour[j]].append(i_cour[k])
				if i_cour[j] not in constraint_list[i_cour[k]]:
					constraint_list[i_cour[k]].append(i_cour[j])
				# if int(i_cour[k][2:]) not in constraint_list[int(i_cour[j][2:])]:
				# 	constraint_list[int(i_cour[j][2:])].append(int(i_cour[k][2:]))
				# if int(i_cour[j][2:]) not in constraint_list[int(i_cour[k][2:])]:					
				# 	constraint_list[int(i_cour[k][2:])].append(int(i_cour[j][2:]))
	
	constraint_adj_matrix=copy.deepcopy(constraint_list)
	CSP.CG=copy.deepcopy(constraint_list)
	# printlist (constraint_matrix)
	# print (constraint_list)
	CSP.constraint_adj_matrix=constraint_adj_matrix
	return [constraint_list,constraint_matrix]

def printlist(l):
	for i in l:
		print(i)

def print_constraint_matrix(d):
	print("Adjacency Matrix \nwhere each cell represent \ncorresponding courses are adjacent to each other")
	for i in d[1:]:
		print i[1:]
