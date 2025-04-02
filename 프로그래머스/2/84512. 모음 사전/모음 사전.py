def mul(num):
    result = 0
    for i in range(int(num)+1):
        result += 5**i
    
    return result

def solution(word):
    char = ["A","E","I","O","U"]
    word = list(word)
    count = 0
    for i in range(len(word)):
        check = char.index(word[i])
        count += check * (mul(4-i))
        count += 1
    
    return count
    
    # print(
    #     1*(5*5*5*5+5*5*5+5*5+5+1)+1
    #     +2*(5*5*5+5*5+5+1)+1
    #     +3*(5*5+5+1)+1)
    # A AEIOU AEIOU AEIOU AEIOU
    # EIO