# Fungsi buat menampilkan Appt.
# Menampilkam Appt. hanya dengan menginput nama owner
# Print(df.loc["John"]) --> kamu buat input
# Impor data_appt.xlsx + new_appt.py

# Fungsi --> Nama Appt.
# Fungsi --> Patient
# Fungsi --> Breed
# Fungsi --> Sex
# Fungsi --> Medical Treatment
# Fungsi --> Date


import pandas as pd

# Assuming your Excel file is named 'your_file.xlsx'
file_path = "Pet-Clinic-Kelompok-19/data_appt.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)
df = df.set_index("Appt")

# Now you can use 'df' as your DataFrame
print(df)

# Mengakses data pasien
def get_patient_data(appt_input):
    return df.loc[appt_input, 'Patient']
# Menampilkan Pasien
def menampilkan_patient():
    appt_input = input("Enter the appointment name: ")
    patient_data = get_patient_data(appt_input)
    print("Patient:", patient_data)

# Mengakses data Breed
def get_breed_data(appt_input):
    return df.loc[appt_input, 'Breed']
# Menampilkan Breed
def menampilkan_breed():
    appt_input = input("Enter the appointment name: ")
    breed_data = get_breed_data(appt_input)
    print("Breed:", breed_data)

# Mengakses data kelamin hewan
def get_sex_data(appt_input):
    return df.loc[appt_input, 'Sex']
# Menampilkan kelamin hewan 
def menampilkan_sex():
    appt_input = input("Enter the appointment name: ")
    sex_data = get_sex_data(appt_input)
    print("Sex:", sex_data)

# Mengakses data umur hewan
def get_age_data(appt_input):
    return df.loc[appt_input, 'Age']
# Menampilkan umur hewan
def menampilkan_age():
    appt_input = input("Enter the appointment name: ")
    age_data = get_age_data(appt_input)
    print("Age:", age_data)

# Mengakses data treatment hewan 
def get_treatment_data(appt_input):
    return df.loc[appt_input, 'Medical Treatment']
# Menampilkan treatment hewan 
def menampilkan_treatment():
    appt_input = input("Enter the appointment name: ")
    treatment_data = get_treatment_data(appt_input)
    print("Treatment:", treatment_data)

# Mengakses data tanggal appointment
def get_date_data(appt_input):
    return df.loc[appt_input, 'Date']
# Menampilkan tanggal appointment
def menampilkan_date():
    appt_input = input("Enter the appointment name: ")
    date_data = get_date_data(appt_input)
    print("Date:", date_data)

menampilkan_date()