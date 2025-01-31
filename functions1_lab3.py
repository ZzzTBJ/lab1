def Filter(list):
    new = []
    for num in list:
        if num < 1:
            continue
        bool = True
        for j in range(2, int(pow(num, 1/2))+1):
            if num%j == 0:
                bool = False
                break
        if bool:
            new.append(num)
    print(new)
arr = list(map(int, input().split()))
Filter(arr)