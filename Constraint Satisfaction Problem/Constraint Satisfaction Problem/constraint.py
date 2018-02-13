#Name T Naga Datta Madhu Kiran	
#ID 2015A7PS0111P


from pre_module import course_ltp,generate_packages,constraint_graph,program_data,prof_data,CSP
import copy
import sys
from combinations import for_loop_function0
from combinations import for_loop_function1
from combinations import for_loop_function2
from combinations import for_loop_function3
from combinations import for_loop_function4
from combinations import for_loop_function5
from combinations import for_loop_function6

# id:[Day,time]

Day={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thrusday',5:'Friday',6:'Saturday'}
Time={1:'09:00',2:'10:00',3:'11:00',4:'12:00',6:'02:00',7:'03:00',8:'04:00'}
def get_slots():

	# id:[Day,time]

	slots=[]
	for i in range(1,7):
		for j in range(1,9):
			slots.append(10*i+j)
	slots.remove(68)                    #As Saturday have 4 hours in morning only.
	slots.remove(67)
	slots.remove(66)
	for i in range(1,7):
		slots.remove(i*10+5)
	return slots

slots=get_slots()


# print course_ltp
# output_package=generate_packages("testcase1")
# constraint_list,constraint_matrix=constraint_graph(output_package)
# from pre_module import course_ltp,program_data
# print CSP()
# print course_ltp
# print program_data


# print init_state

Lecture_hall=5
Laboratories_lab=5

Lecture_matrix={i:0 for i in slots}
Laboratories_matrix={i:0 for i in slots}

# print("here")
# print "_here_"
# print prof_data

#state={'course_name':[lecture_slots,tutorial_slots,lab_slots([1st_batch,2ndBatch]),assigned_flag]}

class node:
	slots={}
	def __init__(self,state,domain,course):
		self.course_changed=course
		self.state=state
		self.domain=domain





# def Laboratory_constraint_1 (node):
# 	state=node.state
# 	for i in state:
# 		if state[i][3]==0:
# 			continue
# 		else:
# 			for k in state[i][2][0]:
# 				if(k%10 <=4):
# 					return False
# 			for k in state[i][2][1]:
# 				if(k%10 <=4):
# 					return False
# 	return True

def Laboratory_constraint_1 (node):
	state=node.state
	i=node.course_changed
	for k in state[i][2][0]:
		if(k%10 <=4):
			return False
	for k in state[i][2][1]:
		if(k%10 <=4):
			return False
	return True


# def Laboratory_constraint_2 (node,CSP):
# 	state=node.state
# 	print state
# 	for i in state:
# 		if state[i][3]==0:
# 			continue
# 		else:
# 			course_ltp=CSP.course_ltp
# 			if course_ltp[i][2]==0:
# 				continue

# 			temp=state[i][2][0].sort()
# 			prev=temp[0]
# 			for i in temp[1:]:
# 				if abs(i-prev) !=1:
# 					return False
# 				prev=i

# 			temp=state[i][2][1].sort()
# 			prev=temp[0]
# 			for i in temp[1:]:
# 				if abs(i-prev) !=1:
# 					return False
# 				prev=i

# 	return True

	
def Laboratory_constraint_2 (node,CSP):
	state=node.state
	i=node.course_changed

	course_ltp=CSP.course_ltp
	if course_ltp[i][2]==0:
		return True

	temp=sorted(state[i][2][0])
	prev=temp[0]
	for k in temp[1:]:
		if abs(k-prev) !=1:
			return False
		prev=k

	temp=sorted(state[i][2][1])
	prev=temp[0]
	for k in temp[1:]:
		if abs(k-prev) !=1:
			return False
		prev=k

	return True

# def Tutorial_constraint_3(node):
# 	state=node.state
# 	for i in state:
# 		if state[i][3]==0:
# 			continue
# 		else:
# 			lec_days=[i//10 for i in state[i][0]]
# 			tut_days=[i//10 for i in state[i][1]]

# 			for i in tut_days:
# 				if i in lec_days:
# 					return False

# 	return True

def Tutorial_constraint_3(node):
	state=node.state
	j=node.course_changed

	lec_days=[i//10 for i in state[j][0]]
	tut_days=[i//10 for i in state[j][1]]

	for i in tut_days:
		if i in lec_days:
			return False

	return True

def Disciplinary_constraint_4(node):
	state=node.state
	
	progA_DC=program_data['progA']['DC']
	progB_DC=program_data['progB']['DC']
	progC_DC=program_data['progC']['DC']
	
	temp=[]
	for i in progA_DC:
		if state[i][3]==0:
			continue
		else:
			temp.append(state[i][0]+state[i][1]+state[i][2][0]+state[i][2][1])
	for i in range(len(temp)):
		for j in range(i+1,len(temp)):
			for k in temp[i]:
				if (k+1 in temp[j] )or (k-1 in temp[j]):
					return False
	temp=[]
	for i in progB_DC:
		if state[i][3]==0:
			continue
		else:
			temp.append(state[i][0]+state[i][1]+state[i][2][0]+state[i][2][1])
	for i in range(len(temp)):
		for j in range(i+1,len(temp)):
			for k in temp[i]:
				if (k+1 in temp[j] )or (k-1 in temp[j]):
					return False
	temp=[]
	for i in progC_DC:
		if state[i][3]==0:
			continue
		else:
			temp.append(state[i][0]+state[i][1]+state[i][2][0]+state[i][2][1])
	for i in range(len(temp)):
		for j in range(i+1,len(temp)):
			for k in temp[i]:
				if (k+1 in temp[j] )or (k-1 in temp[j]):
					return False

	return True

def General_constraint_5(node):
	state=node.state

	Allprog_GE=list(set(program_data['progA']['GE']+program_data['progB']['GE']+program_data['progC']['GE']))

	temp=[]

	for i in Allprog_GE:
		if state[i][3]==0:
			continue
		else:
			temp+=state[i][0]+state[i][1]+state[i][2][0]+state[i][2][1]
	temp_day=[]
	for i in temp:
		temp_day.append(i//10)

	day_l=list(set(temp_day))

	if len(day_l)!=len(temp_day):
		return False

	return True


# def Lecture_constraint_6(node):
# 	state=node.state
# 	for i in state:
# 		if state[i][3]==0:
# 			continue
# 		else:
# 			temp=state[i][0]
# 			c={}
# 			for i in temp:
# 				if(i//10) in c:
# 					return False
# 				c[i//10]=1
# 	return True

def Lecture_constraint_6(node):
	state=node.state
	i=node.course_changed
	temp=state[i][0]
	c={}
	for i in temp:
		if(i//10) in c:
			return False
		c[i//10]=1
	return True

# def Laboratory_constraint_7(node,CSP):
# 	state=node.state
# 	course_ltp=CSP.course_ltp
# 	for i in state:
# 		if state[i][3]==0:
# 			continue
# 		else:
# 			if(len(state[i][2][0]))!=course_ltp[i][2] and len(state[i][2][1])!=course_ltp[i][2]:
# 				return False
# 			if(state[i][2][0]//10==state[i][2][1]//10):
# 				return False
# 	return True

def Laboratory_constraint_7(node,CSP):
	state=node.state
	course_ltp=CSP.course_ltp
	i=node.course_changed
	if(course_ltp[i][2]==0):
		return True
	if(len(state[i][2][0]))!=course_ltp[i][2] and len(state[i][2][1])!=course_ltp[i][2]:
		return False
	if(state[i][2][0][0]//10==state[i][2][1][0]//10):
		return False
	return True

def Professor_constraint_8(node):
	state=node.state
	course=node.course_changed

	if course in prof_data['Prof-4']:
		temp=state[course][0]+state[course][1]+state[course][2][0]+state[course][2][1]
		for j in temp:
				if j//10==4:
					return False
		return True

	elif course in prof_data['Prof-1']:
		temp=state[course][0]+state[course][1]
		for j in temp:
			if j%10 > 2:
				return False
		return True
	return True


def Professor_constraint_9(node,CSP):
	state=node.state
	course_ltp=CSP.course_ltp
	prof_data=CSP.prof_data
	# print node.state
	for z in prof_data:
		courses=prof_data[z]
		# print courses
		temp_lec=[]
		temp_lab1=[]
		temp_lab2=[]
		p=[]
		for j in range(len(courses)):

			if state[courses[j]][3]==0:
				continue


			temp_lec+=state[courses[j]][0]
			
			# print state[courses[j]][2][0]

			if course_ltp[courses[j]][2]==0:
				continue
			temp_lab1+=[min(state[courses[j]][2][0])]
			temp_lab2+=[min(state[courses[j]][2][1])]
			p.append(course_ltp[courses[j]][2])

		temp=temp_lec+temp_lab1+temp_lab2

		for i in temp_lec:
			if i+1 in temp or i-1 in temp:
				return False
		for i in range(len(temp_lab1)):
			if temp_lab1[i]%10 +p[i] <= 8:
				if temp_lab1[i]+p[i] in temp:
					return False
			if temp_lab1[i]%10 -p[i] >= 1:
				if temp_lab1[i]-p[i] in temp:
					return False

		for i in range(len(temp_lab2)):
			if temp_lab2[i]%10 +p[i] <= 8:
				if temp_lab2[i]+p[i] in temp:
					return False
			if temp_lab2[i]%10 -p[i] >= 1:
				if temp_lab2[i]-p[i] in temp:
					return False

	return True

diff_prac_slots=[(7,8),(8,9),(7,8,9)]
day_avail=[1,2,3,4,5]

id_list={}
count=1
for i in day_avail:
	for j in diff_prac_slots:
		t=[]
		for k in j:
			t.append(10*i+k)
		id_list[tuple(t)]=count
		count+=1

# def Student_Prof_constraint_10(node,CG):
# 	state=node.state
# 	course_ltp=CSP.course_ltp
# 	course=node.course_changed
# 	l=state[course][0]
# 	t=state[course][1]
# 	lt=l+t
# 	rem_ltp=[]
# 	num_p_co=0
# 	ltp=state[course][0]+state[course][1]+state[course][2][0]+state[course][2][1]
# 	ltp_set=list(set(ltp))
# 	if(len(ltp)!=len(ltp_set)):
# 		return False
# 	for  j in CG[course]:
# 		rem_ltp+=state[j][0]+state[j][1]+state[j][0]+state[j][1]
# 		if(course_ltp[j][2]!=0 and state[j][3]!=0):
# 			num_p_co+=1
# 	rem_ltp=list(set(rem_ltp))
# 	for i in lt:
# 		if i in rem_ltp:
# 			return False
# 	if(course_ltp[course][2]==0):
# 		return True
# 	# pr=[]
# 	pr_id=[]
# 	temp1=state[course][2][0][0]//10
# 	temp2=state[course][2][1][0]//10
# 	if(temp1==temp2):
# 		return False
# 	# pr.append(temp1,temp2)



# 	temp=tuple(state[course][2][0])
# 	pr_id.append(id_list[temp])
# 	temp=tuple(state[course][2][1])
# 	pr_id.append(id_list[temp])
# 	for i in CG:
# 		if(course_ltp[CG[i]][2]==0):
# 			continue
# 		temp1=state[course][2][0][0]//10
# 		temp2=state[course][2][1][0]//10
# 		if(temp1==temp2):
# 			return False
# 		# pr.append(temp1,temp2)
# 		temp=tuple(state[CG[i]][2][0])
# 		pr_id.append(id_list[temp])
# 		temp=tuple(state[CG[i]][2][1])
# 		pr_id.append(id_list[temp])
# 	pr_id=list(set(pr_id))
# 	if len(pr_id) >= num_p_co:
# 		return True
# 	return False

def Student_Prof_constraint_10(node,CG):
	state=node.state
	course_ltp=CSP.course_ltp
	course=node.course_changed
	l=state[course][0]
	t=state[course][1]
	lt=l+t
	rem_ltp=[]
	num_p_co=0
	ltp=state[course][0]+state[course][1]+state[course][2][0]+state[course][2][1]
	ltp_set=list(set(ltp))
	if(len(ltp)!=len(ltp_set)):
		return False
	for  j in CG[course]:
		rem_ltp+=state[j][0]+state[j][1]+state[j][0]+state[j][1]
		if(course_ltp[j][2]!=0 and state[j][3]!=0):
			num_p_co+=1
	rem_ltp=list(set(rem_ltp))
	for i in lt:
		if i in rem_ltp:
			return False
	if(course_ltp[course][2]==0):
		return True
	# pr=[]
	pr_id=[]
	temp1=state[course][2][0][0]//10
	temp2=state[course][2][1][0]//10
	if(temp1==temp2):
		return False
	# pr.append(temp1,temp2)

	


	pr_id.append(state[course][2][0][0]//10)
	pr_id.append(state[course][2][1][0]//10)

	# print CG
	
	for i in CG[course]:
		if(course_ltp[i][2]==0 or state[i][3]==0):
			continue
		temp1=state[i][2][0][0]//10
		temp2=state[i][2][1][0]//10
		if(temp1==temp2):
			return False
		# pr.append(temp1,temp2)
		pr_id.append(temp1)
		pr_id.append(temp2)

	pr_id=list(set(pr_id))
	if len(pr_id) >= num_p_co:
		return True
	return False

# Student_constraint_10(node([],[]))

def func_generator(num_loops):
	stdout=sys.stdout
	sys.stdout=open("function.py","w+")
	print "#Name T Naga Datta Madhu Kiran"
	print "#ID 2015A7PS0111P"	
	print "def for_loop_function(slots):"
	print "\tcom_list=[]"
	print "\ti0=0"
	# print "\t"+str(num_loops)
	count=1
	for i in range(num_loops):
		print "\t"*count+"for i"+str(count)+" in range(i"+str(count-1)+",len(slots)):"
		count+=1
	sys.stdout.write("\t"*count+"com_list.append([")
	for i in range(1,num_loops+1):
		sys.stdout.write("slots[i"+str(i)+"],")
	print "])"
	print "\t"+"return com_list"
	sys.stdout=stdout
	from function import for_loop_function
	return for_loop_function(slots)
# func_generator(4)
# from function import for_loop_function
# a=for_loop_function(slots[1:])
# print a



def DFS_BT (CSP, variable_list,node,CG):

	# print node.state
	# print "\n"+str(variable_list)+"variable_list\n\n"
	if(len(variable_list)==0):
		return [True,node]

	course_ltp=CSP.course_ltp
	course=variable_list.pop(0)
	domain=node.domain[course][0]
	# course_slots=calculate(slots,course_ltp[course][0],course_ltp[course][1],course_ltp[course][2])
	#to create variable number of for loops
	l=course_ltp[course][0]
	t=course_ltp[course][1]
	p=course_ltp[course][2]

	# print course_ltp

	# print l

	# num_loops=l
	# func_generator(num_loops)
	# from function import for_loop_function
	# l_list=[for_loop_function(slots)]
	# l_list=func_generator(num_loops)


	# print
	# num_loops=t
	# func_generator(num_loops)
	# from function import for_loop_function
	# t_list=for_loop_function(slots)

	# t_list=func_generator(num_loops)

	# print p
	# num_loops=p
	# func_generator(num_loops)
	# from function import for_loop_function
	# p_list=for_loop_function(slots)
	# p_list=func_generator(num_loops)

	# print len(l_list),len(t_list),len(p_list)


	slots=node.domain[course]

	if l==0:
		l_list=for_loop_function0(slots)
	elif l==1:
		l_list=for_loop_function1(slots)
	elif l==2:
		l_list=for_loop_function2(slots)
	elif l==3:
		l_list=for_loop_function3(slots)
	elif l==4:
		l_list=for_loop_function4(slots)
	elif l==5:
		l_list=for_loop_function5(slots)
	elif l==6:
		l_list=for_loop_function6(slots)

	slots=node.domain[course]

	if t==0:
		t_list=for_loop_function0(slots)
	elif t==1:
		t_list=for_loop_function1(slots)
	elif t==2:
		t_list=for_loop_function2(slots)
	elif t==3:
		t_list=for_loop_function3(slots)
	elif t==4:
		t_list=for_loop_function4(slots)
	elif t==5:
		t_list=for_loop_function5(slots)
	elif t==6:
		t_list=for_loop_function6(slots)

	# print p_slots

	slots=node.domain[course]

	p_slots=[]
	for sl in slots:
		if sl%10 >5:
			p_slots.append(sl)
	p_slots.sort()

	if p==0:
		p_list=for_loop_function0(p_slots)
	elif p==1:
		p_list=for_loop_function1(p_slots)
	elif p==2:
		p_list=for_loop_function2(p_slots)
	elif p==3:
		p_list=for_loop_function3(p_slots)
	elif p==4:
		p_list=for_loop_function4(p_slots)
	elif p==5:
		p_list=for_loop_function5(p_slots)
	elif p==6:
		p_list=for_loop_function6(p_slots)


	if p==0:
		p_list=[[]]
	elif p==1:
		p_list=p_slots
	elif p==2:
		p_list=[[16,17],[17,18],[36,37],[26,27],[27,28],[37,38],[46,47],[47,48],[56,57],[57,58],[46,47],[47,48],[56,57],[57,58]]
	elif p==3:
		p_list=[[16,17,18],[26,27,28],[36,37,38],[46,47,48],[56,57,58]]
	# print (l,t,p)
	# print (len(l_list),len(t_list),len(p_list))

	for i in l_list:
		node.state[course][0]=copy.deepcopy(i)
		node.course_changed=course
		if(Lecture_constraint_6(node)!=True):
			continue
		for j in t_list:
			node.state[course][1]=copy.deepcopy(j)
			node.course_changed=course
			if(Tutorial_constraint_3(node)!=True):
				continue
			if(Professor_constraint_8(node)!=True):
				# print("8----------")
				continue
			for k in range(len(p_list)):
				for m in range(k,len(p_list)):
					# print [i,j,[p_list[k],p_list[m]],1]
					node.state[course][0]=copy.deepcopy(i)
					node.state[course][1]=copy.deepcopy(j)
					node.state[course][2][0]=copy.deepcopy(p_list[k])
					node.state[course][2][1]=copy.deepcopy(p_list[m])
					node.state[course][3]=1
					node.course_changed=course
					
					# za=input("enter-")
					if(Laboratory_constraint_1(node)!=True):
						# print("1------")
						continue
					if(Laboratory_constraint_2(node,CSP)!=True):
						# print("2--------")
						continue
					if(Tutorial_constraint_3(node)!=True):
						# print("3---------")
						continue
					if(Disciplinary_constraint_4(node)!=True):
						# print("4---------")
						continue
					if(General_constraint_5(node)!=True):
						# print("5----------")
						continue
					if(Lecture_constraint_6(node)!=True):
						# print("6----------")
						continue
					if(Laboratory_constraint_7(node,CSP)!=True):
						# print("7---------")
						continue
					if(Professor_constraint_8(node)!=True):
						# print("8----------")
						continue
					if(Professor_constraint_9(node,CSP)!=True):
						# print("9----------")
						continue
					if(Student_Prof_constraint_10(node,CG)!=True):
						# print("10------------")
						continue
					# print node.state

					print_timetable(CSP,node.state,"DFS_BT")
					ans=DFS_BT(CSP, copy.deepcopy(variable_list),node,CG)
					if(ans[0]==True):
						return [True,node]

					else:
						continue
	node.state[course][3]=0
	return False,[]

def DFS_BT_propagate (CSP, variable_list,node,CG):

	# print node.state
	# print "\n"+str(variable_list)+"variable_list\n\n"
	if(len(variable_list)==0):
		return [True,node]

	course_ltp=CSP.course_ltp
	course=variable_list.pop(0)
	domain=node.domain[course]
	# course_slots=calculate(slots,course_ltp[course][0],course_ltp[course][1],course_ltp[course][2])
	#to create variable number of for loops
	l=course_ltp[course][0]
	t=course_ltp[course][1]
	p=course_ltp[course][2]

	# print course_ltp

	# print l

	# num_loops=l
	# func_generator(num_loops)
	# from function import for_loop_function
	# l_list=[for_loop_function(slots)]
	# l_list=func_generator(num_loops)


	# print
	# num_loops=t
	# func_generator(num_loops)
	# from function import for_loop_function
	# t_list=for_loop_function(slots)

	# t_list=func_generator(num_loops)

	# print p
	# num_loops=p
	# func_generator(num_loops)
	# from function import for_loop_function
	# p_list=for_loop_function(slots)
	# p_list=func_generator(num_loops)

	# print len(l_list),len(t_list),len(p_list)


	slots=node.domain[course]

	if l==0:
		l_list=for_loop_function0(slots)
	elif l==1:
		l_list=for_loop_function1(slots)
	elif l==2:
		l_list=for_loop_function2(slots)
	elif l==3:
		l_list=for_loop_function3(slots)
	elif l==4:
		l_list=for_loop_function4(slots)
	elif l==5:
		l_list=for_loop_function5(slots)
	elif l==6:
		l_list=for_loop_function6(slots)

	slots=node.domain[course]

	if t==0:
		t_list=for_loop_function0(slots)
	elif t==1:
		t_list=for_loop_function1(slots)
	elif t==2:
		t_list=for_loop_function2(slots)
	elif t==3:
		t_list=for_loop_function3(slots)
	elif t==4:
		t_list=for_loop_function4(slots)
	elif t==5:
		t_list=for_loop_function5(slots)
	elif t==6:
		t_list=for_loop_function6(slots)

	# print p_slots

	slots=node.domain[course]

	p_slots=[]
	for sl in slots:
		if sl%10 >5:
			p_slots.append(sl)
	p_slots.sort()

	if p==0:
		p_list=for_loop_function0(p_slots)
	elif p==1:
		p_list=for_loop_function1(p_slots)
	elif p==2:
		p_list=for_loop_function2(p_slots)
	elif p==3:
		p_list=for_loop_function3(p_slots)
	elif p==4:
		p_list=for_loop_function4(p_slots)
	elif p==5:
		p_list=for_loop_function5(p_slots)
	elif p==6:
		p_list=for_loop_function6(p_slots)


	if p==0:
		p_list=[[]]
	elif p==1:
		p_list=p_slots
	elif p==2:
		p_list=[[16,17],[17,18],[36,37],[26,27],[27,28],[37,38],[46,47],[47,48],[56,57],[57,58],[46,47],[47,48],[56,57],[57,58]]
	elif p==3:
		p_list=[[16,17,18],[26,27,28],[36,37,38],[46,47,48],[56,57,58]]
	# print (l,t,p)
	# print (len(l_list),len(t_list),len(p_list))

	for i in l_list:
		node.state[course][0]=copy.deepcopy(i)
		node.course_changed=course
		if(Lecture_constraint_6(node)!=True):
			continue
		for j in t_list:
			node.state[course][1]=copy.deepcopy(j)
			node.course_changed=course
			if(Tutorial_constraint_3(node)!=True):
				continue
			if(Professor_constraint_8(node)!=True):
				# print("8----------")
				continue
			for k in range(len(p_list)):
				for m in range(k,len(p_list)):
					# print [i,j,[p_list[k],p_list[m]],1]
					node.state[course][0]=copy.deepcopy(i)
					node.state[course][1]=copy.deepcopy(j)
					node.state[course][2][0]=copy.deepcopy(p_list[k])
					node.state[course][2][1]=copy.deepcopy(p_list[m])
					node.state[course][3]=1
					node.course_changed=course
					
					# za=input("enter-")
					if(Laboratory_constraint_1(node)!=True):
						# print("1------")
						continue
					if(Laboratory_constraint_2(node,CSP)!=True):
						# print("2--------")
						continue
					if(Tutorial_constraint_3(node)!=True):
						# print("3---------")
						continue
					if(Disciplinary_constraint_4(node)!=True):
						# print("4---------")
						continue
					if(General_constraint_5(node)!=True):
						# print("5----------")
						continue
					if(Lecture_constraint_6(node)!=True):
						# print("6----------")
						continue
					if(Laboratory_constraint_7(node,CSP)!=True):
						# print("7---------")
						continue
					if(Professor_constraint_8(node)!=True):
						# print("8----------")
						continue
					if(Professor_constraint_9(node,CSP)!=True):
						# print("9----------")
						continue
					if(Student_Prof_constraint_10(node,CG)!=True):
						# print("10------------")
						continue
					# print node.state

					original=copy.deepcopy(node.domain)
					node.domain=propagate(node,CG,course)

					print_timetable(CSP,node.state,"DFS_BT_propagate")
					ans=DFS_BT_propagate(CSP, copy.deepcopy(variable_list),node,CG)
					if(ans[0]==True):
						return [True,node]

					else:
						node.domain=original
						continue
	node.state[course][3]=0
	return False,[]

def propagate(node,CG,course):
	state=node.state
	domain=copy.deepcopy(node.domain)


	lt=state[course][0]+state[course][1]

	for i in CG:
		for j in lt:
			if j in domain[i]:
				domain[i].remove(j)
	return domain


def degree_heuristic(CG):
	varlist=[]
	course_numc=[]
	for i in CG:
		course_numc.append((i,len(CG[i])))
	course_numc.sort(key=lambda(x): x[1])
	for i in course_numc:
		varlist.append(i[0])
	return varlist

def without_degree_heuristic(CG):
	varlist=[]
	course_numc=[]
	for i in CG:
		varlist.append(i)
	varlist.sort()
	return varlist

def print_timetable(csp,state,name):
	stdout=sys.stdout
	sys.stdout=open(name+".csv","w+")
	print "Courses,Professor,Day,Time,whether Lecture/Tutorial/Lab?,Room number(h-# or l-#)"
	prof_data=csp.prof_data
	course_prof={}
	for i in prof_data:
		for j in prof_data[i]:	
			if j not in course_prof:
				course_prof[j]=i
	# print prof_data
	# print course_prof
	slot_num={}
	for i in slots:
		slot_num[i]=[0,0]
	for i in state:
		for j in state[i][0]:
			print str(i)+","+course_prof[i]+","+Day[j//10]+","+Time[j%10]+","+"Lecture"+","+"H_"+str(slot_num[j][0]+1)
			slot_num[j][0]+=1
		for j in state[i][1]:
			print str(i)+","+course_prof[i]+","+Day[j//10]+","+Time[j%10]+","+"Tutorial"+","+"H_"+str(slot_num[j][0]+1)
			slot_num[j][0]+=1
		for j in state[i][2][0]:
			print str(i)+","+course_prof[i]+","+Day[j//10]+","+Time[j%10]+","+"Lab"+","+"L_"+str(slot_num[j][1]+1)
			slot_num[j][1]+=1
		for j in state[i][2][1]:
			print str(i)+","+course_prof[i]+","+Day[j//10]+","+Time[j%10]+","+"Lab"+","+"L_"+str(slot_num[j][1]+1)
			slot_num[j][1]+=1

	sys.stdout=stdout

# z=CSP()
# print_timetable(z,{'C_02': [[11, 21, 31], [], [[16, 17, 18], [26, 27, 28]], 1], 'C_03': [[13, 23, 33], [], [[16, 17], [36, 37]], 1], 'C_01': [[], [], [[], []], 0], 'C_06': [[], [], [[], []], 0], 'C_07': [[], [], [[], []], 0], 'C_04': [[26, 41, 51], [], [[47, 48], [56, 57]], 1], 'C_05': [[12, 22, 32], [], [[16, 17, 18], [26, 27, 28]], 1], 'C_08': [[62, 63, 64], [64], [[], []], 0], 'C_09': [[], [], [[], []], 0], 'C_11': [[], [], [[], []], 0], 'C_10': [[], [], [[], []], 0], 'C_12': [[], [], [[], []], 0]})