def Palindrome(str):
    if str[::-1].casefold() == str.casefold():
        print("It is palindrome")
    else:
        print("It is NOT palindrome")
Palindrome(input())