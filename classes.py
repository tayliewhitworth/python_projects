class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f'Menu: {self.name} - available from {self.start_time} to {self.end_time}'

  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      if item in self.items:
        total_price += self.items[item]
      else:
        print(f'Item {item} is not found in menu')
    return f'The total is: ${total_price:.2f}'

brunch = Menu('brunch', {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)

early_bird = Menu('early bird', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)

print(early_bird.calculate_bill(['salumeria plate', "mushroom ravioli (vegan)"]))

dinner = Menu('dinner', {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)

kids = Menu('kids', {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)

print(kids)

print(brunch.calculate_bill(['home fries', 'pancakes', 'coffee']))

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return f'Address: {self.address}'

  def available_menus(self, time):
    items_available = []
    for item in self.menus:
      if time >= item.start_time and time <= item.end_time:
        items_available.append(item)
      else:
        print('No items available')
    return items_available



flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))


new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

print(new_installment)

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

arepas_menu = Menu('Take a\' Arepa', {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 20)

arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

arepa_biz = Business("Take a' Arepa", [arepas_place])

first_biz = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
