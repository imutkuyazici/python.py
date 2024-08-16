ust_alt_taraf = 9 
ic_kare_yildiz = 5
ic_kare_boyut = 6
sag_sol_taraf=10

def kare(ust_alt_taraf, sag_sol_taraf, ic_kare_yildiz, ic_kare_boyut):
    
    print('* ' * (ust_alt_taraf - 1) + '*')

    for i in range((sag_sol_taraf - ic_kare_boyut) // 2 - 1):
        print('*' + '  ' * (ust_alt_taraf - 2) + ' *')
        
    print('*' + '  ' * ((ust_alt_taraf - ic_kare_yildiz) // 2) + '* ' * (ic_kare_yildiz - 1) + '*')

    for _ in range(ic_kare_boyut - 2):
        print('*' + '  ' * ((ust_alt_taraf - ic_kare_yildiz) // 2) + '*' + '  ' * (ic_kare_yildiz - 2) + ' *' + '  ' * ((ust_alt_taraf - ic_kare_yildiz) // 2 - 1) + ' *')

    print('*' + '  ' * ((ust_alt_taraf - ic_kare_yildiz) // 2) + '* ' * (ic_kare_yildiz - 1) + '*')

    for i in range((sag_sol_taraf - ic_kare_boyut) // 2 - 1):
        print('*' + '  ' * (ust_alt_taraf - 2) + ' *')

    print('* ' * (ust_alt_taraf - 1) + '*')

kare(ust_alt_taraf,sag_sol_taraf,ic_kare_boyut,ic_kare_yildiz)

