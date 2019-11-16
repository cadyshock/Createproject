#Cady Shock
#CSCI 101- Section A
#Create Project

import random

print("WELCOME TO RESTAURANT MANAGEMENT! \n    This program will allow you to manage your \n    restraunt by tracking table usage and returning total revenue.\n")
try:
    mode=int(input('Do you want to use this program in operation mode or simulation mode? (1 or 2) \nN>'))
except:
    print('\nThat is not a valid input\n')


try:
    chosiboi=int(input('Do you want to use a previous table setup, or generate a new one? (1 or 2)\nN> '))
except ValueError:
    print('\nThat is not a valid input\n')

count=0
user=''
tables_list=[]
total_earnings=0
tip_earnings=0
total_served=0
tables_str=''

if chosiboi == 1:
    f=open('tables.csv','r')
    tables=0
    for line in f:
        line=line[:len(line)-1:]
        tables=tables+1
        tables_list.append(line.split(','))
    f.close()
elif chosiboi == 2:
    f=open('tables.csv','w+')
    tables=int(input('Number of Tables > '))
    for i in range(tables):
        print( 'How large is table', i+1, '? (MAX of 8)')
        tablesize=int(input('Number of Seats> '))
        tablesize=['O' for item in range(tablesize) ]
        tables_str=tables_str+','.join(str(x) for x in (tablesize))+'\n'
        tables_list.append(tablesize)
    f.write(tables_str)
    f.close()

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

for i in menu:
    if i[0]=='Food':
        food.append(i)
    elif i[0]=='Drink':
        drinks.append(i)
    elif i[0]=='Side':
        sides.append(i)


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

def occupy(table):
    count=0
    doop=0
    for i in table:
        if i == 'O':
            count=count+1
    doop=len(table)-count
    return doop

def print_table(tables_list):
    n=1
    print()
    for row in tables_list:
        print ('Table', n, '>', end=' ')
        print (*row)
        n=n+1
    print()

print_table(tables_list)

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

def stuff_to_do(tables):
    x=0
    for i in tables:
        if i[0] != 'O':
            x=1
    if x == 1:
        return False
    else:
        return True

def print_party(arrive):
    n=1
    print('\nARRIVALS')
    for row in arrive:
        print ('Party', n, '>', end=' ')
        print (*row)
        n=n+1
    print()

if mode == 2:
    hours=int(input('How many hours will the restaurant be open for?\nHours> '))
    hours=hours*len(tables_list)

score=100

for i in tables_list:
    for item in i:
        score=score+10

if mode == 1:
    while user != 7:
        try:
            user=int(input('What would you like to do? \n 1 = Seat a Table \n 2 = Serve drinks \n 3 = Serve Food \n 4 = Give Check \n 5 = Input Tip \n 6 = Return Restraunt Status \n 7 = Close Restraunt \n N> '))
            if user == 1:
                party=0
                tab=0
                party=int(input('How large is the party? \nN> '))
                print('The following tables are available and large enough for the party:', tablen(tables_list, party))
                tab=int(input('Which table would you like to seat this party at?\nN> '))-1
                if party > len(tables_list[tab]):
                    print ('This party is too large for this table')
                    continue
                if (tables_list[tab][0]) != 'O':
                    print ('This table is already occupied')
                    continue
                for i in range(1, party+1):
                    tables_list[tab].insert(i, 'S')
                    tables_list[tab].remove('O')
            elif user == 2:
                tab=0
                tab=int(input('Which table would you like to serve drinks\nN> '))-1
                if (tables_list[tab][0]) == 'O':
                    print ('This table is empty')
                    continue
                if (tables_list[tab][0]) == 'D':
                    print ('This table has been served drinks')
                    continue
                print('\nDRINK MENU')
                menu_print(drinks, 'Drinks')
                table_total=0
                for i in range(occupy(tables_list[tab])):
                    item=int(input('What item did the customer order? \nN> '))
                    price=float(drinks[item-1][2])
                    table_total=table_total+price
                total_earnings=total_earnings+table_total
                for i in tables_list[tab]:
                    if i != 'O':
                        tables_list[tab].insert(tables_list[tab].index(i), 'D')
                        tables_list[tab].remove('S')
            elif user == 3:
                tab=0
                y=''
                tab=int(input('Which table would you like to serve food\nN> '))-1
                if (tables_list[tab][0]) == 'O':
                    print ('This table is empty')
                    continue
                if (tables_list[tab][0]) == 'F':
                    print ('This table has been served food')
                    continue
                if (tables_list[tab][0]) == 'S':
                    y=input('This table has not been served drinks. Would you like to serve them food (y/n)?\nN> ')
                    if y == 'n':
                        continue
                print('\nFOOD MENU')
                menu_print(food, 'Food')
                table_total=0
                for i in range(occupy(tables_list[tab])):
                    side_price=0
                    item=int(input('What item did the customer order? \nN> '))
                    price=float(food[item-1][2])
                    if food[item-1][3]=='y':
                        print('\nSIDES MENU')
                        menu_print(sides, 'Sides')
                        side_item=int(input('What side did the customer order?\nN> '))
                        side_price=float(food[item-1][2])
                    table_total=table_total+price+side_price
                total_earnings=total_earnings+table_total
                for i in tables_list[tab]:
                    if i != 'O':
                        tables_list[tab].insert(tables_list[tab].index(i), 'F')
                        if y=='':
                            tables_list[tab].remove('D')
                        elif y=='y':
                            tables_list[tab].remove('S')
                    
            elif user == 4:
                tab=0
                y=''
                tab=int(input('Which table would you like to give a check\nN> '))-1
                if (tables_list[tab][0]) == 'O':
                    print ('This table is empty')
                    continue
                if (tables_list[tab][0]) == 'C':
                    print ('This table has been served their check')
                    continue
                if (tables_list[tab][0]) == 'S':
                    print('This table has not been served food or drinks.')
                    continue
                if (tables_list[tab][0]) == 'D':
                    y=input('This table has not been served food. Would you like to give them the check (y/n)? \nN> ')
                    if y == 'n':
                        continue
                for i in tables_list[tab]:
                    if i != 'O':
                        tables_list[tab].insert(tables_list[tab].index(i), 'C')
                        if y=='':
                            tables_list[tab].remove('F')
                        elif y=='y':
                            tables_list[tab].remove('D')
                    
            elif user == 5:
                tab=0
                tab=int(input('Which table would you like to input a tip for?\nN> '))-1
                if (tables_list[tab][0]) != 'C':
                    print ('This table has not yet been given their check')
                    continue
                for i in tables_list[tab]:
                    if i != 'O':
                        tables_list[tab].insert(tables_list[tab].index(i), 'O')
                        tables_list[tab].remove('C')
                earn=0
                earn=float(input('Input Tip Earnings> '))
                tip_earnings=earn+tip_earnings
                total_served=total_served+1
            elif user == 6:
                check(tables_list)
            elif user == 7:
                y=input('End Program (y/n)? \nN> ')
                if y == 'n':
                    user=0
                if y== 'y':
                    f = open('revenue.txt','a')
                    x=(str(total_served)+' : '+ str(total_earnings))
                    f.write('\n'+ x)
                    f.close()
                    print ('TABLES SERVED : %d\nTOTAL EARNINGS : $%.2f' % (total_served, total_earnings))
                    break
            else:
                print('That is not a valid input!')
            print_table(tables_list)
        except ValueError:
            print('\nThat is not a valid input\n')
elif mode == 2:
    while count <= hours:
        if count % len(tables_list)**2 == 0 or ((len(arrivals)==0) and stuff_to_do(tables_list)):
            arrivals=arrive(tables_list)
            arrivals_count=len(arrivals)
        print_party(arrivals)
        count=count+1
        try:
            user=int(input('What would you like to do? \n 1 = Seat a Table \n 2 = Serve drinks \n 3 = Serve Food \n 4 = Give Check \n 5 = Exit Program \n N> '))
            if user == 1:
                tab=0
                party=arrivals[0]
                party_num=int(input('Which party would you like to seat?\nN> '))
                party=arrivals[party_num-1]
                print('The following tables are available and large enough for the party:', tablen(tables_list, len(party)))
                tab=int(input('Which table would you like to seat this party at?\nN> '))-1
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
            elif user == 2:
                tab=0
                tab=int(input('Which table would you like to serve drinks\nN> '))-1
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
            elif user == 3:
                tab=0
                y=''
                tab=int(input('Which table would you like to serve food\nN> '))-1
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
                    
            elif user == 4:
                tab=0
                y=''
                tab=int(input('Which table would you like to give a check\nN> '))-1
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
                    print('This table has not been served food.')
                    score=score-10
                    continue
                for i in tables_list[tab]:
                    if i != 'O':
                        tables_list[tab].insert(tables_list[tab].index(i), 'O')
                        tables_list[tab].remove('F')
                score=score+(tables_list[tab])*3
            elif user == 5 or count == hours:
                y=input('End Program (y/n)? \nN> ')
                if y == 'n':
                    user=0
                if y== 'y':
                    f = open('revenue_for_sim.txt','a')
                    x=(str(total_served)+' : '+ str(total_earnings))
                    f.write('\n'+ x)
                    f.close()
                    print ('TABLES SERVED : %d\nTOTAL EARNINGS : $%.2f' % (total_served, total_earnings))
                    print('FINAL SCORE:', score)
                    break
            else:
                print('That is not a valid input!')
            print_table(tables_list)
            for i in arrivals:
                score=score-len(i)*2
            for i in tables_list:
                if i[0] == 'S':
                    score=score-(len(i))
                elif i[0] == 'D':
                    score=score+(len(i))
                elif i[0] == 'F':
                    score=score+(len(i))*2
            print('SCORE:', score)
        except:
            print('\nThat is not a valid input\n')

