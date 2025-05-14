def solution(elements):

    s = set()
    n = len(elements)

    elements += elements

    for i in range(n):
        for j in range(1,n+1):
            p = sum(elements[i:i+j])
            s.add(p)

    return len(s)