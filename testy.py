chosiboi=int(input('Do you want to use a previous table setup, or generate a new one? (1 or 2)'))
import random
count=0
user=''
tables_list=[]
total_earnings=0
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
    
def tablen(x,y):
    test=[]
    counter=[]
    for i in x:
        print(i)
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
        arrivesize=['O' for item in range(random.randint(1,table_count//table))]
        arrived.append(arrivesize)
    return arrived
        


print (arrive(tables_list))
