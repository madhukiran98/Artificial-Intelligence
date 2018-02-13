#Name T Naga Datta Madhu Kiran
#ID 2015A7PS0111P

import sys

def func_generator(num_loops):

	
	print "def for_loop_function"+str(num_loops)+"(slots):"
	print "\tcom_list=[]"
	print "\ti0=-1"
	# print "\t"+str(num_loops)
	count=1
	for i in range(num_loops):
		print "\t"*count+"for i"+str(count)+" in range(i"+str(count-1)+"+1"+",len(slots)):"
		count+=1
	sys.stdout.write("\t"*count+"com_list.append([")
	for i in range(1,num_loops+1):
		sys.stdout.write("slots[i"+str(i)+"],")
	print "])"
	print "\t"+"return com_list"
	print "\n\n\n\n\n\n"
	
stdout=sys.stdout
sys.stdout=open("combinations.py","w+")
print "#Name T Naga Datta Madhu Kiran"
print "#ID 2015A7PS0111P"
print "\n\n"
for i in range(8):
	func_generator(i)
sys.stdout=stdout