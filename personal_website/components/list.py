import reflex as rx
from personal_website.styles.styles import Size as Size
from personal_website.styles.colors import TextColor as TextColor
from personal_website.styles.colors import Color as Color
import personal_website.constants as const



def list() -> rx.Component:

    texts = [rx.text(skill + " - ") if skill != const.MY_SKILLS[-1] else rx.text(skill) for skill in const.MY_SKILLS]
    return rx.box(
        rx.flex(*texts, 
            width="100%", 
            color=TextColor.LIST_HEADER.value, 
            justify_content="center", 
            flex_wrap="wrap",
            padding=Size.BIG.value),
        border="1px solid #ccc",
        padding=Size.BIG.value

    )

           