def anagram_kontrol(kelime_1, kelime_2):
    kelime_1 = sorted(kelime_1.lower())
    kelime_2 = sorted(kelime_2.lower())
    
    if kelime_1 == kelime_2:
        return True
    else:
        return False

kelime_1 = input("İlk kelimeyi girin : ")
kelime_2 = input("İkinci kelimeyi girin : ")

if anagram_kontrol(kelime_1, kelime_2):
    print("Girdiğiniz kelimeler anagramdır.")
else:
    print("Girdiğiniz kelimeler anagram değildir.")
