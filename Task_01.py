string = input()
def isPalindrome(string):
    string =''.join(filter(str.isalnum, string))
    return string.lower() == string[::-1].lower()
print (isPalindrome(string))





