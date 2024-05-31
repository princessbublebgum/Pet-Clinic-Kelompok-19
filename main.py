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
from kivymd.uix.pickers import MDModalDatePicker, MDModalInputDatePicker
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivy.clock import Clock
from kivymd.uix.pickers import MDTimePickerDialVertical, MDTimePickerInput
from kivymd.uix.dialog import MDDialog
import pandas as pd
import csv

Window.maximize()

KV = '''
<MyScreenManager>:
    # MDScreen:
    #     name: "LoginInterface"
    #     md_bg_color: "#CDE2FF"

    #     MDLabel:
    #         text: "Pet Clinic Adm."
    #         font_style: "bold"
    #         text_color: "#062D3E"
    #         role: "small"
    #         adaptive_size: True
    #         pos_hint: {"x": 0.16, "y": 0.7825}
        
    #     MDBoxLayout:
    #         size_hint: 0.16, 0.16
    #         pos_hint: {"x": 0.025, "y": 0.75}
        
    #         Image:
    #             source: "/Users/Najwa Permata Hadi/Documents/Tugas Besar Programa Komputer/Pet-Clinic-Kelompok-19/logo.png"
        
    #     MDLabel:
    #         text: "Login"
    #         font_style: "bold"
    #         text_color: "#062D3E"
    #         role: "large"
    #         adaptive_size: True
    #         pos_hint: {"x": 0.075, "y": 0.575}
                
    #     MDBoxLayout:
    #         orientation: "vertical"
    #         md_bg_color: "#FFF9E6"
    #         radius: 25, 25, 25, 25
    #         padding: "35dp"
    #         spacing: "5dp"
    #         size_hint: 0.375, 0.425
    #         pos_hint: {"x": 0.075, "y": 0.125}

    #         MDLabel:
    #             text: "ID name"
    #             size_hint: 1, 0.35
    #             font_style: "light"
    #             role: "small"
    #             text_color: "#062D3E"

    #         MDTextField:
    #             id: id_field
    #             style: "outlined"
    #             font_style: "Title"
    #             role: "medium"
    #             radius: 8, 8, 8, 8
                
    #         MDLabel:
    #             text: ""
    #             size_hint: 1, 0.1

    #         MDLabel:
    #             text: "password"
    #             size_hint: 1, 0.35
    #             font_style: "light"
    #             role: "small"
    #             text_color: "#062D3E"
                    
    #         MDTextField:
    #             id: password_field
    #             password: True
    #             style: "outlined"
    #             font_style: "Title"
    #             role: "medium"
    #             radius: 8, 8, 8, 8

    #         MDLabel:
    #             text: ""
    #             size_hint: 1, 0.875

    #     MDButton:
    #         style: "elevated"
    #         theme_bg_color: "Custom"
    #         theme_width: "Custom"
    #         width: "140dp"
    #         md_bg_color: "#062D3E"
    #         pos_hint: {"x": 0.315, "y": 0.1575}
    #         on_release:
    #             app.login()

    #         MDButtonText:
    #             text: "login"
    #             pos_hint: {"center_x": .5, "center_y": .5}
    #             font_style: "semi_bold"
    #             role: "small"
    #             theme_text_color: "Custom"
    #             text_color: "#FFF9E6"
    
    # MDScreen:
    #     name: "Menu"
    #     md_bg_color: "#CDE2FF"

    #     MDLabel:
    #         text: "Good Morning!"
    #         font_style: "bold"
    #         text_color: "#062D3E"
    #         role: "large"
    #         adaptive_size: True
    #         pos_hint: {"center_x": 0.5, "y": 0.7}

    #     MDBoxLayout:
    #         orientation: "vertical"
    #         pos_hint: {"center_x": 0.5, "center_y": 0.47}
    #         spacing: "15dp"
    #         size_hint: 0.35, 0.4

    #         MDButton:
    #             style: "tonal"
    #             theme_bg_color: "Custom"
    #             md_bg_color: "#FFF9E6"
    #             height: "58dp"
    #             theme_width: "Custom"
    #             size_hint_x: 1
    #             radius: 18.75, 18.75, 18.75, 18.75
    #             pos_hint: {"center_x": 0.5, "center_y": 0.5}
    #             on_release: root.current = "OwnerInformation"
                
    #             MDButtonText:
    #                 text: "New Appointment"
    #                 font_style: "semi_bold"
    #                 role: "medium"
    #                 theme_text_color: "Custom"
    #                 text_color: "#062D3E"
    #                 pos_hint: {"center_x": .5, "center_y": .5}

    #         MDButton:
    #             style: "tonal"
    #             theme_bg_color: "Custom"
    #             md_bg_color: "#FFF9E6"
    #             height: "58dp"
    #             theme_width: "Custom"
    #             size_hint_x: 1
    #             radius: 18.75, 18.75, 18.75, 18.75
    #             pos_hint: {"center_x": 0.5, "center_y": 0.5}
    #             # on_release: root.current = "OwnerInformation"
                
    #             MDButtonText:
    #                 text: "View Appointment"
    #                 pos_hint: {"center_x": .5, "center_y": .5}
    #                 font_style: "semi_bold"
    #                 role: "medium"
    #                 theme_text_color: "Custom"
    #                 text_color: "#062D3E"
            
    #         MDButton:
    #             style: "tonal"
    #             theme_bg_color: "Custom"
    #             md_bg_color: "#FFF9E6"
    #             height: "58dp"
    #             theme_width: "Custom"
    #             size_hint_x: 1
    #             radius: 18.75, 18.75, 18.75, 18.75
    #             pos_hint: {"center_x": 0.5, "center_y": 0.5}
    #             # on_release: root.current = "OwnerInformation"
                
    #             MDButtonText:
    #                 text: "Cancel Appointment"
    #                 pos_hint: {"center_x": .5, "center_y": .5}
    #                 font_style: "semi_bold"
    #                 role: "medium"
    #                 theme_text_color: "Custom"
    #                 text_color: "#062D3E"
            
    #         MDButton:
    #             style: "tonal"
    #             theme_bg_color: "Custom"
    #             md_bg_color: "#FFF9E6"
    #             height: "58dp"
    #             theme_width: "Custom"
    #             size_hint_x: 1
    #             radius: 18.75, 18.75, 18.75, 18.75
    #             pos_hint: {"center_x": 0.5, "center_y": 0.5}
    #             on_release: root.current = "PrintBillInformation"
                
    #             MDButtonText:
    #                 text: "Print Bill"
    #                 pos_hint: {"center_x": .5, "center_y": .5}
    #                 font_style: "semi_bold"
    #                 role: "medium"
    #                 theme_text_color: "Custom"
    #                 text_color: "#062D3E"
            
    #     MDButton:
    #         style: "elevated"
    #         theme_bg_color: "Custom"
    #         theme_width: "Custom"
    #         width: "140dp"
    #         md_bg_color: "#062D3E"
    #         pos_hint: {"x": 0.85, "y": 0.07}
    #         on_release:
    #             app.clear_text_field()
    #             root.current = "LoginInterface"

    #         MDButtonText:
    #             text: "logout"
    #             pos_hint: {"center_x": .5, "center_y": .5}
    #             font_style: "semi_bold"
    #             role: "small"
    #             theme_text_color: "Custom"
    #             text_color: "#FFF9E6"
                
    #     MDAnchorLayout:
    #         anchor_x: "left"
    #         anchor_y: "top"

    #         MDBoxLayout:
    #             orientation: "vertical"
    #             size_hint: 0.4, 0.1125
    #             padding: "18dp"
    #             spacing: "8dp"

    #             MDLabel:
    #                 text: "Hello, Nurse!"
    #                 font_style: "semi_bold"
    #                 text_color: "#062D3E"
    #                 role: "small"
                        
    #             MDLabel:
    #                 id: nurse_name
    #                 text: ""
    #                 font_style: "regular"
    #                 text_color: "#062D3E"
    #                 role: "small"
        
    # MDScreen:
    #     name: "OwnerInformation"
    #     md_bg_color: "#CDE2FF"

    #     MDLabel:
    #         text: "New Appointment"
    #         font_style: "bold"
    #         text_color: "#062D3E"
    #         role: "large"
    #         adaptive_size: True
    #         pos_hint: {"x": 0.075, "y": 0.75}
        
    #     MDBoxLayout:
    #         orientation: "vertical"
    #         md_bg_color: "#FFF9E6"
    #         radius: 25, 25, 25, 25
    #         padding: "35dp"
    #         spacing: "5dp"
    #         size_hint: 0.85, 0.58
    #         pos_hint: {"center_x": 0.5, "y": 0.125}

    #         MDLabel:
    #             text: "owner information"
    #             font_style: "bold"
    #             role: "medium"
    #             text_color: "#062D3E"
    #             adaptive_size: True

    #         MDBoxLayout:
    #             orientation: "vertical"

    #             MDLabel:
    #                 text: "name"
    #                 size_hint: 1, 0.35
    #                 font_style: "light"
    #                 role: "small"
    #                 text_color: "#062D3E"

    #             MDTextField:
    #                 id: owner_field
    #                 style: "outlined"
    #                 radius: 8, 8, 8, 8

    #             MDLabel:
    #                 text: ""
    #                 size_hint: 1, 0.05

    #             MDLabel:
    #                 text: "phone number"
    #                 size_hint: 1, 0.35
    #                 font_style: "light"
    #                 role: "small"
    #                 text_color: "#062D3E"
                    
    #             MDTextField:
    #                 id: phone_field
    #                 style: "outlined"
    #                 radius: 8, 8, 8, 8

    #             MDLabel:
    #                 text: ""
    #                 size_hint: 1, 0.25

    #             MDButton:
    #                 id: button_next
    #                 style: "elevated"
    #                 theme_bg_color: "Custom"
    #                 theme_width: "Custom"
    #                 width: "140dp"
    #                 md_bg_color: "#062D3E"
    #                 pos_hint: {"x": 0.83}
    #                 on_release:
    #                     root.current = "PetInformation"

    #                 MDButtonText:
    #                     text: "next"
    #                     pos_hint: {"center_x": .5, "center_y": .5}
    #                     font_style: "semi_bold"
    #                     role: "small"
    #                     theme_text_color: "Custom"
    #                     text_color: "#CDE2FF"
    
    # MDScreen:
    #     name: "PetInformation"
    #     md_bg_color: "#CDE2FF"

    #     MDLabel:
    #         text: "New Appointment"
    #         font_style: "bold"
    #         text_color: "#062D3E"
    #         role: "large"
    #         adaptive_size: True
    #         pos_hint: {"x": 0.075, "y": 0.77}

    #     MDBoxLayout:
    #         orientation: "vertical"
    #         md_bg_color: "#FFF9E6"
    #         radius: 25, 25, 25, 25
    #         padding: "35dp"
    #         spacing: "25dp"
    #         size_hint: 0.85, 0.65
    #         pos_hint: {"center_x": 0.5, "y": 0.078}

    #         MDLabel:
    #             text: "pet information"
    #             font_style: "bold"
    #             role: "medium"
    #             text_color: "#062D3E"
    #             adaptive_size: True
        
    #         MDGridLayout:
    #             cols: 2
    #             row: 6
    #             spacing: "32dp", "22.5dp"

    #             MDLabel:
    #                 text: "name"
    #                 font_style: "light"
    #                 role: "small"
    #                 text_color: "#062D3E"
                    
    #             MDLabel:
    #                 text: "age"
    #                 font_style: "light"
    #                 role: "small"
    #                 text_color: "#062D3E"
                    
    #             MDTextField:
    #                 id: petname_field
    #                 mode: "outlined"
    #                 radius: 8, 8, 8, 8

    #             MDTextField:
    #                 id: age_field
    #                 mode: "outlined"
    #                 radius: 8, 8, 8, 8
                    
    #             MDLabel:
    #                 text: "breed"
    #                 font_style: "light"
    #                 role: "small"
    #                 text_color: "#062D3E"
                
    #             MDLabel:
    #                 text: "sex"
    #                 font_style: "light"
    #                 role: "small"
    #                 text_color: "#062D3E"

    #             MDTextField:
    #                 id: breed_field
    #                 mode: "outlined"
    #                 radius: 8, 8, 8, 8

    #             MDFloatLayout:

    #                 MDLabel:
    #                     text: "male"
    #                     font_style: "light"
    #                     role: "small"
    #                     text_color: "#062D3E"
    #                     pos_hint: {'center_x': 0.575, 'center_y': .5}
                    
    #                 MDCheckbox:
    #                     id: male_field
    #                     size_hint: None, None
    #                     size: dp(20), dp(20)
    #                     pos_hint: {'center_x': 0.025, 'center_y': .5}
    #                     active: False
    #                     on_active: app.on_checkbox_active("Male" if self.active else "")

    #                 MDLabel:
    #                     text: "female"
    #                     font_style: "light"
    #                     role: "small"
    #                     text_color: "#062D3E"
    #                     pos_hint: {'center_x': 0.9, 'center_y': .5}

    #                 MDCheckbox:
    #                     id: female_field
    #                     size_hint: None, None
    #                     size: dp(20), dp(20)
    #                     pos_hint: {'center_x': 0.35, 'center_y': .5}
    #                     active: False
    #                     on_active: app.on_checkbox_active("Female" if self.active else "")

    #             MDLabel:
    #                 text: "weight"
    #                 font_style: "light"
    #                 role: "small"
    #                 text_color: "#062D3E"

    #             MDLabel:
    #                 text: "spayed/neutered"
    #                 font_style: "light"
    #                 role: "small"
    #                 text_color: "#062D3E"

    #             MDTextField:
    #                 id: weight_field
    #                 mode: "outlined"
    #                 radius: 8, 8, 8, 8

    #             MDFloatLayout:

    #                 MDLabel:
    #                     text: "yes"
    #                     font_style: "light"
    #                     role: "small"
    #                     text_color: "#062D3E"
    #                     pos_hint: {'center_x': 0.575, 'center_y': .5}

    #                 MDCheckbox:
    #                     id: spayed_field
    #                     size_hint: None, None
    #                     size: dp(20), dp(20)
    #                     pos_hint: {'center_x': 0.025, 'center_y': .5}
    #                     active: False
    #                     on_active: app.on_checkbox_active2("Yes" if self.active else "")

    #                 MDLabel:
    #                     id: no_spayed_field
    #                     text: "no"
    #                     font_style: "light"
    #                     role: "small"
    #                     text_color: "#062D3E"
    #                     pos_hint: {'center_x': 0.9, 'center_y': .5}

    #                 MDCheckbox:
    #                     size_hint: None, None
    #                     size: dp(20), dp(20)
    #                     pos_hint: {'center_x': 0.35, 'center_y': .5}
    #                     on_active: app.on_checkbox_active2("No" if self.active else "")

    #         MDLabel:
    #             text: ""
    #             size_hint: 1, 0.4

    #     MDButton:
    #         style: "elevated"
    #         theme_bg_color: "Custom"
    #         theme_width: "Custom"
    #         width: "140dp"
    #         md_bg_color: "#062D3E"
    #         pos_hint: {"x": 0.785, "y": 0.115}
    #         on_release:
    #             root.current = "MedTreatmentInformation"

    #         MDButtonText:
    #             text: "next"
    #             pos_hint: {"center_x": .5, "center_y": .5}
    #             font_style: "semi_bold"
    #             role: "small"
    #             theme_text_color: "Custom"
    #             text_color: "#CDE2FF"
        
    #     MDButton:
    #         style: "elevated"
    #         theme_bg_color: "Custom"
    #         theme_width: "Custom"
    #         width: "140dp"
    #         md_bg_color: "#062D3E"
    #         pos_hint: {"x": 0.675, "y": 0.115}
    #         on_release: root.current = "OwnerInformation"

    #         MDButtonText:
    #             text: "back"
    #             pos_hint: {"center_x": .5, "center_y": .5}
    #             font_style: "semi_bold"
    #             role: "small"
    #             theme_text_color: "Custom"
    #             text_color: "#CDE2FF"

    # MDScreen:
    #     name: "MedTreatmentInformation"
    #     md_bg_color: "#CDE2FF"
      
    #     MDLabel:
    #         text: "New Appointment"
    #         font_style: "bold"
    #         text_color: "#062D3E"
    #         role: "large"
    #         adaptive_size: True
    #         pos_hint: {"x": 0.2, "y": 0.75}
        
    #     MDGridLayout:
    #         cols: 2
    #         row: 2
    #         radius: 25, 25, 25, 25
    #         padding: "35dp"
    #         spacing: "35dp"
    #         size_hint: 0.6, 0.55
    #         md_bg_color: "#FFF9E6"
    #         pos_hint: {"center_x": 0.5, "y": 0.15}

    #         MDLabel:
    #             text: "select treatment"
    #             font_style: "bold"
    #             role: "medium"
    #             text_color: "#062D3E"
    #             size_hint: 0.5, 0.05

    #         MDLabel:
    #             text: "date & time"
    #             font_style: "bold"
    #             role: "medium"
    #             text_color: "#062D3E"
    #             size_hint: 0.5, 0.05
            
    #         MDBoxLayout:
    #             orientation: "vertical"
    #             spacing: "20dp"
    #             size_hint: 0.5, 0.95

    #             MDButton:
    #                 id: menu_button
    #                 style: "tonal"
    #                 theme_bg_color: "Custom"
    #                 md_bg_color: "#F4E8D9"
    #                 height: "50dp"
    #                 theme_width: "Custom"
    #                 size_hint_x: 1
    #                 on_release: app.menu_open()

    #                 MDButtonText:
    #                     text: "select treatment"
    #                     font_style: "regular"
    #                     role: "medium"
    #                     text_color: "#062D3E"
    #                     pos_hint: {"center_x": .45, "center_y": .5}

    #                 MDButtonIcon:
    #                     pos_hint: {"center_x": .9, "center_y": .5}
    #                     icon: "triangle-down"
    #                     size_hint: 0.5, 0.5
    #                     md_bg_color: "#062D3E"
                    
    #             MDRelativeLayout:
    #                 md_bg_color: "#F4E8D9"
    #                 size_hint: 1, 0.7
    #                 radius: 25, 25, 25, 25

    #                 MDLabel:
    #                     text: "treatment : "
    #                     font_style: "semi_bold"
    #                     role: "medium"
    #                     text_color: "#062D3E"
    #                     size_hint: 1, 0.2
    #                     pos_hint: {"x": 0.075, "y": 0.65}

    #                 MDLabel:
    #                     id: selected_item_label
    #                     text: ""
    #                     font_style: "regular"
    #                     role: "large"
    #                     text_color: "#062D3E"
    #                     radius: 20, 20, 20, 20
    #                     size_hint: 1, 0.8
    #                     pos_hint: {"x": 0.075, "y": 0.005}  # Adjust position as needed
                    
    #             MDRelativeLayout:
    #                 md_bg_color: "#FFF9E6"
    #                 size_hint: 1, 0.2
    #                 radius: 25, 25, 25, 25

    #         MDBoxLayout:
    #             orientation: "vertical"
    #             size_hint: 0.5, 0.95
    #             spacing: "20dp"

    #             MDButton:
    #                 style: "tonal"
    #                 theme_bg_color: "Custom"
    #                 md_bg_color: "#F4E8D9"
    #                 height: "50dp"
    #                 theme_width: "Custom"
    #                 size_hint_x: 1
    #                 on_release: app.show_date_picker()
            
    #                 MDButtonText:
    #                     id: text
    #                     text: "appointment date"
    #                     font_style: "regular"
    #                     role: "medium"
    #                     text_color: "#062D3E"
    #                     pos_hint: {'center_x': .45, 'center_y': .5}

    #                 MDButtonIcon:
    #                     pos_hint: {"center_x": .9, "center_y": .5}
    #                     icon: "calendar"
    #                     size_hint: 0.5, 0.5
    #                     md_bg_color: "#062D3E"
                
    #             MDRelativeLayout:
    #                 md_bg_color: "#F4E8D9"
    #                 size_hint: 1, 0.7
    #                 radius: 25, 25, 25, 25

    #                 MDLabel:
    #                     text: "date : "
    #                     font_style: "semi_bold"
    #                     role: "medium"
    #                     text_color: "#062D3E"
    #                     size_hint: 1, 0.2
    #                     pos_hint: {"x": 0.075, "y": 0.65}

    #                 MDLabel:
    #                     id: selected_date_label
    #                     text: ""
    #                     font_style: "regular"
    #                     role: "large"
    #                     text_color: "#062D3E"
    #                     radius: 20, 20, 20, 20
    #                     size_hint: 1, 0.8
    #                     pos_hint: {"x": 0.075, "y": 0.005}  # Adjust position as needed
                    
    #             MDRelativeLayout:
    #                 md_bg_color: "#FFF9E6"
    #                 size_hint: 1, 0.2
    #                 radius: 25, 25, 25, 25
        
    #     MDButton:
    #         style: "elevated"
    #         theme_bg_color: "Custom"
    #         theme_width: "Custom"
    #         width: "140dp"
    #         md_bg_color: "#062D3E"
    #         pos_hint: {"x": 0.65, "y": 0.19}
    #         on_release:
    #             app.upload_data()
    #             root.current = "Menu"

    #         MDButtonText:
    #             text: "save"
    #             pos_hint: {"center_x": .5, "center_y": .5}
    #             font_style: "semi_bold"
    #             role: "small"
    #             theme_text_color: "Custom"
    #             text_color: "#CDE2FF"

    #     MDButton:
    #         style: "elevated"
    #         theme_bg_color: "Custom"
    #         theme_width: "Custom"
    #         width: "140dp"
    #         md_bg_color: "#062D3E"
    #         pos_hint: {"x": 0.525, "y": 0.19}
    #         on_release: root.current = "PetInformation"
                
    #         MDButtonText:
    #             text: "back"
    #             pos_hint: {"center_x": .5, "center_y": .5}
    #             font_style: "semi_bold"
    #             role: "small"
    #             theme_text_color: "Custom"
    #             text_color: "#CDE2FF"

    # MDScreen:
    #     name: "PrintBillInformation"
    #     md_bg_color: "#CDE2FF"

    #     MDLabel:
    #         text: "Print Bill"
    #         font_style: "bold"
    #         text_color: "#062D3E"
    #         role: "large"
    #         adaptive_size: True
    #         pos_hint: {"x": 0.2, "y": 0.84}
        
    #     MDBoxLayout:
    #         orientation: "vertical"
    #         md_bg_color: "#FFF9E6"
    #         radius: 25, 25, 25, 25
    #         padding: "20dp"
    #         spacing: "20dp"
    #         size_hint: 0.6, 0.2
    #         pos_hint: {"center_x": 0.5, "y": 0.615}

    #         MDLabel:
    #             text: "find appt"
    #             font_style: "bold"
    #             role: "medium"
    #             text_color: "#062D3E"
    #             pos_hint: {"center_x": 0.5, "y": 0.5}

    #         MDTextField:
    #             id: search_field
    #             style: "outlined"
    #             font_style: "Title"
    #             role: "medium"
    #             radius: 12.5, 12.5, 12.5, 12.5
    #             pos_hint: {"center_x": 0.5, "y": 0.5}
    #             on_text: app.filter_menu(self.text)
    #             on_focus: if self.focus: app.find_appt()

    #             MDTextFieldLeadingIcon:
    #                 icon: "magnify"
    #                 pos_hint: {"x": 0.1}

            
    #     MDBoxLayout:
    #         orientation: "vertical"
    #         md_bg_color: "#FFF9E6"
    #         radius: 25, 25, 25, 25
    #         padding: "30dp"
    #         spacing: "5dp"
    #         size_hint: 0.6, 0.525
    #         pos_hint: {"center_x": 0.5, "y": 0.07}

    #         MDBoxLayout:
    #             orientation: "vertical"
    #             size_hint: 1, 0.2
    #             MDLabel:
    #                 id: owner_name
    #                 text: "Nothing is selected!"
    #                 font_style: "bold"
    #                 role: "medium"
    #                 text_color: "#062D3E"
    #                 pos_hint: {"x": 0.025}

    #         MDBoxLayout:
    #             orientation: "vertical"
    #             size_hint: 1, 0.8

    #             MDLabel:
    #                 id: pet_name
    #                 text: ""
    #                 font_style: "regular"
    #                 role: "medium"
    #                 text_color: "#062D3E"
    #                 pos_hint: {"x": 0.025}

    #             MDLabel:
    #                 id: breed_name
    #                 text: ""
    #                 font_style: "regular"
    #                 role: "medium"
    #                 text_color: "#062D3E"
    #                 pos_hint: {"x": 0.025}

    #             MDLabel:
    #                 id: date_name
    #                 text: ""
    #                 font_style: "regular"
    #                 role: "medium"
    #                 text_color: "#062D3E"
    #                 pos_hint: {"x": 0.025}

    #             MDLabel:
    #                 id: treat_name
    #                 text: ""
    #                 font_style: "regular"
    #                 role: "medium"
    #                 text_color: "#062D3E"
    #                 pos_hint: {"x": 0.025}

    #             MDLabel:
    #                 id: price_name
    #                 text: ""
    #                 font_style: "regular"
    #                 role: "medium"
    #                 text_color: "#062D3E"
    #                 pos_hint: {"x": 0.025}
        
    #     MDButton:
    #         style: "elevated"
    #         theme_bg_color: "Custom"
    #         theme_width: "Custom"
    #         width: "140dp"
    #         md_bg_color: "#062D3E"
    #         pos_hint: {"x": 0.667, "y": 0.125}
    #         on_release:
    #             root.current = "Menu"

    #         MDButtonText:
    #             text: "print"
    #             pos_hint: {"center_x": .5, "center_y": .5}
    #             font_style: "semi_bold"
    #             role: "small"
    #             theme_text_color: "Custom"
    #             text_color: "#CDE2FF"

    #     MDButton:
    #         style: "elevated"
    #         theme_bg_color: "Custom"
    #         theme_width: "Custom"
    #         width: "140dp"
    #         md_bg_color: "#062D3E"
    #         pos_hint: {"x": 0.23, "y": 0.125}
    #         on_release:
    #             root.current = "Menu"

    #         MDButtonText:
    #             text: "back"
    #             pos_hint: {"center_x": .5, "center_y": .5}
    #             font_style: "semi_bold"
    #             role: "small"
    #             theme_text_color: "Custom"
    #             text_color: "#CDE2FF"


    MDScreen:
        name: "CancelInformation"
        md_bg_color: "#CDE2FF"

        MDLabel:
            text: "Cancel Appointment"
            font_style: "bold"
            text_color: "#062D3E"
            role: "large"
            adaptive_size: True
            pos_hint: {"x": 0.2, "y": 0.84}
        
        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#FFF9E6"
            radius: 25, 25, 25, 25
            padding: "20dp"
            spacing: "20dp"
            size_hint: 0.6, 0.2
            pos_hint: {"center_x": 0.5, "y": 0.615}

            MDLabel:
                text: "find appt"
                font_style: "bold"
                role: "medium"
                text_color: "#062D3E"
                pos_hint: {"center_x": 0.5, "y": 0.5}

            MDTextField:
                id: search_cancel_field
                style: "outlined"
                font_style: "Title"
                role: "medium"
                radius: 12.5, 12.5, 12.5, 12.5
                pos_hint: {"center_x": 0.5, "y": 0.5}
                on_text: app.filter_cancel_menu(self.text)
                on_focus: if self.focus: app.find_cancel_appt()

                MDTextFieldLeadingIcon:
                    icon: "magnify"
                    pos_hint: {"x": 0.1}

            
        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#FFF9E6"
            radius: 25, 25, 25, 25
            padding: "30dp"
            spacing: "5dp"
            size_hint: 0.6, 0.525
            pos_hint: {"center_x": 0.5, "y": 0.07}

            MDBoxLayout:
                orientation: "vertical"
                size_hint: 1, 0.2
                MDLabel:
                    id: owner_name
                    text: "Nothing is selected!"
                    font_style: "bold"
                    role: "medium"
                    text_color: "#062D3E"
                    pos_hint: {"x": 0.025}

            MDBoxLayout:
                orientation: "vertical"
                size_hint: 1, 0.8

                MDLabel:
                    id: pet_name
                    text: ""
                    font_style: "regular"
                    role: "medium"
                    text_color: "#062D3E"
                    pos_hint: {"x": 0.025}

                MDLabel:
                    id: breed_name
                    text: ""
                    font_style: "regular"
                    role: "medium"
                    text_color: "#062D3E"
                    pos_hint: {"x": 0.025}

                MDLabel:
                    id: date_name
                    text: ""
                    font_style: "regular"
                    role: "medium"
                    text_color: "#062D3E"
                    pos_hint: {"x": 0.025}

                MDLabel:
                    id: treat_name
                    text: ""
                    font_style: "regular"
                    role: "medium"
                    text_color: "#062D3E"
                    pos_hint: {"x": 0.025}

                MDLabel:
                    id: price_name
                    text: ""
                    font_style: "regular"
                    role: "medium"
                    text_color: "#062D3E"
                    pos_hint: {"x": 0.025}
        
        MDButton:
            style: "elevated"
            theme_bg_color: "Custom"
            theme_width: "Custom"
            width: "140dp"
            md_bg_color: "#062D3E"
            pos_hint: {"x": 0.667, "y": 0.125}
            on_release:
                app.cancel_appt()

            MDButtonText:
                text: "cancel"
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
            pos_hint: {"x": 0.23, "y": 0.125}
            on_release:
                root.current = "Menu"

            MDButtonText:
                text: "back"
                pos_hint: {"center_x": .5, "center_y": .5}
                font_style: "semi_bold"
                role: "small"
                theme_text_color: "Custom"
                text_color: "#CDE2FF"
        



'''


class MyScreenManager(MDScreenManager):
    pass

class Example(MDApp):
    # Membuat Drop Down Menu
    def menu_open(self):
        treatments = self.extract_medical_treatments("Pet-Clinic-Kelompok-19/price.csv")
        menu_items = [
            {
                "text": treatment,
                "on_release": lambda x=treatment: self.menu_callback(x),
            } for treatment in treatments
        ]
        MDDropdownMenu(
            caller=self.root.ids.menu_button,
            items=menu_items,
            position="bottom",
            width=dp(500),
            ver_growth="down",
            radius=[5, 5, 5, 5]
        ).open()

    # Membaca Data untuk Menu Drop Down (Data Treatment yang Ada)
    def extract_medical_treatments(self, csv_file):
        treatments = []
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                treatment = row[0]
                treatments.append(treatment)
        return treatments

    # Menampilkan Treatment yang dipilih
    def menu_callback(self, text_item):
        self.root.ids.selected_item_label.text = f"{text_item}"
    
    # Tombol edit pada kalendar
    def show_modal_input_date_picker(self, *args):
        def on_edit(*args):
            date_dialog.dismiss()
            Clock.schedule_once(self.show_modal_date_picker, 0.2)

        date_dialog = MDModalInputDatePicker()
        date_dialog.bind(on_edit=on_edit)
        date_dialog.open()

    # Event On_edit pada kalendar
    def on_edit(self, instance_date_picker):
        instance_date_picker.dismiss()
        Clock.schedule_once(self.show_modal_input_date_picker, 0.2)
    
    # Tombol OK
    def on_ok(self, instance_date_picker):
        global date
        date = instance_date_picker.get_date()[0]
        self.root.ids.selected_date_label.text = f"{date}"
        instance_date_picker.dismiss()
    
    #Tombol Cancel
    def on_cancel(self, instance_date_picker):
        instance_date_picker.dismiss()

    #Menampilkan Kalendar
    def show_date_picker(self):
        date_dialog = MDModalDatePicker()
        date_dialog.bind(on_edit=self.on_edit)
        date_dialog.bind(on_ok=self.on_ok)
        date_dialog.open()
        date_dialog.bind(on_cancel=self.on_cancel)

    #Login
    def login(self):
        id_name = self.root.ids.id_field.text
        password = self.root.ids.password_field.text
        
        #Membaca Database Pengguna
        file_path = "Pet-Clinic-Kelompok-19/database_login.csv"
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['ID Name'] == id_name and row['Password'] == password:
                    #Berhasil Login
                    self.root.current = "Menu"
                    self.root.ids.nurse_name.text = f"Ns. {id_name}"
                    return
                
        #Gagal Login
        MDSnackbar(
            MDSnackbarText(
                text="Incorrect ID Name or Password",
                ),
                y=dp(24),
                pos_hint={"x" : 0.025},
                size_hint_x=0.4).open()
        
    #Menghapus Input pada TextField
    def clear_text_field(self):
        self.root.ids.id_field.text = f""
        self.root.ids.password_field.text = f""

    #Mengambil Input dari Checkbox Male/Female
    def on_checkbox_active(self, value):
        global male
        male = value
        return male
    
    #Mengambil Input dari Checkbox Spayed/Neuteur
    def on_checkbox_active2(self, value):
        global spayed
        spayed = value
        return spayed

    #Menyimpan Data Appt ke Database
    def upload_data(self):
        appt = str(self.root.ids.owner_field.text)
        patient = str(self.root.ids.petname_field.text)
        weight = str(self.root.ids.weight_field.text)
        breed = str(self.root.ids.breed_field.text)
        age = str(self.root.ids.age_field.text)
        medtreat = str(self.root.ids.selected_item_label.text)

        with open("Pet-Clinic-Kelompok-19/data_appt.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([appt, patient, weight, male, breed, age, spayed, medtreat, date])

    # Filter buat Print
    def filter_menu(self, search_text):
        filtered_items = [item for item in all_appt_items if search_text.lower() in item['text'].lower()]
        menu_bill.items = filtered_items
        if search_text == '':
            menu_bill.items = all_appt_items

    def set_item(self, appt_item):
        self.root.ids.search_field.text = appt_item
        menu_bill.dismiss()
        with open("Pet-Clinic-Kelompok-19/data_appt.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Appt'] == appt_item:
                    self.root.ids.owner_name.text   = f"Appt {appt_item}"
                    self.root.ids.pet_name.text     = f"Pet Name            : {row['Patient']}"
                    self.root.ids.breed_name.text   = f"Breed               : {row['Breed']}"
                    self.root.ids.date_name.text    = f"Appt Date           : {row['Date']}"
                    self.root.ids.treat_name.text   = f"Medical Treatment   : {row['Medical Treatment']}"

                with open("Pet-Clinic-Kelompok-19/price.csv", 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    obat = self.root.ids.treat_name.text
                    for row in reader:
                        if row['Medical Treatment'] == obat:
                            self.root.ids.price_name.text = f"Price : {row['Price']}"
                            return

    def extract_appt(self, csv_file):
        allappt = []
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                appt = row[0]
                allappt.append(appt)
        return allappt

    def find_appt(self):
        allappt = self.extract_appt("Pet-Clinic-Kelompok-19/data_appt.csv")
        global all_appt_items
        all_appt_items = [
            {
                "text": appt,
                "on_release": {lambda x=appt: self.set_item(x)}
            } for appt in allappt
        ]
        global menu_bill
        menu_bill = MDDropdownMenu(
            caller=self.root.ids.search_field,
            items=all_appt_items,
            position="bottom",
        )
        menu_bill.open()

    # Cancel
    def filter_cancel_menu(self, search_text):
        filtered_items = [item for item in all_appt_items if search_text.lower() in item['text'].lower()]
        menu_cancel.items = filtered_items
        if search_text == '':
            menu_cancel.items = all_appt_items

    def find_cancel_appt(self):
        allappt = self.extract_appt("Pet-Clinic-Kelompok-19/data_appt.csv")
        global all_appt_items
        all_appt_items = [
            {
                "text": appt,
                "on_release": lambda x=appt: self.display_cancel_appt(x)
            } for appt in allappt
        ]
        global menu_cancel
        menu_cancel = MDDropdownMenu(
            caller=self.root.ids.search_cancel_field,
            items=all_appt_items,
            position="bottom",
        )
        menu_cancel.open()
    
    def display_cancel_appt(self, appt_item):
        self.root.ids.search_cancel_field.text = appt_item
        menu_cancel.dismiss()

        with open("Pet-Clinic-Kelompok-19/data_appt.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Appt'] == appt_item:
                    self.root.ids.owner_name.text   = f"Appt {appt_item}"
                    self.root.ids.pet_name.text     = f"Pet Name            : {row['Patient']}"
                    self.root.ids.breed_name.text   = f"Breed               : {row['Breed']}"
                    self.root.ids.date_name.text    = f"Appt Date           : {row['Date']}"
                    self.root.ids.treat_name.text   = f"Medical Treatment   : {row['Medical Treatment']}"
                    global nama_appt_cancel
                    nama_appt_cancel = self.root.ids.owner_name.text

                with open("Pet-Clinic-Kelompok-19/price.csv", 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    obat = self.root.ids.treat_name.text
                    for row in reader:
                        if row['Medical Treatment'] == obat:
                            self.root.ids.price_name.text = f"Price : {row['Price']}"
                            return

    def cancel_appt(nama_appt_cancel):
        filtered_rows = []
        with open("Pet-Clinic-Kelompok-19/data_appt.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            for row in reader:
                if row['Appt'] != nama_appt_cancel:
                    filtered_rows.append(row)
        
        with open("Pet-Clinic-Kelompok-19/data_appt.csv", 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_rows)
            print("Berhasil")

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
                "font-size": sp(26),
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
                "font-size": sp(26),
            },
            "medium": {
                "line-height": 1,
                "font-name": "regular",
                "font-size": sp(20),
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