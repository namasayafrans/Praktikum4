a = input ("masukan nilai pertama : ")
b = input ("masukan nilai kedua : ")
c = input ("masukan nilai ketiga : ")

if a < b and a < c:
        if b < c:
            print(a, b, c)
        else:
            print(a, c, b)
elif b < a and b < c:
        if a < c:
            print(b, a, c)
        else:
            print(b, c, a)
else:
    print(c, a, b)

