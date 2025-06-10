def solution(dirs):
    
    x = 0
    y = 0
    new_x = 0
    new_y = 0
    total = []
    
    for dir in dirs:
        path = str(x) + str(y)
        new_x, new_y = x, y
        
        if dir == 'U':
            new_y = y + 1
        elif dir == 'D':
            new_y = y - 1
        elif dir == 'R':
            new_x = x + 1
        elif dir == 'L':
            new_x = x - 1
            
        if -5 <= new_x <= 5 and -5 <= new_y <= 5:
            x = new_x
            y = new_y
            
            path_1 = path + str(x) + str(y)
            path_2 = str(x) + str(y) + path
            
            if path_1 not in total and path_2 not in total:

                total.append(path_1)

    return len(total)