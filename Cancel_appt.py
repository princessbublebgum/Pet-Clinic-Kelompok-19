def load_data():
    """
    Memuat data appointment dari file teks.

    Returns:
        Daftar appointment.
    """
    try:
        with open('appointment_data.txt', 'r') as file:
            data = [
                {
                    'nama_pemilik': baris.split(',')[0],
                    'nama_hewan': baris.split(',')[1],
                    'tanggal_janji': baris.split(',')[2],
                    'jam_janji': baris.split(',')[3],
                    'keterangan': baris.split(',')[4]
                }
                for baris in file.readlines()
            ]
        return data
    except FileNotFoundError:
        return []

def save_data(data):
    """
    Menyimpan data appointment ke file teks.

    Args:
        data: Daftar appointment yang ingin disimpan.
    """
    with open('appointment_data.txt', 'w') as file:
        for appointment in data:
            file.write(f"{appointment['nama_pemilik']},{appointment['nama_hewan']},{appointment['tanggal_janji']},{appointment['jam_janji']},{appointment['keterangan']}\n")

def search_appointment(nama_pemilik):
    """
    Mencari data appointment berdasarkan nama pemilik.

    Args:
        nama_pemilik: Nama pemilik yang ingin dicari datanya.

    Returns:
        Appointment (dict) jika ditemukan, None jika tidak ditemukan.
    """
    data = load_data()
    for appointment in data:
        if appointment['nama_pemilik'] == nama_pemilik:
            return appointment
    return None

def delete_appointment(nama_pemilik):
    """
    Menghapus data appointment berdasarkan nama pemilik.

    Args:
        nama_pemilik: Nama pemilik yang ingin dihapus appointmentnya.
    """
    data = load_data()
    new_data = []
    for appointment in data:
        if appointment['nama_pemilik'] != nama_pemilik:
            new_data.append(appointment)
    save_data(new_data)

def main():
    """
    Fungsi utama untuk menjalankan program.
    """
    nama_pemilik = input("Masukkan nama pemilik hewan: ")
    appointment = search_appointment(nama_pemilik)

    if appointment:
        print(f"Appointment ditemukan untuk {nama_pemilik}:")
        print(appointment)
        konfirmasi = input("Apakah Anda ingin menghapus appointment ini? (y/n): ")
        if konfirmasi.lower() == 'y':
            delete_appointment(nama_pemilik)
            print("Appointment telah dihapus.")
        else:
            print("Appointment tidak dihapus.")
    else:
        print(f"Appointment tidak ditemukan untuk {nama_pemilik}.")

if __name__ == "__main__":
    main()
