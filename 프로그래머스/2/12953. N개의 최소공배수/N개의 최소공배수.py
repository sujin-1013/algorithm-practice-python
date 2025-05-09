import math

def solution(arr):    
    
    lcm_value = int(arr[0])
    
    for i in range(1, len(arr)):
        lcm_value = int((lcm_value * arr[i]) / (math.gcd(lcm_value, arr[i])))
        
    return lcm_value