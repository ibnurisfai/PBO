import math

print("menghitung luas dan volume slinder(tabung)")
print("____________________________________________")
jari2=int(input("masukan jari-jari slinder(tabung): "))
tinggi=int(input("masukan tinggi slinder(tabung): "))

luas_selimut= 2* math.pi * jari2 * tinggi 
luas_permukaan= 2* math.pi* jari2**2 *tinggi+ 2* math.pi* jari2
volume= math.pi * jari2**2 * tinggi

print("tampilkan hasil menghitung luas dan volume slinder")
print("________________________________________________________")
print("luas selimut selinder: ", luas_selimut)
print("luas permukaan selinder: ",luas_permukaan)
print("volume selinder: ",volume)