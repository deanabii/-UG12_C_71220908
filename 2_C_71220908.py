x = input("Masukkan angka :")
y = input("Masukkan angka yang dihitung :")

hitung = 0

for i in x:
    if i == y:
        hitung += 1

print("Angka",y,"muncul sebanyak",hitung,"kali")
