from abc import ABC, abstractmethod


class Kendaraan(ABC):
    nama_rental = "Rental Jaya"
    total_kendaraan = 0
    tarif_denda = 50000

    def __init__(self, kode, nama, jenis, harga_sewa):
        self.kode = kode
        self._nama = nama
        self.jenis = jenis
        self.__harga_sewa = harga_sewa
        Kendaraan.total_kendaraan += 1

    @abstractmethod
    def info_kendaraan(self):
        pass

    @abstractmethod
    def hitung_sewa(self, lama_sewa):
        pass

    def info_umum(self):
        return "Kendaraan di " + self.nama_rental + ": " + self._nama

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


class Mobil(Kendaraan):
    def __init__(self, kode, nama, harga_sewa, jumlah_pintu):
        super().__init__(kode, nama, "Mobil", harga_sewa)
        self.jumlah_pintu = jumlah_pintu

    def info_kendaraan(self):
        print("Kode         :", self.kode)
        print("Nama         :", self._nama)
        print("Jenis        :", self.jenis)
        print("Harga sewa   :", self.harga_sewa)
        print("Jumlah pintu :", self.jumlah_pintu)

    def hitung_sewa(self, lama_sewa):
        return self.harga_sewa * lama_sewa


class Motor(Kendaraan):
    def __init__(self, kode, nama, harga_sewa, kapasitas_cc):
        super().__init__(kode, nama, "Motor", harga_sewa)
        self.kapasitas_cc = kapasitas_cc

    def info_kendaraan(self):
        print("Kode         :", self.kode)
        print("Nama         :", self._nama)
        print("Jenis        :", self.jenis)
        print("Harga sewa   :", self.harga_sewa)
        print("Kapasitas CC :", self.kapasitas_cc)

    def hitung_sewa(self, lama_sewa):
        return self.harga_sewa * lama_sewa


class Pelanggan:
    nama_rental = "Rental Jaya"
    total_pelanggan = 0
    status_default = "Aktif"

    def __init__(self, id_pelanggan, nama, no_hp):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.__no_hp = no_hp
        Pelanggan.total_pelanggan += 1

    def ringkasan(self):
        return "Pelanggan: " + self.nama

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


class DetailRental:
    def __init__(self, lama_sewa):
        self.lama_sewa = lama_sewa

    def ringkasan(self):
        return "Lama sewa: " + str(self.lama_sewa) + " hari"

    def info_detail(self):
        print("Lama sewa :", self.lama_sewa, "hari")


def tampilkan_ringkasan(objek):
    print(objek.ringkasan())


class Rental:
    total_transaksi = 0
    lama_maksimal = 30
    status_default = "Sedang Dirental"

    def __init__(self, pelanggan, kendaraan, lama_sewa):
        self.pelanggan = pelanggan
        self.kendaraan = kendaraan
        self.detail = DetailRental(lama_sewa)
        Rental.total_transaksi += 1

    def __str__(self):
        return "Rental " + self.kendaraan._nama + " selama " + str(self.detail.lama_sewa) + " hari"

    def hitung_total(self):
        return self.kendaraan.hitung_sewa(self.detail.lama_sewa)

    def info_rental(self):
        print("Pelanggan    :", self.pelanggan.nama)
        print("Kendaraan    :", self.kendaraan._nama)
        print("Jenis        :", self.kendaraan.jenis)
        print("Lama sewa    :", self.detail.lama_sewa, "hari")
        print("Harga/hari   :", self.kendaraan.harga_sewa)
        print("Tarif denda  :", Kendaraan.tarif_denda, "/hari")
        print("Total bayar  :", self.hitung_total())
        print("Status       :", Rental.status_default)

    @property
    def lama_sewa(self):
        return self.detail.lama_sewa

    @lama_sewa.setter
    def lama_sewa(self, lama_baru):
        if 0 < lama_baru <= Rental.lama_maksimal:
            self.detail.lama_sewa = lama_baru
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
        if hari_terlambat <= 1:
            return 0

        hari_denda = hari_terlambat - 1
        return hari_denda * Kendaraan.tarif_denda


print("======================================")
print("          RENTAL JAYA")
print("      Rental Mobil dan Motor")
print("======================================")


kendaraan1 = Mobil(
    "M001",
    "Toyota Avanza",
    300000,
    4
)

kendaraan2 = Motor(
    "MT001",
    "Honda Vario",
    100000,
    125
)


try:
    Kendaraan("K001", "Contoh", "Umum", 100000)
except TypeError as error:
    print("Kendaraan tidak bisa dibuat menjadi objek karena masih memiliki abstract method.")
    print("Pesan Python:", error)

for kendaraan in [kendaraan1, kendaraan2]:
    kendaraan.info_kendaraan()
    print("Total sewa 2 hari:", kendaraan.hitung_sewa(2))
    print()

while True:

    print("\n======================================")
    print("          MENU UTAMA")
    print("======================================")

    print("\nKENDARAAN YANG TERSEDIA")
    print("1.", kendaraan1._nama, "-", kendaraan1.jenis,
          "- Rp", kendaraan1.harga_sewa, "/hari")

    print("2.", kendaraan2._nama, "-", kendaraan2.jenis,
          "- Rp", kendaraan2.harga_sewa, "/hari")
    print("0. Keluar")

    

    while True:
        pilihan = input("\nPilih kendaraan (1/2, atau 0 untuk keluar): ")

        if pilihan == "0":
            print("Terima kasih telah menggunakan Rental Jaya.")
            raise SystemExit

        elif pilihan == "1":
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

        if id_pelanggan.isdigit():
            break

        print("ID pelanggan harus berupa angka.")


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
    print("          DATA KENDARAAN")
    print("======================================")

    kendaraan_pilih.info_kendaraan()


    print("\n======================================")
    print("          DATA PELANGGAN")
    print("======================================")

    pelanggan.info_pelanggan()


    print("\n======================================")
    print("          DATA RENTAL")
    print("======================================")

    rental.info_rental()

    print("Dua objek berbeda dipanggil dengan fungsi yang sama:")
    tampilkan_ringkasan(pelanggan)
    tampilkan_ringkasan(rental.detail)

    print(rental)

    print("\nUBAH HARGA SEWA")

    while True:
        try:
            harga_baru = input("Masukkan harga sewa baru: ")

            if harga_baru == "" or not harga_baru.isdigit():
                raise ValueError

            harga_baru = int(harga_baru)

            kendaraan_pilih.harga_sewa = harga_baru

            print("Harga setelah diubah:",
                kendaraan_pilih.harga_sewa)
            break

        except ValueError:
            print("Data tidak boleh kosong dan harus berupa digit!!!")


    print("\nPERIKSA JENIS KENDARAAN")

    if Kendaraan.cek_jenis(kendaraan_pilih.jenis):
        print("Jenis kendaraan:", kendaraan_pilih.jenis)
        print("Jenis kendaraan valid.")
    else:
        print("Jenis kendaraan tidak valid.")


    print("\nPENGEMBALIAN KENDARAAN")

    while True:
        try:
            hari_terlambat = int(
                input("Masukkan jumlah hari terlambat: ")
            )

            if hari_terlambat >= 0:
                break

            print("Jumlah hari terlambat tidak boleh negatif.")

        except ValueError:
            print("Masukkan angka yang benar.")


    if hari_terlambat <= 1:

        denda = Rental.hitung_denda(hari_terlambat)

        print("Keterlambatan maksimal 1 hari tidak dikenakan denda.")
        print("Denda:", denda)

    else:

        print("\nKEBIJAKAN DENDA")
        print("Tarif denda awal:",
              Kendaraan.tarif_denda, "per hari")

        while True:
            tarif_baru = input("Masukkan tarif denda baru: ")

            if tarif_baru == "" or not tarif_baru.isdigit():
                print("Data tidak boleh kosong dan harus berupa digit!!!")
            elif int(tarif_baru) <= 0:
                print("Tarif denda harus lebih dari 0!!!")
            else:
                tarif_baru = int(tarif_baru)
                Kendaraan.ubah_tarif_denda(tarif_baru)
                break

        denda = Rental.hitung_denda(hari_terlambat)

        print("Hari terlambat :", hari_terlambat)
        print("Hari yang dihitung untuk denda :",
              hari_terlambat - 1)
        print("Denda:", denda)


    print("\n======================================")
    print("        TRANSAKSI SELESAI")
    print("======================================")

    print("Total sewa    :", rental.hitung_total())
    print("Denda         :", denda)
    print("Total akhir   :", rental.hitung_total() + denda)
    print("Ringkasan      :", rental)

    input("\nTekan ENTER untuk kembali ke menu awal...")
