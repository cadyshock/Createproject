menu=[]

f=open('Menu.csv', 'r')

for line in f:
    line=line[:len(line)-1:]
    menu.append(line.split(','))

f.close()

def menu_print(menu, call):
    food=[]
    drinks=[]
    sides=[]
    for i in menu:
        if i[0]=='Food':
            food.append(i)
        elif i[0]=='Drink':
            drinks.append(i)
        elif i[0]=='Side':
            sides.append(i)
    if call=='Food':
        count=1
        for item in food:
            print (count,'>', item[1], end=': ')
            count=count+1
    elif call == 'Sides':
        count=1
        for item in sides:
            print (count,'>', item[1], end=': ')
            count=count+1
    elif call == 'Drinks':
        count=1
        for item in drinks:
            print (count,'>', item[1], end=': ')
            count=count+1
    

menu_print(menu, 'Food')

def table_pricer(table, menu):
    cust=0
    price=0
    total=0
    for i in table:
        if i != 'O':
            cust=cust+1
    for i in range(cust):
        item=int(input('Which menu item was ordered? \n>'))
        price=menu[item][2]
        total=total+price
    return (total)

print (table_pricer(tables_list[2],menu))
        
    
    
