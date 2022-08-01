with open('recipes') as file:
    cook_book = {}
    for line in file:
      dish_name = line.strip()
      ingredients_list = []
      for item in range(int(file.readline())):
          ingredient_dict = {}
          name, quantity, measure = file.readline().split(" |")
          ingredient_dict['ingredient_name'] = name.strip(' \n')
          ingredient_dict['quantity'] = int(quantity.strip(' \n'))
          ingredient_dict['measure'] = measure.strip(' \n')
          ingredients_list.append(ingredient_dict)
      cook_book[dish_name] = ingredients_list
      file.readline()
print('cook_book =', cook_book)

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for items in dishes:
    for keys, values in cook_book.items():
      if keys in items:
        for value in values:
          shop_list[value.pop('ingredient_name')] = value
          value['quantity'] *= person_count
  return shop_list
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))