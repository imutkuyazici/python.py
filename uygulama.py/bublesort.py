#buble sort

liste=[6,4,5,1,3,2] ##kendi belirledigim liste
uzunluk=len(liste) 

for i in range (0,uzunluk-1):
    min=i
    for b in range(i+1,uzunluk) :
        if liste[b]<liste[i]:
            yedek=liste[i]
            liste[i]=liste[b]
            liste[b]=yedek
            print(liste)

