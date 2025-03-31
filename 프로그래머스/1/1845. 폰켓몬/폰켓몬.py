def solution(nums):
    count = len(nums)//2
    data = list(set(nums))
    if(len(data)<=count):
        return len(data)
    else:
        return count