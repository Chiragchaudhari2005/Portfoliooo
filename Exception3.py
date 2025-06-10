#Used defined exception using raise keyword

class InvalidPhoneException(Exception):
    def __init__(self,str):
        self.str = str

mobile = input('Enter phone no: ')

try:
    if(len(mobile)!=10):
        raise InvalidPhoneException('Invalid number')
    else:
        print('Valid number')
except InvalidPhoneException as obj:
    print(obj)
