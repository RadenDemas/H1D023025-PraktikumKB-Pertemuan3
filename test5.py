import os
import random

while True:
    list_num = set()
    win = 0
    lose = 0
    while len(list_num) < 5:
        i = random.randint(0, 20)
        list_num.add(i)

    answer = int(input("Masukkan angka tebakan anda: "))

    if answer in list_num:
        print("Selamat anda berhasil menebaknya!\n")
        win+=1
    else:
        print("Anda gagal menebaknya\n")
        lose+=1

    while True:
        try:
            answer = int(input("Apakah Anda ingin lanjut?\n1 untuk Ya, 0 untuk Tidak: "))
            if answer == 1:
                os.system("cls")
                break
            elif answer == 0:
                break
            else:
                print("Masukkan hanya angka 1 atau 0.")
        except ValueError:
            print("Harus memasukkan angka (1 atau 0).")

    if answer == 0:
        os.system("cls")
        print(f"Anda Berhasil Sebanyak {win}\nAnda Gagal Sebanyak {lose}")
        break