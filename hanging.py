import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |

'''
print(logo)

stages = [ '''
  +---+
  |   |
      |
      |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

animal_name=["sheep","dog","goat","monkey"]
animal=(random.choice(animal_name))

animal_hidden=[]
for i in animal:
    animal_hidden.append("_")
print(animal_hidden)
      
life=6
while life>0:
    user_choice=input("Enter the letter:").lower()
    if user_choice in animal:
        for i in range(len(animal)):
            if animal[i]==user_choice:
                animal_hidden[i]= user_choice
        if "_" not in animal_hidden:
            print("\n You won!",animal)
            break
    else:
        life -=1
        print("Lives left:",life)
        print(stages[6 - life])
        if life == 0:
            print("you failed,",animal)
            print(stages[0])
    print(animal_hidden)
    
            
