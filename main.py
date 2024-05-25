from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivy.metrics import sp

class MainApp(MDApp):
    def build(self):
        screen = MDScreen(md_bg_color = get_color_from_hex("#CDE2FF"))

        layout_title = MDAnchorLayout(
            md_anchor_x='left', md_anchor_y='bottom',
            radius = [25, 25, 25, 25],
            md_bg_color = get_color_from_hex("#FFF000"),
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
                "line-height": 1.64,
                "font-name": "font50",
                "font-size": sp(55)
            }
        }

        label_title = MDLabel(
            text = "Owner's Information",
            font_style = "font50"
            )

        layout_title.add_widget(label_title)
        screen.add_widget(layout)
        screen.add_widget(layout_title)

        return screen

if __name__ == "__main__":
    MainApp().run()
