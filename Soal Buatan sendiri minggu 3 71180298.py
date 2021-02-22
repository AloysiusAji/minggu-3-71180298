#Aloysius Gonzaga Ardhian Krisna Aji
#71180298

'''Ilham memiliki usaha peternakan ikan koi ,
untuk ikan koi tersebut memiliki variasi harga:  
1.ukuran kecil Rp. 15.000/ biji
2.ukuran sedang Rp. 60.000/ biji 
3.ukuran super Rp. 250.000/ biji
untuk pembelian ukuran super di atas 6 biji mendapatkan diskon sebesar 5% 
untuk pembelian ukuran sedang di atas 12 biji mendapatkan diskon sebesar 8%
Ilham memerlukan bantuan program komputer untuk membantu membuat hasil catatannya dan menu ringkasnya.'''

'''
input
-nama pembeli
-inputan variasi(kecil,sedang,super)
-input jumlah ikan yang ingin di beli
Output
-keluar nama pembeli
-keluar harga total yang harus di bayar pembeli
'''
print("---Peternakan Ikan Koi Ilham---")

pembeli = str(input("Masukan Nama Pembeli: "))

print("Variasi Ikan Koi: ")
print("1.ukuran kecil Rp. 15.000/ biji")
print("2.ukuran sedang Rp. 60.000/ biji")
print("3.ukuran super Rp. 250.000/ biji")

menu = int(input("Masukan Inputan anda: "))
if menu == 1:
    jumlah = int(input("Jumlah Ikan yang Pembeli Inginkan: "))
    hargaawal = 15000
    hargaakhir = hargaawal * jumlah
    print("Total yang harus dibayar",pembeli,": ", hargaakhir)
elif menu == 2:
    jumlah = int(input("Jumlah Ikan yang Pembeli Inginkan: "))
    hargaawal1 = 60000
    if jumlah > 12 :   
        hargaakhir1 = hargaawal1 * jumlah
        diskon = hargaakhir1 * 8 / 100
        hargatotal = hargaakhir1 - diskon
        print("Total yang harus dibayar",pembeli,": ", hargatotal)
    else:
        hargaakhir2 = hargaawal1 * jumlah
        print("Total yang harus dibayar",pembeli,": ", hargaakhir2)

elif menu == 3:
    jumlah = int(input("Jumlah Ikan yang Pembeli Inginkan: "))
    hargaawal3 = 250000
    if jumlah > 6 :
        hargaakhir3 = hargaawal3 * jumlah
        diskon1 = hargaakhir3 * 5/100
        hargatotal2 = hargaakhir3 - diskon1
        print("Total yang harus dibayar",pembeli,": ", hargatotal2)
    else :
        hargaakhir4 = hargaawal3 * jumlah
        print("Total yang harus dibayar",pembeli,": ", hargaakhir4)
else: 
    print("Inputan yang anda masukan salah")


