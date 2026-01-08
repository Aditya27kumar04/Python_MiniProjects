#To create a random strong password
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9',]
symbols = ['!','#','$','%','&','(',')','*','+']
print("Welcome to the PyPassword Generator")
nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbols= int(input("How many symbols would you like in your password?\n"))
nr_numbers= int(input("How many numbers would you like in your password?\n"))
#First changing them to lists as without lists we cannot change the order of password
#like it will just show 2 char 2 number 2 symbol in sequence,
#so for making it random we used lists here.
password_list = []
for char in range(0,nr_letter):
  password_list+=random.choice(letters)


for char in range(0,nr_symbols):
  password_list+=random.choice(symbols)


for char in range(0,nr_numbers):
  password_list+=random.choice(numbers)
random.shuffle(password_list)
password= ""
#Here we made password again because we want the output to be strings not in lists form
for char in password_list:
  password+=char
print(f"Your password is: {password}")