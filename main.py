import os

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'}

def encrypt(message):
    output = ''
    for letter in message:
        if letter != ' ':
            output += MORSE_CODE_DICT[letter] + '\n'
        else:
            output += '\n'
    output += '\n'
    return output

def decrypt(message):
    message += ' '
    output = ''
    sentence = ''
    for letter in message:
        if (letter != '\n'):
            i = 0
            sentence += letter
        else:
            i += 1
            if i == 2 :
                output += ' '
            else:
                output += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(sentence)]
                sentence = ''
    return output


input_file_name = input("Wpisz nazwę pliku wejściowego: ")
output_file_name = input("Wpisz nazwę pliku wyjściowego: ")
conversion_type = input("Wpisz numer typu konwersji (0 - z tekstu na morsa lub 1 - z morsa na tekst): ")

# wczytaj zawartość pliku wejściowego
with open(input_file_name, 'r') as input_file:
    message = input_file.read()

if conversion_type == "0":
    converted_message = encrypt(message.upper())
elif conversion_type == "1":
    converted_message = decrypt(message)
else:
    print("Zły typ konwersji!")

# wypisz przekonwertowaną wiadomość do pliku tekstowego
with open(output_file_name, 'w') as output_file:
    output_file.write(converted_message)
