import random
#board size
def board_size():
    try:
        inp = int(input('Enter an integer odd number higher than 5: '))
    except:
        print("It's not an integer") #якщо людина ввела не число, то цей код це пише та запускає ще раз цю функцію, щоб людина змогла ввести число
        inp = board_size()
        return inp
    if inp > 6 and inp%2==1:
        return inp
    print('This is a wrong nuber!') #якщо людина ввела число, що не є більшим за 5 та не є непарним, то функція запускається ще раз
    inp = board_size()
    return inp
#create board
def create_board(n): #створює порожнє поле для гри
    t = []
    for x in range(n):
        t.append([' '] * n)
    t[(mid - 1):(mid + 2)] = [['*'] * n, ['*'] * n, ['*'] * n] #додає горизонтальні *
    for y in range(n):
        t[y][(mid-1):(mid+2)] = ['*', '*', '*'] #додає вертикальні *
    for i in range(1,n-1): #додає вертикальні D
        t[i][mid] = 'D'
    t[mid][1:(n-1)] = ['D']*(n-2)      #додає горизонтальні D
    t[mid][mid] = 'X'
    return t
#create cordinates of any player
def one_player_cordinates(n, x, y, player):
    all_cordinates = [[x,y]]
    houses_cordinates = []
    t[y][x] = player
    if y == 0: #цей код записує координати, на яких розміщені букви D кожного гравця
        for i in range(1, mid):
            houses_cordinates.append( [mid, y+i])
    else:
        for i in range(1, mid):
            houses_cordinates.append([mid, y-i])
    board = create_board(n)
    circle = 0
    while circle < 8*mid: #цей код записує по порядку координати *, по яких ходитиме кожен гравець
        if y < (n-1) and board[y + 1][x] == '*' and x > mid: #коли гравець має ходити вниз
            board[y + 1][x] = ''
            y += 1
            all_cordinates.append([x,y])
        elif x < (n-1) and board[y][x + 1] == '*' and y < mid: #коли гравець має ходити направо
            board[y][x + 1] = ''
            x += 1
            all_cordinates.append([x, y])
        elif x > 0 and board[y][x - 1] == '*' and y > mid: #коли гравець має ходити наліво
            board[y][x - 1] = ''
            x -= 1
            all_cordinates.append([x, y])
        elif y > 0 and board[y - 1][x] == '*' and x < mid: #коли гравець має ходити вгору
            board[y - 1][x] = ''
            y -= 1
            all_cordinates.append([x, y])
        circle+=1
    return all_cordinates, houses_cordinates
#defeat player
def defeat_player(y, x): #ця функція перевіряє, чи на координаті, на яку походив гравець, не стоїть інший гравець. Якщо стоїть, то іншого гравця відправляють на початкову координату
    if t[y][x] == 'B': #якщо на координаті стоїть гравець В, то його відправляє на початок
        global count_b
        count_b = 0
        t[n-1][mid - 1] = 'B'
    elif t[y][x] == 'A': #якщо на координаті стоїть гравець А, то його відправляє на початок
        global count_a
        count_a = 0
        t[0][mid + 1] = 'A'
    pass
#one player's move
def one_players_moves(player, cordinates, houses, count = 0, houses_count = 0): #функція робить 1 хід 1 гравця
    c = input('press any key to throw the cube:')
    cube = random.randint(1,6) #рандомне число від 1 до 6 (типу кубик)
    print(cube)
    x, y = cordinates[count]
    t[y][x] = '*' #координата, на якій раніше стояв гравець, перетворюється назад на *
    count += cube #це число запам'ятовує, на якій саме по порядку * знаходиться гравець
    if count > mid * 8 - 1: #якщо гравець пройшов ціле коло, то його ставить в домівку D та на початкові координати
        x, y = houses[houses_count]
        t[y][x] = player #пише гравця замість D
        houses_count += 1 #це зараховує +1 домівку на рахунок
        count = 0
    x, y = cordinates[count]
    defeat_player(y, x)
    t[y][x] = player #гравець пишеться на його координаті
    return count, houses_count
#print board
def board_print(board, n): #друкує поле
    for i in range(n):
        for ii in range(n):
            print(board[i][ii], end=' ')
        print()

#preparation
n = board_size() #дає гравцю ввести розмір дошки
mid = n//2
t = create_board(n) #створює дошку
cordinates_a, houses_a = one_player_cordinates(n, mid+1, 0, 'A') #створює лист з координатами, по яких ходить гравець А
print(cordinates_a)
count_a, houses_count_a = 0, 0 #задає початкове місценаходження гравця А на 0, а також кількість зайнятих D на 0
cordinates_b, houses_b = one_player_cordinates(n, mid-1, n-1, 'B') #створює лист з координатами, по яких ходить гравець В
count_b, houses_count_b = 0, 0
board_print(t, n)

#game starts
while True:
    #A moves
    count_a, houses_count_a = one_players_moves('A', cordinates_a, houses_a, count_a, houses_count_a) #гравець А рухається
    board_print(t, n) #виводиться гральне поле, де уже є показано, що А походив
    if houses_count_a > mid-2: #перевіряє, чи гравець А не зайняв усі D, якщо зайняв, то гра зупиняється, а гравець А виграв
        print('Player "A" won')
        break
    #B moves
    count_b, houses_count_b = one_players_moves('B', cordinates_b, houses_b, count_b, houses_count_b) #гравець В рухається
    board_print(t, n) #виводить гральне поле, де гравець В походив
    if houses_count_b > mid-2: #перевіряє, чи гравець В не зайняв усі D, якщо зайняв, то гра зупиняється, а гравець В виграв
        print('Player "B" won')
        break
