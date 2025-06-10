#Raise exception if value entered by user is less than zero

class MyException(Exception):
    def __init__(self,str):
        self.str = str

num = int(input('Enter num: '))

try:
    if(num<0):
        raise MyException('Num is less than zero')
    else:
        print('Valid num')

except MyException as obj:
    print(obj)
