#  __  __                      ____          _      
# |  \/  | ___  _ __ ___  ___ / ___|___   __| | ___ 
# | |\/| |/ _ \| '__/ __|/ _ \ |   / _ \ / _` |/ _ \
# | |  | | (_) | |  \__ \  __/ |__| (_) | (_| |  __/
# |_|  |_|\___/|_|  |___/\___|\____\___/ \__,_|\___|

ENCRYPT = { 'A':'.-', 'B':'-...', 
    'C':'-.-.', 'D':'-..', 'E':'.', 
    'F':'..-.', 'G':'--.', 'H':'....', 
    'I':'..', 'J':'.---', 'K':'-.-', 
    'L':'.-..', 'M':'--', 'N':'-.', 
    'O':'---', 'P':'.--.', 'Q':'--.-', 
    'R':'.-.', 'S':'...', 'T':'-', 
    'U':'..-', 'V':'...-', 'W':'.--', 
    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
    '1':'.----', '2':'..---', '3':'...--', 
    '4':'....-', '5':'.....', '6':'-....', 
    '7':'--...', '8':'---..', '9':'----.', 
    '0':'-----', ',':'--..--', '.':'.-.-.-', 
    '?':'..--..', '/':'-..-.', '-':'-....-', 
    '(':'-.--.', ')':'-.--.-'
}

DECRYPT = { '.-':'A', '-...':'B',
    '-.-.':'C', '-..':'D', '.':'E',
    '..-':'F', '--':'G', '....':'H',
    '..':'I', '.---':'J', '-.-':'K', 
    '.-..':'L', '--':'M', '-.':'N', 
    '---':'O', '.--.':'P', '--.-':'Q', 
    '.-.':'R', '...':'S', '-':'T', 
    '..-':'U', '...-':'V', '.--':'W', 
    '-..-':'X', '-.--':'Y', '--..':'Z', 
    '.----':'1', '..---':'2', '...--':'3', 
    '....-':'4', '.....':'5', '-....':'6', 
    '--...':'7', '---..':'8', '----.':'9', 
    '-----':'0', '--..--':',', '.-.-.-':'.', 
    '..--..':'?', '-..-.':'/', '-....-':'-', 
    '-.--.':'(', '-.--.-':')'
}

def decrypt(msg):
    upper = msg.upper()
    scentense = upper.split('  ')
    for i in scentense:
        words = i.split(' ')
        for word in words: print(DECRYPT[word], end='')
        print(' ', end='')
    print()

def encrypt(msg):
    scentense = msg.split(' ')
    for word in scentense:
        for char in word: print(ENCRYPT[char], end=' ')
        print(' ', end='')
    print()

print("International Morse Code Translator v1.0")
print("Copyright (c) 2020 miniprime1. All rights reserved.")
print("[Dot: '.'; Dash: '-'; Seperate: ' ', Space: '  ']\n")

print("Options")
print("1. Decrypt Morse Code to Text")
print("2. Encrypt Text to Morse Code")
print("3. Exit")
choice = input("Enter choice: ")

if choice == '1':
    while True:
        i = input("Enter Input: ")
        decrypt(i)

elif choice == '2': 
    while True: 
        i = input("Enter Input: ")
        encrypt(i)