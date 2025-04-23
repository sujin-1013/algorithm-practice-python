def solution(babbling):
    answer = 0
    speak = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        # print(word)
        for s in speak:
            
            if s*2 in word:
                break
            if s in word:
                word = word.replace(s, " ")
        
        word = word.replace(" ", "")
        if word == "":
            answer += 1
        # print(word)

    return answer