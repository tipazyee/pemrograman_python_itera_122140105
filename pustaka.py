from abc import ABC, abstractmethod

# Kelas abstrak
class ItemPerpustakaan(ABC):
    def __init__(self, id_item, judul):
        self._id_item = id_item          # atribut protected
        self._judul = judul              # atribut protected
        self._tersedia = True            # atribut protected

    @abstractmethod
    def tampilkan_info(self):
        pass

    @property
    def judul(self):
        return self._judul

    def cek_ketersediaan(self):
        return self._tersedia

    def set_ketersediaan(self, status):
        self._tersedia = status


# Subclass Buku
class Buku(ItemPerpustakaan):
    def __init__(self, id_item, judul, penulis, jumlah_halaman):
        super().__init__(id_item, judul)
        self._penulis = penulis
        self._jumlah_halaman = jumlah_halaman

    def tampilkan_info(self):
        print(f"[Buku] ID: {self._id_item}, Judul: '{self._judul}', Penulis: {self._penulis}, Halaman: {self._jumlah_halaman}, Tersedia: {self._tersedia}")


# Subclass Majalah
class Majalah(ItemPerpustakaan):
    def __init__(self, id_item, judul, edisi):
        super().__init__(id_item, judul)
        self._edisi = edisi

    def tampilkan_info(self):
        print(f"[Majalah] ID: {self._id_item}, Judul: '{self._judul}', Edisi: {self._edisi}, Tersedia: {self._tersedia}")


# Kelas Perpustakaan
class Perpustakaan:
    def __init__(self):
        self.__koleksi = []  # atribut private untuk enkapsulasi

    def tambah_item(self, item: ItemPerpustakaan):
        self.__koleksi.append(item)
        print(f"Item '{item.judul}' berhasil ditambahkan ke perpustakaan.")

    def tampilkan_semua_item(self):
        print("\n=== Koleksi Perpustakaan ===")
        if not self.__koleksi:
            print("Belum ada item di perpustakaan.")
        for item in self.__koleksi:
            item.tampilkan_info()

    def cari_berdasarkan_judul(self, kata_kunci):
        print(f"\nPencarian judul yang mengandung: '{kata_kunci}'")
        ditemukan = False
        for item in self.__koleksi:
            if kata_kunci.lower() in item.judul.lower():
                item.tampilkan_info()
                ditemukan = True
        if not ditemukan:
            print("Tidak ditemukan item dengan judul tersebut.")

    def cari_berdasarkan_id(self, id_item):
        print(f"\nPencarian berdasarkan ID: '{id_item}'")
        for item in self.__koleksi:
            if item._id_item == id_item:
                item.tampilkan_info()
                return
        print("Tidak ditemukan item dengan ID tersebut.")


# Contoh penggunaan sistem
if __name__ == "__main__":
    perpustakaan = Perpustakaan()

    # Menambahkan item berupa novel dan majalah
    novel1 = Buku("B001", "Laskar Pelangi", "Andrea Hirata", 529)
    novel2 = Buku("B002", "Bumi", "Tere Liye", 444)
    novel3 = Buku("B003", "Pulang", "Tere Liye", 400)
    majalah1 = Majalah("M001", "National Geographic", "April 2025")

    # Menambahkan ke perpustakaan
    perpustakaan.tambah_item(novel1)
    perpustakaan.tambah_item(novel2)
    perpustakaan.tambah_item(novel3)
    perpustakaan.tambah_item(majalah1)

    # Menampilkan seluruh koleksi
    perpustakaan.tampilkan_semua_item()

    # Pencarian berdasarkan judul
    perpustakaan.cari_berdasarkan_judul("Bumi")
    perpustakaan.cari_berdasarkan_judul("Senja")  # tidak ditemukan

    # Pencarian berdasarkan ID
    perpustakaan.cari_berdasarkan_id("B003")
    perpustakaan.cari_berdasarkan_id("X999")  # tidak ditemukan
