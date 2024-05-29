from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.config import Config
Config.set ("graphics", "resizable", False)
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.metrics import sp, dp
from kivymd.uix.menu import MDDropdownMenu
from kivy.utils import get_color_from_hex
from kivymd.uix.pickers import MDModalDatePicker
from kivy.clock import Clock
from kivymd.uix.pickers import MDTimePickerDialVertical, MDTimePickerInput
from kivymd.uix.dialog import MDDialog
import csv

Window.maximize()

KV = '''
<MyScreenManager>:
    MDScreen:
        name: "LoginInterface"
        md_bg_color: "#CDE2FF"

        MDLabel:
            text: "Pet Clinic Adm."
            font_style: "bold"
            text_color: "#062D3E"
            role: "small"
            adaptive_size: True
            pos_hint: {"x": 0.16, "y": 0.7825}
        
        MDBoxLayout:
            size_hint: 0.16, 0.16
            pos_hint: {"x": 0.025, "y": 0.75}
        
            Image:
                source: "/Users/Najwa Permata Hadi/Documents/Tugas Besar Programa Komputer/Pet-Clinic-Kelompok-19/logo.png"
        
        MDLabel:
            text: "Login"
            font_style: "bold"
            text_color: "#062D3E"
            role: "large"
            adaptive_size: True
            pos_hint: {"x": 0.075, "y": 0.6}
                
        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#FFF9E6"
            radius: 25, 25, 25, 25
            padding: "35dp"
            spacing: "5dp"
            size_hint: 0.375, 0.425
            pos_hint: {"x": 0.075, "y": 0.15}

            MDLabel:
                text: "ID name"
                size_hint: 1, 0.35
                font_style: "light"
                role: "small"
                text_color: "#062D3E"

            MDTextField:
                id: id_field
                style: "outlined"
                radius: 8, 8, 8, 8

            MDLabel:
                text: ""
                size_hint: 1, 0.1

            MDLabel:
                text: "password"
                size_hint: 1, 0.35
                font_style: "light"
                role: "small"
                text_color: "#062D3E"
                    
            MDTextField:
                id: password_field
                style: "outlined"
                radius: 8, 8, 8, 8

            MDLabel:
                text: ""
                size_hint: 1, 0.9

        MDButton:
            style: "elevated"
            theme_bg_color: "Custom"
            theme_width: "Custom"
            width: "140dp"
            md_bg_color: "#062D3E"
            pos_hint: {"x": 0.315, "y": 0.185}
            on_release: app.login()

            MDButtonText:
                text: "next"
                pos_hint: {"center_x": .5, "center_y": .5}
                font_style: "semi_bold"
                role: "small"
                theme_text_color: "Custom"
                text_color: "#CDE2FF"
    
    MDScreen:
        name: "Menu"
        md_bg_color: "#CDE2FF"

        MDButton:
            text: "New Appt"
            font_style: "semi_bold"
            text_color: "#062D3E"
            role: "medium"
            pos_hint: {"center_x": 0.5, "y": 0.5}

    MDScreen:
        name: "OwnerInformation"
        md_bg_color: "#CDE2FF"

        MDLabel:
            text: "New Appointment"
            font_style: "bold"
            text_color: "#062D3E"
            role: "large"
            adaptive_size: True
            pos_hint: {"x": 0.075, "y": 0.75}
        
        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#FFF9E6"
            radius: 25, 25, 25, 25
            padding: "35dp"
            spacing: "5dp"
            size_hint: 0.85, 0.58
            pos_hint: {"center_x": 0.5, "y": 0.125}

            MDLabel:
                text: "owner information"
                font_style: "bold"
                role: "medium"
                text_color: "#062D3E"
                adaptive_size: True

            MDBoxLayout:
                orientation: "vertical"

                MDLabel:
                    text: "name"
                    size_hint: 1, 0.35
                    font_style: "light"
                    role: "small"
                    text_color: "#062D3E"

                MDTextField:
                    style: "outlined"
                    radius: 8, 8, 8, 8

                MDLabel:
                    text: ""
                    size_hint: 1, 0.05

                MDLabel:
                    text: "phone number"
                    size_hint: 1, 0.35
                    font_style: "light"
                    role: "small"
                    text_color: "#062D3E"
                    
                MDTextField:
                    style: "outlined"
                    radius: 8, 8, 8, 8

                MDLabel:
                    text: ""
                    size_hint: 1, 0.25

                MDButton:
                    style: "elevated"
                    theme_bg_color: "Custom"
                    theme_width: "Custom"
                    width: "140dp"
                    md_bg_color: "#062D3E"
                    pos_hint: {"x": 0.83}
                    on_release: root.current = "PetInformation"

                    MDButtonText:
                        text: "next"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        font_style: "semi_bold"
                        role: "small"
                        theme_text_color: "Custom"
                        text_color: "#CDE2FF"

        MDAnchorLayout:
            anchor_x: "left"
            anchor_y: "top"

            MDBoxLayout:
                orientation: "vertical"
                size_hint: 0.4, 0.1125
                padding: "18dp"
                spacing: "8dp"

                MDLabel:
                    text: "Hello, Nurse!"
                    font_style: "semi_bold"
                    text_color: "#062D3E"
                    role: "small"
                
                MDLabel:
                    text: "Your Name"
                    font_style: "regular"
                    text_color: "#062D3E"
                    role: "small"
    
    MDScreen:
        name: "PetInformation"
        md_bg_color: "#CDE2FF"

        MDLabel:
            text: "New Appointment"
            font_style: "bold"
            text_color: "#062D3E"
            role: "large"
            adaptive_size: True
            pos_hint: {"x": 0.075, "y": 0.77}

        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#FFF9E6"
            radius: 25, 25, 25, 25
            padding: "35dp"
            spacing: "25dp"
            size_hint: 0.85, 0.65
            pos_hint: {"center_x": 0.5, "y": 0.078}

            MDLabel:
                text: "pet information"
                font_style: "bold"
                role: "medium"
                text_color: "#062D3E"
                adaptive_size: True
        
            MDGridLayout:
                cols: 2
                row: 6
                spacing: "32dp", "22.5dp"

                MDLabel:
                    text: "name"
                    font_style: "light"
                    role: "small"
                    text_color: "#062D3E"
                    
                MDLabel:
                    text: "age"
                    font_style: "light"
                    role: "small"
                    text_color: "#062D3E"
                    
                MDTextField:
                    mode: "outlined"
                    radius: 8, 8, 8, 8

                MDTextField:
                    mode: "outlined"
                    radius: 8, 8, 8, 8
                    
                MDLabel:
                    text: "breed"
                    font_style: "light"
                    role: "small"
                    text_color: "#062D3E"
                
                MDLabel:
                    text: "sex"
                    font_style: "light"
                    role: "small"
                    text_color: "#062D3E"

                MDTextField:
                    mode: "outlined"
                    radius: 8, 8, 8, 8

                MDFloatLayout:

                    MDLabel:
                        text: "male"
                        font_style: "light"
                        role: "small"
                        text_color: "#062D3E"
                        pos_hint: {'center_x': 0.575, 'center_y': .5}

                    MDCheckbox:
                        size_hint: None, None
                        size: dp(20), dp(20)
                        pos_hint: {'center_x': 0.025, 'center_y': .5}

                    MDLabel:
                        text: "female"
                        font_style: "light"
                        role: "small"
                        text_color: "#062D3E"
                        pos_hint: {'center_x': 0.9, 'center_y': .5}

                    MDCheckbox:
                        size_hint: None, None
                        size: dp(20), dp(20)
                        pos_hint: {'center_x': 0.35, 'center_y': .5}

                MDLabel:
                    text: "weight"
                    font_style: "light"
                    role: "small"
                    text_color: "#062D3E"

                MDLabel:
                    text: "spayed/neutered"
                    font_style: "light"
                    role: "small"
                    text_color: "#062D3E"

                MDTextField:
                    mode: "outlined"
                    radius: 8, 8, 8, 8

                MDFloatLayout:

                    MDLabel:
                        text: "yes"
                        font_style: "light"
                        role: "small"
                        text_color: "#062D3E"
                        pos_hint: {'center_x': 0.575, 'center_y': .5}

                    MDCheckbox:
                        size_hint: None, None
                        size: dp(20), dp(20)
                        pos_hint: {'center_x': 0.025, 'center_y': .5}

                    MDLabel:
                        text: "no"
                        font_style: "light"
                        role: "small"
                        text_color: "#062D3E"
                        pos_hint: {'center_x': 0.9, 'center_y': .5}

                    MDCheckbox:
                        size_hint: None, None
                        size: dp(20), dp(20)
                        pos_hint: {'center_x': 0.35, 'center_y': .5}

            MDLabel:
                text: ""
                size_hint: 1, 0.4

        MDButton:
            style: "elevated"
            theme_bg_color: "Custom"
            theme_width: "Custom"
            width: "140dp"
            md_bg_color: "#062D3E"
            pos_hint: {"x": 0.785, "y": 0.115}
            on_release: root.current = "MedTreatmentInformation"

            MDButtonText:
                text: "next"
                pos_hint: {"center_x": .5, "center_y": .5}
                font_style: "semi_bold"
                role: "small"
                theme_text_color: "Custom"
                text_color: "#CDE2FF"
        
        MDButton:
            style: "elevated"
            theme_bg_color: "Custom"
            theme_width: "Custom"
            width: "140dp"
            md_bg_color: "#062D3E"
            pos_hint: {"x": 0.675, "y": 0.115}
            on_release: root.current = "OwnerInformation"

            MDButtonText:
                text: "back"
                pos_hint: {"center_x": .5, "center_y": .5}
                font_style: "semi_bold"
                role: "small"
                theme_text_color: "Custom"
                text_color: "#CDE2FF"

        MDAnchorLayout:
            anchor_x: "left"
            anchor_y: "top"

            MDBoxLayout:
                orientation: "vertical"
                size_hint: 0.4, 0.1125
                padding: "18dp"
                spacing: "8dp"

                MDLabel:
                    text: "Hello, Nurse!"
                    font_style: "semi_bold"
                    text_color: "#062D3E"
                    role: "small"
                
                MDLabel:
                    text: "Your Name"
                    font_style: "regular"
                    text_color: "#062D3E"
                    role: "small"

    MDScreen:
        name: "MedTreatmentInformation"
        md_bg_color: "#CDE2FF"
      
        MDLabel:
            text: "New Appointment"
            font_style: "bold"
            text_color: "#062D3E"
            role: "large"
            adaptive_size: True
            pos_hint: {"x": 0.075, "y": 0.75}
        
        MDGridLayout:
            cols: 2
            row: 2
            md_bg_color: "#FFF9E6"
            radius: 25, 25, 25, 25
            padding: "35dp"
            spacing: "30dp"
            size_hint: 0.85, 0.58
            pos_hint: {"center_x": 0.5, "y": 0.125}

            MDLabel:
                text: "select treatment"
                font_style: "bold"
                role: "medium"
                text_color: "#062D3E"
                size_hint: 0.5, 0.05

            MDLabel:
                text: "date & time"
                font_style: "bold"
                role: "medium"
                text_color: "#062D3E"
                size_hint: 0.5, 0.05
            
            MDBoxLayout:
                md_bg_color: "#FFF000"
                orientation: "vertical"
                size_hint: 0.5, 0.95

                MDButton:
                    id: button
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: "#F4E8D9"
                    height: "48dp"
                    theme_width: "Custom"
                    size_hint_x: 1
                    on_release: app.menu_open()

                    MDButtonText:
                        id: text
                        text: "select treatment"
                        font_style: "light"
                        role: "small"
                        text_color: "#062D3E"
                        pos_hint: {"center_x": .25, "center_y": .5}

                    MDButtonIcon:
                        pos_hint: {"center_x": .9, "center_y": .5}
                        icon: "triangle-down"
                        size_hint: 0.5, 0.5
                        md_bg_color: "#062D3E"
                    
                MDRelativeLayout:
                    size_hint: 1, 0.8
                    md_bg_color: "#FFFFFF"

                    MDLabel:
                        id: selected_item_label
                        text: "None"
                        md_bg_color: "#F4E8D9"
                        font_style: "light"
                        role: "medium"
                        text_color: "#062D3E"
                        halign: "center"
                        radius: 20, 20, 20, 20
                        size_hint: 1, 0.25
                        pos_hint: {"center_x": 0.5, "y": 0.65}  # Adjust position as needed

            MDBoxLayout:
                md_bg_color: "#FFF000"
                orientation: "vertical"
                size_hint: 0.5, 0.95

                MDButton:
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: "#F4E8D9"
                    height: "48dp"
                    theme_width: "Custom"
                    size_hint_x: 1
                    on_release: app.show_date_picker()
            
                    MDButtonText:
                        id: text
                        text: "Open modal date picker dialog"
                        font_style: "light"
                        role: "small"
                        text_color: "#062D3E"
                        pos_hint: {"center_x": .25, "center_y": .5}
                
                MDButton:
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_release: app.show_time_picker_vertical()

                MDButtonText:
                    text: "Open time picker"

                    # MDButtonIcon:
                    #     pos_hint: {"center_x": .9, "center_y": .5}
                    #     icon: "triangle-down"
                    #     size_hint: 0.5, 0.5
                    #     md_bg_color: "#062D3E"
                    
                MDLabel:
                    md_bg_color: "#FFFFFF"
                    text:""
                    size_hint: 1, 0.8

        MDAnchorLayout:
            anchor_x: "left"
            anchor_y: "top"

            MDBoxLayout:
                orientation: "vertical"
                size_hint: 0.4, 0.1125
                padding: "18dp"
                spacing: "8dp"

                MDLabel:
                    text: "Hello, Nurse!"
                    font_style: "semi_bold"
                    text_color: "#062D3E"
                    role: "small"
                
                MDLabel:
                    text: "Your Name"
                    font_style: "regular"
                    text_color: "#062D3E"
                    role: "small"




'''


class MyScreenManager(MDScreenManager):
    pass

class Example(MDApp):
    def menu_open(self):
        treatments = self.extract_medical_treatments("Pet-Clinic-Kelompok-19/price.csv")
        menu_items = [
            {
                "text": treatment,
                "on_release": lambda x=treatment: self.menu_callback(x),
            } for treatment in treatments
        ]
        MDDropdownMenu(
            caller=self.root.ids.button,
            items=menu_items,
            position="bottom",
            width=dp(500),
            ver_growth="down",
            radius=[5, 5, 5, 5]
        ).open()

    def extract_medical_treatments(self, csv_file):
        treatments = []
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                treatment = row[0]  # Assuming the first column contains treatment names
                treatments.append(treatment)
        return treatments

    def menu_callback(self, text_item):
        self.root.ids.selected_item_label.text = f"{text_item}"
    
    def show_date_picker(self):
        date_dialog = MDModalDatePicker()
        date_dialog.open()
    
    def on_edit_time_picker_input(self, time_picker_input):
        time_picker_input.dismiss()
        Clock.schedule_once(self.show_time_picker_vertical, 0.2)

    def show_time_picker_input(self, *args):
        time_picker_input = MDTimePickerInput()
        time_picker_input.bind(on_edit=self.on_edit_time_picker_input)
        time_picker_input.open()

    def on_edit_time_picker_vertical(self, time_picker_vertical):
        time_picker_vertical.dismiss()
        Clock.schedule_once(self.show_time_picker_input, 0.2)

    def show_time_picker_vertical(self, *args):
        time_picker_vertical = MDTimePickerDialVertical()
        time_picker_vertical.bind(on_edit=self.on_edit_time_picker_vertical)
        time_picker_vertical.open()

    def login(self):
        id_name = self.root.ids.id_field.text
        password = self.root.ids.password_field.text
        
        # Load CSV file
        file_path = "Pet-Clinic-Kelompok-19/database_login.csv"
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['ID Name'] == id_name and row['Password'] == password:
                    # Successful login
                    self.root.current = "Menu"
                    return
        # Failed login
        print("Incorrect ID Name or Password")

    def build(self):
        LabelBase.register(
            name="bold",
            fn_regular="bold.ttf",
        )

        self.theme_cls.font_styles["bold"] = {
            "large": {
                "line-height": 1,
                "font-name": "bold",
                "font-size": sp(48),
            },
            "medium": {
                "line-height": 1,
                "font-name": "bold",
                "font-size": sp(30),
            },
            "small": {
                "line-height": 1,
                "font-name": "bold",
                "font-size": sp(62),
            },
        }

        LabelBase.register(
            name="semi_bold",
            fn_regular="semi_bold.ttf",
        )

        self.theme_cls.font_styles["semi_bold"] = {
            "large": {
                "line-height": 1,
                "font-name": "semi_bold",
                "font-size": sp(57),
            },
            "medium": {
                "line-height": 1,
                "font-name": "semi_bold",
                "font-size": sp(30),
            },
            "small": {
                "line-height": 1,
                "font-name": "semi_bold",
                "font-size": sp(18),
            },
        }

        LabelBase.register(
            name="regular",
            fn_regular="regular.ttf",
        )

        self.theme_cls.font_styles["regular"] = {
            "large": {
                "line-height": 1,
                "font-name": "regular",
                "font-size": sp(57),
            },
            "medium": {
                "line-height": 1,
                "font-name": "regular",
                "font-size": sp(28),
            },
            "small": {
                "line-height": 1,
                "font-name": "regular",
                "font-size": sp(16),
            },
        }


        LabelBase.register(
            name="light",
            fn_regular="light.ttf",
        )

        self.theme_cls.font_styles["light"] = {
            "large": {
                "line-height": 1,
                "font-name": "light",
                "font-size": sp(57),
            },
            "medium": {
                "line-height": 1,
                "font-name": "light",
                "font-size": sp(30),
            },
            "small": {
                "line-height": 1,
                "font-name": "light",
                "font-size": sp(18),
            },
        }
        
        Builder.load_string(KV)
        return MyScreenManager()

Example().run()