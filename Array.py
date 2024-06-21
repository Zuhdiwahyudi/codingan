def input_data():
    barang = [
        {"jenis": "celana", "harga": 50000, "stok": 60},
        {"jenis": "baju", "harga": 75000, "stok": 30},
        {"jenis": "jaket", "harga": 67000, "stok": 40},
        {"jenis": "topi", "harga": 26000, "stok": 50},
    ]
    return barang
def transaksi_pembelian(barang, beli, jumlah):
    bayar = 0
    stok = 0

    for item in barang:
        if item["jenis"] == beli and item["stok"] >= jumlah:
            bayar = jumlah * item["harga"]
            stok = item["stok"] - jumlah
            break

    return bayar, stok
def diskon_total(bayar):
    if bayar > 100000:
        diskon = bayar * 0.15
        total = bayar - diskon
    else:
        total = bayar
    return total,diskon

def transaksi():
    data_barang = input_data()
    print("========== Daftar Menu ===========")
    for item in data_barang:
        print(" Daftar menu: ", item["jenis"], "\t Harga : ", item["harga"], "\t Stok : ", item["stok"])
    print("pembelian di atas rp100.000,- mendapatkan diskon 15%")
    print("====================================================")

    beli = input("pilih menu : ")
    jumlah = int(input("jumlah pesanan : "))

    bayar, sisa_stok = transaksi_pembelian(data_barang, beli, jumlah)
    if sisa_stok >= 0:
        total_bayar,diskon = diskon_total(bayar)
        print("================== Detail pembayaran ==================")
        print("menu yang dipesan        : ", beli)
        print("jumlah yang dipesan      : ", jumlah)
        print("total harga             : ", bayar)
        print("tampilkan diskon        :", diskon)
        print("total yang harus dibayar : ", total_bayar)
        print("sisa stok                : ", sisa_stok)
    else:
        print("Maaf, stok tidak mencukupi untuk pesanan Anda.")

# Contoh panggilan fungsi transaksi
transaksi()