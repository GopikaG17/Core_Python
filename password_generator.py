import random
Alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
random.shuffle(Alphabets)
Numbers = ["1","2","3","4","5","6","7","8","9","0"]
random.shuffle(Numbers)
Symbols = ["~","!","@","#","$","%","^","&","*","(",")","_"]
random.shuffle(Symbols)
#a = Alphabets+Numbers+Symbols
#print(a)
user_alphabets=int(input("How much alphabets do you want:"))
user_numbers=int(input("How much number do you want:"))
user_symbols=int(input("How much symbol do you want:"))
alph=Alphabets[0:user_alphabets]
num=Numbers[0:user_numbers]
symb=Symbols[0:user_symbols]
password = alph+num+symb
random.shuffle(password)
print(password)