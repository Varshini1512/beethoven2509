products=[]
#CRUD Operation

def create_product(product):
    global products
    if len(products)==0:
        product.id=1
    else:
        product.id=products[len(products)-1].id+1
 
    products.append(product)



def readall():
     return products

def readby_id(id):
     for product in products:
          if product.id==id:
            return product
     return None

def update_product(product):
     old_product=readby_id(product.id)
     if old_product==None:
         return
     old_product.name=product.name
     old_product.description=product.description
     old_product .category=product.category
     old_product.tags=product.tags
     old_product.stock=product.stock
     old_product.price=product.price
     

def deleteby_id(id):
    product=readby_id(id) #madeamistake check it in chatgpt
    products.remove(product) 