import random, string
from colorama import Fore

#colors
c_yellow = Fore.YELLOW
c_green = Fore.GREEN
c_reset = Fore.RESET

#global vars
pwd_nr = int(input(f"Enter {c_yellow}number{c_reset} of passwords: "))
pwd_len = int(input(f"Enter {c_yellow}length{c_reset} of your password: "))
withDigits = int(input(f"Enter how many {c_yellow}digits{c_reset}: "))
withSpecial = int(input(f"Enter how many {c_yellow}special chars{c_reset}: "))
char = string.ascii_letters + string.digits + string.punctuation


#shuffle
def shuffle_pwd(pwd):
     pwd_list = list(pwd)
     random.shuffle(pwd_list)
     return "".join(pwd_list)



#loop
for pwd_index in range(pwd_nr):
        pwd = ''

        for digits_index in range(withDigits):
            pwd = pwd + random.choice(string.digits)

        for punctuation_index in range(withSpecial):
            pwd = pwd + random.choice(string.punctuation)

        for index in range(pwd_len - withDigits - withDigits):
             pwd = pwd + random.choice(char)
            #output
        print(f'[{c_green}201{c_reset}]$-{c_green}{pwd_index}{c_reset}- PWD Generated: {shuffle_pwd(pwd)}')