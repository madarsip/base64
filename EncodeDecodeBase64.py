import base64
from os import system
from termcolor import colored
import pyfiglet

system("clear")
title = pyfiglet.figlet_format("Base64", font="slant")
title_encode = pyfiglet.figlet_format("Encode", font="slant")
title_decode = pyfiglet.figlet_format("Decode", font="slant")

x = 0
while x == 0:
    print(colored(title, 'red'))
    print("1. Base64 Encode")
    print("2. Base64 Decode\n")
    pilih = int(input("Pilih (1/2) : "))
    if pilih == 1:
        e = 0
        while e == 0:
            system("clear")
            print(colored(title_encode, 'red'))
            encode_text = input(str("Encode here : "))
            encode_text_bytes = encode_text.encode("ascii")
            encode_bytes = base64.b64encode(encode_text_bytes)
            encode_string = encode_bytes.decode("ascii")
            print("Your encode: {}\n".format(colored(encode_string, 'red')))
            encode_lagi = input("Encode lagi (y/t) : ")
            if encode_lagi == "t":
                e = 1
    if pilih == 2:
        d = 0
        while d == 0:
            system("clear")
            print(colored(title_decode, 'red'))
            decode_text = input(str("Decode here : "))
            decode_bytes = decode_text.encode("ascii")
            decode_string_bytes = base64.b64decode(decode_bytes)
            decode_string = decode_string_bytes.decode("ascii")
            print("Your decode: {}\n".format(colored(decode_string, 'red')))
            decode_lagi = input("Decode lagi (y/t) : ")
            if decode_lagi == "t":
                d = 1
    x1 = input("Kembali ke awal (y/t) : ")
    if x1 == "y":
        x = 0
        system("clear")
    else:
        print(colored("\nTerima kasih sudah menggunakan tools ini!\n", 'red'))
        exit()

