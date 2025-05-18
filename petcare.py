#for Inheritence
class Pet:
    def __init__(self,name):
        self.name = name
        self.food = 0
        self.love = 0
        self.happiness = 0 #for happiness meter

    def introduce(self):
        print(f"Hello. I am {self.name} and your virtual pet")

    def feed(self):
        feed = input("Will you feed me hooman y/n:  ").strip() .lower()
        if feed == 'y':
        
            feed= input("You can feed me 1. Pizza🍕 2. Sushi🍣 3. Croissant🥐 and 4. Bubble Tea🧋").strip()
            if feed == '1':
                print("Yayyyy.. You feed me pizza🍕")
                self.food += 30

            elif feed == '2':
                print("Yayyyy.. You feed me sushi🍣")
                self.food += 30
            elif feed == '3':
                print("Yayyyy.. You feed me Croissant🥐")
                self.food += 20
            else: 
                print("Yayyyy.. Bubble tea is delicious🧋")
                self.food += 15
    
    def pet(self):
        
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

class Dog(Pet):
    def make_sound(self):
        print("Woof")
    
    def fetch(self):
        # need to add more ball
        print("fetching the ball....")


class Cat(Pet):
    def make_sound(self):
        print("Meow")
    
    def nap(self):
        print("Purrrr....😸😴")

class Penguin(Pet):
    def slide(self):
        print("🐧Wheee! I'm sliding on the ice⛸️")
   

print("Here's your virtual pet options. Choose 1,2 or 3.")
pet = input("1. Penguin 2. Dog 3. Cat :  ")
if pet == '1':
    name = input("What would you like to name your penguin? ")
    manchot = Penguin(name) 
    manchot.introduce()
    manchot.feed()       
    manchot.pet()
    manchot.about()

if pet == '2':
    name = input("What would you like to name your dog? ")
    chien = Dog(name) 
    chien.introduce()
    chien.make_sound()
    chien.feed()
    chien.pet()
    chien.about()

if pet == '3':
    name = input("What would you like to name your cat? ")
    chat = Cat(name) 
    chat.introduce()
    chat.make_sound()
    chat.feed()
    chat.pet()
    chat.about()