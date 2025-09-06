class Palidrome :

    def __init__(self, string):
        self.string = string

    def isPalindrome(self):
        string = ''.join(filter(str.isalnum,self.string))

        if string.lower() == string[::-1].lower() :
            return True
        else :
            return False


string = Palidrome(input('Введите строку :'))

print (string.isPalindrome())





