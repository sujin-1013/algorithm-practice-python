def solution(people, limit):
    people.sort()
    
    left = 0
    right = len(people) - 1
    
    save = 0
    
    while left <= right:
        save += 1
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
    
    return save