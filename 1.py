def hitungKembalian(total, uang):
    stok = [50000,20000,10000,5000]
    cashback = 0
    if total > 200000:
        cashback = total*10/100
    kembali = uang - total + cashback
    for i in stok:
        if kembali / i >= 1:
            print("%d lembar %d"%(kembali//i,i))
        kembali = kembali % i
    if kembali != 0:
        print("%d Disumbangkan karena tidak ada pecahan dibawah 5000"%kembali)


hitungKembalian(200000,250000)
