import random
import time

userScore=0
computerScore=0

choice=['r','p','s']

i=0

while i<10:
    UserChoices = input('Give me your choice (r)ock, (p)apper, (s)cissors')
    cpuChoices = random.choice(choice)
    print('Computer Choices', cpuChoices)

    UserChoices=UserChoices.lower()

    if len(UserChoices)==0:
        print('Try again')
        time.sleep(1)
    if UserChoices== cpuChoices:
        print('Draw')
    elif UserChoices== 'r' and cpuChoices == 'p':
        print('Computer Win')
        computerScore+=1
    elif UserChoices == 'p' and cpuChoices == 'r':
        print('User Win')
        userScore+=1
    elif UserChoices == 's' and cpuChoices == 'p':
        print('User Win')
        userScore += 1
    elif UserChoices =='p' and cpuChoices == 's':
        print('Computer Win')
        computerScore += 1
    elif UserChoices =='r' and cpuChoices =='s':
        print('User Win')
        userScore += 1
    elif UserChoices =='s' and cpuChoices == 'r':
        print('Computer Win')
        computerScore += 1
    else:
        print('Invalid type. Try again.')
        continue
    i+=1
print('User Score:',userScore,'Computer Score:',computerScore)


