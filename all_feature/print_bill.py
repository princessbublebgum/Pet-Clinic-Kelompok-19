import pandas as pd

# Membaca file Excel
file_appt = "./Pet-Clinic-Kelompok-19/data_appt.xlsx"
df_appt = pd.read_excel(file_appt)
df_appt = df_appt.set_index("Appt")
db_appt = df_appt.to_dict(orient='list')

file_price = "./Pet-Clinic-Kelompok-19/data_price.xlsx"
df_price = pd.read_excel(file_price)
db_price = df_price.set_index('Medical Treatment').squeeze().to_dict()

# Fungsi untuk mendapatkan data Medical Treatment berdasarkan janji temu
def get_medtreat_data(appt_input):
    return df_appt.loc[appt_input, 'Medical Treatment'] if appt_input in df_appt.index else None

# Fungsi untuk menghitung harga berdasarkan Medical Treatment
def get_price(treatment):
    return db_price[treatment] if treatment in db_price else None

if __name__== '__main__':
    pass