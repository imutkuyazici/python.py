
#selection sort

liste=[5,3,2,1,6,8,10]
uzunluk=len(liste)

for i in range (0,uzunluk-1):
    min=i
    for b in range(i+1,uzunluk) :
        if liste[min]>liste[b]:
            min=b
    y=liste[i]
    liste[i]=liste[min]
    liste[min]=y
    print(liste)






