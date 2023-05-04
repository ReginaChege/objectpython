
class Student:
    name="Emily"
    age=21
    school="AkiraChix"
    nationality="Kenya"
    room="khalahari"
class Student:
    school="Akirachix"
    
    def __init__(self,name,age,nationality):
        self.name=name
        self.age=age
        self.nationality=nationality
       
    def greet_student(self):
        return f"Hello {self.name} welcome to {self.school} proudly{self.nationality}"
    def housing(self):
        return f"Hello {self.name} welcome to {self.school} proudly{self.nationality} i stay at {self.room}"

# 1) Update the Student Class to include these attributes - first_name, last_name, age, country
#      - Add these methods to the Student class
#              - show_full_name
#              - year_of_birth
#              - show_initials
class Student:
    name="Regina"
    year0fbirth=1994
    school="AkiraChix"
    nationality="Kenyan"
    first_name="Wairimu"
    last_name="Chege"
    country="Kenya"
    age=29
class Student:
    school="Akirachix"
    
    def __init__(self,name,age,nationality,first_name,last_name,country,yearofbirth):
        self.name=name
        self.age=age
        self.nationality=nationality
        self.first_name=first_name
        self.last_name=last_name
        self.country=country 
        self.yearofbirth=yearofbirth 
    def greet_student(self):
        return f"Hello {self.name} welcome to {self.school} proudly{self.nationality}"
    def show_full_name(self):
        return f"{self.first_name}{self.last_name}"
    def year_of_birth(self):
        return f"{self.age}-"
    def show_initials(self):
        return f"{self.first_name[0]}{self.last_name[0]}"
   

