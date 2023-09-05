weight = int(input('Weight: '))
unit = input('(K)Kilograms or (G)Grams: ')
if unit.lower() == 'k':
    converted = weight * 1000
    print(f"You are {converted} grams")
else:
    converted = weight / 1000
    print(f"You are {converted} kilograms")