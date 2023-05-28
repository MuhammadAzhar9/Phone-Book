# Import modul os
import os

# Deklarasi nama file phone book
kontak_list_file = "kontak_list.txt"

# Fungsi untuk melihat data dalam file
phone_book = {}
if os.path.isfile(kontak_list_file):    
    with open(kontak_list_file, "r") as f:
        for line in f:
            name, number = line.strip().split(":")
            phone_book[name] = number
else :
    file = open(kontak_list_file, "w")

while True:
    os.system("cls")
    print("|==========Phone Book==========|\n")

    # Halaman menu
    print("Apa yang ingin dilakukan?")
    print("1. Tambahkan kontak baru")
    print("2. Tampilkan list kontak")
    print("3. Perbarui kontak yang sudah ada")
    print("4. Hapus kontak")
    print("5. Mencari kontak yang ada")
    print("6. Keluar")

    choice = input("Masukan pilihanmu (1-6): ")

    # Menambahkan kontak baru
    if choice == "1":
        os.system("cls")
        name = input("Masukan nama kontak baru: ")
        number = input("Masukan nomor kontak: ")
        phone_book[name] = number
        print(f"{name} berhasil ditambahkan di phone book.\n")
        choice = input("Tekan Enter untuk kembali ke menu")

    # Menampilkan list kontak yang ada di file
    elif choice == "2":
        os.system("cls")
        if phone_book:
            print("Kontak :")
            for name, number in phone_book.items():
                print(f"{name} : {number}")
            print()
        else :
            print("Tidak ada kontak yang tersedia di dalam phone book.\n")
        choice = input("Tekan Enter untuk kembali ke menu")

    # Memperbarui kontak yang sudah ada
    elif choice == "3":
        os.system("cls")
        name = input("Masukan nama kontak yang ingin diperbarui: ")
        if name in phone_book:
            number = input("Masukan nomor baru : ")
            phone_book[name] = number
            print(f"{name} berhasil diperbarui.\n")
        else:
            print(f"{name} tidak ada didalam phone book.\n")
        choice = input("Tekan Enter untuk kembali ke menu")

    # Menghapus kontak
    elif choice == "4":
        os.system("cls")
        name = input("Masukan nama kontak yang ingin dihapus: ")
        if name in phone_book:
            del phone_book[name]
            print(f"{name} berhasil dihapus dari phone book.\n")
        else:
            print(f"{name} tidak ada didalam phone book.\n")
        choice = input("Tekan Enter untuk kembali ke menu")

    # Mencari kontak yang ada di phone book
    elif choice == "5":
        os.system("cls")
        name = input("Masukan nama kontak yang ingin dicari: ")
        if name in phone_book:
            print(f"{name} : {phone_book[name]}\n")
        else:
            print(f"{name} tidak ada didalam phone book.\n")
        choice = input("Tekan Enter untuk kembali ke menu")

    # Keluar dari program
    elif choice == "6":
        # Menulis phone book kedalam file
        with open(kontak_list_file, "w") as f:
            for name, number in phone_book.items():
                f.write(f"{name}:{number}\n")

        print("\n\n\tTerima Kasih dan Selamat Tinggal")
        print("====================================================")
        break

    # Pilihan salah
    else:
        print("Pilihan tidak ada. Silahkan tekan Enter untuk kembali")
        choice = input()