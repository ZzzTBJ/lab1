def Has_33(nums):
    arr = []
    cnt = 0
    for i in nums:
        arr.append(i)
    for j in range(len(arr) - 1):
        if arr[j] == 3 and arr[j+1] == 3:
            cnt += 1
        else:
            cnt += 0
    if cnt == 1:
        print("True")
    elif cnt == 0:
        print("False")

Has_33([1,3,3])
Has_33([1,3,1,3])
Has_33([3,1,3])