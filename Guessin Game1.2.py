#Functions

def Pick_Number():
    while True:
        try:
            number=int(input('Input a whole number:'))
            return number
        except ValueError:
                print('Type a number')
                continue
            

def Continue_Level():
    while True:
        try:
            Play_Again=int(input('''
    Input 0 to play level again
    Input 1 to continue

type 1/0 here:'''))
            
            if Play_Again==0:
                return False
            elif Play_Again==1:
                return True
            else:
                print('Please input 1 or 0')
                continue
        except ValueError:
            print('Please type 1 or 0')
            continue

                           

def Total_Tries(Lv:int,Lv2:int,Lv3:int)->str:
    Full_Tries=int(Lv)+int(Lv2)+int(Lv3)
    return str(Full_Tries)
                         

                

'''============================================================================
Lv1                              Easy Part
============================================================================'''
def L1():
    print('Guess my number its between 0 and 20')
    x=13
    Level_Try=0
    while True:
        while True:
            number_out=Pick_Number()
         
            

            if x<number_out:
                print('go lower')
                Level_Try=Level_Try+1
                continue
            elif x>number_out:
                print('go higher')
                Level_Try=Level_Try+1
                continue
            else:
                print('You got the number!')
                Level_Try=Level_Try+1
                break
        if Continue_Level()==False:
            Level_Try=0
            continue
        else:
            return str(Level_Try)

            
       
    
'''============================================================================
 Lv2                                  Hard Part
============================================================================'''
import random
def L2():
    print('My number is between 1 and 50')
    Level2_Try=0

    while True:
        Rnd_Num=random.randint(0,50)
        Areal=Rnd_Num-7
        Areag=Rnd_Num+7
        while True:
            number_out=Pick_Number()
            if Rnd_Num==number_out:
                print('you got it')
                Level2_Try=Level2_Try+1
                break
            elif (Areal<=number_out) and (number_out<Rnd_Num):
                print('Within 7, maybe go higher :]')
                Level2_Try=Level2_Try+1
                continue
            elif (Rnd_Num<number_out) and (number_out<=Areag):
                print('Within 7, maybe go lower :p')
                Level2_Try=Level2_Try+1
                continue
            else:
                print('Not even close')
                Level2_Try=Level2_Try+1
                continue
        if Continue_Level()==False:
            Level2_Try=0
            continue
        else:
            return Level2_Try
  
'''============================================================================
Lv3                                   Hardest Part
============================================================================'''
def L3():
    Level3_Try=0
    while True:
        Random1=random.randint(-10,30)
        Random2=random.randint(31,60)
        print('My number is between '+str(Random1)+' and ' +str(Random2))
        Rnd_Num=random.randint(Random1,Random2)
        
        while True:
            number_out=Pick_Number()

            if Rnd_Num<number_out:
                print('go lower')
                Level3_Try=Level3_Try+1
                continue
            elif Rnd_Num>number_out:
                print('go higher')
                Level3_Try=Level3_Try+1
                continue
            else:
                print('You got the number!')
                Level3_Try=Level3_Try+1
                break
        if Continue_Level()==False:
            Level3_Try=0
            continue
        else:
            return Level3_Try









game1=L1()
print('Took you '+str(game1)+' tries')

game2=L2()
print('Took you '+str(game2)+' tries')

game3=L3()

print('Took you '+str(game3)+' tries')




print('''
You Did it, you beat all of my levels!
''')


print('Took you '+Total_Tries(game1,game2,game3)+ ' tries')



while True:
    try:
        Final_Play=int(input('''Do you want to play the levels again?
                Input 0 for No
                Input 1 for level 1
                Input 2 for level 2
                Input 3 for level 3
                Input 4 to play all
            Input here:'''))
        if Final_Play==0:
            quit()
        elif Final_Play==1:
            game1=L1()
            print('Took you '+str(game1)+' tries')
            continue
        elif Final_Play==2:
            game2=L2()
            print('Took you '+str(game1)+' tries')
            continue
        elif Final_Play==3:
            game3=L3()
            print('Took you '+str(game1)+' tries')
            continue
        elif Final_Play==4:
            game1=L1()
            print('Took you '+str(game1)+' tries')

            game2=L2()
            print('Took you '+str(game2)+' tries')

            game3=L3()
            print('Took you '+str(game3)+' tries')
            print('''
            You Did it, you beat all of my levels!
            ''')
            print('Took you '+Total_Tries(game1,game2,game3)+ ' tries')
        else:
            print('Please enter 0,1,2,3,4')
            continue
    except ValueError:
        print('Please enter 0,1,2,3,4')
        continue
    



