print("Tugas Kelompok 1", "\n",
        "Membuat Program Dinamis untuk mengurutkan bilangan dengan Bubble Sort")
print()
print("\t", "SELAMAT DATANG DI MESIN PENGURUTAN BILANGAN DENGAN BUBBLE SORT", "\t")
print()

def pertanyaan():
    bil = int(input("Banyaknya bilangan yang diurutkan: "))
    x = [int(input("Bilangan: ")) for j in range(bil)]
    print()
    print("Bilangann tak terurutnya : ", x)
    print("Pengurutan Mana yang anda inginkan?", "\n",
    "1. Ascending (Naik)", "\n",
    "2. Descending (Turun)", "\n")
    e = int(input("Jawab: "))
    if e == 1:
        return bubble_sort_naik(x)
    elif e == 2:
        return bubble_sort_turun(x)
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

def bubble_sort_naik(list1):
    t = 0
    for j in range(len(list1)-1,0,-1):
        print()
        print("Iterasi ke-", t+1)
        t=t+1
        for i in range(j):
            if list1[i]>list1[i+1]:
                list1[i],list1[i+1]=list1[i+1],list1[i]
                print(list1)
            else:
                print(list1)
    print()
    print("bilangan terurut:",list1)
    return pertulang()

def bubble_sort_turun(list1):
    t = 0
    for j in range(len(list1)-1,0,-1):
        print()
        print("Iterasi ke-", t+1)
        t=t+1
        for i in range(j):
            if list1[i]<list1[i+1]:
                list1[i],list1[i+1]=list1[i+1],list1[i]
                print(list1)
            else:
                print(list1)
    print()
    print("bilangan terurut:",list1)
    return pertulang()

print(pertanyaan())