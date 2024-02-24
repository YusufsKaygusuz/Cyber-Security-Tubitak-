# ---------------------------
# Brute force attack Codes
# ---------------------------
import itertools

def brute_force_attack(password, max_length=6):
    # Mümkün karakterler
    possible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    # Tüm olası kombinasyonlar
    for length in range(1, max_length + 1):
        combinations = itertools.product(possible_characters, repeat=length)
        for combination in combinations:
            attempt = ''.join(combination)
            if attempt == password:
                return attempt
    return None

# Parola
password = input("Parolayı girin: ")

# Parola kırma denemesi
result = brute_force_attack(password)

if result:
    print(f"Parola kırıldı. Parola: {result}")
else:
    print("Parola kırılamadı.")

# ---------------------------
# Dictionary Attack Codes
# ---------------------------
# Önceden oluşturulmuş bir kelimeler sözlük kümesi. Kişinini bilgilerinden edilen detaylar burada kullanılır. 
dictionary = ["password", "123456", "qwerty", "letmein", "hello"]

# Parola tahmin etme fonksiyonu
def dictionary_attack(password):
    if password in dictionary:
        return True
    return False

# Parolayı kontrol et
password = input("Parolayı girin: ")
if dictionary_attack(password):
    print("Parola kırıldı.")
else:
    print("Parola kırılamadı.")

# ---------------------------
# Personalized Attack Codes
# ---------------------------

import itertools

# Kişisel bilgileri tanımla
personal_info = {
    "birth_date": "15071990",
    "hometown": "Ankara",
    "children_names": ["ali", "ayşe"]
}

# Parola tahmin etme fonksiyonu
def personalized_attack(password):
    for length in range(1, len(password) + 1):
        # Kişisel bilgileri tek tek ele alarak kombinasyonlar oluştur
        for info in personal_info.values():
            for combination in itertools.product(*([char.upper(), char.lower()] for char in info), repeat=length):
                attempt = ''.join(combination)
                if attempt == password:
                    return True
    return False

# Hedef parola
target_password = "1507ali"

# Parola kırma denemesi
if personalized_attack(target_password):
    print("Parola kırıldı.")
else:
    print("Parola kırılamadı.")




