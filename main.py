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

import openpyxl
from kivymd.uix.list import MDListItem, MDList
from kivymd.uix.button import MDButton
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp

class AppointmentApp(MDApp):

    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        self.layout = MDList()

        # Baca data Excel
        wb = openpyxl.load_workbook('data_appt.xlsx')
        ws = wb.active

        for row in ws.iter_rows(min_row=2):
            nama_pasien = row[0].value

            # Buat item daftar
            item = MDListItem(
                text=f"{nama_pasien} ",
                padding=(16, 8),
                # Tambahkan properti visual untuk item daftar
                theme_style="B",  
                line_color=(0, 0, 0, 0.4),  
                left_padding=16, 
                right_padding=16, 
                on_press=self.show_detail, 
            )

            # Buat button
            button = MDButton(
                text="Lihat Detail",
                state_press=self.show_detail,
                style="elevated",
                pos_hint={"right": 1, "center_y": 0.5},
                # Tambahkan properti visual untuk button
                elevation_level=4, 
                radius=16, 
                on_release=self.show_detail, 
            )

            # Tambahkan label penjajaran kanan dan button ke item daftar
            item.add_widget(MDLabel(halign="right"))
            item.add_widget(button)

            # Tambahkan item ke daftar
            self.layout.add_widget(item)

    def show_detail(self, instance):
        # Tampilkan layar detail appointment dengan informasi dari instance yang ditekan
        if isinstance(instance, MDListItem):
            nama_pasien = instance()[0] 
            print(f"Detail appointment untuk: {nama_pasien}")
        elif isinstance(instance, MDButton):
            print("Tombol 'Lihat Detail' ditekan")

    def build(self):
        return self.layout