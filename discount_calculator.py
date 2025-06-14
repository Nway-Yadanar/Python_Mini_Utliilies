total_amount = 10000
print("Your total amount is 10000")
age = int(input("Tell me your age: "))
if age <=5:
    actual_amount = total_amount - (total_amount * 0.5)
    print(f"You just need to pay {actual_amount} after discount of 50%")

elif age <=10:
    actual_amount = total_amount - (total_amount * 0.25)
    print(f"You just need to pay {actual_amount} after discount of 25%")

elif age <=13:
    actual_amount = total_amount - (total_amount * 0.1)
    print(f"You just need to pay {actual_amount} after discount of 10%")

else:
    print ("You're not in the discount range. You have to pay full price")