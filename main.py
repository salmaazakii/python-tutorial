# import math
#
# print(math.ceil(2.1))
#
# print('Salma')
# print('+---+')
# print('|   |')
# print('+---+')
#
# name = input('what is your name?')
# print('welcome ' + name)


#Weight converter program
weight = int(input('Weight: '))
unit = input('(K)Kilograms or (G)Grams: ')
if unit.lower() == 'k':
    converted = weight * 1000
    print(f"You are {converted} grams")
else:
    converted = weight / 1000
    print(f"You are {converted} kilograms")


#Guessing game
secret_number =9
guess_count = 0
guess_limit = 3
while guess_count <3:
    guess = int(input('Guess: '))
    guess_count +=1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed')


#Car Game
command = ""
while True:
    command = input("> ").lower()
    if command == 'start':
        print('car started ...')
    elif command == 'stop':
        print('car stopped.')
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    elif command == 'quit':
        break
    else:
        print("sorry, I don't understand that")


