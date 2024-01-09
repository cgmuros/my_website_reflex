import reflex as rx
from school_bus.styles.styles import Size as Size
from school_bus.styles.colors import TextColor as TextColor
from school_bus.styles.colors import Color as Color



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