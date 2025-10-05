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

<<<<<<< HEAD
print (string.isPalindrome())
=======
print (string.isPalindrome())





>>>>>>> 27b1679cb9fa73711e7953a797ec09e2b2b3f8fc
