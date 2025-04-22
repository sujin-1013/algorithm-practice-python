def solution(s, skip, index):
    answer = ''
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_li = list(alphabet)
    new_alphabet = ""
    
    for i in skip:
        # if i in alphabet_li:
            # del alphabet_li[alphabet_li.index(i)]
        alphabet_li.remove(i)
        

    for ch in s:
        cur_idx = alphabet_li.index(ch)
        new_idx = (cur_idx + index) % len(alphabet_li)
        answer += alphabet_li[new_idx]
    
    return answer