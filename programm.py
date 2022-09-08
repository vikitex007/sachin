import random

winning_number = random.randint(0,100)

print(winning_number)

def guess_function(user_provided_number):
    game_over=False
    guess_counter=1
    while not game_over:
        if winning_number==user_provided_number:
            print(f"You won the game in {guess_counter} {'time' if guess_counter==1 else 'times'}")
            game_over=True
        else:
            if user_provided_number>winning_number:
                print('the number is too high')
            else:
                print("The number is too low")
            guess_counter +=1
            user_provided_number = int(input("Please guess again:"))
            
user_provided_num = int(input("Please provide your number:"))
print(guess_function(user_provided_num))