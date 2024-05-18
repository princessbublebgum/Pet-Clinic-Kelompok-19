from all_feature import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


# Kelas untuk Kivy App
class PetClinicApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # TextInput untuk memasukkan janji temu
        self.appt_input = TextInput(
            hint_text='Enter Appointment Name',
            size_hint=(1, 0.2),
            multiline=False
        )
        self.layout.add_widget(self.appt_input)

        # Tombol untuk mencari janji temu dan mencetak tagihan
        self.search_button = Button(text='Search', size_hint=(1, 0.2))
        self.search_button.bind(on_press=self.show_medtreat_and_print_bill)
        self.layout.add_widget(self.search_button)

        # Label untuk menampilkan Medical Treatment
        self.treatment_label = Label(text='Medical Treatment: ', size_hint=(1, 0.2))
        self.layout.add_widget(self.treatment_label)

        # Label untuk menampilkan harga
        self.price_label = Label(text='Price: ', size_hint=(1, 0.2))
        self.layout.add_widget(self.price_label)

        return self.layout

    def show_medtreat_and_print_bill(self, instance):
        appt_input = self.appt_input.text
        treatment_data = get_medtreat_data(appt_input)
        if treatment_data:
            self.treatment_label.text = f'Medical Treatment: {treatment_data}'
            price = get_price(treatment_data)
            if price:
                self.price_label.text = f'Price: {price}'
            else:
                self.price_label.text = 'Price: Not Available'
        else:
            self.treatment_label.text = 'Medical Treatment: Not Found'
            self.price_label.text = 'Price: Not Found'

if __name__ == '__main__':
    PetClinicApp().run()

# Buatan Zhill
import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner

# File path to the Excel file
file = "./Pet-Clinic-Kelompok-19/data_appt.xlsx"

# Load the data from the Excel file
df_appt = pd.read_excel(file)
df_appt = df_appt.set_index("Appt")
db_appt = df_appt.to_dict(orient='list')

# Function to cancel appointment based on name
def cancel_appt(appt_name):
    if appt_name in df_appt.index:
        for key in db_appt:
            db_appt[key].remove(db_appt[key][df_appt.index.get_loc(appt_name)])
        df_appt.drop(appt_name, inplace=True)
        df_appt.reset_index().to_excel(file, index=False)
        return f"Appointment '{appt_name}' has been cancelled."
    else:
        return f"Appointment '{appt_name}' not found."

# Custom widget for the main window
class CancelApptWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        self.label = Label(text="Select Appointment to Cancel:")
        self.add_widget(self.label)
        
        self.spinner = Spinner(
            text='Select Appointment',
            values=list(df_appt.index),
            size_hint=(None, None),
            size=(1500, 500)
        )
        self.add_widget(self.spinner)
        
        self.cancel_button = Button(text="Cancel Appointment")
        self.cancel_button.bind(on_press=self.on_cancel_button_press)
        self.add_widget(self.cancel_button)
    
    def on_cancel_button_press(self, instance):
        appt_name = self.spinner.text
        if appt_name != 'Select Appointment':
            message = cancel_appt(appt_name)
            self.show_popup(message)
            self.spinner.text = 'Select Appointment'
            self.spinner.values = list(df_appt.index)
    
    def show_popup(self, message):
        popup = Popup(title='Notification',
                      content=Label(text=message),
                      size_hint=(None, None), size=(100, 700))
        popup.open()

# Main App class
class CancelApptApp(App):
    def build(self):
        return CancelApptWindow()

# Create and run the app
if __name__ == '__main__':
    CancelApptApp().run()
