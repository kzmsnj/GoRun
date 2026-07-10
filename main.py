import sys
import run_classifier
import binary_classifier

def main():
    while True:
        print("\n" + "="*45)
        print("    CLI RUN & REST ADVISOR EXPERT SYSTEM")
        print("="*45)
        print("1. Deteksi Kesiapan Fisik (Hamming)")
        print("2. Klasifikasi Tipe Lari (Euclidean)")
        print("0. Keluar")
        print("="*45)
        
        pilihan = input("Pilih menu (0-2): ")
        
        if pilihan == '1':
            binary_classifier.jalankan_menu()
            input("\nTekan Enter untuk kembali ke menu utama...")
        elif pilihan == '2':
            run_classifier.jalankan_menu()
            input("\nTekan Enter untuk kembali ke menu utama...")
        elif pilihan == '0':
            print("Keluar dari program. Selamat beristirahat atau berlari!")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()