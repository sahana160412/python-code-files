class IoString():
    def __int__(self):
        self.str1=""
    def get_string(self):
        self.str1 = input("Enter String: ")
    def print_string(self):
        print("result is:",self.str1.upper())

str1=IoString()
str1.get_string()
str1.print_string()