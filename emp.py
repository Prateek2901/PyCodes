
class Employee:
	empCount=0
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
		Employee.empCount+=1
	def displayCount(self):
		print "Total employee %d"%Employee.empCount
	def displayEmployee(self):
		print "Name:",self.name,"Salary",self.salary
	def print_salary(self):
		if(self.salary>10000):
			print "Salary is Greater then 10000",self.salary

ini=1
obj=list()
while ini != 0:

	n=raw_input("Name")	
	s=int(raw_input("Salary"))
	emp=Employee(n,s)
	emp.displayEmployee()
	obj.append(emp)
	print ("Press 0 to exit\nPress 1 for new Employee")
	ini =int(raw_input("Your Choice"))
	
for e in obj:
		
	e.print_salary();
