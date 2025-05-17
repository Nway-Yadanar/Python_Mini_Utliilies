#for Inheritence
class Pet:
    def __init__(self,name):
        self.name = name
print("Here's your virtual pet")
pet = input("1. Penguin 2. Dog 3. Cat")
if pet == 1:
    Cat()