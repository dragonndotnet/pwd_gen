import random, string
from colorama import Fore

#colors
c_yellow = Fore.YELLOW
c_green = Fore.GREEN
c_reset = Fore.RESET

pwd_nr = int(input(f"Enter {c_yellow}number{c_reset} of passwords: "))


#shuffle
def shuffle_pwd(pwd):
     pwd_list = list(pwd)
     random.shuffle(pwd_list)
     return "".join(pwd_list)


#loop
for pwd_index in range(pwd_nr):
    pwd = ''
    pwd_len = int(input(f"Enter {c_yellow}length{c_reset} of your password: "))
    withDigits = input(f"Include {c_yellow}digits{c_reset}(y/n)?: ")
    withSpecial = input(f"Include {c_yellow}special chars{c_reset}(y/n)?: ")

    # Convert to integer for calculations
    withDigits_int = 1 if withDigits.lower() == 'y' else 0
    withSpecial_int = 1 if withSpecial.lower() == 'y' else 0

    char_pool = string.ascii_letters #Dynamic built based on user input
    if withDigits == 'y':
        char_pool += string.digits
    if withSpecial == 'y':
        char_pool += string.punctuation

# Generate main part of password
    for index in range(pwd_len - withDigits_int - withSpecial_int):
        pwd += random.choice(char_pool)


    if withDigits_int == 1:
        pwd += random.choice(string.digits)


    if withSpecial_int == 1:
        pwd += random.choice(string.punctuation)
    print(f'[{c_green}201{c_reset}]$-{c_green}{pwd_index}{c_reset}- PWD Generated: {shuffle_pwd(pwd)}')
