import random

def is_win(user, computer):
    # return true if user win
    if(user == 'R' and computer == 'S') or (user == 'S' and computer == 'P') or \
        (user == 'P' and computer == 'R'):
        return True


def get_choice(choice):
    if choice == 'R':
        return "Rock"
    elif choice == 'P':
        return "Paper"
    elif choice == "S":
        return "Scissors"
    else:
        print('Symtax Error. Please Try again')

def main():
    print('Welcome to Rock, Paper, Scissor Game')
    print('R = Rock, [P]= Paper, [S]=Scissor and [Q] = Quit')

    choices = ['R','P','S']
    counter = 1
    game_on = True

    while game_on:
        user_choice = input(f'Game #{counter}. Please enter your choice: ')
        user_choice = user_choice.upper()

        if user_choice == 'Q':
            print('Thank for joining !')
            game_on = False 
        else:
            # random.choice(['r','p','s'])
            random_index = random.randint(0,2)
            computer_choice = choices[random_index]
            
            print(f"You selected: {get_choice(user_choice)} vs Computer choice: {get_choice(computer_choice)}")
            if user_choice == computer_choice:
                print('Tie')
            elif is_win(user_choice,computer_choice) == True:
                print('You win')
            else:
                print('You lose')
if __name__ == '__main__':
    main()