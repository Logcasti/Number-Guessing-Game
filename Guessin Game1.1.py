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

                           
                   
    
                         

                

'''============================================================================
Lv1                              Easy Part
============================================================================'''
print('Guess my number its between 0 and 20')
x=13
Lv1_Try=0
while True:
    while True:
        number_out=Pick_Number()
     
        

        if x<number_out:
            print('go lower')
            Lv1_Try=Lv1_Try+1
            continue
        elif x>number_out:
            print('go higher')
            Lv1_Try=Lv1_Try+1
            continue
        else:
            print('You got the number!')
            Lv1_Try=Lv1_Try+1
            break
    if Continue_Level()==False:
        Lv1_Try=0
        continue
    else:
        break
print('Took you '+str(Lv1_Try)+' tries')

            
       
    
'''============================================================================
 Lv2                                  Hard Part
============================================================================'''
import random

Lv2_Try=0
print('My number is between 1 and 50')

while True:
    Rnd_Num=random.randint(0,50)
    Areal=Rnd_Num-7
    Areag=Rnd_Num+7
    while True:
        number_out=Pick_Number()
        if Rnd_Num==number_out:
            print('you got it')
            Lv2_Try=Lv2_Try+1
            break
        elif (Areal<=number_out) and (number_out<Rnd_Num):
            print('Within 7, maybe go higher :]')
            Lv2_Try=Lv2_Try+1
            continue
        elif (Rnd_Num<number_out) and (number_out<=Areag):
            print('Within 7, maybe go lower :p')
            Lv2_Try=Lv2_Try+1
            continue
        else:
            print('Not even close')
            Lv2_Try=Lv2_Try+1
            continue
    if Continue_Level()==False:
        Lv2_Try=0
        continue
    else:
        break
print('Took you '+str(Lv2_Try)+' tries')
'''============================================================================
Lv3                                   Hardest Part
============================================================================'''
Lv3_Try=0

while True:
    Random1=random.randint(-10,30)
    Random2=random.randint(31,60)
    print('My number is between '+str(Random1)+' and ' +str(Random2))
    Rnd_Num=random.randint(Random1,Random2)
    
    while True:
        number_out=Pick_Number()

        if Rnd_Num<number_out:
            print('go lower')
            Lv3_Try=Lv3_Try+1
            continue
        elif Rnd_Num>number_out:
            print('go higher')
            Lv3_Try=Lv3_Try+1
            continue
        else:
            print('You got the number!')
            Lv3_Try=Lv3_Try+1
            break
    if Continue_Level()==False:
        Lv3_Try=0
        continue
    else:
        break
print('Took you '+str(Lv3_Try)+' tries')

Full_Tries=Lv1_Try + Lv2_Try + Lv3_Try

print('''
You Did it, you beat all of my levels!
''')

print('Took you '+str(Full_Tries)+ ' tries')


