#To-Do
""" -What if I want to gen more than 1 pwd?
-That's right! I can't.
-To-Do: All of the above lmao
 """


import random, string
from colorama import Fore

#colors
c_yellow = Fore.YELLOW
c_green = Fore.GREEN
c_reset = Fore.RESET

#global vars
char = string.ascii_letters + string.digits + string.punctuation
pwd = ''
pwd_len = int(input(f"Enter {c_yellow}length{c_reset} of your password: "))


#loop
for index in range(pwd_len):
    pwd = pwd + random.choice(char)

#output
print(f'[{c_green}201{c_reset}]$ PWD Generated: {pwd}')