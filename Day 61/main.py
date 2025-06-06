class College:
    def __init__(self,name,address):
        self.name = name
        self.address  = address 
    def show(self):
        print(f"{self.name} is in {self.address}")

class Teachers(College):
    def __init__(self, t_name, id ):
        # Call parent class's __init__ method
        super().__init__("CCP", "Jamsoro")
        self.t_name = t_name
        self.id = id
    def show(self):
        print(f"{self.t_name} with id:{self.id} teaches in {self.name} in city {self.address}")


college_details = College("Cadet College Petaro", "Jamshoro")
print(college_details.name)
college_details.show()


teacher_1 = Teachers("Sir Anees" , 123)
teacher_2 = Teachers("Sir Asif Maqbool", 234)

teacher_1.show()
teacher_2.show()
