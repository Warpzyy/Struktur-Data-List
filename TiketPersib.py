# Aplikasi Pemesanan Tiket Pertandingan Persib

# Daftar pemesanan tiket (berupa list of dictionary)
daftar_pemesanan = []

# Harga tiket per kategori
harga_tiket = {
    "VIP": 250000,
    "Selatan": 130000,
    "Utara": 130000,
    "Timur": 130000
}

# Fungsi 1: Tambah pemesanan
def tambah_pemesanan(nama, kategori, jumlah):
    if kategori not in harga_tiket:
        print("Kategori tiket tidak valid!")
        return
    if jumlah <= 0 or jumlah > 5:
        print("Jumlah tiket harus antara 1-5.")
        return
    pesanan = {
        "nama": nama,
        "kategori": kategori,
        "jumlah": jumlah
    }
    daftar_pemesanan.append(pesanan)
    print("Pemesanan berhasil ditambahkan.")

# Fungsi 2: Tampilkan semua pemesanan
def tampilkan_pemesanan():
    if not daftar_pemesanan:
        print("Belum ada pemesanan.")
        return
    print("\nDaftar Pemesanan:")
    for i, p in enumerate(daftar_pemesanan, 1):
        print(f"{i}. {p['nama']} - {p['kategori']} - {p['jumlah']} tiket")

# Fungsi 3: Hapus pemesanan berdasarkan nama
def hapus_pemesanan(nama):
    ditemukan = False
    for p in daftar_pemesanan:
        if p['nama'].lower() == nama.lower():
            daftar_pemesanan.remove(p)
            ditemukan = True
            print("Pemesanan berhasil dihapus.")
            break
    if not ditemukan:
        print("Nama tidak ditemukan dalam daftar.")

# Fungsi 4: Hitung total tiket terjual
def total_tiket_terjual():
    total = sum(p['jumlah'] for p in daftar_pemesanan)
    print(f"Total tiket terjual: {total}")

# Fungsi 5: Hitung total pemasukan
def total_pemasukan():
    total = 0
    for p in daftar_pemesanan:
        total += harga_tiket[p['kategori']] * p['jumlah']
    print(f"Total pemasukan: Rp{total:,}")

# Menu interaktif sederhana
def menu():
    while True:
        print("\n=== Aplikasi Tiket Persib ===")
        print("1. Tambah Pemesanan")
        print("2. Tampilkan Pemesanan")
        print("3. Hapus Pemesanan")
        print("4. Total Tiket Terjual")
        print("5. Total Pemasukan")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            nama = input("Nama Pemesan: ")
            kategori = input("Kategori Tiket (VIP/Selatan/Utara/Timur): ")
            jumlah = int(input("Jumlah Tiket (max 5): "))
            tambah_pemesanan(nama, kategori, jumlah)
        elif pilihan == "2":
            tampilkan_pemesanan()
        elif pilihan == "3":
            nama = input("Masukkan nama untuk dihapus: ")
            hapus_pemesanan(nama)
        elif pilihan == "4":
            total_tiket_terjual()
        elif pilihan == "5":
            total_pemasukan()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan menu
menu()
