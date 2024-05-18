import pandas as pd

file = "./Pet-Clinic-Kelompok-19/data_appt.xlsx"
df_appt = pd.read_excel(file)
df_appt = df_appt.set_index("Appt")
db_appt = df_appt.to_dict(orient='list')

# Buat Daftar Harga untuk tiap-tiap Medical Treatment
file = "./Pet-Clinic-Kelompok-19/data_price.xlsx"
df_price = pd.read_excel(file)
db_price = df_price.set_index('Medical Treatment').squeeze().to_dict()
print(db_price)

# Mengakses Data Appt
def get_medtreat_data(appt_input):
    return df_appt.loc[appt_input, 'Medical Treatment']

# Menampilkan Medical Treatment Hewan 
def show_medtreat_data():
    global treatment_data
    global appt_input
    appt_input = input("Appointment Name: ")
    treatment_data = get_medtreat_data(appt_input)

def print_bill1():
    global price
    price = db_price[treatment_data]
    return price

show_medtreat_data()
print("Appt. Name : ", appt_input)
print("Medical Treament : ", treatment_data)
print_bill1()
print("Total Bill : ", price)

if __name__== '__main__':
    pass