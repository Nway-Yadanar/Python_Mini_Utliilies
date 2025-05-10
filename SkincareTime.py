def show_product(name, description,skintype, weight, price):
    print(name)
    print(description)
    print(skintype)
    print(f"Weight: {weight}")
    print(f"Price: ${price}")
    buy = input("Will you buy this product? y/n: ")
    if buy == "y":
        receipt()
    else:
        skincare()



# Skincare Products (with functions)
def blacksoap():
    name = "Black Soap"
    description = "Moroccan black soap offers numerous benefits for the skin," \
    " including deep cleansing, exfoliation, moisturizing, and potential anti-aging effects." \
    " It's known for its ability to remove dead skin cells, unclog pores, and soothe irritation, making it suitable "
    "for various skin types, including acne-prone skin. "
    skintype = "Suitable for oily, dry, combination, and sensitive skin."
    weight = "200g"
    price = 18  
    show_product(name, description,skintype, weight, price)

def NilaSabounia():
    name = "Nila Sabounia"
    price = 20
    weight = "200g"
    skintype = "Suitable for acne-prone skin,sensitive, dry, oily, and combination skin "
    description ="This soap gently and effectively diminishes dark spots and " \
    "uneven skin tone, revealing a brighter, more even complexion.This daily essential is your key to a radiant, healthy glow. "
    show_product(name, description,skintype, weight, price)
    
def blackseedoil():
    name = "Black Seed Oil"
    price = 16
    weight = "30ml"
    skintype = "Suitable for dry, oily, and sensitive skin"
    description = "An ancient beauty secret rich in antioxidants and anti-inflammatory properties. This natural elixir, also known as Habbatus Sauda, helps to reduce acne, scars, and pigmentation for a more even skin tone. "
    show_product(name, description,skintype, weight, price)
    

def NilaScrub():
    name = "Nila Scrub"
    price = 18
    weight = "200ml"
    skintype = "Suitable for dry, oily, and sensitive skin"
    description = "Ultimate daily face care ritual with this exquisite Nila face scrub. Infused with the brightening power of Nila powder, this gentle exfoliator buffs away dullness and impurities, revealing a luminous, even-toned complexion."
    show_product(name, description,skintype, weight, price)

def Sahara():
    name = "Royal Sahara Facial"
    price = 18
    weight = "120g"
    skintype = "Royal Sahara Facial, crafted from Nila powder, brightens and diminishes the appearance of pigmentation, freckles, and sun damage." \
    "This powerful mask, enriched with minerals, refines pores and rejuvenates the complexion for a youthful glow. Suitable for all skin types, it combats dryness, dullness, and uneven texture, revealing radiant, healthy skin."
    description = "Ultimate daily face care ritual with this exquisite Nila face scrub. Infused with the brightening power of Nila powder, this gentle exfoliator buffs away dullness and impurities, revealing a luminous, even-toned complexion."
    show_product(name, description,skintype, weight, price)

def skincare():
     print("1. Black Soap\n2. Nila Sabounia\n3. Black Seed Oil\n4. Nila Scrub\n5. Royal Sahara Facial")
     choice = input("Choose: ")
     if choice == "1":
        blacksoap()
     elif choice == "2":
        NilaSabounia()
     elif choice == "3":
        blackseedoil()
     elif choice == "4":
        NilaScrub()
     elif choice == "5":
        Sahara()
     else:
        print("Invalid choice")
    
# Body Care Product (used with dictionaries)
body_products = {
    "1": {
        "name": "Terbrima Powder",
        "price": 20,
        "description": "A luxurious body mask crafted from an exquisite blend of herbs and flowers that gently purifies, deeply cleanses, and intensely nourishes, unveiling a luminous complexion and imparting a healthy, rosy glow as it rejuvenates the skin ",
        "weight": "200g"
    },
    "2": {
        "name": "Terbrima Mask",
        "price": 20,
        "benefits": "This exquisite blend of herbs and flowers gently purifies, cleanses, and nourishes, revealing a luminous complexion.",
        "weight": "200g"
    },
    "3": {
        "name": "Aker Fassi Sabounia",
        "price": 20,
        "benefits": "A traditional Moroccan body soap. Infused with the power of Aker Fassi powder, this daily essential combats acne, promotes elasticity, and unveils a youthful luminosity.",
        "weight": "200g"
    }
}

def bodycare():
    print("1. Terbrima Powder\n2. Terbrima Mask\n3. Aker Fassi Sabounia ")
    choice = input("Choose: ")
    product = body_products.get(choice)

    if product:
        print(f"{product['name']} - {product['benefits']}")
        print(f"Weight: {product['weight']}")
        print(f"Price: ${product['price']}")
    else:
        print("Invalid choice.")
        bodycare()








def start():
    print("Welcome to Harmony Skincare! We offer Moroccan Skincare for effortless beauty")
    print("1. Skincare\n2. Bodycare\n3. Haircare")
    care = input("Choose a category (1–3): ")

    options = {
        "1": skincare,
        "2": bodycare,
        # "3": haircare,
        
    }

    options.get(care)()

start()