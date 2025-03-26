# H1D023025-PraktikumKB-Pertemuan3

```python
import os
import random
```
Mengimport atau mengambil package/library os dan random dari sistem

```python
whiel True:
  list_num = set()
  win = 0
  lose = 0
```
Melakukan looping sampai bertemu break dan membuat variabel list_num bertipe set dan win lose bertipe int

```python
while len(list_num) < 5:
        i = random.randint(0, 20)
        list_num.add(i)
```
Memasukkan angka int secara random menggunakan package random dan memasukkannya ke list_num hingga 5 angka

```python
answer = int(input("Masukkan angka tebakan anda: "))
    if answer in list_num:
        print("Selamat anda berhasil menebaknya!\n")
        win+=1
    else:
        print("Anda gagal menebaknya\n")
        lose+=1
```
Pengguna harus memasukkan input berupa int dan akan di sinpan di answer, jika answer berada pada list_num maka akan menjalankan perintah if jika tidak ada maka akan menjalankan perintah else

```python
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
```
Pengguna harus memasukkan angka 1 atau 0, jika pengguna memasukkan selain 0 atau 1 maka akan menjalankan perintah except dan jika bukan 0 atau 1 maka akan menjalankan perintah else, jika pengguna memasukkan 1 akan menjalankan perintah if yang mana akan memberishkan terminal dan keluar dari loop dan jika pnegguna memasukkan 0 akan menjalankan perintah else dan langsung keluar dari loop

```python
if answer == 0:
        os.system("cls")
        print(f"Anda Berhasil Sebanyak {win}\nAnda Gagal Sebanyak {lose}")
        break
```
Jika variabel answer sebelumnya bernilai 0 maka akan membersihkan terminal dan menampilkan Anda berhasil sebanyak nilai win dan Anda gagal sebanyak nilai lose kemudian keluar dari loop yang pertama
