
kata_rahasia = "KOMPUTER"

print("Game Tebak Huruf")
print("Kata punya 8 huruf")

while True:
   
    huruf = input("\nMasukin 1 huruf: ")
    
    if len(huruf) != 1:
        print("Input salah! Cuma boleh 1 huruf")
        continue
    
    if not huruf.isalpha():
        print("Input salah! Cuma boleh huruf a-z")
        continue
    
    if huruf.upper() in kata_rahasia:
        print(f"Huruf '{huruf}' ADA di kata rahasia!")
    else:
        print(f"Huruf '{huruf}' TIDAK ADA di kata rahasia!")
    
    lanjut = input("\nMau coba lagi? (y/t): ")
    if lanjut.lower() != 'y':
        break
