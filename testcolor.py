import sys
from colorama import Fore, Back, Style
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.RESET_ALL)
# print(Style.BRIGHT + 'and in dim text')
# print('back to normal now')


def lprint(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text))

lprint(10,1,"jorge")

for x in range(1,81):
    lprint(x,1,"-")
    lprint(x,24,"-")
for y in range (2,24):
    lprint(1,y,"|")
    lprint(80,y,"|")

lprint(1,26,"Hola")