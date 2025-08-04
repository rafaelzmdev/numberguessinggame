print("Think of a number between 1 and 100. Good? Now let's go.")
print("I will say a random number and you will have to say if yours is higher or lower than the one I previously said. Good? Let's start.")
low = 1
high = 100
import random
firstrand = (random.randint(low, high))
print(firstrand)
first_feedback = str(input("Is your number higher, lower or the exact one I just described? Type 'higher', 'lower' or 'guess' just like so >> "))
while True:
    if first_feedback == 'higher':
        low = int(firstrand) + 1
        while True:
            secondrand = (random.randint(low, high))
            if secondrand > firstrand:
                print(secondrand)
                break
    elif first_feedback == 'lower':
        high = int(firstrand) - 1
        while True:
            secondrand = (random.randint(low, high))
            if secondrand < firstrand:
                print(secondrand)
                break
    elif first_feedback == 'guess':
        print("That was a good one. Thanks mate!")
        break
    break
second_feedback = str(input("Is your number higher, lower or the exact one I just described? Type 'higher', 'lower' or 'guess' just like so >> "))
while True:
    if second_feedback == 'higher':
        low = int(secondrand) + 1
        while True:
            thirdrand = (random.randint(low, high))
            if thirdrand > secondrand:
                print(thirdrand)
                break
    elif second_feedback == 'lower':
        high = int(secondrand) - 1
        while True:
            thirdrand = (random.randint(low, high))
            if thirdrand < secondrand:
                print(thirdrand)
                break
    elif second_feedback == 'guess':
        print("That was a good one. Thanks mate!")
        break
    break
third_feedback = str(input("Is your number higher, lower or the exact one I just described? Type 'higher', 'lower' or 'guess' just like so >> "))
while True:
    if third_feedback == 'higher':
        low = int(thirdrand) + 1
        while True:
            fourthrand = (random.randint(low, high))
            if fourthrand > thirdrand:
                print(fourthrand)
                break
    elif third_feedback == 'lower':
        high = int(thirdrand) - 1
        while True:
            fourthrand = (random.randint(low, high))
            if fourthrand < thirdrand:
                print(fourthrand)
                break
    elif third_feedback == 'guess':
        print("That was a good one. Thanks mate!")
        break
    break
fourth_feedback = str(input("Is your number higher, lower or the exact one I just described? Type 'higher', 'lower' or 'guess' just like so >> "))
while True:
    if fourth_feedback == 'higher':
        low = int(fourthrand) + 1
        while True:
            fifthrand = (random.randint(low, high))
            if fifthrand > fourthrand:
                print(fifthrand)
                break
    elif fourth_feedback == 'lower':
        high = int(fourthrand) - 1
        while True:
            fifthrand = (random.randint(low, high))
            if fifthrand < fourthrand:
                print(fifthrand)
                break
    elif fourth_feedback == 'guess':
        print("That was a good one. Thanks mate!")
        break
    break
fifth_feedback = str(input("This will be my last attempt! Is your number higher, lower or the exact one I just described? Type 'higher', 'lower' or 'guess' just like so >> "))
while True:
    if fifth_feedback == 'higher':
        low = int(fifthrand) + 1
        while True:
            lastrand = (random.randint(low, high))
            if lastrand > fifthrand:
                print(lastrand)
                break
    elif fifth_feedback == 'lower':
        high = int(fifthrand) - 1
        while True:
            lastrand = (random.randint(low, high))
            if lastrand < fifthrand:
                print(lastrand)
                break
        break
    break
lastfeedback = str(input("So, did I guess your number? Type 'y' or 'n' like so, here >> "))
if lastfeedback == 'y':
    print("Yess! It was nice to play with you, thanks!")
else:
    print("Aww. Maybe we could play again and you would give me another chance? ;)")


            
        


    
    
    