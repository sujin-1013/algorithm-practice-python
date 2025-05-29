def solution(s):
    answer = 0
        
    for i in range(len(s)):
        new_s = s[i:] + s[:i]

        if check(new_s) == True:
            answer += 1
    
    return answer

def check(chr):
    
    pairs = {')':'(', ']':'[', '}':'{'}
    stack = []
    
    for c in chr:
        
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or (stack[-1] != pairs[c]):
                return False
            stack.pop()
                   
    return not stack
                    
        
    