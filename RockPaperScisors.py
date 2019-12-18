import random



#ascii art for outcomes of the game
def show_moves(player, computer):
    print('entered')
    # rock rock
    if player == 0 and computer == 0:
        print(' <Your choice>   <Computers choice>')
        print('    _______       _______   \n---\'   ____)     (____   \'---')
        print('      (_____)    (_____)\n      (_____)    (_____)      ')
        print('      (____)     (____)\n---.__(___)\'     \'(___)__.---')
    # rock paper
    elif player == 0 and computer == 1:
        print(' <Your choice>   <Computers choice>')
        print('    _______           _______\n---\'   ____)     ____(____    \'---')
        print('      (_____)   (______          \n      (_____)   (_______          ')
        print('      (____)     (_______ \n---.__(___)        (__________.---')
    # rock scissors
    elif player == 0 and computer == 2:
        print(' <Your choice>   <Computers choice>')
        print('    _______            _______\n---\'   ____)      ____(____   \'---')
        print('      (_____)    (______\n      (_____)   (__________')
        print('      (____)          (____)\n---.__(___)            (___)__.---')
    #paper rock
    elif player == 1 and computer == 0:
        print(' <Your choice>   <Computers choice>')
        print('     _______             _______\n---\'    ____)____       (____   \'---')
        print('           ______)     (_____)      \n          _______)     (_____)')
        print('         _______)       (____)\n---.__________)          (___)__.---')
    # paper paper
    elif player == 1 and computer == 1:
        print(' <Your choice>   <Computers choice>')
        print('     _______                   _______     \n---\'    ____)____         ____(____    \'---')
        print('           ______)       (______           \n          _______)       (_______          ')
        print('         _______)         (_______         \n---.__________)              (__________.---')
    # paper scissors
    elif player == 1 and computer == 2:
        print(' <Your choice>   <Computers choice>')
        print('     _______                 _______\n---\'    ____)____       ____(____   \'---')
        print('           ______)     (______\n          _______)    (__________')
        print('         _______)           (____)\n---.__________)              (___)__.---')
    # scissors rock
    elif player == 2 and computer == 0:
        print(' <Your choice>   <Computers choice>')
        print('    _______              _______\n---\'   ____)____       (____   \'---')
        print('          ______)     (_____)\n       __________)    (_____)')
        print('      (____)           (____)\n---.__(___)             (___)__.---')
    # scissors paper
    elif player == 2 and computer == 1:
        print(' <Your choice>   <Computers choice>')
        print('    _______                  _______\n---\'   ____)____       ____(____    \'---')
        print('          ______)     (______\n       __________)    (_______')
        print('      (____)            (_______\n---.__(___)              (__________.---')
    # scissors scissors
    elif player == 2 and computer == 2:
        print(' <Your choice>   <Computers choice>')
        print('     _______              _______ \n---\'   ____)____     ____(____    \'---')
        print('          ______)   (______  \n       __________) (__________   ')
        print('      (____)              (____)\n---.__(___)                (___)__.---')


def win_conditions(player, computer):
    if player == 0:
        if computer == 0:
            return 3
        if computer == 1:
            return 2
        if computer == 2:
            return 1
    elif player == 1:
        if computer == 0:
            return 1
        elif computer == 1:
            return 3
        elif computer == 2:
            return 2
    elif player == 2:
        if computer == 0:
            return 2
        if computer == 1:
            return 1
        if computer == 2:
            return 3
    else:
        print('There was an error in win conditions')
        return 0


def game():
    run_till_false = True
    winner = False
    player_score = 0
    comp_score = 0
    score = [player_score, comp_score]
    player_inp = 0
    comp_inp = 0

    while run_till_false:
        length = input('What game length would you like... first to: ')
        while not winner:

            player_inp = input('0 - Rock,1 - Paper, or 2 - Scissors?')
            while int(player_inp) >= 3:
                player_inp = input('That is not a valid input. 0 - Rock,1 - Paper, or 2 - Scissors?')
            comp_inp = random.randint(0, 2)
            show_moves(int(player_inp), comp_inp)
            if win_conditions(int(player_inp), comp_inp) == 1:
                player_score += 1
                print('you won the round!')
            elif win_conditions(int(player_inp), int(comp_inp)) == 2:
                comp_score += 1
                print('you lost the round!')
            elif win_conditions(int(player_inp), int(comp_inp)) == 3:
                print('It was a tie! no points awarded.')
            score = [player_score, comp_score]
            if score[0] == int(length):
                winner = True
            elif score[1] == int(length):
                winner = True
            print('The current score is', str(score))
            input('press enter to continue...')
        if score[0] == int(length):
            print('You Win! Play again!')
        elif score[1] == int(length):
            print('You Lost, better luck next time.')
        run_till_false = False


def main():
    print('Welcome to Rock Paper Scissors! Do you have what it takes to win? \n')
    game()


if __name__ == '__main__':
    main()