from salary_manager import create_salary,salaries,deleteby_salary,readall,readby_salary,update_salary

def menu():
     message='''
 1-Create Salary
 2-Read All Salaries
 3-Read By Salary
 4-Update
 5-Delete
 6-Exit/Logout
'''
     choice=int(input(message))
     if choice==1:
          salary=int(input('Salary:'))
          create_salary(salary)
     elif choice==2:
        result_salaries=readall()
        print('Salaries')
        for salary in result_salaries:
            print(salary)
     elif choice==3:
        salary=int(input('Search salary'))
        index=readby_salary(salary)
        if salary==-1:
            print("Salary not found")
        else:
            print(f'Salary is at index{index}')
     elif choice==4:
            salary=int(input('Salary to update:'))
            new_salary=int(input('New Salary:'))
            update_salary(salary,new_salary)
     elif choice==5:
          salary=int(input('Salary to delete:'))
          deleteby_salary(salary)
     return choice

def menus():
     choice=menu()
     while choice!=6:
          choice=menu()
     print("Thank you for using app")
'''create_salary(20000)
create_salary(30000)
create_salary(40000)
create_salary(80000)

results=readall()

for salary in results:
     print(salary)

    
print(readby_salary(40000))
print(readby_salary(4000))
print(salaries[readby_salary(40000)])
update_salary(20000,25000)
deleteby_salary(20000)
print(readall())'''

menus()