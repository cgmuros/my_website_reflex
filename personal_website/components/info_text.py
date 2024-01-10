import reflex as rx
from personal_website.styles.styles import Size as Size
from personal_website.styles.colors import TextColor as TextColor
from personal_website.styles.colors import Color as Color



def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.span(
            title, 
            font_weight="bold", 
            color=Color.PRIMARY.value
        ),
        f" {body}", 
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value
    )