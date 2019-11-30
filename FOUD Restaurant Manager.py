#Cady Shock
#CSCI 101- Section A
#Create Project

import random

'''BEFORE YOU START THIS PROGRAM, MAKE SURE YOU HAVE THESE FILES IN YOUR DIRECTORY
Menu.csv
revenue.txt
revenue_for_sim.txt
tables.csv
'''

#Values intialized for tutorial, mode, and table setup

#Mode is used to determine what mode the user wants to use
mode=0

#Chosiboi is used to determine whether the user wants to input their own table setup or use a previous one
chosiboi=0

#Tutorial is used to determine whether the user wants to go through the tutorial
tutorial=''

print("Welcome to Front-end Operated User Defined (FOUD) Restaurant Manager!\n")

#DOES THE USER GO THROUGH THE TUTORIAL
while tutorial.lower() != 'y' and tutorial.lower() !='n':
    try:
        tutorial=(input('Would you like to run this program in tutorial mode? (y or n) \nN> '))
        if tutorial.lower() != 'y' and tutorial.lower() != 'n':
            print('That is not a valid input\n')
    except:
        print('That is not a valid input!\n')

#tutorial
if tutorial.lower() == 'y':
    #operation mode
    print('Operation Mode:\n    This mode is most useful for use in actual restaurants, during operating hours.\n    It allows you to record table statuses, record tip values, and return total restauraunt revenue.\n')
    dummy=input('Press enter to continue\n')
    #simulation mode
    print('Simulation Mode:\n   This mode is most useful for training with the program.\n   This mode has the same mechanics as operation mode, but makes customers arrive automatically.\n   You can also set the diffculty of the simulation.\n   A score is returned based on the efficency of the user.\n')
    dummy=input('Press enter to continue\n')
    #tables
    print('This program allows you to cutomize table setups.\n  You can input a CSV file named tables.csv where cells represent seats and rows represent tables. \n  The program can also generate new table setups and save them as a CSV file.\n')
    dummy=input('Press enter to continue\n')
    print("Tables are represented by the following output \n Table 1 > O O\n Table 2 > O\n")
    print("O's represent empty seats at a table.\n")
    dummy=input('Press enter to continue\n')
    #management
    print('Once all your tables are implemented, you will be given a list of actions in the form of this menu. \n\nWhat would you like to do? \n 1 = Seat a Table \n 2 = Serve drinks \n 3 = Serve Food \n 4 = Give Check \n 5 = Input Tip \n 6 = Return Restaurant Status \n 7 = Close Restaurant. \n')
    dummy=input('Press enter to continue\n')
    print('To seat a table, press 1. In operation mode, you manually input the size of the party you want to seat.\nIn simulation mode, parties arrive automatically. \nYou can only seat parties at tables that are larger than the party.\n   Once a table has been seated, the occupied seats are represented by an S.\n   Once you serve a table drinks, the S for seated becomes a D for drink.\n   Once a table is served food, the D becomes an F.\n   Once a table is given a check, the F becomes a C.\n   To clear a table in operation mode, you have to enter a tip value.\n   In simulation mode, the tables clear when the check is served.\n')
    dummy=input('Press enter to continue\n')
    print('If your party is smaller than the table, there will still be empty seats.\nTrying to put parties at the smallest possible table maximizes efficency.\n')
    dummy=input('Press enter to begin!\n')
    
    
#WHAT MODE IS THE USER GOING TO UTALIZE
while mode != 1 and mode !=2:
    try:
        mode=int(input('Do you want to use this program in operation mode or simulation mode? (1 or 2) \nN> '))
        if mode != 1 and mode !=2:
            print('That is not a valid input\n')
    except:
        print('That is not a valid input!\n')


#DOES THE USER WANT TO USE A PREVIOUS TABLE SETUP
while chosiboi != 1 and chosiboi != 2:
    try:
        chosiboi=int(input('Do you want to use a previous table setup, or generate a new one? (1 or 2)\nN> '))
        if chosiboi == 1:
            f=open('tables.csv','r')
            empty=0
            for i in f:
                empty=1
            if empty==0:
                print('\nThere is no data in this file. Please input new table setup!\n')
                chosiboi=2
            if mode != 1 and mode !=2:
                print('That is not a valid input!\n')
    except:
        print('That is not a valid input!\n')
        

#Intialized values for the table and the 
count=0
user=''
tables_list=[]
total_earnings=0
tip_earnings=0
total_served=0
tables_str=''

#This branch is used to read the tables in from a CSV file
if chosiboi == 1:
    f=open('tables.csv','r')
    tables=0
    for line in f:
        line=line[:len(line)-1:]
        tables=tables+1
        tables_list.append(line.split(','))
    f.close()

#This branch is used to create a new table setup
elif chosiboi == 2:
    f=open('tables.csv','w+')
    tables=0
    while tables < 1 or tables > 16:
        try:
            tables=int(input('Number of Tables (MAX of 15) > '))
            if tables < 1 or tables > 16:
                print ('That is not a valid input!\n')
        except:
            print ('That is not a valid input!\n')
    for i in range(tables):
        tablesize=0
        while tablesize > 8 or tablesize < 1:
            print( 'How large is table', i+1, '? (MAX of 8)')
            try:
                tablesize=int(input('Number of Seats> '))
                if tablesize > 8 or tablesize < 1:
                    print ('That is not a valid input!\n')
            except:
                print ('That is not a valid input!\n')
        tablesize=['O' for item in range(tablesize) ]
        tables_str=tables_str+','.join(str(x) for x in (tablesize))+'\n'
        tables_list.append(tablesize)
    f.write(tables_str)
    f.close()

#This block of code is used to read in all the information from a menu file
menu=[]

f=open('Menu.csv', 'r')

for line in f:
    line=line[:len(line)-1:]
    menu.append(line.split(','))

f.close()


food=[]
drinks=[]
sides=[]
final=''

#This block of code is used to seperate the drinks, sides and food into seperate lists
for i in menu:
    if i[0]=='Food':
        food.append(i)
    elif i[0]=='Drink':
        drinks.append(i)
    elif i[0]=='Side':
        sides.append(i)

#This function is used to print the menu
def menu_print(choose, call):
    if call=='Food':
        count=1
        for item in choose:
            print (count,'>', item[1])
            count=count+1
    elif call == 'Sides':
        count=1
        for item in choose:
            print (count,'>', item[1])
            count=count+1
    elif call == 'Drinks':
        count=1
        for item in choose:
            print (count,':', item[1])
            count=count+1

#This function is used to determine how much of a table is occupied
def occupy(table):
    count=0
    doop=0
    for i in table:
        if i == 'O':
            count=count+1
    doop=len(table)-count
    return doop


#This function is used to print out tables in the right format
def print_table(tables_list):
    n=1
    print()
    for row in tables_list:
        print ('Table', n, '>', end=' ')
        print (*row)
        n=n+1
    print()

print_table(tables_list)


#This function is used to check the status of the restraunt
def check(table):
    emp=0
    seat=0
    drink=0
    food=0
    chec=0
    for row in table:
        for i in row:
            if i == 'O':
                emp=emp+1
            elif i == 'S':
                seat=seat+1
            elif i == 'D':
                drink=drink+1
            elif i == 'F':
                food=food+1
            elif i == 'C':
                chec=chec+1
    print ('Status| Vaccant =', emp, '| Seated =', seat, '| Served Drinks =',drink,'| Served Food =',food, '|Given Check = ', chec, '|')


#This function is used to determine if a table is large enough and empty so it can be utalized
def tablen(x,y):
    test=[]
    counter=[]
    for i in x:
        test.append(i)
        if len(i)>=y and i[0]=='O':
            counter.append(test.index(i)+1)
            test.insert(test.index(i), ' ')
            test.remove(i)
    return counter

#This function is used to generate randomly sized arriving parties
def arrive(tables):
    table=0
    table_count=0
    arrived=[]
    for i in tables:
        table=table+1
        for item in i:
            table_count=table_count+1
    for i in range(random.randint(1,table)):
        arrivesize=['X' for item in range(random.randint(1,table_count//table))]
        arrived.append(arrivesize)
    return arrived

#This function determines if the user has anything to do in simulation mode so more arrivals can be generated
def stuff_to_do(tables):
    x=0
    for i in tables:
        if i[0] != 'O':
            x=1
    if x == 1:
        return False
    else:
        return True

#This function prints out arriving parties
def print_party(arrive):
    n=1
    print('\nARRIVALS')
    for row in arrive:
        print ('Party', n, '>', end=' ')
        print (*row)
        n=n+1
    print()

hours=0

#This block of code is only used in simulation mode to determine the difficulty
if mode == 2:
    difficult=0
    while difficult != 1 and difficult != 2 and difficult != 3:
        try:
            difficult=int(input('\nWhat difficulty would you like?\n RARE-(Easy)> (1) \n MEDIUM RARE-(Medium)> (2) \n WELL DONE-(Hard)> (3)\nN> '))
            if difficult != 1 and difficult != 2 and difficult != 3:
                print('That is not a valid input')
        except:
            print('That is not a valid input')
    diff=0
    if difficult==1:
        diff=2
    elif difficult==2:
        diff=1
    elif difficult==3:
        diff=0

#The base score is 100. Then 10 is added to the score for the number of tables
score=100

for i in tables_list:
    for item in i:
        score=score+10

#OPERATION MODE
if mode == 1:
    user=0
    while user != 7:
        print('---------------------------------------------------------------')
        try:
            user=int(input('What would you like to do? \n 1 = Seat a Table \n 2 = Serve drinks \n 3 = Serve Food \n 4 = Give Check \n 5 = Input Tip \n 6 = Return Restaurant Status \n 7 = Close Restaurant \n N> '))
            
            #SEAT A TABLE
            if user == 1:
                party=0
                tab=0
                while party <= 0:
                    party=int(input('How large is the party? \nN> '))
                    if party <= 0:
                        print('That is not a valid input! \n')
                if len(tablen(tables_list, party)) == 0:
                    print('\nNo table avaliable is large enough for this party!\n')
                    continue
                else:
                    print('The following tables are available and large enough for the party:', tablen(tables_list, party))
                tab=int(input('Which table would you like to seat this party at?\nN> '))-1
                if tab >= len(tables_list) or tab <= -1:
                    print ('This table does not exist\n')
                    continue
                if party > len(tables_list[tab]):
                    print ('This party is too large for this table\n')
                    continue
                if (tables_list[tab][0]) != 'O':
                    print ('This table is already occupied\n')
                    continue
                for i in range(1, party+1):
                    tables_list[tab].insert(i, 'S')
                    tables_list[tab].remove('O')
                    
            #SERVE DRINKS
            elif user == 2:
                tab=0
                tab=int(input('Which table would you like to serve drinks\nN> '))-1
                if tab >= len(tables_list) or tab <= -1:
                    print ('This table is does not exist\n')
                    continue
                if (tables_list[tab][0]) == 'O':
                    print ('This table is empty\n')
                    continue
                if (tables_list[tab][0]) == 'D':
                    print ('This table has been served drinks\n')
                    continue
                print('\nDRINK MENU')
                menu_print(drinks, 'Drinks')
                table_total=0
                for i in range(occupy(tables_list[tab])):
                    item=0
                    while item < 1 or item > len(drinks):
                        item=int(input('What item did the customer order? \nN> '))
                        if item < 1 or item > len(drinks):
                            print ('That is not a valid input')
                    price=float(drinks[item-1][2])    
                    table_total=table_total+price
                total_earnings=total_earnings+table_total
                for i in tables_list[tab]:
                    if i != 'O':
                        tables_list[tab].insert(tables_list[tab].index(i), 'D')
                        tables_list[tab].remove('S')
                        
            #SERVE FOOD
            elif user == 3:
                tab=0
                y=''
                tab=int(input('Which table would you like to serve food\nN> '))-1
                if tab >= len(tables_list) or tab <= -1:
                    print ('This table is does not exist\n')
                    continue
                if (tables_list[tab][0]) == 'O':
                    print ('This table is empty')
                    continue
                if (tables_list[tab][0]) == 'F':
                    print ('This table has been served food')
                    continue
                if (tables_list[tab][0]) == 'S':
                    y=''
                    while y.lower() != 'y' and y.lower() != 'n':
                        y=input('This table has not been served drinks. Would you like to serve them food (y/n)?\nN> ')
                        if y.lower() != 'y' and y.lower() != 'n':
                            print('That is not a valid input!\n')
                    if y.lower() == 'n':
                        continue
                print('\nFOOD MENU')
                menu_print(food, 'Food')
                table_total=0
                for i in range(occupy(tables_list[tab])):
                    side_price=0
                    item=0
                    while item < 1 or item > len(food):
                        item=int(input('What item did the customer order? \nN> '))
                        if item < 1 or item > len(food):
                            print('That is not a valid input')
                    price=float(food[item-1][2])
                    if food[item-1][3]=='y':
                        print('\nSIDES MENU')
                        menu_print(sides, 'Sides')
                        side_item=0
                        while side_item < 1 or side_item > len(sides):
                            side_item=int(input('What side did the customer order?\nN> '))
                            if side_item < 1 or side_item > len(drinks):
                                print('That is not a valid input')
                        side_price=float(food[item-1][2])
                    table_total=table_total+price+side_price
                total_earnings=total_earnings+table_total
                for i in tables_list[tab]:
                    if i != 'O':
                        tables_list[tab].insert(tables_list[tab].index(i), 'F')
                        if y=='':
                            tables_list[tab].remove('D')
                        elif y.lower()=='y':
                            tables_list[tab].remove('S')
            
            #GIVE CHECK TO PATRONS        
            elif user == 4:
                tab=0
                y=''
                tab=int(input('Which table would you like to give a check\nN> '))-1
                if tab >= len(tables_list) or tab <= -1:
                    print ('This table is does not exist\n')
                    continue
                if (tables_list[tab][0]) == 'O':
                    print ('This table is empty')
                    continue
                if (tables_list[tab][0]) == 'C':
                    print ('This table has been served their check\n')
                    continue
                if (tables_list[tab][0]) == 'S':
                    print('This table has not been served food or drinks.\n')
                    continue
                if (tables_list[tab][0]) == 'D':
                    y=''
                    while y.lower() != 'y' and y.lower() != 'n':
                        y=input('This table has not been served food. Would you like to give them the check (y/n)? \nN> ')
                        if y.lower() != 'y' and y.lower() != 'n':
                            print('That is not a valid input!\n')
                    if y.lower() == 'n':
                        continue
                for i in tables_list[tab]:
                    if i != 'O':
                        tables_list[tab].insert(tables_list[tab].index(i), 'C')
                        if y=='':
                            tables_list[tab].remove('F')
                        elif y.lower()=='y':
                            tables_list[tab].remove('D')
            
            #INPUT TIP (THIS FUNCTION ALSO CLEARS THE TABLE)        
            elif user == 5:
                tab=0
                tab=int(input('Which table would you like to input a tip for?\nN> '))-1
                if tab >= len(tables_list) or tab <= -1:
                    print ('This table is does not exist\n')
                    continue
                if (tables_list[tab][0]) != 'C':
                    print ('This table has not yet been given their check\n')
                    continue
                earn=-1
                while earn < 0:
                    try:
                        earn=float(input('Input Tip Earnings> '))
                    except:
                        print()
                    if earn < 0:
                        print('That is not a valid input!\n')
                for i in tables_list[tab]:
                    if i != 'O':
                        tables_list[tab].insert(tables_list[tab].index(i), 'O')
                        tables_list[tab].remove('C')
                tip_earnings=earn+tip_earnings
                total_served=total_served+1
                
            #RETURNS THE TABLE STATUS
            elif user == 6:
                check(tables_list)
                
            #ALLOWS THE USER TO END THE PROGRAM AND RETURN REVENUE AND TABLES SERVED
            elif user == 7:
                y=''
                while y.lower() != 'y' and y.lower() != 'n':
                    y=input('End Program (y/n)? \nN> ')
                    if y.lower() != 'y' and y.lower() != 'n':
                            print('That is not a valid input!\n')
                if y.lower() == 'n':
                    user=0
                if y.lower() == 'y':
                    f = open('revenue.txt','a')
                    x=(str(total_served)+' : '+ str(total_earnings))
                    f.write('\n'+ x)
                    f.close()
                    print ('TABLES SERVED : %d\nTOTAL EARNINGS : $%.2f\nTIP EARNINGS : $%.2f' % (total_served, total_earnings, tip_earnings))
                    break
                
            else:
                print('That is not a valid input!')
            print_table(tables_list)
        except ValueError:
            print('\nThat is not a valid input\n')

#IF THE USER DECIDES TO RUN THE PROGRAM IN SIMULATION MODE
elif mode == 2:
    user=0
    #This while loop determines how long the user plays for
    while user != 5:
        print('---------------------------------------------------------------')
        #This if branch determines if a new arrival batch will be generated. It will happen more frequently on higher difficulty
        if count % len(tables_list)** diff == 0 or ((len(arrivals)==0) and stuff_to_do(tables_list)):
            arrivals=arrive(tables_list)
            arrivals_count=len(arrivals)
        print_party(arrivals)
        count=count+1
        try:
            user=int(input('What would you like to do? \n 1 = Seat a Table \n 2 = Serve drinks \n 3 = Serve Food \n 4 = Give Check \n 5 = Exit Program \n N> '))

            #SEAT A TABLE
            if user == 1:
                tab=0
                party=arrivals[0]
                party_num=int(input('Which party would you like to seat?\nN> '))
                party=arrivals[party_num-1]
                print('The following tables are available and large enough for the party:', tablen(tables_list, len(party)))
                tab=int(input('Which table would you like to seat this party at?\nN> '))-1
                if tab >= len(tables_list) or tab <= -1:
                    print ('This table is does not exist\n')
                    score=score-10
                    continue
                if len(party) > len(tables_list[tab]):
                    print ('This party is too large for this table\n')
                    score=score-10
                    continue
                if (tables_list[tab][0]) != 'O':
                    print ('This table is already occupied\n')
                    score=score-10
                    continue
                for i in range(1, len(party)+1):
                    tables_list[tab].insert(i, 'S')
                    tables_list[tab].remove('O')
                arrivals.pop(party_num-1)
                score=score+len(party)

            #SERVE DRINKS
            elif user == 2:
                tab=0
                tab=int(input('Which table would you like to serve drinks\nN> '))-1
                if tab >= len(tables_list) or tab <= -1:
                    print ('This table is does not exist\n')
                    score=score-10
                    continue
                if (tables_list[tab][0]) == 'O':
                    print ('This table is empty\n')
                    score=score-10
                    continue
                if (tables_list[tab][0]) == 'D':
                    print ('This table has been served drinks\n')
                    score=score-10
                    continue 
                table_total=0
                for i in range(occupy(tables_list[tab])):
                    item=random.randint(0,len(drinks))
                    price=float(drinks[item-1][2])
                    table_total=table_total+price
                total_earnings=total_earnings+table_total
                for i in tables_list[tab]:
                    if i != 'O':
                        tables_list[tab].insert(tables_list[tab].index(i), 'D')
                        tables_list[tab].remove('S')
                score=score+occupy(tables_list[tab])

            #SERVE FOOD
            elif user == 3:
                tab=0
                y=''
                tab=int(input('Which table would you like to serve food\nN> '))-1
                if tab >= len(tables_list) or tab <= -1:
                    print ('This table is does not exist\n')
                    score=score-10
                    continue
                if (tables_list[tab][0]) == 'O':
                    print ('This table is empty\n')
                    score=score-10
                    continue
                if (tables_list[tab][0]) == 'F':
                    print ('This table has been served food\n')
                    score=score-10
                    continue
                if (tables_list[tab][0]) == 'S':
                    print('This table has not been served drinks.\n')
                    score=score-10
                    continue
                table_total=0
                for i in range(occupy(tables_list[tab])):
                    side_price=0
                    item=random.randint(0, len(food))
                    price=float(food[item-1][2])
                    if food[item-1][3]=='y':
                        side_item=random.randint(0, len(sides))
                        side_price=float(sides[side_item-1][2])
                    table_total=table_total+price+side_price
                total_earnings=total_earnings+table_total
                for i in tables_list[tab]:
                    if i != 'O':
                        tables_list[tab].insert(tables_list[tab].index(i), 'F')
                        if y=='':
                            tables_list[tab].remove('D')

            #GIVE A CHECK. THIS BRANCH ALSO CLEARS THE TABLE        
            elif user == 4:
                tab=0
                y=''
                tab=int(input('Which table would you like to give a check?\nN> '))-1
                if tab >= len(tables_list) or tab <= -1:
                    print ('This table is does not exist\n')
                    score=score-10
                    continue
                if (tables_list[tab][0]) == 'O':
                    print ('This table is empty')
                    score=score-10
                    continue
                if (tables_list[tab][0]) == 'C':
                    print ('This table has been served their check\n')
                    score=score-10
                    continue
                if (tables_list[tab][0]) == 'S':
                    print('This table has not been served food or drinks.\n')
                    score=score-10
                    continue
                if (tables_list[tab][0]) == 'D':
                    print('This table has not been served food.\n')
                    score=score-10
                    continue
                for i in tables_list[tab]:
                    if i != 'O':
                        tables_list[tab].insert(tables_list[tab].index(i), 'O')
                        tables_list[tab].remove('F')
                score=score+(len(tables_list[tab]))*3
                total_served=total_served+1

            #THIS BRANCH ENDS THE PROGRAM AND RETURNS STATISTICS
            elif user == 5:
                y=input('End Program (y/n)? \nN> ')
                if y == 'n':
                    user=0
                if y== 'y':
                    f = open('revenue_for_sim.txt','a')
                    x=(str(total_served)+' : '+ str(total_earnings)+ ' : '+ str(score))
                    f.write('\n'+ x)
                    f.close()
                    print ('TABLES SERVED : %d\nTOTAL EARNINGS : $%.2f' % (total_served, total_earnings))
                    print('FINAL SCORE:', score)
                    break
            else:
                print('That is not a valid input!')
                score=score-10
            print_table(tables_list)

            #THIS BLOCK OF CODE DETERMINES SCORING
            #The goal of scoring is to motivate the user to move tables as quickly as possible
            #Trying to do actions that are not yet avaliable or have already been done also loses the user points
            #Giving a table their check gains the most points
            for i in arrivals:
                #Unseated arrivals lose the user the most points
                score=score-len(i)*2
            for i in tables_list:
                if i[0] == 'S':
                    #Seated tables also lose points
                    score=score-(len(i))
                elif i[0] == 'D':
                    #Tables with drinks gain points
                    score=score+(len(i))
                elif i[0] == 'F':
                    #Tables with food gain points
                    score=score+(len(i))*2
            print('SCORE:', score)
        except:
            print('\nThat is not a valid input\n')
            score=score-10
            print('SCORE:', score)

