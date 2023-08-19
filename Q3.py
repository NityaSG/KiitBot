shopping_list = []

while True:
    item = input("Enter an item for your shopping list: ")
    if item == 'DONE':
        break
    shopping_list.append(item)

print("Your shopping list:")
for item in shopping_list:
    print("- " + item)