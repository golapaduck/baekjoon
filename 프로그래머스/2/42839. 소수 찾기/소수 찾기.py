from itertools import permutations

def checkPrime(num):
    if num<=1:
        return False
    for i in range(2,int(num**(1/2))+1):
        if num%i == 0:
            return False
    return True


def solution(numbers):
    numbers = list(numbers)
    
    temp = []
    for i in range(1,len(numbers)+1):
        for data in permutations(numbers,i):
            string = ""
            for char in data:
                string += char
            temp.append(int(string))
        
    temp = list(set(temp))
    
    print(temp)
    
    primeCount = 0
    
    for i in temp:
        if checkPrime(i):
            primeCount += 1 
    
    return primeCount