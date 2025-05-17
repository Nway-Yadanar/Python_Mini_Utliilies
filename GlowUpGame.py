class player:
    def __init__(self,name, age, skintype):
        self.skinhealth = 25
        self.name = name
        self.age = int(age) #age nk sat lok mhr mo int change
        self.skintype = skintype

    def about(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Skin Type: {self.skintype}")
        print(f"Skin Health: {self.skinhealth}")
        if self.skinhealth <= 15:
            print ("You have to learn more about skincare")
        else:
            print ("You are doing great")

    def make_choice(self):
        print("It's your skincare time✨\n")
        facewash = input("Will you use facewash or water?").strip().lower()
        if facewash =="facewash":
            print("🫧Excellent choice. 5 points to you")
            self.skinhealth += 5
        else:
            print("Hmm...Just water is not enough💧. 5 points from you ")
            self.skinhealth -=5
        
        toner = input("After face wash, will you use toner?").strip().lower()
        if toner =="yes":
            print("🫧Optional but Excellent choice. 2 points to you")
            self.skinhealth += 2
        else:
            print("Hmm...Toner is optional💧.")

        moisturizer = input("Will you use moisturizer?").strip().lower()
        if moisturizer =="yes":
            print("🧴Excellent choice. 5 points to you")
            self.skinhealth += 5
        else:
            print("🧴Moisturizer is IMPORTANT. 5 points from you ")
            self.skinhealth -=5

        if self.age >= 25:
            print("👵 You might want to use anti-aging products in your routine.")
   

print("🎀 Welcome to Glow Up game 🎀")
name = input ("What's your name? ")
age  = input ("Tell me your age.. ")
skintype = input ("What's your skin type? ")
print("You will now have 25 points for skinhealth. " \
"For each choice you make, your points will be added or reduced." \
)
player = player(name, age, skintype)
player.make_choice()
player.about()