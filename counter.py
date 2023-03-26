nama = input('Masukkan sebuah file = ')
handle = open(nama)

hitung = dict()
for kalimat in handle:
    kata = kalimat.split()
    for word in kata:
        hitung[word] = hitung.get(word,0) + 1
    
bigcount = None
terbesar = None
for word,count  in hitung.items():
    if bigcount is None or count > bigcount:
        terbesar = word
        bigcount = count 

print(terbesar, bigcount)
