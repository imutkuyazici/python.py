kelime_1 = input("lütfen birinci kelimeyi girin : ")
kelime_2 = input("lütfen ikinci kelimeyi girin : ")

def anagram_kontrol(kelime_1,kelime_2):
    kelime_1 = sorted(kelime_1.lower())
    kelime_2 = sorted(kelime_2.lower())
    
    if kelime_1 == kelime_2 :
        return True
    else:
        return False
    

if anagram_kontrol(kelime_1, kelime_2):
    print("girdiginiz kelimeler anagramdır")
else:
    print("girdiginiz kelimeler anagram degildir")
    

 