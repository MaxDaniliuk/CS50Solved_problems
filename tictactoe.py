rows, cols = (3, 3)
arr = [[[] for i in range(cols)] for j in range(rows)]

arr[0][0], arr[0][1], arr[0][2] = 'a1', 'a2', 'a3'
arr[1][0], arr[1][1], arr[1][2] = 'b1', 'b2', 'b3'
arr[2][0], arr[2][1], arr[2][2] = 'c1', 'c2', 'c3'

mark1 = input('Player 1, choose x or 0 :')
if mark1 == 'x' :
     mark2 = '0'
if mark1 == '0' :
     mark2 = 'x'
#Consider whether it is possible to shorten conditionals
N = 9
while N > 0 : 
    print('Current score')
    for layer in arr :
        print(layer)
    
    num = input('Player 1, mark the grid by typing the coordinate: ')
    if num == 'a1' :
        arr[0][0] = mark1
    elif num == 'a2' : 
        arr[0][1] = mark1
    elif num == 'a3' : 
        arr[0][2] = mark1
    elif num == 'b1' :
        arr[1][0] = mark1
    elif num == 'b2' :
        arr[1][1] = mark1
    elif num == 'b3' :
        arr[1][2] = mark1
    elif num == 'c1' :
        arr[2][0] = mark1
    elif num == 'c2' :
        arr[2][1] = mark1
    elif num == 'c3' :
        arr[2][2] = mark1
    for layer in arr : 
        print(layer)
    if arr[0][0] == 'x' and arr[0][1] == 'x' and arr[0][2] == 'x' or arr[1][0] == 'x' and arr[1][1] == 'x' and arr[1][2] == 'x' or arr[2][0] == 'x' and arr[2][1] == 'x' and arr[2][2] == 'x' or arr[0][0] == 'x' and arr[1][0] == 'x' and arr[2][0] == 'x' or arr[0][1] == 'x' and arr[1][1] == 'x' and arr[2][1] == 'x' or arr[0][2] == 'x' and arr[1][2] == 'x' and arr[2][2] == 'x' or arr[0][0] == 'x' and arr[1][1] == 'x' and arr[2][2] == 'x' or arr[2][0] == 'x' and arr[1][1] == 'x' and arr[0][2] == 'x' :
        print('X wins')
        break
   
    if arr[0][0] == '0' and arr[0][1] == '0' and arr[0][2] == '0' or arr[1][0] == '0' and arr[1][1] == '0' and arr[1][2] == '0' or arr[2][0] == '0' and arr[2][1] == '0' and arr[2][2] == '0' or arr[0][0] == '0' and arr[1][0] == '0' and arr[2][0] == '0' or arr[0][1] == '0' and arr[1][1] == '0' and arr[2][1] == '0' or arr[0][2] == '0' and arr[1][2] == '0' and arr[2][2] == '0' or arr[0][0] == '0' and arr[1][1] == '0' and arr[2][2] == '0' or arr[2][0] == '0' and arr[1][1] == '0' and arr[0][2] == '0' :
        print('0 wins')
        break
    
    N -= 1 
    if N == 0 : 
        print('draw')
        break

    num = input('Player 2, mark the grid by typing the coordinate: ')
    if num == 'a1' :
        arr[0][0] = mark2
    elif num == 'a2' : 
        arr[0][1] = mark2
    elif num == 'a3' : 
        arr[0][2] = mark2
    elif num == 'b1' :
        arr[1][0] = mark2
    elif num == 'b2' :
        arr[1][1] = mark2
    elif num == 'b3' :
        arr[1][2] = mark2
    elif num == 'c1' :
        arr[2][0] = mark2
    elif num == 'c2' :
        arr[2][1] = mark2
    elif num == 'c3' :
        arr[2][2] = mark2
    for layer in arr : 
        print(layer)
    
    N -= 1 
    if arr[0][0] == '0' and arr[0][1] == '0' and arr[0][2] == '0' or arr[1][0] == '0' and arr[1][1] == '0' and arr[1][2] == '0' or arr[2][0] == '0' and arr[2][1] == '0' and arr[2][2] == '0' or arr[0][0] == '0' and arr[1][0] == '0' and arr[2][0] == '0' or arr[0][1] == '0' and arr[1][1] == '0' and arr[2][1] == '0' or arr[0][2] == '0' and arr[1][2] == '0' and arr[2][2] == '0' or arr[0][0] == '0' and arr[1][1] == '0' and arr[2][2] == '0' or arr[2][0] == '0' and arr[1][1] == '0' and arr[0][2] == '0' :
        print('0 wins')
        break
     
    if arr[0][0] == 'x' and arr[0][1] == 'x' and arr[0][2] == 'x' or arr[1][0] == 'x' and arr[1][1] == 'x' and arr[1][2] == 'x' or arr[2][0] == 'x' and arr[2][1] == 'x' and arr[2][2] == 'x' or arr[0][0] == 'x' and arr[1][0] == 'x' and arr[2][0] == 'x' or arr[0][1] == 'x' and arr[1][1] == 'x' and arr[2][1] == 'x' or arr[0][2] == 'x' and arr[1][2] == 'x' and arr[2][2] == 'x' or arr[0][0] == 'x' and arr[1][1] == 'x' and arr[2][2] == 'x' or arr[2][0] == 'x' and arr[1][1] == 'x' and arr[0][2] == 'x' :
        print('X wins')
        break
    
