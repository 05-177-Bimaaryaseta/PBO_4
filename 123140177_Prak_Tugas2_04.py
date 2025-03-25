class TugasTidakDitemukanError(Exception):
    pass

class InputTidakValidError(Exception):
    pass

def main():
    daftar_tugas = []
    
    while True:
        try:
            print("\nPilih aksi:")
            print("1. Tambah tugas")
            print("2. Hapus tugas")
            print("3. Tampilkan daftar tugas")
            print("4. Keluar")
            
            pilihan = input("Masukkan pilihan (1/2/3/4): ")
            
            if pilihan == "1":
                tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
                if not tugas:
                    raise InputTidakValidError("Input tugas tidak boleh kosong")
                daftar_tugas.append(tugas)
                print("Tugas berhasil ditambahkan!")
                
            elif pilihan == "2":
                if not daftar_tugas:
                    print("Daftar tugas kosong")
                    continue
                    
                print("Daftar Tugas:")
                for i, tugas in enumerate(daftar_tugas, 1):
                    print(f"{i}. {tugas}")
                    
                try:
                    nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                    if nomor < 1 or nomor > len(daftar_tugas):
                        raise TugasTidakDitemukanError(f"Tugas dengan nomor {nomor} tidak ditemukan")
                    daftar_tugas.pop(nomor - 1)
                    print("Tugas berhasil dihapus!")
                except ValueError:
                    raise InputTidakValidError("Harap masukkan nomor yang valid")
                    
            elif pilihan == "3":
                if not daftar_tugas:
                    print("Daftar tugas kosong")
                else:
                    print("Daftar Tugas:")
                    for tugas in daftar_tugas:
                        print(f"- {tugas}")
                        
            elif pilihan == "4":
                print("Keluar dari program.")
                break
                
            else:
                raise InputTidakValidError("Pilihan tidak valid. Harap masukkan 1, 2, 3, atau 4")
                
        except InputTidakValidError as e:
            print(f"Error: {e}")
        except TugasTidakDitemukanError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan tak terduga: {e}")

if __name__ == "__main__":
    main()