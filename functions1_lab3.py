def New(list):
    arr = []
    for i in list:
        if i not in arr:
            arr.append(i)
    print(arr)
nums = list(map(int, input().split()))
New(nums)