import colorama
import os
from colorama import Fore, Back, Style, init
colorama.init(autoreset=True)
while True:
    text = """
                      ______             _     _ 
                     / _____)           (_)   | |
                    ( (____   ____ _   _ _  __| |
                    \ ____ \ / _  | | | | |/ _  |
                     _____) ) |_| | |_| | ( (_| |
                    (______/ \__  |____/|_|\____|
                                |_|"""
    print(Fore.LIGHTCYAN_EX + text)
    print(end ='\n')
    print(Fore.LIGHTGREEN_EX + "1. Hesap Makinesi")
    user_input = input(Fore.LIGHTBLUE_EX + "Seç : ")
    if user_input  == '1':
        print(Fore.LIGHTGREEN_EX + "HESAP MAKİNESİ")
        print(Fore.LIGHTRED_EX + "1. Toplama")
        print(Fore.LIGHTRED_EX + "2. Çıkarma")
        print(Fore.LIGHTRED_EX + "3. Çarpma")
        print(Fore.LIGHTRED_EX + "4. Bölme")
        secim = input("İşlem yapmak istediğiniz numarayı girin (1/2/3/4): ")
        sayi1 = int(input("İlk sayıyı girin: "))
        sayi2 = int(input("İkinci sayıyı girin: "))
        if secim == '1':
            print(sayi1, "+", sayi2, "=", sayi1+sayi2)
            input(Fore.RED + 'Ana Menüte Dönmek İçin Entera Bas!')
            os.system("cls")
        elif secim == '2':
            print(sayi1, "-", sayi2, "=", sayi1+sayi2)
            input(Fore.RED + 'Ana Menüte Dönmek İçin Entera Bas!')
            os.system("cls")
        elif secim == '3':
            print(sayi1, '*', sayi2, "=", sayi1*sayi2)
            input(Fore.RED + 'Ana Menüte Dönmek İçin Entera Bas!')
            os.system("cls")
        elif secim == '4':
            print(sayi1, '/', sayi2, sayi1/sayi2)
            input(Fore.RED + 'Ana Menüte Dönmek İçin Entera Bas!')
            os.system("cls")