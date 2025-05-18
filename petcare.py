#for Inheritence
class Pet:
    def __init__(self,name):
        self.name = name
        self.food = 0
        self.love = 0

    def introduce(self):
        print(f"Hello. I am {self.name} and your virtual pet")

    def feed(self):
        for i in range(5):
            feed= input("You can feed me 1. Pizza🍕 2. Sushi🍣 3. Croissant🥐 and 4. Bubble Tea🧋")
            if feed == 1:
                print("Yayyyy.. You feed me pizza🍕")
                self.food += 30
            elif feed == 2:
                print("Yayyyy.. You feed me sushi🍣")
                self.food += 30
            elif feed == 3:
                print("Yayyyy.. You feed me Croissant🥐")
                self.food += 20
            else: 
                print("Yayyyy.. Bubble tea is delicious🧋")
                self.food += 15
    
    def pet(self):
        for i in range (5):
            pet = input("Will you pet me hooman🥺 y/n").strip().lower()
            if pet == 'y':
                print ("Happi❤️")
                self.love += 10
            else:
                print("It's ok hooman🥺")
    
    def about(self):
        print(f"Name: {self.name}")
        print(f"Hunger level: {self.food}%")
        print(f"Love: {self.love}%")
        if self.food <= 15:
            print ("I'm about to die. Feed me more🥺")
        elif self.food >=20 or self.food <150:
            print ("Half energy but still hungry")
        else:
            print("Full energy")

class Cat(Pet):
    def make_sound(self):
        print("Meow")

print("Here's your virtual pet options. Choose 1,2 or 3.")
pet = input("1. Penguin 2. Dog 3. Cat :  ")
if pet == '3':
    name = input("What would you like to name your cat")