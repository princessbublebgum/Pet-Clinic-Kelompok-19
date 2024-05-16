import pandas as pd

# Data Base Appointment
db_appt = {
    "Appt" : [],
    "Patient" : [],
    "Breed" : [],
    "Sex" : [],
    "Age" : [],
    "Medical Treatment" : [],
    "Date" : [],
    }

# Command Untuk Input Nama Pemilik
def owner_name():
    owners_name = input("Owner's Name : ")
    db_appt["Appt"].append(owners_name)

# Command Untuk Input Nama Hewan
def patient_name():
    patient_name = input("Patient Name : ")
    db_appt["Patient"].append(patient_name)

# Command Untuk Input Jenis Hewan
def breed():
    patient_breed = input("Breed : ")
    db_appt["Breed"].append(patient_breed)

# Command Untuk Input Jenis Kelamin
def sex():
    patient_sex = input("Sex : ")
    db_appt["Sex"].append(patient_sex)

def age():
    patient_age = input("Age : ")
    db_appt["Age"].append(patient_age)

def med_treat():
    med_treat = input("Medical Treatment : ")
    db_appt["Medical Treatment"].append(med_treat)

def date():
    date = input("Date : ")
    db_appt["Date"].append(date)

def data_frame():
    global df_appt
    df_appt = pd.DataFrame.from_dict(db_appt, orient='index')
    df_appt = df_appt.transpose()
    df_appt = df_appt.set_index("Appt")
    print(df_appt)

def df_to_excel():
    file = "Pet-Clinic-Kelompok-19/data_appt.xlsx"
    df_appt.to_excel(file)


owner_name()
patient_name()
breed()
sex()
age()
med_treat()
date()
data_frame()
df_to_excel()