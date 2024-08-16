dizi = input("Lütfen Bir Dizi Veya Kelime Girin : ")

def diziyi_tersine_cevirme(dizi):
    ters_dizi=dizi[ : : -1]
    return ters_dizi                        


ters_dizi=diziyi_tersine_cevirme(dizi)


if ters_dizi == dizi :
    print("kelime palingramdır ")
else:
    print("kelime palingram degildir ")

