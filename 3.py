def cetak_gambar(panjang):
    if panjang %2 ==0 :
        return false
    tengah, jarak = panjang//2 + 1, panjang//2
    for i in range(panjang):
        if i+1 < tengah:            
            if tengah - jarak != 1:
                print(" "*(jarak), end="")
                print("*"+" "*(tengah-(jarak+2)), end="")
                print("*", end="")
                print(" "*(tengah-(jarak+2))+"*")
            else:
                print(" "*jarak+"*")
            jarak = jarak -1            
        else:
            if jarak == 0:
                print("*"*panjang)
            elif tengah - jarak != 1:
                print(" "*(jarak), end="")
                print("*"+" "*(tengah-(jarak+2)), end="")
                print("*", end="")
                print(" "*(tengah-(jarak+2))+"*")
            else:
                print(" "*jarak+"*")
            jarak = jarak + 1    

cetak_gambar(11)        
