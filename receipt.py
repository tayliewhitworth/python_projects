print("Welcome to my resturant!\n")
print("What would you like to order?(Enter the number for your order)\n")

meal = input("1.Cheeseburger with Fries\n2.Chicken Nuggets\n3.Salad\nEnter your order: ")

print(f"Thanks! You ordered {meal} \nHere is your receipt:")

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

print()
print('Thanks for stopping by!')

