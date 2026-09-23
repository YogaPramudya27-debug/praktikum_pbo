class Kendaraan:
    nama_rental = "Rental Jaya"
    total_kendaraan = 0
    tarif_denda = 50000

    def __init__(self, kode, nama, jenis, harga_sewa):
        self.kode = kode
        self.nama = nama
        self.jenis = jenis
        self.__harga_sewa = harga_sewa
        Kendaraan.total_kendaraan += 1

    def info_kendaraan(self):
        print("Kode       :", self.kode)
        print("Nama       :", self.nama)
        print("Jenis      :", self.jenis)
        print("Harga sewa :", self.__harga_sewa)

    @property
    def harga_sewa(self):
        return self.__harga_sewa

    @harga_sewa.setter
    def harga_sewa(self, harga_baru):
        if harga_baru > 0:
            self.__harga_sewa = harga_baru
            print("Harga sewa berhasil diubah.")
        else:
            raise ValueError("Harga sewa harus lebih dari 0.")

    @classmethod
    def ubah_tarif_denda(cls, tarif_baru):
        if tarif_baru > 0:
            cls.tarif_denda = tarif_baru
            print("Tarif denda berhasil diubah.")
        else:
            raise ValueError("Tarif denda harus lebih dari 0.")

    @staticmethod
    def cek_jenis(jenis):
        return jenis.lower() in ["mobil", "motor"]


class Pelanggan:
    nama_rental = "Rental Jaya"
    total_pelanggan = 0
    status_default = "Aktif"

    def __init__(self, id_pelanggan, nama, no_hp):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.__no_hp = no_hp
        Pelanggan.total_pelanggan += 1

    def info_pelanggan(self):
        print("ID Pelanggan :", self.id_pelanggan)
        print("Nama         :", self.nama)
        print("No. HP       :", self.__no_hp)
        print("Status       :", Pelanggan.status_default)

    @property
    def no_hp(self):
        return self.__no_hp

    @no_hp.setter
    def no_hp(self, no_hp_baru):
        if no_hp_baru.isdigit() and len(no_hp_baru) >= 10:
            self.__no_hp = no_hp_baru
            print("Nomor HP berhasil diubah.")
        else:
            raise ValueError("Nomor HP minimal 10 digit.")

    @staticmethod
    def cek_nama(nama):
        return nama.strip() != ""


class Rental:
    total_transaksi = 0
    lama_maksimal = 30
    status_default = "Sedang Dirental"

    def __init__(self, pelanggan, kendaraan, lama_sewa):
        self.pelanggan = pelanggan
        self.kendaraan = kendaraan
        self.__lama_sewa = lama_sewa
        Rental.total_transaksi += 1

    def hitung_total(self):
        return self.kendaraan.harga_sewa * self.__lama_sewa

    def info_rental(self):
        print("Pelanggan   :", self.pelanggan.nama)
        print("Kendaraan   :", self.kendaraan.nama)
        print("Jenis       :", self.kendaraan.jenis)
        print("Lama sewa   :", self.__lama_sewa, "hari")
        print("Harga/hari  :", self.kendaraan.harga_sewa)
        print("Total bayar :", self.hitung_total())
        print("Status      :", Rental.status_default)

    @property
    def lama_sewa(self):
        return self.__lama_sewa

    @lama_sewa.setter
    def lama_sewa(self, lama_baru):
        if 0 < lama_baru <= Rental.lama_maksimal:
            self.__lama_sewa = lama_baru
            print("Lama sewa berhasil diubah.")
        else:
            raise ValueError("Lama sewa 1-30 hari.")

    @classmethod
    def ubah_lama_maksimal(cls, lama_baru):
        if lama_baru > 0:
            cls.lama_maksimal = lama_baru
            print("Batas lama sewa berhasil diubah.")
        else:
            raise ValueError("Lama maksimal harus lebih dari 0.")

    @staticmethod
    def hitung_denda(hari_terlambat):
        if hari_terlambat > 0:
            return hari_terlambat * Kendaraan.tarif_denda
        return 0


print("======================================")
print("          RENTAL JAYA")
print("      Rental Mobil dan Motor")
print("======================================")


kendaraan1 = Kendaraan(
    "M001", "Toyota Avanza", "Mobil", 300000
)

kendaraan2 = Kendaraan(
    "MT001", "Honda Vario", "Motor", 100000
)


print("\nKENDARAAN YANG TERSEDIA")
print("1.", kendaraan1.nama, "-", kendaraan1.jenis,
      "- Rp", kendaraan1.harga_sewa, "/hari")

print("2.", kendaraan2.nama, "-", kendaraan2.jenis,
      "- Rp", kendaraan2.harga_sewa, "/hari")

while True:
    pilihan = input("\nPilih kendaraan (1/2): ")

    if pilihan == "1":
        kendaraan_pilih = kendaraan1
        break

    elif pilihan == "2":
        kendaraan_pilih = kendaraan2
        break

    else:
        print("Pilihan tidak tersedia. Silakan pilih 1 atau 2.")


print("\nDATA PELANGGAN")

while True:
    id_pelanggan = input("ID pelanggan : ")

    if id_pelanggan.strip() != "":
        break

    print("ID pelanggan tidak boleh kosong.")

while True:
    nama_pelanggan = input("Nama pelanggan : ")

    if Pelanggan.cek_nama(nama_pelanggan):
        break

    print("Nama pelanggan tidak boleh kosong.")

while True:
    no_hp = input("No. HP : ")

    if no_hp.isdigit() and len(no_hp) >= 10:
        break

    print("No. HP harus berupa angka dan minimal 10 digit.")


pelanggan = Pelanggan(
    id_pelanggan,
    nama_pelanggan,
    no_hp
)

while True:
    try:
        lama_sewa = int(input("Lama sewa (hari) : "))

        if 0 < lama_sewa <= Rental.lama_maksimal:
            break

        print("Lama sewa harus 1-30 hari.")

    except ValueError:
        print("Lama sewa harus berupa angka.")


rental = Rental(
    pelanggan,
    kendaraan_pilih,
    lama_sewa
)


print("\n======================================")
print("          DATA RENTAL")
print("======================================")

rental.info_rental()


print("\nHarga kendaraan:", kendaraan_pilih.harga_sewa)
print("No. HP pelanggan:", pelanggan.no_hp)
print("Lama sewa:", rental.lama_sewa, "hari")

print("\nUBAH HARGA SEWA")

while True:
    try:
        harga_baru = int(input("Masukkan harga sewa baru: "))

        kendaraan_pilih.harga_sewa = harga_baru

        print("Harga setelah diubah:", kendaraan_pilih.harga_sewa)
        break

    except ValueError as e:
        print("Error:", e)


print("\nKEBIJAKAN RENTAL")

while True:
    try:
        tarif_baru = int(input("Masukkan tarif denda baru: "))

        Kendaraan.ubah_tarif_denda(tarif_baru)

        print("Tarif denda sekarang:", Kendaraan.tarif_denda)
        break

    except ValueError as e:
        print("Error:", e)

print("\nPERIKSA JENIS KENDARAAN")


if Kendaraan.cek_jenis(kendaraan_pilih.jenis):
    print("Jenis kendaraan:", kendaraan_pilih.jenis)
    print("Jenis kendaraan valid.")
else:
    print("Jenis kendaraan tidak valid.")

while True:
    try:
        hari_terlambat = int(
            input("\nMasukkan jumlah hari terlambat: ")
        )

        if hari_terlambat >= 0:
            break

        print("Jumlah hari terlambat tidak boleh negatif.")

    except ValueError:
        print("Masukkan angka yang benar.")


print("Denda:", Rental.hitung_denda(hari_terlambat))


print("\nJUMLAH DATA")
print("Total kendaraan :", Kendaraan.total_kendaraan)
print("Total pelanggan :", Pelanggan.total_pelanggan)
print("Total transaksi :", Rental.total_transaksi)
