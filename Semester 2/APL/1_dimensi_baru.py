import os
import inquirer
from colorama import init, Fore, Style

init (autoreset=True)

Nama = ["nisa", "intan", "mariska", "jiwoo", "carmen"]
instrumen = ["Gitar", "Piano", "Drum", "Biola", "Bass"]

masuk = True

while masuk:
    print("-" * 30)
    print("KURSUS MUSIK.member".center(30))
    print("-" * 30)
    Menu = [
        inquirer.List('pilih',
                message="Pilih menu: ",
                choices=["Tampilkan Member",
                            "Cari Instrumen Member", 
                            "Tambah Member", 
                            "Keluar"])    
    ]

    jawaban = inquirer.prompt(Menu)
    pilih = jawaban["pilih"]
    os.system("cls")

    if pilih == "Tampilkan Member" :
        print("-" * 45)
        print("DAFTAR MEMBER KURSUS MUSIK".center(45))
        print("-" * 45)
        print(f"{"No":<5} {"Nama":<15} {"Instrumen":<15}")
        print("-" * 45)

        for i in range(len(Nama)):
            print(f"{i+1:<5} {Nama[i]:<15} {instrumen[i]:<15}")
            print("-" * 45)
        input("\nTekan Enter untuk kembali ke menu...")
        os.system("cls")

    elif pilih == "Cari Instrumen Member":
        print ("="*30)
        print ("CARI MEMBER".center(30))
        print ("="*30)
        while True:
            cari = input("Masukkan nama: ").lower()
            ketemu = False

            for i in range(len(Nama)):
                if Nama[i].lower() == cari:
                    print(Fore.GREEN+f"✅ {Nama[i]} memainkan {instrumen[i]}")
                    ketemu = True
                    break
            if not ketemu:
                print(Fore.RED+f"❌ Nama {cari} tidak terdaftar")
            print() 
            print("Ingin mencari lagi (y/n)? ")
            pilihan = [
                inquirer.List('ulang',
                                message="Pilih jawaban ", 
                                choices=["Iya",
                                        "Tidak"])
            ]
            jawaban_pilihan = inquirer.prompt(pilihan)
            ulang = jawaban_pilihan["ulang"]
            if ulang == "Iya":
                os.system("cls")
                print ("="*30)
                print ("CARI MEMBER".center(30))
                print ("="*30)
                continue
            elif ulang == "Tidak":
                os.system("cls")
                break

    elif pilih == "Tambah Member" :
        print ("="*30)
        print("TAMBAH MEMBER BARU".center(30))
        print ("="*30)
        namabaru = input("Masukkan nama: ").lower()
        
        if namabaru == "":
            print(Fore.RED+"❌ Nama tidak boleh kosong!")
        elif namabaru in Nama:
            print(Fore.RED+"❌ Nama sudah terdaftar!")
        else:
            instrumenbaru = input("Masukkan instrumen: ")
            if instrumenbaru == "":
                print(Fore.RED+"❌ Instrumen tidak boleh kosong!")
            else:
                Nama.append(namabaru)
                instrumen.append(instrumenbaru)
                print(Fore.GREEN+f"✅ {namabaru} berhasil ditambahkan!")

        input("\nTekan Enter untuk kembali ke menu...")
        os.system("cls")

    elif pilih == "Keluar" :
        print("Terima kasih 🙏")
        masuk = False

    else:
        print(Fore.RED+"❌ Pilihan tidak valid")
        input("\nTekan Enter untuk lanjut...")
        os.system("cls")