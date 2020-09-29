# Rock - Paper - Scissors
countA = 0
countB = 0

while True: 
    print('This is the Rock-Paper-Scissors game\nPlease write: rock, paper or scissors')
    a = input('Player A - your turn:')
    while a != 'rock' and a != 'paper' and a != 'scissors':
        print('Player A: Input correct item: rock, paper or scissors')
        a = input('Player A - your turn:')
    b = input('Player B - your turn:')
    if b != 'rock' and b != 'paper' and b != 'scissors':
        print('Player B: Input correct item: rock, paper or scissors')
        b = input('Player B - your turn:')

    if a == b:
        print('Draw')
    elif (a == 'paper' and b == 'rock'):
        print('Player A wins')
        countA+=1
    elif (a == 'rock' and b == 'paper'):
        print('Player B wins')
        countB+=1
    elif (a == 'rock' and b == 'scissors'):
        print('Player A wins')
        countA+=1
    elif (a == 'scissors' and b == 'rock'):
        print('Player B wins')
        countB+=1
    elif (a == 'scissors' and b == 'paper'):
        print('Player A wins')
        countA+=1
    elif (a == 'paper' and b == 'scissors'):
        print('Player B wins')
        countB+=1

    if countA == 3 or countB == 3:
        print('Player A : Player B')
        print(countA, ':', countB)
        break

    finish = input('Would you like to play again? (Yes/No)')
    if finish == 'No' or finish == 'no':
        print('Player A : Player B')
        print(countA, ':', countB)
        break

    