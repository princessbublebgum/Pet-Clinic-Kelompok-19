from kivy.lang import Builder
import webbrowser
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.config import Config
Config.set ("graphics", "resizable", False)
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.metrics import sp, dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDModalDatePicker, MDModalInputDatePicker
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivy.clock import Clock
from fpdf import FPDF
from kivy.utils import get_color_from_hex
from kivymd.uix.list import (
    MDListItem,
    MDListItemHeadlineText,
    MDListItemSupportingText,
)
import pandas as pd
import csv

Window.maximize()

KV = '''
<MyScreenManager>:
    MDScreen:
        name: "LoginInterface"
        FitImage:
            source: "image/BG_Login.png"

        MDLabel:
            text: "Pet Clinic Adm."
            font_style: "bold"
            text_color: "#062D3E"
            role: "large"
            adaptive_size: True
            pos_hint: {"x": 0.16, "y": 0.7825}
        
        MDBoxLayout:
            size_hint: 0.16, 0.16
            pos_hint: {"x": 0.025, "y": 0.755}
        
            Image:
                source: "image/logo.png"
        
        MDLabel:
            text: "Login"
            font_style: "bold"
            text_color: "#062D3E"
            role: "medium"
            adaptive_size: True
            pos_hint: {"x": 0.075, "y": 0.59}
                
        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#FFF9E6"
            radius: 25, 25, 25, 25
            padding: "35dp"
            spacing: "8dp"
            size_hint: 0.375, 0.45
            pos_hint: {"x": 0.075, "y": 0.115}

            MDLabel:
                text: "ID name"
                size_hint: 1, 0.35
                font_style: "light"
                role: "small"
                text_color: "#062D3E"

            MDLabel:
                text: ""
                size_hint: 1, 0.025

            MDTextField:
                id: id_field
                style: "outlined"
                font_style: "Title"
                role: "large"
                radius: 8, 8, 8, 8
            
            MDLabel:
                text: ""
                size_hint: 1, 0.025

            MDLabel:
                text: "password"
                size_hint: 1, 0.35
                font_style: "light"
                role: "small"
                text_color: "#062D3E"
            
            MDLabel:
                text: ""
                size_hint: 1, 0.025
                    
            MDTextField:
                id: password_field
                password: True
                style: "outlined"
                font_style: "Title"
                role: "large"
                radius: 8, 8, 8, 8

            MDLabel:
                text: ""
                size_hint: 1, 0.925

        MDButton:
            style: "elevated"
            theme_bg_color: "Custom"
            theme_width: "Custom"
            width: "140dp"
            md_bg_color: "#062D3E"
            pos_hint: {"x": 0.3215, "y": 0.1475}
            on_release:
                app.login()

            MDButtonText:
                text: "login"
                pos_hint: {"center_x": .5, "center_y": .5}
                font_style: "semi_bold"
                role: "small"
                theme_text_color: "Custom"
                text_color: "#FFF9E6"
    
    MDScreen:
        name: "Menu"
        md_bg_color: "#CDE2FF"

        MDLabel:
            text: "Hello!"
            font_style: "bold"
            text_color: "#062D3E"
            role: "large"
            adaptive_size: True
            pos_hint: {"x": 0.4, "y": 0.7}
        
        Image:
            source: "image/pawprint2.png"
            size_hint: 0.15, 0.15
            pos_hint: {"x": 0.525, "y": 0.6875}

        MDBoxLayout:
            orientation: "vertical"
            pos_hint: {"center_x": 0.5, "center_y": 0.45}
            spacing: "12.5dp"
            size_hint: 0.35, 0.4

            MDButton:
                style: "tonal"
                theme_bg_color: "Custom"
                md_bg_color: "#FFF9E6"
                height: "60dp"
                theme_width: "Custom"
                size_hint_x: 1
                radius: 20, 20, 20, 20
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                on_release: root.current = "OwnerInformation"
                
                MDButtonText:
                    text: "New Appointment"
                    font_style: "semi_bold"
                    role: "medium"
                    theme_text_color: "Custom"
                    text_color: "#062D3E"
                    pos_hint: {"center_x": .5, "center_y": .5}

            MDButton:
                style: "tonal"
                theme_bg_color: "Custom"
                md_bg_color: "#FFF9E6"
                height: "60dp"
                theme_width: "Custom"
                size_hint_x: 1
                radius: 20, 20, 20, 20
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                on_release:
                    root.current = "ViewAllAppt"
                    # app.list_all()
                
                MDButtonText:
                    text: "View All Appointment"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_style: "semi_bold"
                    role: "medium"
                    theme_text_color: "Custom"
                    text_color: "#062D3E"
            
            MDButton:
                style: "tonal"
                theme_bg_color: "Custom"
                md_bg_color: "#FFF9E6"
                height: "60dp"
                theme_width: "Custom"
                size_hint_x: 1
                radius: 20, 20, 20, 20
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                on_release: root.current = "CancelInformation"
                
                MDButtonText:
                    text: "Cancel Appointment"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_style: "semi_bold"
                    role: "medium"
                    theme_text_color: "Custom"
                    text_color: "#062D3E"
            
            MDButton:
                style: "tonal"
                theme_bg_color: "Custom"
                md_bg_color: "#FFF9E6"
                height: "60dp"
                theme_width: "Custom"
                size_hint_x: 1
                radius: 20, 20, 20, 20
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                on_release: root.current = "PrintBillInformation"
                
                MDButtonText:
                    text: "Print Bill"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    font_style: "semi_bold"
                    role: "medium"
                    theme_text_color: "Custom"
                    text_color: "#062D3E"

        MDButton:
            style: "elevated"
            theme_bg_color: "Custom"
            theme_width: "Custom"
            width: "140dp"
            md_bg_color: "#062D3E"
            pos_hint: {"x": 0.85, "y": 0.0675}
            on_release:
                app.close_program()

            MDButtonText:
                text: "logout"
                pos_hint: {"center_x": .5, "center_y": .5}
                font_style: "semi_bold"
                role: "small"
                theme_text_color: "Custom"
                text_color: "#FFF9E6"
                
        MDAnchorLayout:
            anchor_x: "left"
            anchor_y: "top"

            MDBoxLayout:
                orientation: "vertical"
                size_hint: 0.4, 0.1125
                padding: "18dp"
                spacing: "20dp"

                MDLabel:
                    text: "Hello,"
                    font_style: "semi_bold"
                    text_color: "#062D3E"
                    role: "medium"
                        
                MDLabel:
                    id: nurse_name
                    text: ""
                    font_style: "regular"
                    text_color: "#062D3E"
                    role: "medium"
        FitImage:
            source: "image/BG_1.png"
        
    MDScreen:
        name: "OwnerInformation"
        md_bg_color: "#CDE2FF"

        MDLabel:
            text: "New Appointment"
            font_style: "bold"
            text_color: "#062D3E"
            role: "medium"
            adaptive_size: True
            pos_hint: {"x": 0.1975, "y": 0.75}
        
        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#FFF9E6"
            radius: 25, 25, 25, 25
            padding: "35dp"
            spacing: "5dp"
            size_hint: 0.6, 0.55
            pos_hint: {"center_x": 0.5, "y": 0.165}

            MDLabel:
                text: "owner information"
                font_style: "bold"
                role: "small"
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
                    id: owner_field
                    style: "outlined"
                    font_style: "Title"
                    role: "large"
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
                    id: phone_field
                    style: "outlined"
                    font_style: "Title"
                    role: "large"
                    radius: 8, 8, 8, 8

                MDLabel:
                    text: ""
                    size_hint: 1, 0.25

                MDButton:
                    id: button_next
                    style: "elevated"
                    theme_bg_color: "Custom"
                    theme_width: "Custom"
                    width: "140dp"
                    md_bg_color: "#062D3E"
                    pos_hint: {"x": 0.815}
                    on_release:
                        app.validate_owner_info()

                    MDButtonText:
                        text: "next"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        font_style: "semi_bold"
                        role: "small"
                        theme_text_color: "Custom"
                        text_color: "#CDE2FF"
                
        MDButton:
            id: button_back
            style: "elevated"
            theme_bg_color: "Custom"
            theme_width: "Custom"
            width: "140dp"
            md_bg_color: "#062D3E"
            pos_hint: {"x": 0.225, "y": 0.215}
            on_release:
                root.current = "Menu"

            MDButtonText:
                text: "back"
                pos_hint: {"center_x": .5, "center_y": .5}
                font_style: "semi_bold"
                role: "small"
                theme_text_color: "Custom"
                text_color: "#CDE2FF"
        
        FitImage:
            source: "image/BG_3.png"
    
    MDScreen:
        name: "PetInformation"
        md_bg_color: "#CDE2FF"

        MDLabel:
            text: "New Appointment"
            font_style: "bold"
            text_color: "#062D3E"
            role: "medium"
            adaptive_size: True
            pos_hint: {"x": 0.0715, "y": 0.8}

        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#FFF9E6"
            radius: 25, 25, 25, 25
            padding: "38dp"
            spacing: "27.5dp"
            size_hint: 0.86, 0.675
            pos_hint: {"center_x": 0.5, "y": 0.09}

            MDLabel:
                text: "pet information"
                font_style: "bold"
                role: "small"
                text_color: "#062D3E"
                adaptive_size: True
        
            MDGridLayout:
                cols: 2
                row: 8
                spacing: "38dp", "22.5dp"

                MDLabel:
                    text: "name"
                    font_style: "light"
                    role: "small"
                    text_color: "#062D3E"
                    
                MDLabel:
                    text: "age (in years old)"
                    font_style: "light"
                    role: "small"
                    text_color: "#062D3E"
                    
                MDTextField:
                    id: petname_field
                    font_style: "Title"
                    role: "large"
                    mode: "outlined"
                    radius: 8, 8, 8, 8

                MDTextField:
                    id: age_field
                    font_style: "Title"
                    role: "large"
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
                    id: breed_field
                    font_style: "Title"
                    role: "large"
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
                        id: male_field
                        size_hint: None, None
                        size: dp(20), dp(20)
                        pos_hint: {'center_x': 0.025, 'center_y': .5}
                        active: False
                        on_active: app.check_sex("Male" if self.active else "")

                    MDLabel:
                        text: "female"
                        font_style: "light"
                        role: "small"
                        text_color: "#062D3E"
                        pos_hint: {'center_x': 0.9, 'center_y': .5}

                    MDCheckbox:
                        id: female_field
                        size_hint: None, None
                        size: dp(20), dp(20)
                        pos_hint: {'center_x': 0.35, 'center_y': .5}
                        active: False
                        on_active: app.check_sex("Female" if self.active else "")

                MDLabel:
                    text: "weight (in kg)"
                    font_style: "light"
                    role: "small"
                    text_color: "#062D3E"

                MDLabel:
                    text: "spayed/neutered"
                    font_style: "light"
                    role: "small"
                    text_color: "#062D3E"

                MDTextField:
                    id: weight_field
                    font_style: "Title"
                    role: "large"
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
                        id: spayed_yes_field
                        size_hint: None, None
                        size: dp(20), dp(20)
                        pos_hint: {'center_x': 0.025, 'center_y': .5}
                        active: False
                        on_active: app.check_spay("Yes" if self.active else "")

                    MDLabel:
                        id: no_spayed_field
                        text: "no"
                        font_style: "light"
                        role: "small"
                        text_color: "#062D3E"
                        pos_hint: {'center_x': 0.9, 'center_y': .5}

                    MDCheckbox:
                        id: spayed_no_field
                        size_hint: None, None
                        size: dp(20), dp(20)
                        pos_hint: {'center_x': 0.35, 'center_y': .5}
                        on_active: app.check_spay("No" if self.active else "")

            MDLabel:
                text: ""
                size_hint: 1, 0.4

            MDLabel:
                text: ""
                size_hint: 1, 0.4

            MDLabel:
                text: ""
                size_hint: 1, 0.6
            
            MDLabel:
                text: ""
                size_hint: 1, 0.6

        MDButton:
            style: "elevated"
            theme_bg_color: "Custom"
            theme_width: "Custom"
            width: "140dp"
            md_bg_color: "#062D3E"
            pos_hint: {"x": 0.8, "y": 0.125}
            on_release:
                app.validate_pet_info()

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
            pos_hint: {"x": 0.096, "y": 0.125}
            on_release: root.current = "OwnerInformation"

            MDButtonText:
                text: "back"
                pos_hint: {"center_x": .5, "center_y": .5}
                font_style: "semi_bold"
                role: "small"
                theme_text_color: "Custom"
                text_color: "#CDE2FF"

    MDScreen:
        name: "MedTreatmentInformation"
        md_bg_color: "#CDE2FF"
      
        MDLabel:
            text: "New Appointment"
            font_style: "bold"
            text_color: "#062D3E"
            role: "medium"
            adaptive_size: True
            pos_hint: {"x": 0.2, "y": 0.75}
        
        MDGridLayout:
            cols: 2
            row: 2
            radius: 25, 25, 25, 25
            padding: "35dp"
            spacing: "35dp"
            size_hint: 0.6, 0.55
            md_bg_color: "#FFF9E6"
            pos_hint: {"center_x": 0.5, "y": 0.15}

            MDLabel:
                text: "treatment"
                font_style: "bold"
                role: "small"
                text_color: "#062D3E"
                size_hint: 0.5, 0.05

            MDLabel:
                text: "date"
                font_style: "bold"
                role: "small"
                text_color: "#062D3E"
                size_hint: 0.5, 0.05
            
            MDBoxLayout:
                orientation: "vertical"
                spacing: "20dp"
                size_hint: 0.5, 0.95

                MDButton:
                    id: menu_button
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: "#F4E8D9"
                    height: "50dp"
                    theme_width: "Custom"
                    size_hint_x: 1
                    on_release: app.menu_open()

                    MDButtonText:
                        text: "select treatment"
                        font_style: "regular"
                        role: "medium"
                        text_color: "#062D3E"
                        pos_hint: {"center_x": .45, "center_y": .5}

                    MDButtonIcon:
                        pos_hint: {"center_x": .9, "center_y": .5}
                        icon: "triangle-down"
                        size_hint: 0.5, 0.5
                        md_bg_color: "#062D3E"
                    
                MDRelativeLayout:
                    md_bg_color: "#F4E8D9"
                    size_hint: 1, 0.7
                    radius: 25, 25, 25, 25

                    MDLabel:
                        text: "treatment : "
                        font_style: "semi_bold"
                        role: "medium"
                        text_color: "#062D3E"
                        size_hint: 1, 0.2
                        pos_hint: {"x": 0.075, "y": 0.65}

                    MDLabel:
                        id: selected_item_label
                        text: ""
                        font_style: "regular"
                        role: "large"
                        text_color: "#062D3E"
                        radius: 20, 20, 20, 20
                        size_hint: 1, 0.8
                        pos_hint: {"x": 0.075, "y": 0.005}
                    
                MDRelativeLayout:
                    md_bg_color: "#FFF9E6"
                    size_hint: 1, 0.2
                    radius: 25, 25, 25, 25

            MDBoxLayout:
                orientation: "vertical"
                size_hint: 0.5, 0.95
                spacing: "20dp"

                MDButton:
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: "#F4E8D9"
                    height: "50dp"
                    theme_width: "Custom"
                    size_hint_x: 1
                    on_release: app.show_modal_date_picker()
            
                    MDButtonText:
                        id: text
                        text: "appointment date"
                        font_style: "regular"
                        role: "medium"
                        text_color: "#062D3E"
                        pos_hint: {'center_x': .45, 'center_y': .5}

                    MDButtonIcon:
                        pos_hint: {"center_x": .9, "center_y": .5}
                        icon: "calendar"
                        size_hint: 0.5, 0.5
                        md_bg_color: "#062D3E"
                
                MDRelativeLayout:
                    md_bg_color: "#F4E8D9"
                    size_hint: 1, 0.7
                    radius: 25, 25, 25, 25

                    MDLabel:
                        text: "date : "
                        font_style: "semi_bold"
                        role: "medium"
                        text_color: "#062D3E"
                        size_hint: 1, 0.2
                        pos_hint: {"x": 0.075, "y": 0.65}

                    MDLabel:
                        id: selected_date_label
                        text: ""
                        font_style: "regular"
                        role: "large"
                        text_color: "#062D3E"
                        radius: 20, 20, 20, 20
                        size_hint: 1, 0.8
                        pos_hint: {"x": 0.075, "y": 0.005}
                    
                MDRelativeLayout:
                    md_bg_color: "#FFF9E6"
                    size_hint: 1, 0.2
                    radius: 25, 25, 25, 25
        
        MDButton:
            style: "elevated"
            theme_bg_color: "Custom"
            theme_width: "Custom"
            width: "140dp"
            md_bg_color: "#062D3E"
            pos_hint: {"x": 0.66, "y": 0.19}
            on_release:
                app.validate_med_treat()

            MDButtonText:
                text: "save"
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
            pos_hint: {"x": 0.545, "y": 0.19}
            on_release: root.current = "PetInformation"
                
            MDButtonText:
                text: "back"
                pos_hint: {"center_x": .5, "center_y": .5}
                font_style: "semi_bold"
                role: "small"
                theme_text_color: "Custom"
                text_color: "#CDE2FF"
        
        FitImage:
            source: "image/BG_Pet.png"

    MDScreen:
        name: "PrintBillInformation"
        md_bg_color: "#CDE2FF"

        MDLabel:
            text: "Print Bill"
            font_style: "bold"
            text_color: "#062D3E"
            role: "medium"
            adaptive_size: True
            pos_hint: {"x": 0.2, "y": 0.8}
        
        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#FFF9E6"
            radius: 25, 25, 25, 25
            padding: "20dp"
            spacing: "20dp"
            size_hint: 0.6, 0.14
            pos_hint: {"center_x": 0.5, "y": 0.64}

            MDTextField:
                id: search_field
                style: "outlined"
                font_style: "Title"
                role: "large"
                radius: 12.5, 12.5, 12.5, 12.5
                adaptive_size: True
                on_text: app.filter_menu(self.text)
                on_focus: if self.focus: app.find_appt()

                MDTextFieldLeadingIcon:
                    icon: "magnify"
                    pos_hint: {"x": 0.1}

            
        MDBoxLayout:
            id: print_box
            orientation: "vertical"
            md_bg_color: "#FFF9E6"
            radius: 25, 25, 25, 25
            padding: "20dp"
            size_hint: 0.6, 0.525
            pos_hint: {"center_x": 0.5, "y": 0.1}

            MDBoxLayout:
                orientation: "vertical"
                size_hint: 1, 0.2
                MDLabel:
                    id: owner_print_name
                    text: "Nothing is selected!"
                    font_style: "bold"
                    role: "small"
                    text_color: "#062D3E"
                    pos_hint: {"x": 0.025}

            MDBoxLayout:
                orientation: "vertical"
                size_hint: 1, 0.8

                MDLabel:
                    id: pet_print_name
                    text: ""
                    font_style: "regular"
                    role: "medium"
                    text_color: "#062D3E"
                    pos_hint: {"x": 0.025}

                MDLabel:
                    id: breed_print_name
                    text: ""
                    font_style: "regular"
                    role: "medium"
                    text_color: "#062D3E"
                    pos_hint: {"x": 0.025}

                MDLabel:
                    id: date_print_name
                    text: ""
                    font_style: "regular"
                    role: "medium"
                    text_color: "#062D3E"
                    pos_hint: {"x": 0.025}

                MDLabel:
                    id: treat_print_name
                    text: ""
                    font_style: "regular"
                    role: "medium"
                    text_color: "#062D3E"
                    pos_hint: {"x": 0.025}

                MDLabel:
                    id: price_print_name
                    text: ""
                    font_style: "regular"
                    role: "medium"
                    text_color: "#062D3E"
                    pos_hint: {"x": 0.025}
                
                MDLabel:
                    text: ""
                    size_hint: 1, 0.95

                MDLabel:
                    text: ""
                    size_hint: 1, 0.95
        
        MDButton:
            style: "elevated"
            theme_bg_color: "Custom"
            theme_width: "Custom"
            width: "140dp"
            md_bg_color: "#062D3E"
            pos_hint: {"x": 0.67, "y": 0.14}
            on_release:
                app.print_bill()

            MDButtonText:
                text: "print"
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
            pos_hint: {"x": 0.227, "y": 0.14}
            on_release:
                root.current = "Menu"

            MDButtonText:
                text: "back"
                pos_hint: {"center_x": .5, "center_y": .5}
                font_style: "semi_bold"
                role: "small"
                theme_text_color: "Custom"
                text_color: "#CDE2FF"
        
        FitImage:
            source: "image/BG_2.png"
    
    MDScreen:
        name: "CancelInformation"
        md_bg_color: "#CDE2FF"

        MDLabel:
            text: "Cancel Appointment"
            font_style: "bold"
            text_color: "#062D3E"
            role: "medium"
            adaptive_size: True
            pos_hint: {"x": 0.2, "y": 0.76}
        
        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#FFF9E6"
            radius: 25, 25, 25, 25
            padding: "25dp"
            spacing: "20dp"
            size_hint: 0.6, 0.225
            pos_hint: {"center_x": 0.5, "y": 0.5}

            MDTextField:
                id: search_cancel_field
                style: "outlined"
                font_style: "Title"
                role: "large"
                radius: 12.5, 12.5, 12.5, 12.5
                on_text: app.filter_cancel_menu(self.text)
                on_focus: if self.focus: app.find_cancel_appt()

                MDTextFieldLeadingIcon:
                    icon: "magnify"
                    pos_hint: {"x": 0.1}
            
            MDLabel:
                text: ""
                size_hint: 1, 0.9

        MDButton:
            style: "elevated"
            theme_bg_color: "Custom"
            theme_width: "Custom"
            width: "140dp"
            md_bg_color: "#062D3E"
            pos_hint: {"x": 0.68, "y": 0.525}
            on_release:
                app.cancel_appt()
                app.clear_cancel_field()

            MDButtonText:
                text: "cancel"
                pos_hint: {"center_x": .5, "center_y": .5}
                font_style: "semi_bold"
                role: "small"
                theme_text_color: "Custom"
                text_color: "#FFF9E6"

        MDButton:
            style: "elevated"
            theme_bg_color: "Custom"
            theme_width: "Custom"
            width: "140dp"
            md_bg_color: "#062D3E"
            pos_hint: {"x": 0.216, "y": 0.525}
            on_release:
                root.current = "Menu"

            MDButtonText:
                text: "back"
                pos_hint: {"center_x": .5, "center_y": .5}
                font_style: "semi_bold"
                role: "small"
                theme_text_color: "Custom"
                text_color: "#FFF9E6"

        FitImage:
            source: "image/BG_Pet.png"
        
    MDScreen:
        name: "ViewAllAppt"
        md_bg_color: "#CDE2FF"
        on_enter: app.list_all()

        MDLabel:
            text: "All Appointment"
            font_style: "bold"
            text_color: "#062D3E"
            role: "medium"
            adaptive_size: True
            pos_hint: {"x": 0.2105, "y": 0.8}
        
        MDRelativeLayout:
            orientation: "vertical"
            radius: 25, 25, 25, 25
            padding: "35dp"
            spacing: "5dp"
            size_hint: 0.6, 0.57
            pos_hint: {"center_x": 0.5, "y": 0.2}

            MDScrollView:
                do_scroll_x: False
                padding: "15dp"
                spacing: "5dp"

                MDBoxLayout:
                    id: main_scroll
                    orientation: "vertical"
                    padding: "15dp"
                    spacing: "5dp"
                    adaptive_height: True
        
        MDButton:
            style: "elevated"
            theme_bg_color: "Custom"
            theme_width: "Custom"
            width: "140dp"
            md_bg_color: "#062D3E"
            pos_hint: {"x": 0.21, "y": 0.1}
            on_release:
                app.clear_list()
                root.current = "Menu"

            MDButtonText:
                text: "back"
                pos_hint: {"center_x": .5, "center_y": .5}
                font_style: "semi_bold"
                role: "small"
                theme_text_color: "Custom"
                text_color: "#FFF9E6"

        FitImage:
            source: "image/BG_1.png"

'''


class MyScreenManager(MDScreenManager):
    pass

class PetClinic(MDApp):
    #Autentikasi Laman Login
    def login(self):
        id_name = self.root.ids.id_field.text
        password = self.root.ids.password_field.text

        #Kalau TextFieldnya Kosong
        if id_name == '' or password == '':
            sb_kosong = MDSnackbar(
            MDSnackbarText(
                text="Please Enter your Username and Password",
                ),
                y=dp(24),
                pos_hint={"x" : 0.025},
                size_hint_x=0.4)
            sb_kosong.open()
            return
        
        #Membaca Database Pengguna
        file_path = "data_pet_clinic/database_login.csv"
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if  id_name == row['ID Name'] and password == row['Password']:
                    #Kalau Berhasil Login
                    self.root.current = "Menu"
                    self.root.ids.nurse_name.text = f"Vet. {id_name}!"
                    return
            
            #Kalau Gagal Login
            sb_salah = MDSnackbar(
                MDSnackbarText(
                    text="Incorrect ID Name or Password",
                ),
                y=dp(24),
                pos_hint={"x" : 0.025},
                size_hint_x=0.4)
            sb_salah.open()

    #Laman New Appt
    #Kalendar
    def show_modal_date_picker(self, *args):
        date_dialog = MDModalDatePicker()
        date_dialog.bind(on_edit=self.on_edit)
        date_dialog.bind(on_cancel=self.on_cancel)
        date_dialog.bind(on_ok=self.on_ok)
        date_dialog.open()

    #Kalendar Input (untuk tombol edit)
    def show_modal_input_date_picker(self, *args):
        def on_edit(*args):
            date_dialog.dismiss()
            Clock.schedule_once(self.show_modal_date_picker, 0.2)

        date_dialog = MDModalInputDatePicker()
        date_dialog.bind(on_edit=on_edit)
        date_dialog.open()

    #Tombol Edit
    def on_edit(self, instance_date_picker):
        instance_date_picker.dismiss()
        Clock.schedule_once(self.show_modal_input_date_picker, 0.2)

    # Tombol OK
    def on_ok(self, instance_date_picker):
        global format_date
        date = instance_date_picker.get_date()[0]
        format_date = date.strftime("%d/%m/%Y")
        self.root.ids.selected_date_label.text = f"{format_date}"
        instance_date_picker.dismiss()
    
    #Tombol Cancel
    def on_cancel(self, instance_date_picker):
        instance_date_picker.dismiss()

    #Mengambil Input dari Checkbox Male/Female
    def check_sex(self, value):
        global male_female
        male_female = value
        return male_female
    
    #Mengambil Input dari Checkbox Spayed/Neuteur
    def check_spay(self, value):
        global spay
        spay = value
        return spay

    #Menyimpan Data Appt ke Database
    def upload_data(self):
        appt = self.root.ids.owner_field.text
        patient = self.root.ids.petname_field.text
        weight = self.root.ids.weight_field.text
        breed = self.root.ids.breed_field.text
        age = self.root.ids.age_field.text
        medtreat = self.root.ids.selected_item_label.text

        with open("data_pet_clinic/data_appt.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([appt, patient, weight, breed, male_female, age, spay, medtreat, format_date])
        MDSnackbar(
            MDSnackbarText(
                text="Appointment has been made!",
                ),
                y=dp(24),
                pos_hint={"x" : 0.025},
                size_hint_x=0.4).open()
    
    #Menghapus Input pada TextField
    def clear_newappt(self):
        self.root.ids.owner_field.text = ""
        self.root.ids.petname_field.text = ""
        self.root.ids.weight_field.text = ""
        self.root.ids.breed_field.text = ""
        self.root.ids.age_field.text = ""
        self.root.ids.phone_field.text = ""
        self.root.ids.selected_item_label.text = ""
        self.root.ids.selected_date_label.text = ""
        self.root.ids.spayed_no_field.active = False
        self.root.ids.spayed_yes_field.active = False
        self.root.ids.male_field.active = False
        self.root.ids.female_field.active = False
    
    def validate_owner_info(self):
        if self.root.ids.owner_field.text.strip() == "" or self.root.ids.phone_field.text.strip() == "":
            self.root.ids.owner_field.error = True
            self.root.ids.phone_field.error = True
        else:
            self.root.current = "PetInformation"

    def validate_pet_info(self):
        if self.root.ids.petname_field.text.strip() == "" or self.root.ids.weight_field.text.strip() == "" or self.root.ids.breed_field.text.strip() == "" or self.root.ids.age_field.text.strip() == "" or self.root.ids.spayed_no_field.active == False and self.root.ids.spayed_yes_field.active == False or self.root.ids.male_field.active == False and self.root.ids.female_field.active == False:
            self.root.ids.petname_field.error = True
            self.root.ids.weight_field.error = True
            self.root.ids.breed_field.error = True
            self.root.ids.age_field.error = True
        else:
            self.root.current = "MedTreatmentInformation"
    
    def validate_med_treat(self):
        if self.root.ids.selected_item_label.text == "" or self.root.ids.selected_date_label.text == "":
            MDSnackbar(
            MDSnackbarText(
                text="Please fill all the requirements!",
                ),
                y=dp(24),
                pos_hint={"x" : 0.025},
                size_hint_x=0.4).open()
        else:
            self.upload_data()
            self.clear_newappt()
            self.root.current = "Menu"

    #View All Appt
    def list_all(self):
        df_appt = pd.read_csv("data_pet_clinic/data_appt.csv")
        df_appt['Date'] = pd.to_datetime(df_appt['Date'], dayfirst=True).dt.date
        df_appt = df_appt.sort_values(by='Date')
        global info
        info = {}
        for i, row in df_appt.iterrows():
            info[i] = row.tolist()

        global headline, display_info
        for info_item, info_value in info.items():
            headline = info_value[0]
            format_date = info_value[8]
            converted_format_date =  format_date.strftime("%d/%m/%Y")
            appt_info = [info_value[7], (info_value[8])]
            display_info = str(appt_info[0]) + " | " + converted_format_date

            self.root.ids.main_scroll.add_widget(
            MDListItem(
                MDListItemHeadlineText(text=str(headline),
                                       theme_font_name= "Custom",
                                       font_name="font/semi_bold.ttf",
                                       theme_font_size= "Custom",
                                       font_size="18dp"),
                MDListItemSupportingText(text=str(display_info),
                                         theme_font_name= "Custom",
                                         font_name="font/light.ttf",
                                         theme_font_size= "Custom",
                                         font_size="15dp"),
                pos_hint={"center_x": .5, "center_y": .5},
                radius= [15, 15, 15, 15],
                theme_bg_color="Custom",
                md_bg_color = get_color_from_hex("#FFF9E6")
            )
        )
    
    def clear_list(self):
        self.root.ids.main_scroll.clear_widgets()
        
    # Membuat Drop Down Menu
    def menu_open(self):
        treatments = self.extract_medical_treatments("data_pet_clinic/price.csv")
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
        
    #Menghapus Input pada TextField
    def clear_cancel_field(self):
        self.root.ids.search_cancel_field.text = f""

#Halaman Print Bill
    # Filter buat Print
    def filter_menu(self, search_text):
        filtered_items = [item for item in all_appt_items if search_text.lower() in item['text'].lower()]
        menu_bill.items = filtered_items
        if search_text == '':
            menu_bill.items = all_appt_items

    # Menampilkan Data Appt
    def set_item(self, appt_item):
        self.root.ids.search_field.text = appt_item
        menu_bill.dismiss()
        with open("data_pet_clinic/data_appt.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Appt'] == appt_item:
                    self.root.ids.owner_print_name.text   = f"Appointment {appt_item}"
                    self.root.ids.pet_print_name.text     = f"Patient : {row['Patient']}"
                    self.root.ids.breed_print_name.text   = f"Breed : {row['Breed']}"
                    self.root.ids.date_print_name.text    = f"Date : {row['Date']}"
                    self.root.ids.treat_print_name.text   = f"Medical Treatment : {row['Medical Treatment']}"

        with open("data_pet_clinic/price.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            obat = self.root.ids.treat_print_name.text
            for row in reader:
                if row['Medical Treatment'] == obat:
                    return row['Price']
                
                self.root.ids.price_print_name.text = f"Total Payment : {row['Price']}"
                        
    # Mengambil Data dari Data Base
    def extract_appt(self, csv_file):
        allappt = []
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                appt = row[0]
                allappt.append(appt)
        return allappt

    # Menu DropDown Mencari Appt
    def find_appt(self):
        allappt = self.extract_appt("data_pet_clinic/data_appt.csv")
        global all_appt_items
        all_appt_items = [
            {
                "text": appt,
                "on_release": lambda x=appt: self.set_item(x),
            } for appt in allappt
        ]
        global menu_bill
        menu_bill = MDDropdownMenu(
            caller=self.root.ids.search_field,
            items=all_appt_items,
            position="bottom",
            width=dp(500),
            ver_growth="down",
            radius=[5, 5, 5, 5]
        )

        menu_bill.open()

# Halaman Cancel
    def filter_cancel_menu(self, search_text):
        filtered_items = [item for item in all_appt_items if search_text.lower() in item['text'].lower()]
        menu_cancel.items = filtered_items
        if search_text == '':
            menu_cancel.items = all_appt_items

    def find_cancel_appt(self):
        allappt = self.extract_appt("data_pet_clinic/data_appt.csv")
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
            width=dp(600),
            ver_growth="down",
            radius=[10, 10, 10, 10],
            position="bottom",
        )
        menu_cancel.open()

    def display_cancel_appt(self, appt_item):
        self.root.ids.search_cancel_field.text = appt_item
        menu_cancel.dismiss()

    def cancel_appt(self):
        nama_appt_cancel = self.root.ids.search_cancel_field.text
        filtered_rows = []
        if nama_appt_cancel.strip() == "":
            sb_gagal_cancel = MDSnackbar(
            MDSnackbarText(
                text="Please select an appointment first",
                ),
                y=dp(24),
                pos_hint={"x" : 0.025},
                size_hint_x=0.4)
            sb_gagal_cancel.open()
        else:
            with open("data_pet_clinic/data_appt.csv", 'r', newline='') as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                for row in reader:
                    if row['Appt'] != nama_appt_cancel:
                        filtered_rows.append(row)
            
                with open("data_pet_clinic/data_appt.csv", 'w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(filtered_rows)
                self.root.current = "Menu"

                sb_berhasil_cancel = MDSnackbar(
                MDSnackbarText(
                    text="Appointment Removed",
                    ),
                    y=dp(24),
                    pos_hint={"x" : 0.025},
                    size_hint_x=0.4)
                sb_berhasil_cancel.open()
        
    def print_bill(self):
        appt = self.root.ids.owner_print_name.text
        date = self.root.ids.date_print_name.text
        new_date = date.replace("Appt Date : ", "")
        patient = self.root.ids.pet_print_name.text
        breed = self.root.ids.breed_print_name.text
        med = self.root.ids.treat_print_name.text
        price = self.root.ids.price_print_name.text

        if appt.strip() == "" or date.strip() == "" or new_date.strip() == "" or patient.strip() == "" or breed.strip() == "" or med.strip() == "" or price.strip() == "":
            sb_gagal_print = MDSnackbar(
            MDSnackbarText(
                text="Please select an appointment first",
                ),
                y=dp(24),
                pos_hint={"x" : 0.025},
                size_hint_x=0.4)
            sb_gagal_print.open()
        else:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size = 12)
            pdf.cell(100, 8, txt = "=============================================", ln = True, align = 'C')
            pdf.cell(100, 8, txt = "Pet Clinic", ln = True, align = 'C')
            pdf.cell(100, 8, txt = "Veterinary Invoices", ln = True, align = 'C')
            pdf.cell(100, 8, txt = "=============================================", ln = True, align = 'C')

            pdf.set_font("Arial", size = 12)
            pdf.cell(100, 8, txt = "=============================================", ln = True, align = 'C')
            pdf.cell(100, 8, txt = f"{appt}", ln = True)
            pdf.cell(100, 8, txt = f"Date : {new_date}",  ln = True)
            pdf.cell(100, 8, txt = f"{patient}",  ln = True)
            pdf.cell(100, 8, txt = f"{breed}",  ln = True)
            
            pdf.cell(100, 8, txt = "=============================================", ln = True, align = 'C')
            pdf.cell(100, 8, txt = f"{med}",  ln = True)
            pdf.cell(100, 8, txt = f"Total Payment : {price}",  ln = True)
            pdf.cell(100, 8, txt = "=============================================", ln = True, align = 'C')

            pdf_file_path = "vet_invoice.pdf"
            pdf.output(pdf_file_path)

            self.root.current = "Menu"

            MDSnackbar(
                MDSnackbarText(
                    text="Invoice Printed",
                    ),
                    y=dp(24),
                    pos_hint={"x" : 0.025},
                    size_hint_x=0.4).open()
            
            path = "vet_invoice.pdf"
            webbrowser.open_new(path)
    
    def close_program(self):
        PetClinic().stop()

    def build(self):
        
        LabelBase.register(
            name="bold",
            fn_regular="font/bold.ttf",
        )

        self.theme_cls.font_styles["bold"] = {
            "large": {
                "line-height": 1,
                "font-name": "bold",
                "font-size": sp(68),
            },
            "medium": {
                "line-height": 1,
                "font-name": "bold",
                "font-size": sp(48),
            },
            "small": {
                "line-height": 1,
                "font-name": "bold",
                "font-size": sp(30),
            },
        }

        LabelBase.register(
            name="semi_bold",
            fn_regular="font/semi_bold.ttf",
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
            fn_regular="font/regular.ttf",
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
            fn_regular="font/light.ttf",
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
                "font-size": sp(22),
            },
        }
        
        Builder.load_string(KV)
        return MyScreenManager()

PetClinic().run()