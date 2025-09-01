import salary_manager 

salary_manager.create_salary(20000)
salary_manager.create_salary(30000)
salary_manager.create_salary(40000)
salary_manager.create_salary(80000)

results=salary_manager.readall()

for salary in results:
     print(salary)

    
print(salary_manager.readby_salary(40000))
print(salary_manager.readby_salary(4000))
print(salary_manager.salaries[salary_manager.readby_salary(40000)])
salary_manager.update_salary(20000,25000)
salary_manager.deleteby_salary(20000)
print(salary_manager.readall())