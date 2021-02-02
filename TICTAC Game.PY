b = {1:'-', 2:'-', 3:'-', 4:'-', 5:'-', 6:'-', 7:'-', 8:'-', 9:'-'}
def plot(a):
    print(a[1], '|', a[2], '|', a[3])
    print(a[4], '|', a[5], '|', a[6])
    print(a[7], '|', a[8], '|', a[9])

plot(b)
a= ['x', 'y', 'x', 'y', 'x', 'y', 'x', 'y', 'x',]

for i in a:
    c=int(input('Choose your position between 1 to 9: '))
    if c !=1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        c=int(input('chose only a number between 1-9'))
    print( "its your turn", i)
    b[c]=i
    plot(b)
    if '-'!=b[1]==b[2]==b[3]:
        print(b[1], "won the game")
        break
    elif '-'!=b[4]==b[5]==b[6]:
        print(b[4], "won the game")
        break
    elif '-'!=b[7]==b[8]==b[9]:
        print(b[7], "won the game")
        break
    elif '-'!=b[1]==b[4]==b[7]:
        print(b[1], "won the game")
        break
    elif '-'!=b[2]==b[5]==b[8]:
        print(b[2], "won the game")
        break
    elif '-'!=b[3]==b[6]==b[9]:
        print(b[3], "won the game")
        break
    elif '-'!=b[1]==b[5]==b[9]:
        print(b[1], "won the game")
        break
    elif '-'!=b[3]==b[5]==b[7]:
        print(b[3], "won the game")
        break
        
    