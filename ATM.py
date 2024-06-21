saldo = 0

def menu():
    print("="*40)
    print("=== Selamat Datang di ATM Sederhana ====")
    print("="*40)

    print("1. Cek Saldo")
    print("2. Tarik Uang")
    print("3. Setor Uang")
    print("4. keluar")

def proses_tarik_uang(jumlah_penarikan):
    global saldo
    print("ini adalah proes tarik uang")
    saldo = saldo - jumlah_penarikan
    cek_saldo()

def cek_saldo():
    print("Saldo anda : ", saldo)
    print("ini adalah menu untuk tampilkan saldo")

def menampilkan_opsi_penarikan():
    print("Pilihan jumlah uang yang ingin Anda tarik:")
    print("1. Rp 300,000")
    print("2. Rp 400,000")
    print("3. Rp 200,000")
    print("4. Jumlah lainnya")

running = True
saldo = 1000000 # Proses inisialisasi
while(running):

    pin = input("Masukkan PIN anda : ")
    if(pin == "1234"):

        menu()
        pilihan = int(input("Masukkan Menu : "))
        if pilihan == 4:
            running = False
            print("Terima kasih sudah menggunakan layanan ATM Bank Sederhana")
        elif pilihan == 1:
            cek_saldo()
        elif pilihan == 2:

            menampilkan_opsi_penarikan()
            Menarik_uang = input("Pilih opsi penarikan: ")
            if Menarik_uang == '1':
                print("jumlah uang yang di tarik adalah",(300000))
                proses_tarik_uang(300000)
            elif Menarik_uang == '2':
                print("jumlah uang yang di tarik adalah",(400000))
                proses_tarik_uang(400000)
            elif Menarik_uang == '3':
                print("jumlah uang yang di tarik adalah",(200000))
                proses_tarik_uang(200000)
            elif Menarik_uang == '4':
                custom_amount = int(input("Masukkan jumlah yang ingin Anda tarik: "))
                proses_tarik_uang(custom_amount)
                print()
            else:
                print("Pilihan tidak valid.")
    else:
        print("PIN ANDA SALAH, SILAHKAN MASUKKAN PIN YANG BENAR")
