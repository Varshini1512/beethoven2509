#id,name,description,category,tags,stock
class Product:
    def __init__(self,id,name,description,category,tags,stock,price):
        self.id=id
        self.name=name
        self.description=description
        self.category=category
        self.tags=tags
        self.stock=stock
        self.price=price
    
    def __str__(self):
         return f'[id={self.id}, name={self.name}, description={self.description}, category={self.category}, tags={self.tags}, stock={self.stock}, price={self.price}]'
    
    def __repr__(self):
        return self.__str__()
    
mobile_Samsung=Product(1001,'Samsung M21','Good battery and camera quality','Mobile','mobile,smartphone',33,22000)  

print(mobile_Samsung)