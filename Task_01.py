class Palidrome :

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, string):
        self.string = string

    def isPalindrome(self):
        string = ''.join(filter(str.isalnum,self.string))

        if string.lower() == string[::-1].lower() :
            return True
        else :
            return False


string = Palidrome(input())

print(string.isPalindrome())





