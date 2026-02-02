import json

FILE_NAME = 'saldo.json'

def load_data():
    try:
        with open(FILE_NAME, 'r') as f:
            data = json.load(f)
            return data.get('saldo', 0.0), data.get('transaksi', [])
    except FileNotFoundError:
        return 0.0, []

def save_data(saldo, transaksi):
    with open(FILE_NAME, 'w') as f:
        json.dump({'saldo': saldo, 'transaksi': transaksi}, f)

saldo, transaksi = load_data()

def tambah_pemasukan():
    global saldo, transaksi
    jumlah = float(input("Masukkan jumlah pemasukan: "))
    saldo += jumlah
    transaksi.append({'type': 'pemasukan', 'jumlah': jumlah})
    print("Pemasukan berhasil ditambahkan!")

def tambah_pengeluaran():
    global saldo, transaksi
    jumlah = float(input("Masukkan jumlah pengeluaran: "))
    if saldo >= jumlah:
        saldo -= jumlah
        transaksi.append({'type': 'pengeluaran', 'jumlah': jumlah})
        print("Pengeluaran berhasil!")
    else:
        print("Saldo tidak cukup!")

def lihat_saldo():
    print(f"Saldo saat ini: Rp {saldo:.2f}")

def laporan():
    total_pemasukan = sum(j['jumlah'] for j in transaksi if j['type'] == 'pemasukan')
    total_pengeluaran = sum(j['jumlah'] for j in transaksi if j['type'] == 'pengeluaran')
    print(f"Total Pemasukan: Rp {total_pemasukan:.2f}")
    print(f"Total Pengeluaran: Rp {total_pengeluaran:.2f}")
    print(f"Saldo Saat Ini: Rp {saldo:.2f}")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Laporan")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        laporan()
    elif pilihan == "5":
        save_data(saldo, transaksi)
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")
        