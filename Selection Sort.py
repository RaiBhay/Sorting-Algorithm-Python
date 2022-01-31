print("Tugas Kelompok 4 No 3", "\n",
        "Membuat Program Dinamis untuk mengurutkan bilangan menggunakan selection sort")
print()
print("\t", "SELAMAT DATANG DI MESIN PENGURUTAN BILANGAN DENGAN SELECTION SORT", "\t")
print()

def pertulang():
    print("Apakah ingin menggunakan program ini lagi? (Y/T)")
    e = str(input("Jawab : "))
    if e == "Y":
        return selection_sort()
    elif e == "T":
        s = "Terima Kasih sudah memakai jasa konversi bilangan desimal kami"
        return s
    else:
        print("Jangan tulis macem-macem ya!! silahkan tulis Y/T")
        return pertulang()

def selection_sort():
    bil = int(input("Banyaknya bilangan:"))
    list1=[int(input()) for x in range(bil)]
    print("bilangan tak terurut",list1)
    t = 0
    for i in range(len(list1)-1):
        indeks_m = i
        print()
        print("Iterasi ke- ", t+1)
        for j in range(i+1,len(list1)):
            if list1[j]<list1[indeks_m]:
                indeks_m=j
        if list1[i] != list1[indeks_m]:
            list1[i],list1[indeks_m]=list1[indeks_m],list1[i]
        print(list1)
        t=t+1
    print("bilangan terurut:",list1)
    return pertulang()

print(selection_sort())
