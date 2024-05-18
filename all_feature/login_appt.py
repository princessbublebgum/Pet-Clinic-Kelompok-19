#Database untuk menyimpan data pengguna
database = {
    "Hanif": "120505",
    "Najwa": "010405",
    "Natasya": "050904",
    "Zhill": "281204",
    "Rafa": "311205"
}

def login():
    username = input("Masukkan nama pengguna: ")
    password = input("Masukkan kata sandi: ")

    # Autentikasi akun
    if username in database and database[username] == password:
        print("Login berhasil, Selamat datang di Pet Clinic!")
    else:
        print("Nama pengguna atau kata sandi salah. Silakan coba lagi.")
        
if __name__== '__main__':
    pass

