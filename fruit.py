class Fruit:
    type="tropical"

    def __int__(self,variety,shape,color):
        self.variety=variety
        self.shape=shape
        self.color=color
    
    def grow(self):
        return f"It grew to a {self.shape}"
    def die(self):
        return f"Lack of water has led to {self.variety} of fruit to die"
    def all(self):
        return f"The {self.variety} is of {self.shape} shape and {self.color}"