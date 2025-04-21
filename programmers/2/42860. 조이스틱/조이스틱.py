def solution(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    n = len(alphabet)
    alphabet_dict = {}
    for i in range(n):
        alphabet_dict[alphabet[i]] = i+1
    
    m = len(name)
    move = 0
    for name_ in name:
        idx = alphabet_dict[name_]
        updown = min(abs(1 - idx), 1 + abs(26 - idx))
        move += updown

    min_move = m-1
    for i in range(m):
        next_i = i+1
        while next_i < m and name[next_i] == 'A':
            next_i += 1
        distance = i + (m - next_i) + min(i, m - next_i) 
        min_move = min(min_move, distance)
        
    move += min_move
    
    return move
