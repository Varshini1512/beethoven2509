salaries=[]
#CRUD Operation

def create_salary(salary):
    global salaries
    salaries.append(salary)



def readall():
     return salaries

def readby_salary(salary):
     for i in range(len(salaries)):
          if salaries[i]==salary:
            return i
     return -1

def update_salary(old_salary,new_salary):
     global salaries
     index=readby_salary(old_salary)
     salaries[index]=new_salary #updating the salary

def deleteby_salary(salary):
    global salaries
    index=readby_salary(salary)
    salaries.pop(index)