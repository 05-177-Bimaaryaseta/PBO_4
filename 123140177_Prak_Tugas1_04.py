import math

def hitung_akar_kuadrat():
    while True:
        try:
           
            angka = input("Masukkan angka: ")
            
            
            angka_float = float(angka)
            
            
            if angka_float < 0:
                print("Input tidak valid. Harap masukkan angka positif.")
                continue
            elif angka_float == 0:
                print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
                continue
                
            
            hasil = math.sqrt(angka_float)
            print(f"Akar kuadrat dari {angka} adalah {hasil}")
            break
            
        except ValueError:
            
            print("Input tidak valid. Harap masukkan angka yang valid.")


hitung_akar_kuadrat()