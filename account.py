# Randomly generates login credentials for an account

import string
import random

class Account:

    def __init__(self, user_length: int = 20, pass_length: int = 20, include_special: bool = True):
        '''
            user_length: length of the username 
            pass_length: length of the password 
            include_special: whether to include special characters in login credentials
        '''

        self.USER_LENGTH = user_length
        self.PASS_LENGTH = pass_length

        if include_special == True:
            self.CHARACTERS  = string.ascii_letters + string.digits + string.punctuation
        else:
            self.CHARACTERS = string.ascii_letters + string.digits

    
    def generate_username(self):
        return ''.join(random.SystemRandom().choices(self.CHARACTERS, k = self.USER_LENGTH)) 
    
    def generate_password(self):
        return ''.join(random.SystemRandom().choices(self.CHARACTERS, k = self.PASS_LENGTH)) 


if __name__ == '__main__':
    user = Account(user_length=20, include_special= False)
    print('Username: {}'.format( user.generate_username() ))
    
    password = Account(pass_length=20, include_special=True)
    print('Password: {}'.format( password.generate_username() ))
