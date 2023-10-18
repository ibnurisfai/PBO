#inputan data kubus
print("menghitung luas dan volume kubus")
panjang=int(input("masukan panjang kubus: "))
lebar=int(input("masukan lebar tinggi: "))
tinggi=int(input("masukan tinggi kubus: "))

#proses perhitugan
volume= panjang*lebar*tinggi
luas=(2 * panjang)+(2* lebar)+(2*tinggi)

print("volume kubus", volume)
print("luas kubus",luas)