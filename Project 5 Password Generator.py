import random
print("Welcome to Password Generator")
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
print("How many letters would you like in your password?")
your_letters=int(input())
print("How many symbols would you like?")   
your_symbols=int(input())
print("How many numbers would you like?")
your_numbers=int(input())
password=""
for i in range(0,your_letters):
    password+=random.choice(letters)
for i in range(0,your_symbols):
    password+=random.choice(symbols)
for i in range(0,your_numbers):
    password+=random.choice(numbers)
password_list=list(password)
random.shuffle(password_list)
final_password = "".join(password_list)
print(f"Your password is: {final_password}")
