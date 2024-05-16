import pandas as pd

# Membuka Data
file_path = "./Pet-Clinic-Kelompok-19/data_appt.xlsx"
df_appt = pd.read_excel(file_path)
df_appt = df_appt.set_index("Appt")

# Mengakses Data Pasien
def get_patient_data(appt_input):
    return df_appt.loc[appt_input, 'Patient']

# Menampilkan Pasien
def show_patient_data():
    appt_input = input("Appointment Name: ")
    patient_data = get_patient_data(appt_input)
    print("Patient:", patient_data)

# Mengakses Data Breed
def get_breed_data(appt_input):
    return df_appt.loc[appt_input, 'Breed']

# Menampilkan Breed
def show_breed_data():
    appt_input = input("Appointment Name: ")
    breed_data = get_breed_data(appt_input)
    print("Breed:", breed_data)

# Mengakses data kelamin hewan
def get_sex_data(appt_input):
    return df_appt.loc[appt_input, 'Sex']

# Menampilkan kelamin hewan 
def show_sex_data():
    appt_input = input("Appointment Name: ")
    sex_data = get_sex_data(appt_input)
    print("Sex:", sex_data)

# Mengakses data umur hewan
def get_age_data(appt_input):
    return df_appt.loc[appt_input, 'Age']

# Menampilkan umur hewan
def show_age_data():
    appt_input = input("Appointment Name: ")
    age_data = get_age_data(appt_input)
    print("Age:", age_data)

# Mengakses data medical treatment hewan 
def get_medtreat_data(appt_input):
    return df_appt.loc[appt_input, 'Medical Treatment']

# Menampilkan medical treatment hewan 
def show_medtreat_data():
    appt_input = input("Appointment Name: ")
    treatment_data = get_medtreat_data(appt_input)
    print("Treatment:", treatment_data)

# Mengakses data tanggal appointment
def get_date_data(appt_input):
    return df_appt.loc[appt_input, 'Date']

# Menampilkan tanggal appointment
def show_date_data():
    appt_input = input("Appointment name: ")
    date_data = get_date_data(appt_input)
    print("Date:", date_data)

show_breed_data()