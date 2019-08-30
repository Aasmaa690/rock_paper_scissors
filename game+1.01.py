
# coding: utf-8

# In[ ]:

def game() :
# this is the heart of the game 

    while True:
    # to keep the game running 
        x = input ('Please choose a tool to play ')
        # to assign a value to the input 
        y = 0 
        if x == 'rock':
            y= 1
        elif x =='paper':
            y = 2
        elif x == 'scissors ':
            y = 3
        # to assagin a value to the words 
        else:
            print ('this is an invalid choise  please try again')
            break
    
    
        import random 
        w=int (random.randint(1,3))
        # to make the computer choose a value 

        if w == 1:
            print (' The computer chose rock'.format())
        elif w == 2 :
            print ('the computer chose paper'.format())
        elif w == 3:
            print ('the computer chose scissors'.format())
        # to print the statements 
        
    
    
        if y == w :
            print ('there is no winner ')
            break
        elif y == 1 and w== 2 :
            print ('you lose , good  luck next time ')
            break
        elif y == 1 and w == 3 :
            print ('you win , congratulations ')
            break
    
        else:
            break
        # to print the results 

    
i=0 
while i < 3:
    w = input ('Do you want to play? ')
    if w =='yes':
        game()
        i = i+1
        # to end the game after three rounds
    elif w == 'no' : 
        print ('may be next time')    
        i = i+5
        # i = 5 to break out of the loop and end the game 
    else  : 
        print ('this is an invalid input please try again')    
        i = i+1
 # to start an end the game   


# In[ ]:



