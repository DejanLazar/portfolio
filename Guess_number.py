"""In this program you can enter numbers between min an maximum, and then you have to guess which number was randomised by
program. When you guess it, you will be informed"""
import random 
while(True): #loop if error ocures
    try: #Checking if a value is a integer, if no error iz risen
        min = int(input("Please enter minimim value for a random range "))
        max = int(input("Please enter maximum value for a random range "))
        if (max<min): #Checking if max is more then min, if not values are swapped
            max,min = min, max
            print ("maximum is lower then minimum, values are swapped")
        x=random.randint(min, max) #random value is generated
        while(True): #loop for guessing
            try: #Checking if a guess number is integer
                guess = int(input("Please enter your guess between {} and {} ".format(min, max)))
                if x == guess:
                    print('YOU GUESSED A NUMBER!!!')
                    break
                else:
                    print('You didnt guess it :( please try again')
            except ValueError: #Error risen if not
                print("You didn't enter integer number, please do it again")
            continue    
        break
    except ValueError:
        print("You didn't enter integer number, please do it again")
        continue
              
 