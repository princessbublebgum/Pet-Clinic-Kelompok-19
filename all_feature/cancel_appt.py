import pandas as pd

file = "./Pet-Clinic-Kelompok-19/data_appt.xlsx"
df_appt = pd.read_excel(file)
df_appt = df_appt.set_index("Appt")
db_appt = df_appt.to_dict(orient='list')

def cancel_appt_name():
    global appt_name
    appt_name = input("Appointment Name : ")

def cancel_appt1():
    for key in db_appt:
        db_appt[key].remove(db_appt[key][df_appt.index.get_loc(appt_name)])
    df_appt.drop(appt_name, inplace=True)
    df_appt.reset_index().to_excel(file, index=False)

if __name__== '__main__':
    pass