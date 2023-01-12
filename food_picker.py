import requests
import random

url = 'https://www.themealdb.com/api/json/v1/1/random.php'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    random_meal = data['meals'][0]['strArea']
    print(f'You should eat {random_meal} food tonight')
else:
    print("No data")


search_meal = input('Want to search a meal? (Enter yes or no): ')

if search_meal == 'yes':
    search_input = input('What meal do you want to search? ')
    search_url = 'https://www.themealdb.com/api/json/v1/1/search.php?' # add {search}
    request_url = f'{search_url}s={search_input}'
    new_response = requests.get(request_url)
    meal_data = new_response.json()
    # meal = meal_data['meals'][0]['strMeal']
    meal_list = []
    try:
        for i in meal_data['meals']:
            # print(i['strMeal'])
            meal_list.append(i['strMeal'])
    except TypeError:
        print('There are no meals under that category')
    # print(meal)
else:
    print("Ok! See ya!")

meal_choice = random.choice(meal_list)
print(f'You should try {meal_choice}!')