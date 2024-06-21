# #nama =("jamal","indra","zuhdi","ulya","dawan","tobi","fajri","rudi")
# from collections.abc import Set
#
# from pip._internal.utils.misc import partition
#
# print(nama)
# cari_nama = "ulya"
# for nama in nama:
#     if nama == cari_nama:
#       ada = True
#
# #print(ada)
#
# teks = "orang yang hebat itu buakan orang yang banyak cinta akan tetapi orang hebat itu oarang yang mempertahankan satu cinta "
#
#
#
# chars = teks.partition("")
# print(chars)
#
# for chars in chars:
#     print(chars," = ",teks.partition(""))
#
#
#
# tugas
# buat untuk program mencari kata uniqwe pada teks
# fungsinya partion

text = "aku anak pintar karena aku pintar karena aku belajar supaya pintar dan pintar itu aku"
print(text)

partText = text.partition("aku anak pintar karena aku pintar karena aku belajar supaya pintar dan pintar itu aku")
print(partText)

chars = set(text)
print(chars)

for char in chars:
    print(char ,"=", text.count(char))

# Menampilkan kata yang sama
words = text.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word, count in word_counts.items():
    if count > 0:
        print(f"{word} = {count}")
