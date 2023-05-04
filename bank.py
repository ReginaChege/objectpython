# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

# Discuss in your group and come up with the attributes and three methods (behaviours) for each class and implement them

# Then do the following in the interpreter 
# Create two instances of each class. 
# Call each of the methods you defined.

class Account:
    amount=2000

class Account:
    def __init__(self,amount,account_name,loan):
        self.amount=amount
        self.account_name=account_name
        self.loan=loan
  
    def widthdrawal(self):
        return f"my balance is{self.amount}"
    
    def deposit(self):
        return f"The owner is {self.account_name}"
    
    def insefficient(self):
        return f"You have insufficient balance, you can get a loan of{self.loan}"
    


        
