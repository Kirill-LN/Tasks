class String :

    def __new__(cls, *args, **kwargs):
        print('Вызов __new__ для ' + str(cls) )
        return super().__new__(cls)

    def __init__(self, string):
        print('Вызов метода __init__ для ' + str(self))
        self.string = string

    def isPalindrome(self, string):
        print ('Вызов метода isPalindrome для ' + str(self))
        string = ''.join(filter(str.isalnum(string)))
        return string.lower() == string[::-1].lower()


string = String(input())

string.isPalindrome(string)







