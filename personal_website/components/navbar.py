import reflex as rx
from personal_website.styles.styles import Size as Size
from personal_website.styles.colors import TextColor as TextColor
from personal_website.styles.colors import Color as Color
import personal_website.styles.styles as styles
from personal_website.components.ant_components import float_button
import personal_website.constants as cons



def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.hstack(
                rx.link("cmuros", color=Color.PRIMARY.value, href="/"),
                rx.link("dev", color=Color.SECONDARY.value, href="/"),
                
                # width="100%",
                style=styles.navbar_title_style,
            ),
        ),
    
        rx.hstack(
            rx.image(src="/icons/download.svg"),
            rx.link(
                "Download CV", 
                href="/docs/cv_english.pdf", 
                color=Color.PRIMARY.value, 
                is_external=True
            ),
        ),
        float_button(
            icon=rx.Image(src="/icons/whatsapp.svg"),
            href=cons.MY_WHATSAPP,
        ),
        justify_content="space-between",
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )  