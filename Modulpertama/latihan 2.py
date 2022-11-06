print("mengurutkan nilai terkecil - terbesar")
print("============================")

a = input("masukan angka pertama : ")
b = input("masukan angka kedua : ")
c = input("masukan angka ketiga : ")

if a < b and a < c:
    if b < c:
        print(a, b, c)
    else:
        print(a, c, b)
if b < a and b < c:
    if a < b:
        print(b, c, a )
    else:
        print(b, c, a,)
else:
    print(c, b, a)