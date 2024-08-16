#hesap makinesi#
import os
import math

def toplama_islemi():
    os.system("cls")
    sayı1=float(input("lütfen islem yapmak istediginiz birinci sayıyı giriniz : "))
    sayı2=float(input("lütfen islem yapmak istediginiz ikinci sayıyı giriniz : "))
    sonuc=sayı1+sayı2
    print(sonuc)
    input(" ")
    os.system("cls")

def cıkarma_islemi():
    os.system("cls")
    sayı1=float(input("lütfen islem yapmak istediginiz birinci sayıyı giriniz : "))
    sayı2=float(input("lütfen islem yapmak istediginiz ikinci sayıyı giriniz : "))
    sonuc=sayı1-sayı2
    print(sonuc)
    input(" ")
    os.system("cls")

def bölme_islemi():
    os.system("cls")
    sayı1=float(input("lütfen islem yapmak istediginiz birinci sayıyı giriniz : "))
    sayı2=float(input("lütfen islem yapmak istediginiz ikinci sayıyı giriniz : "))
    sonuc=sayı1/sayı2
    print(sonuc)
    input(" ")
    os.system("cls")

def carpma_islemi():
    os.system("cls")
    sayı1=float(input("lütfen islem yapmak istediginiz birinci sayıyı giriniz : "))
    sayı2=float(input("lütfen islem yapmak istediginiz ikinci sayıyı giriniz : "))
    sonuc=sayı1*sayı2
    print(sonuc)
    input(" ")
    os.system("cls")

def sayının_karesi():
    os.system("cls")
    sayı1=float(input("lütfen karesini hesaplamak istediginiz sayıyı giriniz : "))
    sonuc=sayı1*sayı1
    print(sonuc)
    input(" ")
    os.system("cls")

def sayının_kupu():
    os.system("cls")
    sayı1=float(input("lütfen kupunu almak istediginiz sayıyı giriniz : "))
    sonuc=sayı1*sayı1*sayı1
    print(sonuc)
    input(" ")
    os.system("cls")

def factorial():
    os.system("cls")
    sayı1=float(input("lütfen faktöriyelini hesaplamak istediginiz sayıyı giriniz : "))
    factorial = math.factorial(sayı1)
    print(f"{sayı1} faktöriyeli: {factorial}")
    input(" ")
    os.system("cls")

while True :
    secim=input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz \n\n1-Toplama\n\n2-Çıkarma\n\n3-Bölme\n\n4-Çarpma\n\n5-çıkış\n\n6-Bir sayının karesini hesaplama\n\n7-bir sayının küpünü alma\n\n8-sayının faktöriyelini alma\n\nSeçiminiz : ")
    if secim == "1" : 
        os.system("cls")
        toplama_islemi()
    elif secim == "2":
        os.system("cls")
        cıkarma_islemi()
    elif secim == "3":
        os.system("cls")
        bölme_islemi()
    elif secim =="4":
        os.system("cls")
        carpma_islemi()
    elif secim == "6":
        os.system("cls")
        sayının_karesi()
    elif secim == "7":
        os.system("cls")
        sayının_kupu()
    elif secim == "8":
        os.system("cls")
        factorial()
    elif secim == "5":
        os.system("cls")
        print("işleminiz gerçekleştiriliyor....")
        input("lütfen devam etmek icin 'enter' tusuna basınız ")
        break
    else:
        os.system("cls")
        print("gecersiz secim lutfen daha sonra tekrar deneyiniz...")
        input("ana ekrana dönmek icin 'enter' tusuna basınız : ")
