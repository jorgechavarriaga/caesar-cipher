from colorama import Fore, Back, Style

import os
import art

def cc():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_text += char

  print(f"Here's the {cipher_direction}d result: {Fore.YELLOW}{end_text}{Style.RESET_ALL}\n")

def start():
    cc()

    print(f"{Fore.BLUE}{art.logo}{Style.RESET_ALL}")
    direction = input(f"Type {Fore.GREEN}'encode'{Style.RESET_ALL} to encrypt, type {Fore.RED}'decode'{Style.RESET_ALL} to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: ")) % 25

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    again = input(f"\nType {Fore.GREEN}'yes'{Style.RESET_ALL} if you want to go again. Otherwaise type {Fore.RED}'no'{Style.RESET_ALL}. \n").lower()
    if again == "yes":
        start()
    else:
        print("Goodbye")

start()
