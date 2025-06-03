def solution(keymap, targets):
    answer = []
    key_dict = {}
    
    for key in keymap:
        idx = 1
        for k in key:
            if k not in key_dict.keys():
                key_dict[k] = idx
            else:
                key_dict[k] = min(key_dict[k], idx)
            idx += 1
                
    for target in targets:
        push = 0
        for t in target:
            if t in key_dict.keys():
                push += key_dict[t]
            else:
                push = -1
                break
        answer.append(push) 
        
    return answer