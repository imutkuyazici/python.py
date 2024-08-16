cumle=input("lütfen bir cümle giriniz : ")
def mtt_title(cumle):
    cumle_y=""
    bosluk=True
    for i in cumle :
        if bosluk == True :
            if type(i)==int :
                cumle_y+=i
                bosluk=False
            else:
                cumle_y+=i.upper()
                bosluk=False
        else:
            if i == " " :
                cumle_y+=i
                bosluk=True
            elif type(i)==int:
                cumle_y+=i
            else:
                cumle_y+=i.lower()
    return cumle_y

print(mtt_title(cumle))
               
