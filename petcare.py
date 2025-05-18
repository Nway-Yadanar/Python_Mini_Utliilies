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
        while True:
            feed = input("Will you feed me hooman y/n:  ").strip() .lower()
            if feed != 'y':
                print("Okkk hooman.. may be later")
                break
        
            feed= input("You can feed me 1. Pizza🍕 2. Sushi🍣 3. Croissant🥐 and 4. Bubble Tea🧋  ").strip()
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
        
        while True:
            feed = input("Will you pet me hooman🥺 y/n:  ").strip() .lower()
            if feed != 'y':
                print("Okkk hooman.. may be later")
                break
            else:
                print ("Happi❤️")
                self.love += 10
          
    
    def about(self):
        print(f"Name: {self.name}")
        print(f"Happiness: {self.happiness}%")
        print(f"Energy: {self.food}%")
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
        while True:
            play = input("Will you play with me hooman y/n:  ").strip() .lower()
            if play != 'y':
                print("Okkk hooman.. may be later")
                break
            print("fetching the ball...⚽")
            self.happiness +=10

class Cat(Pet):
    def make_sound(self):
        print("Meow")
    
    def nap(self):
        while True:
            nap = input("Will you let me nap y/n:  ").strip() .lower()
            if nap != 'y':
                print("Okkk hooman.. may be later")
                break
            print("Purrrr....😸😴")
            self.happiness +=10

        

class Penguin(Pet):
    def slide(self):
        while True:
            slide = input("Let's slide on the ice! y/n:  ").strip() .lower()
            if slide != 'y':
                print("Okkk hooman.. may be later")
                break
            print("🐧Wheee! I'm sliding on the ice⛸️")
            self.happiness +=10
        

print("Here's your virtual pet options. Choose 1,2 or 3.")
pet = input("1. Penguin 2. Dog 3. Cat :  ")
if pet == '1':
    name = input("What would you like to name your penguin? ")
    manchot = Penguin(name) 
    manchot.introduce()
    manchot.feed()       
    manchot.pet()
    manchot.slide()
    manchot.about()

if pet == '2':
    name = input("What would you like to name your dog? ")
    chien = Dog(name) 
    chien.introduce()
    chien.make_sound()
    chien.feed()
    chien.pet()
    chien.fetch()
    chien.about()

if pet == '3':
    name = input("What would you like to name your cat? ")
    chat = Cat(name) 
    chat.introduce()
    chat.make_sound()
    chat.feed()
    chat.pet()
    chat.nap()
    chat.about()