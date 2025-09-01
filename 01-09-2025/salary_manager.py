salaries=[]
salaries.append(20000)
salaries.append(40000)
salaries.append(70000)


print(salaries)

search=40000
index=-1
I=0
for salary in salaries:
     if salary==search:
          index=search
          break
     I+=1


print(index)
salaries.remove(search)
print(salaries)