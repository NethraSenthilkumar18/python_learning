import random
number = random.randint(1,10)
user_num = int(input("Enter your number: "))
if(user_num == number):
    print("The two numbers are Same")
elif(user_num > number):
    print("too high")
else:
    print("too low")

        
    
   
