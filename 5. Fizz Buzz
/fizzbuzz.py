
countUpToMe = 50
thisNumber = 1

while thisNumber <= countUpToMe:

    if thisNumber % 3 == 0 and thisNumber % 5 == 0: # this has to go first to ensure that numbers like 15 and 30 don't get assigned "FIZZ"
        print("FIZZBUZZ!")
    elif thisNumber % 3 == 0:
        print('FIZZ!')
    elif thisNumber % 5 == 0:
       print('BUZZ!')
    else:
        print(str(thisNumber))

    thisNumber = thisNumber + 1

