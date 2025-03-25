from abc import ABC, abstractmethod
import random

class ZooError(Exception):
    """Base class for zoo exceptions"""
    pass

class InvalidAnimalError(ZooError):
    """Raised when invalid animal data is provided"""
    pass

class Animal(ABC):
    def __init__(self, name, age):
        if not name or not isinstance(name, str):
            raise InvalidAnimalError("Nama hewan harus berupa string ")
        if not isinstance(age, (int, float)) or age <= 0:
            raise InvalidAnimalError("Usia hewan harus angka positif!")
        
        self._name = name
        self._age = age
        self._mood = random.choice(["senang", "lapar", "mengantuk", "kesal"])
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def mood(self):
        return self._mood
    
    @abstractmethod
    def make_sound(self):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__} bernama {self._name} (usia: {self._age} tahun)"
    
    def daily_routine(self):
        print(f"{self._name} sedang {self._mood}!")
        self.make_sound()
        if self._mood == "lapar":
            print(f"{self._name} mencari makanan...")
        elif self._mood == "mengantuk":
            print(f"{self._name} tidur siang... zzz")

class Lion(Animal):
    def make_sound(self):
        print(f"🦁 {self.name}: Rawrrr,btw namanya siapa kak")
    
    def hunt(self):
        print(f"🦁 {self.name} sedang berburu thr")

class Monkey(Animal):
    def make_sound(self):
        print(f"🐵 {self.name}: Bro minjem duit bro")
    
    def climb(self):
        print(f"🐵 {self.name} Panjat sosial")

class Penguin(Animal):
    def make_sound(self):
        print(f"🐧 {self.name}: wak wakkkk")
    
    def swim(self):
        print(f"🐧 {self.name} yihaaa")

class Sloth(Animal):
    def make_sound(self):
        print(f"🦥 {self.name}: Turu wakkk..")
    
    def move(self):
        print(f"🦥 {self.name} makan tidur makan tidur")

class Zoo:
    def __init__(self):
        self._animals = []
    
    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise InvalidAnimalError("Hanya objek Animal yang bisa ditambahkan!")
        self._animals.append(animal)
        print(f"🐾 {animal.name} telah bergabung dengan kebun binatang kami!")
    
    def show_animals(self):
        if not self._animals:
            print("Kebun binatang kosong karena dikorupsi, ayooo tambahkan hewan!")
            return
        
        print("\n🌿 Penghuni Kebun Binatang 🌿")
        for i, animal in enumerate(self._animals, 1):
            print(f"{i}. {animal}")
    
    def daily_activities(self):
        print("\n🌟 Aktivitas Sehari-hari di Kebun Binatang 🌟")
        for animal in self._animals:
            animal.daily_routine()
            print()

def main():
    zoo = Zoo()
    
    while True:
        print("\n=== 🏡 Hewanpedia sistem ===")
        print("1. Tambah Hewan Baru")
        print("2. Lihat Daftar Hewan")
        print("3. Lihat Aktivitas Harian")
        print("4. Keluar")
        
        try:
            choice = input("Pilih menu (1-4): ")
            
            if choice == "1":
                print("\nJenis Hewan:")
                print("1. Singa (Lion)")
                print("2. Monyet (Monkey)")
                print("3. Penguin")
                print("4. Sloth (Kungkang)")
                
                animal_type = input("Pilih jenis hewan (1-4): ")
                name = input("Nama hewan: ").strip()
                age = float(input("Usia hewan: "))
                
                if animal_type == "1":
                    zoo.add_animal(Lion(name, age))
                elif animal_type == "2":
                    zoo.add_animal(Monkey(name, age))
                elif animal_type == "3":
                    zoo.add_animal(Penguin(name, age))
                elif animal_type == "4":
                    zoo.add_animal(Sloth(name, age))
                else:
                    print("Pilihan tidak valid!")
            
            elif choice == "2":
                zoo.show_animals()
            
            elif choice == "3":
                zoo.daily_activities()
            
            elif choice == "4":
                print("Terima kasih telah mengunjungi HewanPedia!")
                break
            
            else:
                print("Pilihan tidak valid!")
        
        except InvalidAnimalError as e:
            print(f"⚠️ Error: {e}")
        except ValueError:
            print("⚠️ Error: Usia itu angka blok!")
        except Exception as e:
            print(f"⚠️ Terjadi kesalahan sistem: {e}")

if __name__ == "__main__":
    main()
