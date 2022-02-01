print("Tugas Kelompok 1", "\n",
        "Membuat Program Dinamis untuk mengurutkan bilangan dengan Counting Sort")
print()
print("\t", "SELAMAT DATANG DI MESIN PENGURUTAN BILANGAN DENGAN COUNTING SORT", "\t")
print()

def masuk_list():
    n = int(input("Silahkan Masukkan Jumlah bilangan yang ingin diurutkan: "))
    A = []
    for i in range(0, n):
        a = int(input(" Angka ke-" + str(i+1) + ": "))
        A.append(a)
    print()
    print("Bilangan tak terurutnya: ", A)
    print()
    Counting_sort(A, n)

def Counting_sort(B, m):
    List_Out = [0]*m
    Max_List = max(B)
    Count2 = []
    for i in range(0, (Max_List+1)):
        Count2.append(i)

    #Buat List untuk Count Array nya yaitu MaxList + 1
    Count = [0]*(Max_List+1)
    print("Counting List", "\n", Count)
    print()
    #Menghitung masing-masing Elemen dari list yang ingin diurutkan
    for i in range(0, m):
        Count[B[i]] += 1
    print("Counting List dari Elemen pada list yang ingin diurutkan:","\n", Count , "\n", Count2)
    print()
    #Mencari Frekuensi kumulatif untuk Count_List
    for i in range(1, (Max_List+1)):
        Count[i] += Count[i-1]
    print("Counting List dari Elemen pada list yang ingin diurutkan dalam bentuk frekuensi kumulatif:","\n", Count)
    print()
    #Menyamakan Index
    u = 1
    i = m - 1
    while i >= 0:
        print("Iterasi ke-", u)
        List_Out[Count[B[i]] - 1] = B[i]
        print('\033[91m',Count2 ,'\033[0m')
        print('\033[92m',Count,'\033[0m')
        print()
        print('\033[93m',List_Out,'\033[0m')
        print()
        Count[B[i]] -= 1
        i -= 1
        u += 1

    # Copy the sorted elements into original array
    for i in range(0, m):
        B[i] = List_Out[i]
    print("Bilangan yang terurut adalah", B)
    return pertulang()

def pertulang():
    print("Apakah ingin mengurutkan bilangan lagi? (Y/T)")
    e = str(input("Jawab : "))
    if e == "Y":
        return masuk_list()
    elif e == "T":
        print("Terima Kasih sudah memakai jasa mengurutkan bilangan kami")
        o = ""
        return o
    else:
        print("Jangan tulis macem-macem ya!! silahkan tulis Y/T")
        return pertulang()

print(masuk_list())