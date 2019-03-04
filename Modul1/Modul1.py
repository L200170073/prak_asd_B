#Soal - soal untuk mahasiswa

#Nomor 1 :
def cetakSiku(x):
    for i in range(x):
        for j in range(i+1):
            print("*", end="")
        print()

#Nomor 2:
def gambarlahPersegiEmpat(x,y):
    for i in range(x):
        if i == 0 or i == x-1:
            print("@"*y)
        else:
            print ("@"+" "*(y-2)+"@")

#Nomor 3:
## A
def jumlahHurufVokal(x):
    hvokal=["a","i","u","e","o","A","I","U","E","O"]
    hitung = 0
    for i in x :
        if i in hvokal:
            hitung +=1
    huruf = len(x)
    return (huruf, hitung)
## B
def jumlahHurufKonsonan(x):
    hkonsonan="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    hitung = 0
    for i in x :
        if i in hkonsonan:
            hitung +=1
    huruf = len(x)
    return (huruf, hitung)

#Nomor 4:
def rerata(b):
    jum = 0
    for i in b:
        jum += i
        hasil = (jum/len(b))
    return hasil

#Nomor 5:
from math import sqrt as sq
def apakahPrima(n):
    n = int(n)
    assert n>=0
    primaKecil = [2,3,5,7,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2, int(sq(n))+1):
            if n%i == 0:
                return False
                break
            else:
                return True

#Nomor 6:
from math import sqrt as sq
n=100
for i in range(2,60):
	print (i)

#Nomor 7:
def faktorPrima(n) : # n untuk input yang akan di dicari faktor prima nya
    a = []  #menyimpan bilangan prima
    b = []  #menyimpan faktor prima dari bilangan yg diinputkan
    hasil = 0
    bil = n
    prima =True
    for i in range(2,n):
        prima = True
        for u in range(2, i) :
            if i % u == 0 :
               prima = False
        if prima :
            a.append(i)     #menambahkan bilangan prima ke variabel a
    idx = 0
    while bil > 1 :      
        try:    #untuk mengatasi error saat index out of range,semisal list pnya 5 data maka ketika mengindex data ke6 akan error.
            if (bil%a[idx]) == 0 : # a[idx] untuk mengambil bilangan prima dari list a berdasarkan indexing nya
                hasil = bil/a[idx]
                bil = hasil
                b.append(a[idx])#memasukkan faktor primanya ke 'b'
            else :
                idx = idx + 1
        except IndexError :
            break
    print (b)

#Nomor 8:
def apakahTerkandung(h,k):
    return h.lower() in k.lower()

#Nomor 9:
def CetakAngka(x):
    i = 0
    for i in range (x):
        if i % 3 == 2 and i % 5 == 4:
            print("Python UMS")
        elif i % 3 == 2:
            print("Python")
        elif i % 5 == 4:
            print("UMS")
        else:
            print(i + 1)

#Nomor 10:
def selesaikanABC(a,b,c):
    if a <= 0 and b <= 0 and c <= 0:
        print("Determinannya Positif. Persamaan Mempunyai akar Real")
    else:
        print("Determinannya Negatif. Persamaan tidak Mempunyai akar Real")

#Nomor 11:
import datetime;
def apakahKabisat(x):
    if (x % 4) == 0:
        if (x % 100) == 0:
            if (x % 400) == 0:
                print ("Tahun Kabisat")
            else:
                print("Bukan Tahun Kabisat")
        else:
            print("Tahun Kabisat")
    else:
        print("Bukan Tahun Kabisat")

#Nomor 12:
import random;

def Number(a):

    n = random.randint(0, 100)
    
    print("Permainan Tebak Angka")
    print("Ssya  Menyimpan Sebuah Angka bulat Antara 1 sampai 100. Coba tebak")

    bil = -1

    while bil != a:

        bil =  eval(input("Masukan Tebakan"))

        if bil == a:
            print("Ya. Anda Benar", a)
        elif bil > a:
            print("Itu Terlalu Besar. Coba Lagi")
        elif bil < a:
            print("Itu Terlalu Kecil. Coba Lagi")
print(Number(9))

#Nomor 13:
def katakan(x):
    angka = ["","Satu ","Dua ","Tiga ","Empat ","Lima ","Enam ",
             "Tujuh ","Delapan ","Sembilan ","Sepuluh ","Sebelas "]
    hasil = ""
    n = int(x)
    if n >= 0 and n <= 11:

 
        hasil = angka[n]
    elif n < 20:
        hasil = katakan(n-10) + " Belas "
    elif n < 100:
        hasil = katakan(n/10) + " Puluh " + katakan(n%10)
    elif n < 200:
        hasil = " Seratus " + katakan(n-100)
    elif n < 1000:
        hasil = katakan(n/100) + " Ratus " + katakan(n%100)
    elif n < 2000:
        hasil = " Seribu " + katakan(n-1000)
    elif n < 1000000:
        hasil = katakan(n/1000) + " Ribu " + katakan(n%1000) 
    elif n < 1000000000:
        hasil = katakan(n/1000000) + " Juta " + katakan(n%1000000)
    elif n > 1000000000:
        hasil = 'Maaf, program tidak membaca angka lebih dari Satu Milyar'
    return hasil


a = 1
while a != 0:
    a = input(' Masukkan angka dari 1 sd 1.000.000.000: ')
    huruf = katakan(a)
    print(huruf +' Rupiah')

#Nomor 14:
def formatRupiah(x):
    y = str(x)
    if len(y) <= 3 :
        return 'Rp ' + y     
    else :
        p = y[-3:]
        q = y[:-3]
        return   formatRupiah(q) + '.' + p
        print ('Rp' +  (formatRupiah(q)) + '.' + p) 
