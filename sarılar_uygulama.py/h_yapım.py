satir=int(input(" Lütfen bir satır sayısı giriniz : "))

for i in range(1,satir,+1):
    print("*"*i,end=" ")
    print(" "*(satir-i)*2,end="")   ####üst taraf####
    print ("*"*i)
for i in range(satir,0,-1):
    print("*"*i,end=" ")
    print(" "*(satir-i)*2,end="")   ####üst taraf####
    print ("*"*i)

#row=satır0


