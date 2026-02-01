def update_display_word(secret_word, guessed_letters):
    
    tampilan = ""
    for huruf in secret_word:
        if huruf in guessed_letters:
            tampilan = tampilan + huruf + " "
        else:
            tampilan = tampilan + "_ "
    return tampilan

def update_text(guess, secret_word):
   
    if guess in secret_word:
        print(f"Benar! Huruf '{guess}' ada.")
        return True
    else:
        print(f"Salah! Huruf '{guess}' tidak ada.")
        return False

def main_game(secret_word):
    
    guessed_letters = [] 
    chances = 5           
    
    print("=== GAME TEBAK DONG ===")
    
    while chances > 0:
        
        status_saat_ini = update_display_word(secret_word, guessed_letters)
        print(f"\nKata: {status_saat_ini}")
      
        if "_" not in status_saat_ini:
            print("\nSELAMAT! lu Menang!")
            print(f"Kata rahasianya: {secret_word}")
            return 
        
        print(f"Sisa nyawa: {chances}")
        guess = input("Masukkan satu huruf: ").upper() 
      
        guessed_letters.append(guess)
        
        apakah_benar = update_text(guess, secret_word)
        
        if apakah_benar == False:
            chances = chances - 1

    print("\nGAME OVER. Lu Kalah.")
    print(f"Kata rahasianya: {secret_word}")

main_game("BUMAME")