class Palidrome :

    def __new__(cls, *args, **kwargs):
        print('Вызов __new__ для ' + str(cls) )
        return super().__new__(cls)

    def __init__(self, string):
        print('Вызов метода __init__ для ' + str(self))
        self.string = string

    def isPalindrome(self):
        print ('Вызов метода isPalindrome для ' + str(self))
        string = ''.join(filter(str.isalnum,self.string))

        if string.lower() == string[::-1].lower() :
            return True
        else :
            return False


string = Palidrome(input())

print(string.isPalindrome())





