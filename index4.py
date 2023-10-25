# a = ["1,2,3,4"]
# nama=["jagung,apel"]

# print(nama)

# cuaca=input("apakah cuaca pada hari ini?")
# match cuaca:
#     case "panas":
#         print("ke kampus memakai mobil")
#     case "hujan":
#         print("ke kampus memakai jas hujan")
#     case "badai":
#         print("tidak berangkat ke ke kampus")
#     case _:
#         print("berangkat ke kampus")

# a=int (input("masukan bilangan 1:"))
# b=int(input("masukan bilangan 2:"))

# luas=3.14 * a * a
# print(luas)

#(---latihan---)
# buat variabel list dengan value:[nama kendaraan, jenis kendaraan, cckendaraan, warna kendaraan, roda kendaran]
# tambahakan dari list tersebut di belakamg dengan value:[harga kendaraan, tipe kendaraan]
# tambahkan setelah jenis kendaraan dengan value [merek kendaraan]

# buat program python dengan macth case untuk menghuting luas
# bangun datar:
# jika pilih 1, maka menghitung luas persegi
# jika pilih 2, maka menghitung luas lingkaran
# jika pilih 3, maka menghitung luas segitiga
# selain pilihan di atas maka keterangan : salah pilih angka

#membuat variabel list dengan value
# nama_kendaraan=["motor,mobil"]
# jenis_kendaraan=["2019,2020,2021,2022"]
# cckendaraan=[100,200,250,700,750,300]
# warna_kendaraan=["merah,kuning,hijau"]
# roda_kendaraan=["roda 2, roda 4"]
# harga_kendaraan=[7,8,40,550,600,800,]
# tipe_kendaraan=["matic,koping,manual"]
# merek_kendaraab=["vario,beet,vesmet,bmw,suppra,avanza"]




#(---menghitung luas---)
# bangun_datar=int(input("masukan bangun datar:"))
# a=int(input("masukan bilangan 1:"))
# b=int(input("masukan bilangan 2:"))

# rumus_persegi=a * a
# rumus_lingkaran= 3.14 * a
# rumus_segitiga= 0.5 * a * b

# match bangun_datar:
#     case "persegi":
#         print(rumus_persegi)
#     case "lingkaran":
#         print(rumus_lingkaran)
#     case "segitiga":
#         print(rumus_segitiga)


#(---latihan---)
#(---bangun datar---)
# bangun_datar=int(input("masukan jenis bangun datar:"))
# match bangun_datar :
#     case 1 : 
#         print("s x s")
#         s1 = float(input("Sisi 1 :"))
#         s2 = float(input("Sisi 2 :"))
#         hasil= s1 * s2
#         print("hasilnnya adalah:", hasil)
#     case 2 : 
#         print("3,14 * r * r")
#         r1 = float(input("r1 :"))
#         r2 = float(input("r2 :"))
#         hasil= 3.14 * r1 * r2
#         print("hasilnya adaalah", hasil)
#     case 3 :
#         print("1/2 x alas x tinggi")
#         alas = float(input("alas :"))
#         tinggi = float(input("tingi :"))
#         hasil = 0.5 * alas * tinggi
#         print("hasilnya adalah :", hasil)

#(---list kendaraan---)
list = ["mobil", "sport", "5000", "merah", "roda 4"]

list.append("7000 dolar")
list.append("sport")
list.insert(2, "ferrary")

print(list)

