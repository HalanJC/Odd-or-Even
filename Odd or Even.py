import random, time

limit=6
wickets=1
penalty=1
totaluserrun=0
totalairun=0
winner='NOBODY CUZ THE CODE MALFUNCTIONED'
rep='YES'

breaker='True'

while True:
    #CHOOSING ODD OR EVEN#
    while breaker=='True':
        print('Odd or Even ?')
        choose=input()
        if choose.isdigit():
            choose=int(choose)
            if choose%2==0:
                choose='Even'
                print("OK, I'll be Odd")
            elif choose%2==1:
                choose='Odd'
                print("OK, I'll be Even")
            breaker='False'
        elif choose=='Even' or choose=='EVEN' or choose=='even' or choose=='E' or choose=='e':
            print("OK, I'll be Odd")
            choose='Even'
            breaker='False'
        elif choose=='Odd' or choose=='ODD' or choose=='odd' or choose=='O' or choose=='o':
            print("OK, I'll be Even")
            choose='Odd'
            breaker='False'
        else:
            print('TYPE IN ODD OR EVEN')
            time.sleep(2)
            print("I'TS THAT EASY YOU IDIOT")
            print()
            time.sleep(1)
    breaker='True'
    
    #CHOOSING WHO'S CHOOSING IT IS#
    
    print('Throw')
    airun=random.randrange(1,limit+1)
    while breaker=='True':
        userrun=int(input())
        if userrun>0 and userrun<limit+1:
            breaker='False'
        elif userrun==0:
            print('No 0 in choosing')
        else:
            print('Between 1 and 6 dear')
    choosetotal=airun+userrun
    breaker='True'
    print(airun)
    if (choosetotal)%2==0:
        if choose=='Even':
            print('Your Choosing')
            chooser='user'
        elif choose=='Odd':
            print('My Choosing')
            chooser='ai'
    elif (airun+userrun)%2==1:
        if choose=='Even':
            print('My Choosing')
            chooser='ai'
        elif choose=='Odd':
            print('Your Choosing')
            chooser='user'
    
    #CHOOSING WHAT THE CHOSEN ONE CHOSE#
    
    if chooser=='user':
        while breaker=='True':
            print('Batting or Balling ?')
            choice=input()
            if choice=='Batting' or choice=='BATTING' or choice=='batting' or choice=='Bat'or choice=='BAT'or choice=='bat':
                choice='Batting'
                breaker='False'
            elif choice=='Balling' or choice=='BALLING' or choice=='balling'or choice=='Ball'or choice=='BALL'or choice=='ball':
                choice='Balling'
                breaker='False'
            else:
                print('ARE YOU ******* STUPID MATE')
                time.sleep(2.5)
                print('CAN YOU NOT READ ?')
                time.sleep(2.5)
                print('OR ARE YOU INCAPABLE OF FOLLOWING SIMPLE INSTRUCTIONS')
                time.sleep(2.5)
                print('JUST PICK BATTING OR BALLING YOU DUMB***')
                time.sleep(2.5)
            if choice=='Batting':
                print('Ok, My balling')
            elif choice=='Balling':
                print('Ok, My batting')
        breaker='True'
    elif chooser=='ai':
        choice=random.choice(['Batting','Balling'])
        if choice=='Batting':
            print('Ok, My balling')
            print('So, Your Batting')
        elif choice=='Balling':
            print('Ok, My batting')
            print('So, Your Balling')
    
    #THE ACTUAL GAME#
    
    userrun=0
    airun=-1
    wicket=wickets
    if choice=='Batting':
        
        while wicket>0:
            while userrun!=airun:
                airun=random.randrange(0,limit+1)
                userrun=input()
                print(airun)
                if userrun.isdigit():
                    userrun=int(userrun)
                    if userrun!=airun:
                        if userrun>0 and userrun<limit+1:
                            totaluserrun+=userrun
                        elif userrun==0:
                            totaluserrun+=airun
                        else:
                            print('YOU HAVE TO PICK BETWEEN 0 AND 6')
                            print("DON'T THINK I WON'T NOTICE")
                            print("I'M TAKING AWAY",penalty,"RUNS FROM YOU")
                            print("AND I'LL KEEP INCREASING THE PENALTY")
                            print('SO PLAY WISELY')
                            totaluserrun-=penalty
                            penalty+=1
                else:
                    print('HOW STUPID ARE YOU ?')
                    print('DO YOU NOT KNOW HOW TO PLAY ?')
                    print('DOES',userrun,'LOOK LIKE A NUMBER TO YOU')
                    print('YOUR GETTING A PENALTY')
                    print("I'M TAKING AWAY",penalty,"RUNS FROM YOU")
                    print("AND I'LL KEEP INCREASING THE PENALTY")
                    print('SO GROW A BRAINCELL AND PLAY')
                    totaluserrun-=penalty
                    penalty+=1
            wicket-=1
        if totaluserrun==0:
            print('DUCK!')
            print('LOSER!')
        else:
            print('OUT')
            print('You scored',totaluserrun)
            print('I need',totaluserrun+1,'runs to win')
            print('Lets Begin')
        
        
        
        airun=0
        userrun=-1
        wicket=wickets
        while wicket>0:
            while airun!=userrun and totaluserrun>=totalairun:
                airun=random.randrange(0,limit+1)
                userrun=input()
                print(airun)
                if userrun.isdigit():
                    userrun=int(userrun)
                    if userrun>=0 and userrun<limit+1:
                        totalairun+=airun
                    elif airun==0:
                        totalairun+=userrun
                    else:
                        print("I don't care if you chose a wrong number")
                        print("It's my batting")
                        print('Do whatever the fuck you want')
                        print("I'm still getting my runs")
                else:
                    print("I don't care if you chose a number or not")
                    print("I'm still getting my runs")
            wicket-=1
        
        if airun==userrun:
            print('OUT!')
            print('I scored',totalairun,'runs')
            winner='User'
        elif totalairun==0:
            print('FUCK YOU DUCKED ME!')
            if totaluserrun==0:
                winner='Draw'
            else:
                winner='AI'
        elif airun>userrun:
            print('Game Over!')
            winner='AI'
    
    #THE BALLING#
    
    elif choice=='Balling':
        
        while wicket>0:
            while airun!=userrun:
                airun=random.randrange(0,limit+1)
                userrun=input()
                print(airun)
                if userrun.isdigit():
                    userrun=int(userrun)
                    if userrun>=0 and userrun<limit+1:
                        totalairun+=airun
                    elif airun==0:
                        totalairun+=userrun
                    else:
                        print("I don't care if you chose a wrong number")
                        print("It's my batting")
                        print('Do whatever the fuck you want')
                        print("I'm still getting my runs")
                else:
                    print("I don't care if you chose a number or not")
                    print("I'm still getting my runs")
            wicket-=1
            
        if totalairun==0:
            print('FUCK YOU DUCKED ME!')
        else:
            print('OUT')
            print('I scored',totalairun)
            print('You need',totalairun+1,'runs to win')
            print('Lets Begin')
        
        userrun=0
        airun=-1
        wicket=wickets
        
        while wicket>0:
            while userrun!=airun and totalairun>=totaluserrun:
                airun=random.randrange(0,limit+1)
                userrun=input()
                print(airun)
                if userrun.isdigit():
                    userrun=int(userrun)
                    if userrun!=airun:
                        if userrun>0 and userrun<limit+1:
                            totaluserrun+=userrun
                        elif userrun==0:
                            totaluserrun+=airun
                        else:
                            print('YOU HAVE TO PICK BETWEEN 0 AND 6')
                            print("DON'T THINK I WON'T NOTICE")
                            print("I'M TAKING AWAY",penalty,"RUNS FROM YOU")
                            print("AND I'LL KEEP INCREASING THE PENALTY")
                            print('SO PLAY WISELY')
                            totaluserrun-=penalty
                            penalty+=1
                else:
                    print('HOW STUPID ARE YOU ?')
                    print('DO YOU NOT KNOW HOW TO PLAY ?')
                    print('DOES',userrun,'LOOK LIKE A NUMBER TO YOU')
                    print('YOUR GETTING A PENALTY')
                    print("I'M TAKING AWAY",penalty,"RUNS FROM YOU")
                    print("AND I'LL KEEP INCREASING THE PENALTY")
                    print('SO GROW A BRAINCELL AND PLAY')
                    totaluserrun-=penalty
                    penalty+=1
            wicket-=1
        
        if userrun==airun:
            print('OUT!')
            print('You scored',totaluserrun,'runs')
            print()
            winner='AI'
        elif totaluserrun==0:
            print('What sound do you make ?')
            print('Oh I know')
            print('QUACK QUACK QUACK QUACK')
            print("Cuz you're a DUCK")
            if totalairun==0:
                winner='Draw'
            else:
                winner='User'
        elif totaluserrun>totalairun:
            print('Game Over!')
            print('You scored',totaluserrun,'runs')
            print()
            winner='User'
    #THE AWARDING CEREMONY#
    
    if winner=='User':
        print('YOU WON!')
    elif winner=='AI':
        print('I WON!')
        print("YOU'RE A LOSER!")
        
    print()
    #REPEATER#
    if winner=='User':
        rep=input('')
    elif winner=='AI':
        rep=input('Wanna lose again ?')
    
    if rep=='Y' or rep=='y' or rep=='Yes' or rep=='YES' or rep=='yes':
        print("That's the spirit")
        continue
    elif rep=='N' or rep=='n' or rep=='No' or rep=='NO' or rep=='no':
        print("You're just scared to lose")
        print('LOSER')
        break
