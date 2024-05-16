# Untuk Display Menu itu gak perlu dibuat fungsi (ini kamu kerjainnya nanti aja pas buat GUI)
# Fungsi main() juga gak perlu
# Yang harus kamu buat itu fungsi untuk command tiap button di menu (kayaknya kerjain pas buat GUI-nya aja)

def display_menu():
    print("Pilih opsi menu:")
    print("Buat appointment baru")
    print("Batalkan appointment")
    print("Tampilkan seluruh apoointment")
    print("Cetak tagihan")

def main():
    while True:
        display_menu()
        choice = input("Masukkan pilihan Anda (1/2/3/4): ")

        if choice == '1':
            print("Anda memilih untuk membuat appointment baru.")
            # Panggil fungsi untuk melihat profil
        elif choice == '2':
            print("Anda memilih untuk membatalkan appointment yang telah dipilih sebelumnya.")
            # Panggil fungsi untuk mengedit profil
        elif choice == '3':
            print("Anda memilih untuk menampilkan appointment yang telah dipilih.")
            # Panggil fungsi untuk mengirim pesan
        elif choice == '4':
            print("Anda memilih untuk mencetak tagihan")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan nomor 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()
