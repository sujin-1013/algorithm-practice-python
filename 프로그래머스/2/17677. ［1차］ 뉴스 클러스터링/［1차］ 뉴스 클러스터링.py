from collections import Counter

def solution(str1, str2):
    
    str1_li = []
    str2_li = []

    special = " 0123456789=*-+.!@#$%^&*()_{}[];:<>,/?\"\'"
    
    for i in range(len(str1)-1):
        if str1[i] not in special and str1[i+1] not in special:
            str1_li.append(str1[i:i+2].lower())
    
    for i in range(len(str2)-1):
        if str2[i] not in special and str2[i+1] not in special:
            str2_li.append(str2[i:i+2].lower())
    
    C1 = Counter(str1_li)
    C2 = Counter(str2_li)
    
    inter_cnt = len(list((C1 & C2).elements()))
    union_cnt = len(list((C1 | C2).elements()))
    
    if union_cnt == 0:
        return 65536
    
    return int((inter_cnt/union_cnt)*65536)