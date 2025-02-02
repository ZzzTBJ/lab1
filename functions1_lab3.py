def Spy_game(nums):
    code = [0, 0, 7]
    cnt = 0
    
    for num in nums:
        if cnt < len(code) and num == code[cnt]:
            cnt += 1
        if cnt == len(code):
            return True
    return False

print(Spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(Spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(Spy_game([1, 7, 2, 0, 4, 5, 0]))  