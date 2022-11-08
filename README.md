# Tugas-ke-7
Nama    : Frans Putra Sinaga

NIM     : 312210046

Kelas   : TI.22.A1

### DAFTAR ISI <br>
| No | Description | Link |
| ----- | ----- | ---- |
| 1 | Lab 2 : Struktur Kondisi | [Silahkan Klik](#Lab-2-Struktur-Kondisi) |
| 2 | Lab 3 : Perulangan | [Silahkan Klik](#Lab-3-Perulangan) |
| 3 | modul praktikum2 | [Silahkan Klik](#Labpy02) |
| 4 | modul praktikum3  | [Silahkan Klik](#Labpy03) |
| 5 | Author  : Danang Nurcahyo | [Silahkan Klik](#Author-DANUR) |




# KONDISI DAN PERULANGAN

## Lab 2 Struktur Kondisi

### Latihan 1

• Buat program sederhana dengan input 2 buah bilangan, kemudian tentukan bilangan terbesar dari kedua bilangan tersebut menggunakan statement if!

Langkah - langkah 

1. Buat programnya terlebih dahulu seperti gambar di bawah ini

![Screenshot (65)](https://user-images.githubusercontent.com/115677839/200220587-e2a4e40a-adfa-4482-b522-dd6bb5dc6a9d.png)



# menentukan bilangan
print('Menentukan bilangan terbesar dari 2 bilangan')
a = int(input("Masukkan nilai A:"))
b = int(input("Masukkan nilai B:"))
if a > b:
    print("A =", a, "yang terbesar")
elif b > a:
    print("B=", b, "yang terbesar")
`

2. Hasil Run 
![Screenshot (66)](https://user-images.githubusercontent.com/115677839/200220791-7b71dfc3-488b-4bac-b2e9-311ea0848a6b.png)

### Latihan 2
• Buat program untuk mengurutkan data berdasarkan input sejumlah data (minimal 3 variable input atau lebih), kemudian tampilkan hasilnya secara berurutan mulai dari data terkecil.

Langkah - langkah
programnya terlebih dahulu seperti gambar di bawah ini
1. Buat ![Screenshot (67)](https://user-images.githubusercontent.com/115677839/200220987-86be9399-e126-4fea-9483-4ebb76e8a991.png)


print("_____Mengurutkan bilangan dari yang terkecil ke yang terbesar_____")
print("Masukan 3 bilangan yang akan diurutkan:")
a = int(input("masukkan bilangan 1 = "))
b = int(input("masukkan bilangan 2 = "))
c = int(input("masukkan bilangan 3 = "))

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
    if a < b:
        print(c, a, b)
    else:
        print(c, b, a)
`

2. Hasil Run
![Screenshot (68)](https://user-images.githubusercontent.com/115677839/200221153-bd26fb31-211e-4f6a-b948-45c95b2f4203.png)

## Lab 3 Perulangan

### Latihan 1
• Buat program dengan perulangan bertingkat (nested) for yang menghasilkan output sebagai berikut:

![tugas](https://user-images.githubusercontent.com/115678171/200156779-cc2eb0c1-293c-4089-84d8-7dde04482340.png)

Langkah - langkah
1. Buat programnya terlebih dahulu seperti gambar di bawah ini

![Screenshot (70)](https://user-images.githubusercontent.com/115677839/200221455-6fb1d139-279d-4c46-9dfe-7e70f2554d26.png)


for i in range(0,10):
    print()
    print(i, end="\t")
    for j in range(1,10):
        print(i+j,end="\t")
`
2. Hasil Run

![Screenshot (71)](https://user-images.githubusercontent.com/115677839/200221521-3e90f11e-0f7a-4d5e-a6e2-20c0557420fa.png)


### Latihan 2
• Tampilkan n bilangan acak yang lebih kecil dari 0.5.

• nilai n diisi pada saat runtime

• anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya

Langkah - langkah
programnya terlebih dahulu seperti gambar dibawah ini

1. Buatlah![Screenshot (72)](https://user-images.githubusercontent.com/115677839/200221660-a596e3a8-bc83-405f-89e1-0e1f91974543.png)

from random import random

n = int(input("Masukan Beberapa perulangan : "))
while n == n:
    break
for i in range(n):
    bil = random() % 0.5
    print("Perulangan ke : ", bil)
`
2. Hasil Run

![Screenshot (73)](https://user-images.githubusercontent.com/115677839/200221764-81e12400-72b4-4888-ab7a-fb0539594b33.png)

# MODUL PRAKTIKUM 2 DAN 3

## Labpy02 dan Labpy03

### Labpy02
• Buat program sederhana dengan input tiga buah bilangan, dari ketiga bilangan tersebut tampilkan bilangan terbesarnya. Gunakan statement if.

Langkah - langkah
1. Buatlah flowchart dari mencari angka terbesar dari 3 bilangan seperti gambar dibawah ini

![Flowchart program mencari angka terbesar](https://user-images.githubusercontent.com/115678171/200159462-6b7e6bcb-8a43-4d48-a4c4-5bf8bda85a42.png)

2. Buatlah program codenya seperti gambar dibawah ini

![Mencari angka terbesar dari 3 bilangan ](https://user-images.githubusercontent.com/115678171/200159489-cf95f820-11ad-4366-a852-11da99dcfb2c.png)

a, b, c = (
    int(input('Masukkan nilai a: ')),
    int(input('Masukkan nilai b: ')),
    int(input('Masukkan nilai c: '))
)
if a > b and a > c:
    print('A yang terbesar')
elif b > a and b > c:
    print('B yang terbesar')
else:
    print('C yang terbesar')
`
3. Hasil dari Run

![Run Mencari angka terbesar dari 3 bilangan](https://user-images.githubusercontent.com/115678171/200159535-dce4f301-3d18-433f-9af9-170e57869329.png)

## Labpy03

### Latihan 1

Flowchart dari latihan 1

![Floawchart lat 1 labpy03](https://user-images.githubusercontent.com/115678171/200159707-ccb1abdb-be69-4849-96c8-6c02c439d199.png)

### Algoritma dari latihan 1
Menampilkan n bilangan acak yang lebih kecil dari 0,5, nilai n diisi pada saat runtime.

1.Memasukan/ import fungsi RANDOM terlebih dahulu

2.Deklarasi integer , masukkan jumlah n :

3.Memasukan deskripsi kombinasi for untuk menyelesaikannya.

4.Memasukan nilai jumlah (n) : 5

5.Mencetak data ke 1 sampai 5 dengan hasil nilai kurang dari 0,5.

6.Selesai

Langkah - langkah

1. Buat program caodenya seperti gambar dibawah ini 

![Screenshot (78)](https://user-images.githubusercontent.com/115677839/200224007-15492498-16ae-47d5-aeec-453781c207ac.png)

print("bilangan acak yang lebih kecil dari o.5")
import random

n = int(input("masukan nilai:"))
a = 0
for c in range(n):
    a += 1
    b = random.uniform(.0, .5)
    print("data ke:", a, "==>", i)

print("selesai")
`
2. Hasil Run 

![Screenshot (79)](https://user-images.githubusercontent.com/115677839/200224054-f45955bf-da4e-46e6-a70a-cf956cf0caa8.png)


### Latihan 2

Flowchart dari latihan 2

![Flowchart lat 2 labpy03](https://user-images.githubusercontent.com/115678171/200159970-42dd1c12-2af8-416d-b808-822ed3c3c7fc.png)

### Algoritma latihan 2

Membuat program untuk menampilkan bilangan terbesar dari n buah data yang diinputkan.Masukkan angka 0 untuk berhenti

1.Mulai

2.Mencetak "latihan 2"

3.Mencetak "menampilkan bilangan, berhenti ketika bilangan 0, menampilkan bilangan terbesar"

4.integer max = 0

5.Menggunakan fungsi perulangan while true, hingga menampilkan perulangan sampai batas tertentu.

6.Memasukan bilangan integer pada "a"

7.Menggunakan fungsi if jika max kurang dari nilai a, maka max sama dengan a

8.Mengunakan fungsi if jika nilai a adalah 0 maka fungsi break artinya perulangan berhenti jika menulis nilai 0.

9.Mencetak nilai paling terbesarv setelah break, sehingga menampilkan nilai terbesar diantara bilangan tersebut dalam perulangan.

10.Selesai

Langkah - langkah

1. Buatlah program code seperti gambar dibawah ini

![Lat 2 labpy03](https://user-images.githubusercontent.com/115678171/200160088-30776945-8ecb-43f6-a0e0-920299103224.png)

print("menampilkan bilangan, berhenti ketika bilangan 0, dan menampilkan bilangan terbesar")

max = 0
while True:
    angka = int(input("masukan bilangan : "))
    if max < angka:
        max = angka
    if angka == 0:
        break
print("bilangan terbesarnya adalah = ", max)
print("======selesai======")
`
2. Hasil Run

![Run lat 2 labpy03](https://user-images.githubusercontent.com/115678171/200160147-58f2c04e-970f-4781-b34b-e4bd61d64e37.png)

### Program 1

Flowchart dari program 1

![Flowchart Program 1](https://user-images.githubusercontent.com/115678171/200160200-2f3db728-7d3d-48c0-b21a-b8d3bf11438b.png)

### Algoritma dari program 1

1.Mulai

2.Mencetak latihan1

3.Mencetak "Program menghitung laba dengan modal awal 100 juta"

4.Membuat Note

5.Mencetak Bulan pertama dan kedua = 0%

6.Mencetak bulan ke 3 = 1%

7.Mencetak bulan ke 5 = 5%

8.Mencetak bulan ke 8 = 2%

9.integer a = 100.000.000( modal awal)

10.Menggunakan fungsi looping for pada nilai x 1-9 untuk menampilkan bulan 1 sampai bulan 8.

11.Menggunakan fungsi if, untuk menghitung laba bulan 1 sampai 8

12.bulan pertama dan kedua laba adalah 0

13.bulan ke 3 dan ke 4 mendapat laba 1% sehingga modal di kali 1% = keuntungan

14.bulan ke 5 mendapatkan laba 5%, sehingga modal dikali 5% = keuntungan

15.Bulan ke 8 mmendapatkan laba 2% sehingga keuntungan menurun dari bulan sebelumnya, modal dikali 2% = keuntungan.

16.Menghitung jumlah total laba dengan menjumlah keuntungan dari bulan ke 1 sampai bulan 8, hasilnya adalah total keuntungan yang didapat.

17.Selesai

Langkah - langkah

1. Buatlah program codenya seperti gambar dibawah ini

![Program 1](https://user-images.githubusercontent.com/115678171/200160306-fc80e487-e655-4d7d-a633-c54acaaeb641.png)

x = 100000000
sum = 0
y = 0
lb = [int(0), int(0), int(x) * .1, int(x) * .1, int(x) * .5, int(x) * .5, int(x) * .5, int(x) * .2]
print("modal awal seorang pengusaha :', x")
for i in lb:
    sum = sum + i
    y += 1
    print("#laba bulan ke - ", y, "sebesar :", i)

    print("  TOTAL LABA YANG DIDAPAT ADALAH :", sum)
`
2. Hasil Run

![Run Program 1](https://user-images.githubusercontent.com/115678171/200160346-15ada2ee-a65f-480e-b36f-63d3a5804d57.png)

Sekian penjelasan dari saya Terima Kasih 

### Author Scorpio
