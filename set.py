#crate a set of integr type
#type ini pungsiny untuk mengecek tipe data

paagraf = " aku adalah orang pintar"
student_id = {112,114,126,118,112,118,119,117}
print(student_id)

student_id.add(100)#untuk menambahkan
print(student_id)

student_id.discard(126)#untuk  membuang
print(student_id)

print(list(enumerate(student_id)))#untunk mengakses indek
print(max(student_id))
print(min(student_id))
print(sum(student_id))#untunk mejumlahkan
print(sorted(student_id))#untung mengurutkan dari yang kecil sampai yang terbesar
for i in student_id:
    print(i)
print(type(student_id))
print(type(paagraf))

#first set
A = {1,6,7}
#second set
B= {1,2,3,4,5}
unionAB = A. union(B)
print(unionAB)

intsec= A&B
print(intsec)

diffAB= A-B
print(diffAB)

diffAB = B-A
print(diffAB)

