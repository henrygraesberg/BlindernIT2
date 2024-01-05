class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.hobbies = []

    def addHobby(self, hobby: str):
        self.hobbies.append(hobby)

    def printHobbies(self):
        for i in self.hobbies:
            print(i)
    
    def printSelf(self):
        print(self.name)
        print(self.age)
        self.printHobbies()

def test():
    in_name = input("Skriv et navn: ")
    in_age = int(input("Skriv inn alder: "))

    person = Person(in_name, in_age)

    end = False

    while end is not True:
        in_hobby = input("Hva liker denne personen å gjøre? ")
        
        if in_hobby != "q":
            person.addHobby(in_hobby)
        else:
            end = True
    
    person.printSelf()

test()