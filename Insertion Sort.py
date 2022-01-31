print("Tugas Kelompok 4 No 2", "\n",
        "Membuat Program Dinamis untuk pengurutan secara Insertion Sort")
print()
print("\t", "SELAMAT DATANG DI MESIN PENGURUTAN BILANGAN DENGAN INSERTION SORT", "\t")
print()
"Kita Akan Mengurutkan Bilangan Menggunakan Konsep Insertion Sort"

def pertanyaan():
    bil = int(input("Banyaknya bilangan yang diurutkan: "))
    x = [int(input("Bilangan: ")) for j in range(bil)]
    print()
    print("Pengurutan Mana yang anda inginkan?", "\n",
    "1. Ascending (Naik)", "\n",
    "2. Descending (Turun)", "\n",
    "3. Ascending dan Descending")
    e = int(input("Jawab: "))
    if e == 1:
        print(insertion_sort_asc(x))
        return pertulang()
    elif e == 2:
        print(insertion_sort_desc(x))
        return pertulang()
    elif e == 3:
        print("Secara Ascending(Menaik)")
        print(insertion_sort_asc(x))
        print("Secara Descending(Menurun)")
        print(insertion_sort_desc(x))
        return pertulang()
    else:
        print("Jangan tulis macem-macem ya!! silahkan tulis 1/2")
        return pertanyaan()

def pertulang():
    print("Apakah ingin menggunakan program ini lagi? (Y/T)")
    e = str(input("Jawab : "))
    if e == "Y":
        return pertanyaan()
    elif e == "T":
        s = "Terima Kasih sudah memakai jasa mengurutkan bilangan kami"
        return s
    else:
        print("Jangan tulis macem-macem ya!! silahkan tulis Y/T")
        return pertulang()

def insertion_sort_asc(x):
    print()
    print("Bilangan tak terurut:",x)
    t = 0
    for i in range (1,len(x)):
        current_element = x[i]
        pos = i
        while current_element<x[pos-1] and pos>0:
            x[pos] = x[pos-1]
            pos = pos-1
            x[pos] = current_element
        print()
        print("Iterasi ke-", t+1)
        t = t+1
        for k in range(0, len(x)):
            print(x[k]) 
    print()   
    a = "bilangan terurut adalah:", x 
    return a

def insertion_sort_desc(x):
    print()
    print("Bilangan tak terurut:",x)
    t = 0
    for i in range (1,len(x)):
        current_element = x[i]
        pos = i
        while current_element>x[pos-1] and pos>0:
            x[pos] = x[pos-1]
            pos = pos-1
            x[pos] = current_element
        print()
        print("Iterasi ke-", t+1)
        t = t+1
        for k in range(0, len(x)):
            print(x[k]) 
    print()   
    b = "bilangan terurut adalah:", x 
    return b

print(pertanyaan())


