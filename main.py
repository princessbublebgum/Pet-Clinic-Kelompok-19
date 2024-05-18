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
