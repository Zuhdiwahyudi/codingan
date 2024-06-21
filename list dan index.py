nama = ["N","U","R","S","I","K","I","N"]
print(nama)
listnama = list(nama)
print(nama)
print(nama[4])
print(nama[3:])
print(nama[:3])
print(nama[0:5])

listnama.append("  ")
listnama.append("U")
listnama.append("L")
listnama.append("Y")
listnama.append("A")
print(listnama)

listnama.append("  ")
listnama.append("A")
listnama.append("B")
listnama.append("A")
listnama.append("D")
listnama.append("I")
print(listnama)

listnama.insert(8,"A")
listnama.insert(9,"H")
print(listnama)

listnama2 = ["P","U","T","R","I"]
listnama.extend(listnama2)
print(listnama)
listnama[4] = "A"
print(listnama)
listnama.remove("A")
print(listnama)
print(len(listnama))

jumlah  = 0
for item in listnama2:
    jumlah+=1
    print(item)
print(jumlah)

def hitung_karakter_U(teks):
    jumlah_U = 0

    for karakter in teks:
        if karakter == "U":
            jumlah_U+=1

    return jumlah_U
teks_penguna = input("masukan sebuah teks ")

jumlah_U = hitung_karakter_U(teks_penguna)

print(f"jumlah karakter 'U' dalam teks adalah: {jumlah_U}")




#tugas
#perogram menghitung karakter (U)
#buat program menghitung semua char "A" jadi bitang *
#buatkan perogram untuk menampilkan carakter apa saja