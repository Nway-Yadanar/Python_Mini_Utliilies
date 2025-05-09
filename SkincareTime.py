def blacksoap():
    price = 18
    print("Moroccan black soap offers numerous benefits for the skin," \
    " including deep cleansing, exfoliation, moisturizing, and potential anti-aging effects." \
    " It's known for its ability to remove dead skin cells, unclog pores, and soothe irritation, making it suitable "
    "for various skin types, including acne-prone skin. ")
    print(f"Price: ${price}")

def NilaSabounia():
    price = 19
    print("Moroccan black soap offers numerous benefits for the skin," \
    " including deep cleansing, exfoliation, moisturizing, and potential anti-aging effects." \
    " It's known for its ability to remove dead skin cells, unclog pores, and soothe irritation, making it suitable "
    "for various skin types, including acne-prone skin. ")
    print(f"Price: ${price}")
    

def skincare():
     print("1. Black Soap\n2. Nila Cream")
     choice = input("Choose: ")
     if choice == "1":
        blacksoap()
     elif choice == "2":
        NilaSabounia()
     else:
        print("Invalid choice")


def start():
    print("Welcome to Harmony Skincare! We offer Moroccan Skincare for effortless beauty")
    print("1. Skincare\n2. Bodycare\n3. Haircare")
    care = input("Choose a category (1–3): ")

    options = {
        "1": skincare,
        # "2": bodycare,
        # "3": haircare,
        
    }

    options.get(care)()

start()