import random 
a =['rock','paper','scissor']



def game():
    c = 'y'
    u = 0
    y = 0
    print('Now you are playing amazing game of (rock , paper and scissor) .......')
    print('')
    print('***************************** START GAME *****************************')
    while (c == 'y'):
        print('')
        print("ROCK , PAPER , SCISSOR")
        b = input('==>')
        x = random.choice(a)
        if b == x or b.lower()== x:
            print('You:',b)
            print('CPU :',x)
            print('')
            print('Its a tie!')
        elif x == 'rock' and b.lower() == 'paper' :
            print('You:',b)
            print('CPU :',x)
            print('')
            print('Paper covers rock! You win!')
            print('You are just lucky ...')
            y = y+1
        elif x == 'paper' and b.lower() == 'scissor':
            print('You:',b)
            print('CPU :',x)
            print('')
            print('Scissors cuts paper! You win!')
            print('You are just lucky ...')
            y = y+1
        elif x == 'rock' and b.lower() == 'scissor':
            print('You:',b)
            print('CPU :',x)
            print('')
            print('Rock smashes scissors! You lose.')
            print('Haa.. haa ..')
            u = u+1
        elif x == 'paper' and b.lower() == 'rock':
            print('You:',b)
            print('CPU :',x)
            print('')
            print('Paper covers rock! You lose')
            print('Haa.. haa ..')
            u = u+1
        elif x == 'scissor' and b.lower() == 'paper':
            print('You:',b)
            print('CPU :',x)
            print('')
            print('Scissors cuts paper! You lose.')
            print('Haa.. haa ..')
            u = u+1
        elif x == 'scissor' and b.lower() == 'rock':
            print('You:',b)
            print('CPU :',x)
            print('')
            print('Rock smashes scissors! You win!')
            print('You are just lucky ...')
            y = y+1
        else:
            print('Wrong choice !!!!')
            print('Choises are : (rock/paper/scissor)')
            print('please try again from start')
            print('')
            continue

        print('')
        print('********************Round  End********************')
        print('')
        start(y,u)
        c = input('==>')
        if c == 'y' :
            continue
        elif c == 'n':
            print()
            print('*********************Final Scores*********************')
            print('')
            print('Your Points :',y)
            print('CPU points :',u)
            print('')
            print('')
            print('**************************END GAME*****************************')
        else:
            print('Wrong input')
            print('please try again from start')
            game()





            



def start(a,b):
    print("Enter Your Choice:")
    print('1.for continuing or exit')
    print('2. Scores board')
    p = int(input('==>'))
    if p == 2:
        print('*********************Scores Board*********************')
        print('')
        print('Your Points :',a)
        print('CPU points :',b)
        print('')
        print('******************************************************')
        start(a,b)
    elif p == 1:
        print('for continue enter ..("y")')
        print('for exit enter .. ("n")')
    else:
        print('Invalid Option')
        print('please try again   .....')
        print('')
        start(a,b)
    
















