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

# Buatan Hanif
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import csv

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.padding = [100, 20]
        
        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        
        self.login_button = Button(text='Login')
        self.signup_button = Button(text='Sign Up')
        
        self.add_widget(Label(text='Welcome to the Login Screen', font_size=24))
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)
        self.add_widget(self.login_button)
        self.add_widget(self.signup_button)
        
        self.login_button.bind(on_press=self.login)
        self.signup_button.bind(on_press=self.signup)
        
    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        
        if self.authenticate(username, password):
            self.clear_widgets()
            self.add_widget(MenuScreen())
        else:
            print("Invalid username or password.")
    
    def authenticate(self, username, password):
        with open('database_login.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    return True
        return False
    
    def signup(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        
        if self.username_exists(username):
            print("Username already exists. Please choose another one.")
        else:
            with open('database_login.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, password])
            print("Account created successfully!")
    
    def username_exists(self, username):
        with open('database_login.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    return True
        return False

class MenuScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.padding = [100, 20]
        
        self.welcome_label = Label(text='Welcome to the Menu Screen', font_size=24)
        self.menu_button1 = Button(text='Buat Appointment baru')
        self.menu_button2 = Button(text='Batalkan Appointment')
        self.menu_button3 = Button(text='Tampilkan seluruh Appointment')
        self.menu_button4 = Button(text='Cetak Tagihan')
        self.logout_button = Button(text='Logout')
        
        self.add_widget(self.welcome_label)
        self.add_widget(self.menu_button1)
        self.add_widget(self.menu_button2)
        self.add_widget(self.menu_button3)
        self.add_widget(self.menu_button4)
        self.add_widget(self.logout_button)
        
        self.menu_button1.bind(on_press=self.option1)
        self.menu_button2.bind(on_press=self.option2)
        self.menu_button3.bind(on_press=self.option3)
        self.menu_button4.bind(on_press=self.option4)
        self.logout_button.bind(on_press=self.logout)
        
    def option1(self, instance):
        print("Option 1 selected.")
    
    def option2(self, instance):
        print("Option 2 selected.")
    
    def option3(self, instance):
        print("Option 3 selected.")
    
    def option4(self, instance):
        print("Option 4 selected.")
    
    def logout(self, instance):
        self.clear_widgets()
        self.add_widget(LoginScreen())

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()
