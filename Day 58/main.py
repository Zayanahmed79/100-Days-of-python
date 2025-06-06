class Person:

    def __init__(self , name , occupation):
        print("I am  a Person!")
        self.name  = name 
        self.occupation = occupation

    def info(self):
        print(f"My name is {self.name} and i am a {self.occupation}")

a = Person("Zayan", "Millionaire")
a.info()

b = Person("Hamdan" , "Billionaire")
b.info()


