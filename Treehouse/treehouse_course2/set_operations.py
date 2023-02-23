turkey = {'turkey', 'cheese'}
vegetarian = {'tomato', 'onion', 'mushrooms'}
denver = {'tomato', 'eggs'}
bacon = ['mushrooms', 'eggs']

print(turkey.union(vegetarian, denver))


all_ingredients = turkey | vegetarian | denver
print(all_ingredients)


shared_ingredients = vegetarian.intersection(bacon, denver, turkey)
print(shared_ingredients)


print(vegetarian.intersection(bacon))
shared_ingredients = vegetarian & bacon & denver
print(shared_ingredients)

different_ingredients = vegetarian ^ bacon
print(different_ingredients) 


custom_ingredients = all_ingredients.difference(shared_ingredients)
print(custom_ingredients)


custom_ingredients_2 = all_ingredients - shared_ingredients
print(custom_ingredients_2)
print(custom_ingredients == custom_ingredients_2)