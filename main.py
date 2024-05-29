from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.config import Config
Config.set ("graphics", "resizable", False)
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivy.metrics import sp

class MainApp(MDApp):
    def build(self):
        screen = MDScreen(md_bg_color = get_color_from_hex("#CDE2FF"))

        layout_title = MDAnchorLayout(
            anchor_x='center', anchor_y='top',
            radius = [25, 25, 25, 25],
            md_bg_color = get_color_from_hex("#FFF9E6"),
            size_hint = (0.5, 0.2),
            pos_hint={"center_x": 0.325, "center_y": 0.7},
        )

        layout = MDFloatLayout(
            radius = [25, 25, 25, 25],
            md_bg_color = get_color_from_hex("#FFF9E6"),
            size_hint = (0.85, 0.6),
            pos_hint={"center_x": 0.5, "center_y": 0.4}
        )

        LabelBase.register(
            name="font50",
            fn_regular="/Users/Najwa Permata Hadi/Documents/Tugas Besar Programa Komputer/Pet-Clinic-Kelompok-19/font50.ttf",
        )

        self.theme_cls.font_styles["font50"] = {
            "large": {
                "line-height": 1,
                "font-name": "font50",
                "font-size": "55sp"
            }
        }

        label_title = MDLabel(
            text = "Owner's Information",
            text_color = get_color_from_hex("#062D3E"),
            font_style = "font50",
            size_hint=(0.9, 0.5),
            text_size= (1, 1),
            halign = "left"
        )

        layout_title.add_widget(label_title)
        screen.add_widget(layout)
        screen.add_widget(layout_title)

        return screen

if __name__ == "__main__":
    MainApp().run()

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.config import Config
Config.set ("graphics", "resizable", False)
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.metrics import sp

Window.maximize()

KV = '''
<MyScreenManager>:
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
                    pos_hint: {"x": 0.855}
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
                spacing: "30dp", "22.5dp"

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
            pos_hint: {"x": 0.785, "y": 0.12}
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
            pos_hint: {"x": 0.675, "y": 0.12}
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
        
        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: "#FFF9E6"
            radius: 25, 25, 25, 25
            padding: "30dp"
            spacing: "5dp"
            size_hint: 0.85, 0.58
            pos_hint: {"center_x": 0.5, "y": 0.125}

            MDLabel:
                text: "Medical Treatment"
                font_style: "bold"
                role: "medium"
                text_color: "#062D3E"
                adaptive_size: True
            
            MDBoxLayout:
            
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
                "font-size": sp(20),
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
                "font-size": sp(45),
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
                "font-size": sp(42),
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