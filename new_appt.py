import pandas as pd

# Data Base Appointment

file = "./Pet-Clinic-Kelompok-19/data_appt.xlsx"
df_appt = pd.read_excel(file)
db_appt = df_appt.to_dict(orient='list')

# Command Untuk Input Nama Pemilik
def owner_name():
    owners_name = input("Owner's Name : ")
    db_appt["Appt"].append(owners_name)
    update_df = pd.DataFrame.from_dict(db_appt, orient='index')
    update_df = update_df.transpose()
    update_df.to_excel(file, index=False)

# Command Untuk Input Nama Hewan
def patient_name():
    patient_name = input("Patient Name : ")
    db_appt["Patient"].append(patient_name)
    update_df = pd.DataFrame.from_dict(db_appt, orient='index')
    update_df = update_df.transpose()
    update_df.to_excel(file, index=False)

# Command Untuk Input Jenis Hewan
def breed():
    patient_breed = input("Breed : ")
    db_appt["Breed"].append(patient_breed)
    update_df = pd.DataFrame.from_dict(db_appt, orient='index')
    update_df = update_df.transpose()
    update_df.to_excel(file, index=False)

# Command Untuk Input Jenis Kelamin
def sex():
    patient_sex = input("Sex : ")
    db_appt["Sex"].append(patient_sex)
    update_df = pd.DataFrame.from_dict(db_appt, orient='index')
    update_df = update_df.transpose()
    update_df.to_excel(file, index=False)

def age():
    patient_age = input("Age : ")
    db_appt["Age"].append(patient_age)
    update_df = pd.DataFrame.from_dict(db_appt, orient='index')
    update_df = update_df.transpose()
    update_df.to_excel(file, index=False)

def med_treat():
    med_treat = input("Medical Treatment : ")
    db_appt["Medical Treatment"].append(med_treat)
    update_df = pd.DataFrame.from_dict(db_appt, orient='index')
    update_df = update_df.transpose()
    update_df.to_excel(file, index=False)

def date():
    date = input("Date : ")
    db_appt["Date"].append(date)
    update_df = pd.DataFrame.from_dict(db_appt, orient='index')
    update_df = update_df.transpose()
    update_df.to_excel(file, index=False)

owner_name()
patient_name()
breed()
sex()
age()
med_treat()
date()
