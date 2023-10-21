class Student:
    group = "C2016"
    counter = 0
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Student.counter += 1
        print("The object was created")
    def grow(self, height=1):
        self.height = height

    def __str__(self):
        return f"I'm name {self.name}. My age is {self.age}"
    def __del__(self):
        print("Object is delete")

nick = Student( "Nick", 16, 165, )
print(nick.age)
print(nick.height)



# print (Student.group)
#
# print (nick.name)
# print (nick.group)
# kate = Student (name: "Ekaterina", age: 17, height: 175, )
# print (kate.age)
# print (kate.height)
# print(kate.name)
# print(kate.group)
# print(Student.counter)
# elena Student ("Elena", age: 18, height: 155, name: )
# print (Student.counter)
# print("Height Nick", nick.height)
# nick.grow()
# print("Height Nick", nick.height)

# print(nick.name)
# kate = Student('Kate')
#
# print (kate.name)
# nick.age = 16
# print(nick.age)
# print (kate.age)
# kate.height = 175
# print(kate.height)