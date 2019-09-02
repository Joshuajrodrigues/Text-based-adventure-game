import sys
print("Here is a small puzzle,To make it interesting i have made it invisible!")
print("Use the commands 'u' for up,'r'for right, 'l'for left and 'd' for down to move")
print("Every move is 1 unit")
print("To make it more challenging, the walls are made of sharp invisible glass")
print("You have a max health of 10")
print("LETS PLAY")

print("**********************************************************************************************************************************************************")

health = 10
direc='beg'
print("START:")
print("First move is UP : ")
#level0
while direc !='u':
    
    direc = input()

    if direc == 'u':
        print("Moved up a ladder, You can see a hatch but, its far above")


    else:
        health =health-1
        print('You hit a wall, health :'+str(health))
        if health == 0:
            print("YOU DIED ~ dark souls theme plays~")

#level1
direc2='beg'
while direc2 !='u':
    
    direc2 = input('Next move : ')

    if direc2 == 'u':
        print("Moved up a ladder again, You can see a hatch , its still far above")


    else:
        health =health-1
        print('You hit a wall, health :'+str(health))
        if health == 0:
            print("YOU DIED ~ dark souls theme plays~")
#level2
direc3='beg'
while direc3 !='u':
    
    direc3 = input('Next move: ')

    if direc3 == 'u':
        print("Moved up a ladder again, You can see a hatch , its closer now, maybe one more step")


    else:
        health =health-1
        print('You hit a wall, health :'+str(health))
        if health == 0:
            print("YOU DIED ~ dark souls theme plays~")        
#level3

direc4='beg'
while direc4 !='u':
    
    direc4 = input('Next move: ')

    if direc4 == 'u':
        print("You open the hatch and enter a dim lit room, you can smell the cheese but its very faint.\nYou were right! its alwys good to trust your gut when not sure\nMost of the time its always right")


    else:
        health =health-1
        print('You hit a wall, health :'+str(health))
        if health == 0:
            print("YOU DIED ~ dark souls theme plays~")
#level4
direc5='beg'
while direc5 !='r':
    
    direc5 = input('Next move: ')

    if direc5 == 'r':
        print("You move right.Its still dark, you can barely see anything, you should probably keep on going in this direction")


    else:
        health =health-1
        print('You hit a wall, health :'+str(health))
        if health == 0:
            print("YOU DIED ~ dark souls theme plays~")
#level5
direc6='beg'
while direc6 !='r':
    
    direc6 = input('Next move: ')

    if direc6 == 'r':
        print("As you walk on ahead you start hearing strange noises, always remember\nyou still have your secret move that even the programmer does not know, jump(j) but you can use it only once, for now do what all the superheroes do")


    else:
        health =health-1
        print('You hit a wall, health :'+str(health))
        if health == 0:
            print("YOU DIED ~ dark souls theme plays~")
#level6
direc7='beg'
while direc7 !='r':
    
    direc7 = input('Next move: ')

    if direc7 == 'r':
        print("That's weird, you are sure that the faint smell of cheese is still far away.\n Then what is this? and why is it kept on this strange metal instrument ? should you take it maybe ? ('g' to grab)\n Just ahead you see a hole that goes down")


    else:
        health =health-1
        print('You hit a wall, health :'+str(health))
        if health == 0:
            print("YOU DIED ~ dark souls theme plays~")
#level6.1
direc8='beg'
while direc8 !='j':
    
    direc8 = input('Next move: ')

    if direc8 == 'j':
        print("You jump over the strange metal cheese, and down the hole,its good to let gravity do it's job")
    elif direc8=='g':
        print('A mouse trap! YOU DIED ~faint dark souls music plays~')
        sys.exit()


    else:
        health =health-1
        print('You hit a wall, health :'+str(health))
        if health == 0:
            print("YOU DIED ~ dark souls theme plays~")
#level6.2
direc9='beg'
while direc9 !='d':
    
    direc9 = input('Next move: ')

    if direc9 == 'd':
        print("You enter a new room, there is a door to your left and right...What was your philosophy on things like this again ?")


    else:
        health =health-1
        print('You hit a wall, health :'+str(health))
        if health == 0:
            print("YOU DIED ~ dark souls theme plays~")
#level7
direc10='beg'
while direc10 !='r':
    
    direc10 = input('Next move: ')

    if direc10 == 'r':
        print("The door opens into a narrow hallway, you look up. The smell of cheese is getting stronger")


    else:
        health =health-1
        print('You hit a wall, health :'+str(health))
        if health == 0:
            print("YOU DIED ~ dark souls theme plays~")

#level8
direc11='beg'
while direc11 !='u':
    
    direc11 = input('Next move: ')

    if direc11 == 'u':
        print("You start climbing, this is it jut a few more steps")


    else:
        health =health-1
        print('You hit a wall, health :'+str(health))
        if health == 0:
            print("YOU DIED ~ dark souls theme plays~")
#level9
direc12='beg'
while direc12 !='u':
    
    direc12 = input('Next move: ')

    if direc11 == 'u':
        print("You see it, its probably the best looking cheese your mousy eyes have ever seen, you go to grab it")


    else:
        health =health-1
        print('You hit a wall, health :'+str(health))
        if health == 0:
            print("YOU DIED ~ dark souls theme plays~")

#level10
direc12='beg'
while direc12 !='g':
    
    direc12 = input('Next move: ')

    if direc12 == 'g':
        print("It look even better up close, you take a bite and fireworks go off inside your brain, so tasty !")
        print('The End, Your health: '+str(health))


    else:
        health =health-1
        print('You hit a wall, health :'+str(health))
        if health == 0:
            print("YOU DIED ~ dark souls theme plays~")
