tercih = input("toplama icin 1 , bolme icin 2 ye basiniz : ")


def toplama():
    x1 = input("birinci sayiyi giriniz : ")
    x2 = input("birinci sayiyi giriniz : ")
    print("toplam : " , int(x1) + int(x2) )


def bolme():
    x1 = input("birinci sayiyi giriniz : ")
    x2 = input("birinci sayiyi giriniz : ")
    print("toplam : " , int(x1) / int(x2) )

    
if int(tercih) == 1:
    toplama()
if int(tercih) == 2:
    bolme()
