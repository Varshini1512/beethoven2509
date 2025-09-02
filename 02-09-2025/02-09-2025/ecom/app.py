from product_manager import create_product,deleteby_id,readall,readby_id,update_product
from product import Product

def menu():
     message='''
The menu choices are
 1-Create Product
 2-Read All Products
 3-Read By id
 4-Update
 5-Delete
 6-Exit/Logout
 Your choice:'''
     choice=int(input(message))
     if choice==1:
          name=input('Name:')
          description=input('Description:')
          category=input('Category:')
          tags=input('Tags:')
          stock=int(input('Stock:'))
          price=int(input('Price:'))
          id=-1

          product=Product(id,name,description,category,tags,stock,price)
          create_product(product)
          print('Product created successfully')

     elif choice==2:
        products=readall()
        print('Products')
        for product in products:
            print(product)

     elif choice==3:
        id=int(input('ID'))
        product=readby_id(id)
        if product==None:
            print("Product not found")
        else:
            print(product)

     elif choice==4:
            id=int(input('ID:'))
            old_product=readby_id(id)
            if old_product==None:
                 print("Product not found")
            else:
               print(old_product)
               name=input('Name:')
               description=input('Description:')
               category=input('Category:')
               tags=input('Tags:')
               stock=int(input('Stock:'))
               price=int(input('Price:'))
               new_product=Product(id,name,description,category,tags,stock,price)
               update_product(new_product)
               print("Product updated successfully")
           

     elif choice==5:
          id=int(input('ID:'))
          old_product=readby_id(id)
          if old_product==None:
                 print("Product not found")
          else:
               print(old_product)
               if input("Are you want to delete(y/n)")=='y':
                    deleteby_id(id)
               print("Deleted Successfully")
     return choice

def menus():
     choice=menu()
     while choice!=6:
          choice=menu()
     print("Thank you for using app")
'''create_product(20000)
create_product(30000)
create_product(40000)
create_product(80000)

results=readall()

for product in results:
     print(product)

    
print(readby_product(40000))
print(readby_product(4000))
print(salaries[readby_product(40000)])
update_product(20000,25000)
deleteby_product(20000)
print(readall())'''

menus()