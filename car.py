class Car:
    make="Mercede"

class Car:
    def __init__(self,make,model,colors):
        self.make=make
        self.model=model
        self.colors=colors

    def color(self):
        return f"The color of {self.make}is {self.colors}"
    def origin(self):
        return f"The car is {self.make}"
    
    def structure(self):
        return f"It is a{self.model}"
