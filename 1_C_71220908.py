kata = input("Masukkan Kata atau angka:")

def reverse(kata):
    str = ""
    for i in kata:
        str = i + str
    return str

print(reverse(kata))