import pandas as pd

# Membuka Data
file_path = "./Pet-Clinic-Kelompok-19/data_appt.xlsx"
df_appt = pd.read_excel(file_path)
df_appt = df_appt.set_index("Appt")

# Mengakses data pasien
def get_data_appt():
    return df_appt.index.values

def input_name():
    global appt_input
    appt_input = input("Enter the appointment name: ")

def get_data():
    return df_appt.loc[appt_input]




