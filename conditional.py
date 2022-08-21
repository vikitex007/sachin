# conditional statement in python



name= input("What is your name please?")
age= int(input("what is your age please"))



if age < 0:
    print(f"Invalid Age")
    
elif age==10:
    print(f"Dear {name}, Your ticket price is: 100")
       
elif age>10:
    print (f"Dear {name}, Your ticket price is: 150")
    
else:
    print(f"Dear {name}, Your ticket price is: 50")
    
    


def calc_weight(m,g=10):
    print(f"Your weight is:{m*g}N ")
    
    
mass = int(input("please enter your mass:"))
print(calc_weight(mass))  

# Today's question:
#1  Ask a two integer number with user and a function should return their addition
#2  Ask an information of your laptop and a function should return like this: 
""" 
Brand_Name Model_Name available_at Price
Ex: Dell Vostro @ Rs. 80000
"""

#1
'''
def add(num1,num2):
    sum = num1+num2
    return(sum)
FNum = int(input("enter first number: "))
SNum = int(input("Enter second number: "))
sum = add(FNum, SNum)
print(f"Sum is {sum}")
Brand_Name = input("Enter brand name:")
Model_Name = input("Enter model name:")
price = int(input("Enter price"))
def laptop_specs(brand, model, price):
    print(f"The laptop is {brand}, {model} @ Rs.{price}")
mylaptop=laptop_specs(Brand_Name, Model_Name, price)
print(mylaptop)
'''

# Working model of atm machine:

total_price = 0
card_type = "visa"
is_same_bank = True
is_expired=False

def read_card():
    print("Fetching Card Details from bank ....")
    card_details = [1200,True,False]
    total_price = card_details[0]
    is_same_bank=card_details[1]
    is_expired= card_details[2]
    if is_expired:
        print("Sorry, this card can not be accepted here")
    else:
        perform_tansaction(total_price,is_same_bank)


def perform_tansaction(total_amt, is_same_bank):
    charge = 0
    if not is_same_bank:
        charge = 5
        if required_amt > total_amt:
            return "Not enough balance"
        else:
            print(f"Ant withdrwn: {required_amt}")
            print(f"Remaining available balance: {total_amt-required_amt-charge}")
    else:
        if required_amt > total_amt:
            return "Not enough balance"
        else:
            print(f"Ant withdrwn: {required_amt}")
            print(f"Remaining available balance: {total_amt-required_amt-charge}")


print("Please insert your atm card:")
input()
print("Card inserted!!")
required_amt = int(input("Please enter a amount:"))
read_card()
