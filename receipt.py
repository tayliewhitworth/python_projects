print("Welcome to my resturant!\n")
print("What would you like to order?(Enter the number for your order)\n")

meal = input("1.Cheeseburger with Fries\n2.Chicken Nuggets\n3.Salad\nEnter your order: ")

print(f"Thanks! You ordered #{meal} \nHere is your receipt:")

def get_meal():
    if meal == '1':
        meal_price = 10
        meal_name = "Cheeseburger with Fries"
    elif meal == '2':
        meal_price = 8
        meal_name = "Chicken Nuggets"
    else:
        meal_price = 12.50
        meal_name = "Salad"
    return meal_price, meal_name

meal_price, meal_name = get_meal()

def calculateBill(meal_price, taxRate):
    total = meal_price * (1 + taxRate)
    return total

my_total = calculateBill(meal_price, 0.13)


print(f'Food Item: {meal_name}\nPrice: ${meal_price:.2f}')
print(f'Total: ${my_total:.2f}')

tip = input("Do you want to leave a tip? (Yes or No): ")

if tip.lower() == 'yes':
    print("How much do you want to tip?")
    tip_choice = input("1.20%\n2.18%\n3.15%\nSelect the number with the tip amount you want: ")
else:
    print("Thanks for stopping by!")
    quit()

if tip_choice == '1':
    tip_amount = 0.2
    tip_percentage = '20%'
elif tip_choice == '2':
    tip_amount = 0.18
    tip_percentage = '18%'
else:
    tip_amount = 0.15
    tip_percentage = '15%'

new_total = my_total * (1.0 + tip_amount)
print(f'Your total including tip ({tip_percentage}) is: ${new_total:.2f}')
print()
print('Thanks for stopping by!')

