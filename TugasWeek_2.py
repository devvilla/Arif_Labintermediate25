import random

kata_list = ["hangman"]

kata_rahasia = random.choice(kata_list).upper()
kata_tersembunyi = ["_"] * len(kata_rahasia)
huruf_ditebak = set()
percobaan = 0
maks_percobaan = 6

print("Welcome to Hangman 2.0!")
print("Tebak kata dengan menebak huruf. Kamu punya 6 kesempatan menebak huruf baru.")
print("Menebak huruf yang sama tidak mengurangi kesempatan.")

while percobaan < maks_percobaan and "_" in kata_tersembunyi:
    print("\nKata:", " ".join(kata_tersembunyi))
    print(f"Percobaan tersisa: {maks_percobaan - percobaan}")
    
    tebakan = input("Tebak huruf: ").upper()
    
    if tebakan in huruf_ditebak:
        print("Huruf ini sudah ditebak sebelumnya. Coba huruf lain.")
        continue
    
    huruf_ditebak.add(tebakan)
    percobaan += 1
    
    if tebakan in kata_rahasia:
        for i in range(len(kata_rahasia)):
            if kata_rahasia[i] == tebakan:
                kata_tersembunyi[i] = tebakan
        print("Benar!")
    else:
        print("Salah!")

if "_" not in kata_tersembunyi:
    print("\nSelamat! Kamu menang. Kata:", "".join(kata_tersembunyi))
else:
    print("\nKamu kalah. Kata rahasia:", kata_rahasia)