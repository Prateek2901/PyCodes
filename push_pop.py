ar=list()
top=0
size=0
def push_(a,size_i):
	if len(ar)==size_i:
		print "Overflow"
	else:
		ar.append(a)

def pop_():
	if len(ar)==0:
		print "Underflow"
	else: 
		ar.pop()


size=raw_input("Enter the size")
size_i=int(size)

print "1 for PUSH\n2 for POP\n 0 to EXIT"

ini = raw_input("Enter your choice")
in_i=int(ini)

while in_i!=0:
	if in_i==1:
		no=raw_input("Enter the no to PUSHED")
		no_i=int(no)
		push_(no,size_i)
	
	if in_i==2:
		pop_()
	if in_i==3:
		print "ouptup start\n\n"
		for i in ar:
			print i
		print "\n\nouptup ends"
	if in_i==0:
		break
	print "1 for PUSH\n2 for POP\n3 to Display\n 0 to EXIT"
	ini = raw_input("Enter your choice")
	in_i=int(ini)